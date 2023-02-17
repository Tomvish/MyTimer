from tkinter import *
import time
# import Pomodoro

# Define window size and title
root = Tk()
root.geometry('320x240')
root.title('Work/Break Timer')
# root.
 # Define work and break times in minutes
index = 1  # 60 - минут, 1 - секунд для проверки
work_time = 5   # minutes
rest_time = 3  # minutes
work_day = 5    # час
 # Create text labels for work and break times
txt = f"Начнём с {work_day}"
time.sleep(3)
# work_label = Label(root, text="Work Time: {} min".format(work_time))
# rest_label = Label(root, text="Break Time: {} min".format(rest_time))
# work_label.grid()
# rest_label.grid()
# txtw = f"Ещё поработать:,# {font = ('Arial Bold', 15)}"
work_btn = Button(root, text="Ещё поработать:\n {} min".format(work_time), font=('Arial Bold', 20), width=20, height=3)
rest_btn = Button(root, text="Осталось отдохнуть:\n {} min".format(rest_time), font=('Arial Bold', 20), width=20, height=3)
work_btn.grid()
rest_btn.grid()

# root.update()
# root.mainloop()
start1= time.time()
elapseTime1= 0

while elapseTime1 < work_time*index:
    elapseTime1= time.time()-start1
    mins, secs= divmod(work_time*index-elapseTime1,index)

    txt = f'\nЕщё поработать:{int(mins)}:{int(secs)}'
    work_btn.configure(text = txt, bg='red', default='active')
    time.sleep(1)
    root.update()
work_btn.configure(text =("\nВремя отдохнуть!"),  bg='yellow', default='normal')


start2 = time.time ()                                   # Start timer for break interval
elaps2eTime2= 0                                         # Initialize elapseTime as 0
while elaps2eTime2 < rest_time*index:
    elaps2eTime2= time.time()-start2
    mins, secs= divmod(rest_time*index-elaps2eTime2,index)
    txt = f'\nЕщё отдохнуть:{int(mins)}:{int(secs)}'
    rest_btn.configure(text=txt, bg='green', default='active')
    time.sleep(1)
    root.update()
rest_btn.configure(text=("\nОтдых окончен!"),  bg='grey', default='normal')
work_btn.configure(text=("\nСтарт!"), anchor='n')



root.mainloop()

"""
res = messagebox.askretrycancel('Заголовок', 'Текст')


spin = Spinbox(window, values=(3, 8, 11), width=5)
var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
"""
