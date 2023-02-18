import tkinter as tk
from tkinter import messagebox
from  tkinter import  ttk
import time
import  re

index = 60  # 60 - минуты, 1 - секунды для проверки
step = False #True
work_time = 1  # Уст. по-умолчанию в функции start.
rest_time = 1
work_day = 1    # час
#################
# def option():
#     tk.messagebox.askyesnocancel('Укажите время', f"запустить {spin}")

def is_valid(newal, op):
    # try:
    result = re.match("^\d{0,3}$", newal) is not None #
    if op=="key":
        err_lbl.configure(text=newal)
    elif op=="focus":
        err_lbl.configure(text="focus")
    if not result or len(newal) >=3:
        errmsg=("Рекомендуется делать перерывы")
        print("Рекомендуется делать перерывы")
        err_lbl.configure(text=(errmsg), bg='orange',)
    else:
        err_lbl.configure(text=newal, )
    return result
    # except:
    #     err_lbl.configure(text=(errmsg), bg='orange')
    # finally:
    #     return result

def start():
    global step
    step = not step # старт/отдых
    work_time = (ent_work.get()) #int(s))
    if work_time == "":
        work_time = 25 # Это работа по-умолчанию, если не введено пользователем.
    else:
        work_time = int(work_time)
    rest_time = ent_rest.get()
    if rest_time == "":
        rest_time = 5 # Это отдых по-умолчанию, если не введено пользователем.
    else:
        rest_time = int(rest_time)

    # Обработка клика кнопки старт/отдых
    if step: # работа
        print(f'Тип: {type(work_time)} введено: {work_time}') ### при if
        btnStart.configure(text='Отдых', bg='magenta', default='active',) # command=option) #text[1]) #
        lbl.configure(text=('Удачи в работе!'))
        ent_work.configure(bg='yellow')
        ent_rest.configure(bg='white')
        timer(work_time, rest_time)
    else: # отдых
        print(f'Тип: {type(rest_time)} введено: {rest_time}') ### при else
        btnStart.configure(text='Старт', bg='yellow', default='normal') #text[0]) #
        lbl.configure(text=('Отдохни!'))
        print("Пауза,'Отдохни!' ") #, elapse_rest_time) ###
        ent_work.configure(bg='white')
        ent_rest.configure(bg='green')
        # timer(work_time, rest_time)
    # step = not step

#### Основной цикл:
def timer(work_time, rest_time):

    while step:
        lbl.configure(text=('Начинаем работу!'), bg='orange')
        print('Начинаем работу!') ###
        start_time = time.time()

        # Запустим таймер для рабочего интервала.
        start_work = time.time()
        elapse_work_time = 0
        while elapse_work_time <= work_time * index -1 and step: # -1 на издержки запуска
            elapse_work_time = time.time() - start_work
            mins, secs = divmod(work_time * index - elapse_work_time, index)

            txt = f'{int(mins)}:{int(secs)}' # Табло Ещё поработать
            lbl_tablo.configure(text=txt)
            print(txt)
            time.sleep(1)
            win.update()
        lbl.configure(text=("Время отдохнуть!"), bg='green')
        print("Время отдохнуть! в работе прошло: ", elapse_work_time )
        print(step, 'work') ###

        # Запустите таймер для интервала отдыха.
        start_rest = time.time()  # Отмерять отдых с этой секунды
        elapse_rest_time = 0  # установить истёкшее время = 0
        print('старт отдыха:', start_rest//60)
        while elapse_rest_time <= rest_time * index -1: # -1 на издержки запуска, иначе уходит в -1.
            elapse_rest_time = time.time() - start_rest
            mins, secs = divmod(rest_time * index - elapse_rest_time, index)
            txt = f'{int(mins)}:{int(secs)}' # Табло Ещё отдохнуть
            lbl_tablo.configure(text=txt)
            print(txt)
            time.sleep(1)
            win.update()
        lbl.configure(text=("Отдых окончен!"))
        print('"Отдых окончен!"', elapse_rest_time, 'end:', time.time()//60 ) ###
        print(step, 'rest')
        # step = not step
        ########################
win = tk.Tk()
win.title("Мой таймер")
win.attributes('-toolwindow', True)
# win.columnconfigure(3, minsize=3)
# win.rowconfigure(1, minsize=10)
win.geometry('235x152-150-205')  #######
# print(win.geometry())

# spin = tk.Spinbox(messagebox, from_=0, to=100)
# var = IntVar()
# var.set(36)
# spin = tk.Spinbox(win, from_=0, to=100, width=5,) # textvariable=var)

frm = tk.Frame(win, width=15, height=3, relief=tk.RIDGE, bg='green', borderwidth=4,)
frmb = tk.Frame(win, width=15, height=3, relief=tk.RIDGE, borderwidth=4,) # bg='green',SUNKEN

lbl = tk.Label(frm, text='Время вперёд', bg='green', anchor='nw', font=('Arial Bold', 16), height=1)
lbl_tablo = tk.Label(frm, text='12:13:14',  anchor='center', font=('Arial Bold', 35), width=8, height=1)
err_lbl = tk.Label(frm, text="***",  bg='green', )

btnStart = tk.Button(frmb, text='<<< Дело-Отдых >>>', width=20, command=start)

check = (win.register(is_valid), "%P", "%V")

ent_work = tk.Entry(frmb, validate='key', validatecommand=check, width=5)
ent_rest = tk.Entry(frmb, validate='key', validatecommand=check, width=5)

frm.pack(fill=tk.Y,  side=tk.TOP,)
frmb.pack(fill=tk.Y,  side=tk.BOTTOM,)
lbl.pack(fill=tk.Y)
lbl_tablo.pack()
err_lbl.pack(fill=tk.Y,)
ent_work.grid(column=0, row=0, sticky='w' )
btnStart.grid(column=1, row=0, sticky='s' )
ent_rest.grid(column=2, row=0, sticky='e' )
#
win.mainloop()
