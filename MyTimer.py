import tkinter as tk
from tkinter import messagebox
from  tkinter import  ttk
import time
import  re

index = 1  # 60 - минуты, 1 - секунды для проверки
step = False #True
work_time = 1
rest_time = 1
work_day = 1    # час
#################
def option():
    tk.messagebox.askyesnocancel('Укажите время', f"запустить {spin}")

def is_valid(newal):
    # try:
    result = re.match("\d$", newal) is not None
    if not result or len(newal) >=4:
        errmsg=("Рекомендуется делать перерывы")
        print("Рекомендуется делать перерывы")
        err_lbl.configure(text=(errmsg), bg='orange')
    else:
        err_lbl.configure(text="норм", )
    return result
    # except:
    #     err_lbl.configure(text=(errmsg), bg='orange')
    # finally:
    #     return result

def start():
    global  step
    step = not step
    work_time = (ent_work.get()) #int(s))
    work_time = int(work_time)
    print(f'Тип: {type(work_time)} введено: {work_time}')
    rest_time = ent_rest.get()
    rest_time = int(rest_time)
    if step: # работа
        btnStart.configure(text='Пауза', bg='red', default='active',) # command=option) #text[1]) #
        lbl.configure(text=('Удачи в работе!'))
        ent_work.configure(bg='yellow')
        ent_rest.configure(bg='white')
        timer(work_time, rest_time)

    else: # отдых
        btnStart.configure(text='Старт', bg='yellow', default='normal') #text[0]) #
        lbl.configure(text=('Отдохни!'))
        print("Пауза,'Отдохни!' ", elaps2eTime2)
        ent_work.configure(bg='white')
        ent_rest.configure(bg='green')
        # timer(work_time, rest_time)
    # step = not step

#### Основной цикл:
def timer(work_time, rest_time):

    while step:
        lbl.configure(text=('Начинаем работу!'), bg='orange')
        start_time = time.time()

        # Запустите таймер для рабочего интервала.
        start_work = time.time()
        elapseTime1 = 0
        while elapseTime1 <= work_time * index -1: #7: #
            elapseTime1 = time.time() - start_work
            mins, secs = divmod(work_time * index - elapseTime1, index)

            txt = f'{int(mins)}:{int(secs)}' # Ещё поработать
            lbl_tablo.configure(text=txt)
            time.sleep(1)
            win.update()
        lbl.configure(text=("Время отдохнуть!"), bg='green')
        print("Время отдохнуть!",elapseTime1 )
        print(step, '1')

        # Запустите таймер для интервала отдыха.
        start_rest = time.time()  # Start timer for break interval
        elaps2eTime2 = 0  # Initialize elapseTime as 0
        while elaps2eTime2 <= rest_time * index :
            elaps2eTime2 = time.time() - start_rest -1
            mins, secs = divmod(rest_time * index - elaps2eTime2+1, index)
            txt = f'{int(mins)}:{int(secs)}' # \nЕщё отдохнуть
            lbl_tablo.configure(text=txt)
            time.sleep(1)
            win.update()
        lbl.configure(text=("Отдых окончен!"))
        print('"Отдых окончен!"', elaps2eTime2 )
        # step = not step
        ########################
win = tk.Tk()
win.attributes('-toolwindow', True)
# win.columnconfigure(3, minsize=3)
# win.rowconfigure(1, minsize=10)
win.geometry('235x152-150-205')  #######
print(win.geometry())

# spin = tk.Spinbox(messagebox, from_=0, to=100)
# var = IntVar()
# var.set(36)
# spin = tk.Spinbox(win, from_=0, to=100, width=5,) # textvariable=var)

frm = tk.Frame(win, width=15, height=3, relief=tk.RIDGE, bg='green', borderwidth=4,)
frmb = tk.Frame(win, width=15, height=3, relief=tk.RIDGE, borderwidth=4,) # bg='green',SUNKEN

lbl = tk.Label(frm, text='Время вперёд', bg='green', anchor='nw', font=('Arial Bold', 16), height=1)
lbl_tablo = tk.Label(frm, text='12:13:14',  anchor='center', font=('Arial Bold', 35), width=8, height=1)
err_lbl = tk.Label(frm, text="***",  bg='green')

btnStart = tk.Button(frmb, text='<<< Дело-Отдых >>>', width=20, command=start)

check = (win.register(is_valid), "%P")

ent_work = tk.Entry(frmb, validate='key', validatecommand=check, width=5)
ent_rest = tk.Entry(frmb, width=5)

frm.pack(fill=tk.Y,  side=tk.TOP,)
frmb.pack(fill=tk.Y,  side=tk.BOTTOM,)
lbl.pack()
lbl_tablo.pack()
err_lbl.pack()
ent_work.grid(column=0, row=0, sticky='w' )
btnStart.grid(column=1, row=0, sticky='s' )
ent_rest.grid(column=2, row=0, sticky='e' )
#
win.mainloop()
