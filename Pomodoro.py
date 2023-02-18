# Console Pomodoro Application in Python
import time


def pomodoro(index=60):
    print('Добро пожаловать в приложение Pomodoro!')
    # Задайте пользователю интервалы работы и отдыха в минутах.
    index = 60  # 60 - минут, 1 - секунд для проверки
    work_time = int(input('Как долго вы бы хотели работать (в минутах)? '))
    rest_time = int(input('Как долго вы хотели бы отдыхать (в минутах)? '))
    work_day = int(input("Сколько часов вместе с перерывами хотите поработать?")) * index * index  # сразу в минуты
    while work_day > 0:
        # Запустите таймер для рабочего интервала.
        print(' * '*8,'\n  Начинаем работу!\n','\n'' * '*8)
        # TODO: Добавить сигнал

        start_time = time.time() # Время на момент старта
        print(f'\nНастраиваемся на {work_day//index} минут работы с перерывами')

        elapse_work_time = 0 # истёкшее_время

        while elapse_work_time < work_time * index:
            elapse_work_time = time.time() - start_time
            #

            # Рассчитайте оставшееся время.                  # Перевести секунды в минуты и секунды.
            mins, secs = divmod(work_time * index - elapse_work_time, index) # divmod(a,b)=(a//b, a%b)

            print(f'\rЕщё работать: {int(mins)}:{int(secs)}', end='')

            time.sleep(1)  # Перед повторной проверкой задержитесь на 1 секунду.

        print('\nРабочая сессия окончена! Сделайте перерыв.')  # Рабочая сессия окончена, отдохните!
        work_day = work_day - elapse_work_time
        print(f'\n Истёкшее_время {elapse_work_time} из {work_day//index}') ###

        start2 = time.time()  # Запуск таймера на интервал перерыва

        elapse_rest_time = 0  # Initialize elapseTime as 0
        while elapse_rest_time < rest_time* index:
            elapse_rest_time = time.time()-start2
            mins, secs= divmod(rest_time * index - elapse_rest_time, index)
            print(f'\rОсталось отдыхать:{int(mins)}:{int(secs)}',end="")
            time.sleep(1)
        print("\nПерерыв окончен!")
        work_day = work_day - elapse_rest_time

        print(f'\n Истёкшее_время {elapse_rest_time} из {work_day//index} минут работы') ###
    exit(print('Рабочий день закончился\n...гуляй смело'))

pomodoro()