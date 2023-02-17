from tkinter import *
from tkinter import messagebox
import time
# import Pomodoro

# Define window size and title
root = Tk()
root.geometry('285x190-15-45')  #('320x240-30-50') #-350-300') # font=20
# root.minsize('105x150')  # не имеет смысла
# root.maxsize('350x220')
root.title('Клик - настройка')
# root.
 # Define work and break times in minutes
index = 1 # 60 - минут, 1 - секунд для проверки
work_time = 15   # minutes
rest_time = 5  # minutes
work_day = 5    # час
########################################
def option():
    messagebox.askyesnocancel('Укажите время', f"запустить {spin}")

# spin = Spinbox(root, from_=0, to=100)
var = IntVar()
var.set(36)
spin = Spinbox(root, from_=0, to=100, width=5, textvariable=var)




########################################
# txtw = f"Ещё поработать:,# {font = ('Arial Bold', 15)}"
work_btn = Button(root, text="поработать:\n {} min".format(work_time),  anchor='n', font=('Arial Bold', 18), width=20, height=3, command=option)
rest_btn = Button(root, text=" отдохнуть:\n {} min".format(rest_time),  font=('Arial Bold', 18), width=20, height=3,  command=option)
work_btn.grid()
rest_btn.grid()

# root.update()

# работа !!!
start1= time.time()
elapseTime1= 0
while elapseTime1 < work_time*index:
    elapseTime1= time.time()-start1
    mins, secs= divmod(work_time*index-elapseTime1,index)

    txt = f'\nЕщё поработать:{int(mins)}:{int(secs)}'
    work_btn.configure(text = txt, bg='orange', default='active')
    time.sleep(1)
    root.update()
work_btn.configure(text =("\nВремя отдохнуть!"), bg='yellow', default='normal')

# Отдых !!!
start2 = time.time ()                                   # Start timer for break interval
elaps2eTime2= 0                                         # Initialize elapseTime as 0
while elaps2eTime2 < rest_time*index:
    elaps2eTime2= time.time()-start2
    mins, secs= divmod(rest_time*index-elaps2eTime2,index)
    txt = f'\nОтдыхаем:{int(mins)}:{int(secs)}'
    rest_btn.configure(text=txt, bg='green', anchor='n', default='active')
    time.sleep(1)
    root.update()
rest_btn.configure(text=("\nОтдых окончен!"),  bg='grey', default='normal')
work_btn.configure(text=("\nСтарт!"), )



root.mainloop()