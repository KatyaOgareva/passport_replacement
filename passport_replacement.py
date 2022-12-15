from tkinter import *
import re
from tkcalendar import DateEntry
from datetime import datetime

window = Tk()
window.title("Когда менять паспорт")
window.geometry('380x550+760+250')

lbl_description = Label(window,
                        text="Данная программа поможет Вам рассчитать через какой промежуток времени Вам нужно поменять паспорт",
                        wraplength=390, justify=CENTER, padx=10, pady=10)
lbl_input = Label(window, text="Для этого Вам необходимо ввести свои ФИО и дату рождения", wraplength=390,
                  justify=CENTER, padx=10, pady=10)

lbl_name = Label(window, text="ФИО: ", wraplength=400)

result2 = StringVar()
result2.set("АВАВАВА")
lbl_result = Label(window, textvariable=result2, wraplength=370)


def validate_username(username):
    result = re.match("[а-яА-ЯёЁ ]+$", username) is not None
    if not result and len(username) <= 50:
        errmsg.set("Используйте только кириллицу")
    else:
        errmsg.set("")
    return result


def test1():
    global result2
    fio_str = entry_name.get()
    fio = fio_str.split()
    if fio_str == "":
        errmsg.set("Введите ФИО")
        result2.set("tttttt")
    elif len(fio) == 3:
        date2 = cal.get()
        month_num = int(date2.split("/")[0])
        day_num = int(date2.split("/")[1])
        year_num = int("20" + date2.split("/")[2])

        now = datetime.now()
        old = datetime(day=day_num, month=month_num, year=year_num)
        timedelta = now - old

        print(fio[0].title(), fio[1][0].upper() + ".", fio[2][0].upper() + ".", date2)
        print("День:", day_num, "Месяц:", month_num, "Год:", year_num)
        print("Сегодня:", datetime.today())
        print("Прошло:", timedelta)
        result2.set("ahahahaha")
    else:
        errmsg.set("Некорректные данные")

check = (window.register(validate_username), "%P")

errmsg = StringVar()

entry_name = Entry(window, validate="key", validatecommand=check, width=40)

lbl_error = Label(foreground="red", textvariable=errmsg, wraplength=250)

lbl_date = Label(window, text="Дата рождения: ")

cal = DateEntry(window, selectmode='day', background="#AAA")

btn_calculation = Button(window, text="Произвести рассчет", relief=GROOVE, command=test1)

output = StringVar()
output.set("Здесь будет результат")
lbl_output = Label(window, textvariable=output)

lbl_description.grid(row=0, column=0, columnspan=2)
lbl_input.grid(row=1, column=0, columnspan=2)
lbl_name.grid(row=2, column=0, sticky=W, padx=10)
entry_name.grid(row=2, column=1, sticky=W)
lbl_error.grid(row=3, column=1, columnspan=1, sticky=W)
lbl_date.grid(row=4, column=0, columnspan=1, sticky=W, padx=10)
cal.grid(row=4, column=1, sticky=W)
btn_calculation.grid(row=5, column=0, columnspan=2, sticky=N, pady=30)
lbl_result.grid(row=6, column=0, columnspan=2)
lbl_output.grid(row=7, column=0, columnspan=2)
window.mainloop()
