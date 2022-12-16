import re
from datetime import datetime
from tkinter import *

from tkcalendar import DateEntry

window = Tk()
window.title("Когда менять паспорт")
window.geometry('380x550+760+250')

lbl_description = Label(window,
                        text="Данная программа поможет Вам рассчитать через какой промежуток времени Вам нужно поменять паспорт",
                        wraplength=390, justify=CENTER, padx=10, pady=10)
lbl_input = Label(window, text="Для этого Вам необходимо ввести свои ФИО и дату рождения", wraplength=390,
                  justify=CENTER, padx=10, pady=10)

lbl_name = Label(window, text="ФИО: ", wraplength=400)


def validate_username(username):
    result = re.match("[а-яА-ЯёЁ ]+$", username) is not None
    if not result and len(username) <= 50:
        errmsg_name.set("Используйте только кириллицу")
    else:
        errmsg_name.set("")
    return result

# def
def your_age(d_a, m_a, y_a, d_n, m_n, y_n):
    day_num_cal, month_num_cal, year_num_cal, now_day, now_month, now_year = d_a, m_a, y_a, d_n, m_n, y_n
    if now_month == month_num_cal:
        if now_day > day_num_cal:
            age = now_year - year_num_cal
            return age
        else:
            age = now_year - year_num_cal - 1
            return age
    elif now_month > month_num_cal:
        age = now_year - year_num_cal
        return age
    else:
        age = now_year - year_num_cal - 1
        return age


def after_replace(d_a, m_a, d_n, m_n):
    days_num = str(datetime(day=d_n, month=m_n, year=2022) - datetime(day=d_a, month=m_a, year=2022))
    days = days_num.split()[0]
    if days == "0:00:00":
        days = 0
    elif int(days) < 0:
        days = 365 + int(days)
    return days


def before_replace(d_a, m_a, y_a, d_n, m_n, your_ages):
    days_num = str(datetime(day=d_a, month=m_a, year=2022) - datetime(day=d_n, month=m_n, year=2022))
    days = days_num.split()[0]
    if days == "0:00:00":
        days = 0
    elif int(days) < 0:
        days = 365 + int(days)
    return days


def test1():
    global output
    fio_str = entry_name.get()
    fio = fio_str.split()
    if fio_str == "":
        errmsg_name.set("Введите ФИО")
    elif len(fio) == 3:
        date2 = cal.get()
        month_num_cal = int(date2.split("/")[0])
        day_num_cal = int(date2.split("/")[1])
        if int(date2.split("/")[2]) > 22:
            year_num_cal = int("19" + date2.split("/")[2])
        else:
            year_num_cal = int("20" + date2.split("/")[2])

        now = datetime.now()
        now_day = int(str(now).split()[0].split("-")[2])
        now_month = int(str(now).split()[0].split("-")[1])
        now_year = int(str(now).split()[0].split("-")[0])
        old = datetime(day=day_num_cal, month=month_num_cal, year=year_num_cal)

        timedelta = now - old

        initials = str(fio[0].title()) + " " + str(fio[1][0].upper()) + ". " + str(fio[2][0].upper())


        if timedelta.days <= 0:
            errmsg_date.set("Введите корректную дату")
        else:
            errmsg_date.set("")
            your_ages = your_age(day_num_cal, month_num_cal, year_num_cal, now_day, now_month, now_year)
            if your_ages > 45:
                output.set("Здравствуйте, " + str(initials) + ". Вам больше не нужно менять паспорт.")
            elif 18 < your_ages < 21:
                if your_ages >= 20:
                    after = after_replace(day_num_cal, month_num_cal, now_day, now_month)
                    if int(after) == 0:
                        output.set("Здравствуйте, " + str(initials) + ". До срока замены паспорта более года. На данный момент вам не стоит беспокоиться по этому поводу.")
                    elif int(after) <= 90:
                        count = - (int(after) - 90)
                        output.set("Здравствуйте, " + str(initials) + ". На данный момент вам " + str(your_ages) + " лет. " + "Если вы до сих пор не поменяли паспорт, сделайте это в ближайшем МФЦ. У Вас осталось " + str(count) + " дней на замену. Если вы не поменяете паспорт в течении этого времени, на Вас будет наложен штраф.")
                    else:
                        count = int(after) - 90
                        output.set("Здравствуйте, " + str(initials) + ". На данный момент вам " + str(your_ages) + " лет. " + "Если вы до сих пор не поменяли паспорт, сделайте это в ближайшем МФЦ. У вас просрочка в " + str(count) + " дней. Не забудьте оплатить штраф.")

                else:
                    before = before_replace(day_num_cal, month_num_cal, year_num_cal, now_day, now_month, your_ages)
                    if before == 0:
                        output.set("С днём рождения, " + str(initials) + "! На данный момент вам " + str(your_ages + 1) + " лет. " + "Поменяйте паспорт в течении следующих 90 дней.")
                    else:
                        output.set("Здравствуйте, " + str(initials) + ". На данный момент вам " + str(your_ages) + " лет. " + "До замены паспорта осталось " + str(before) + " дней.")

            elif 43 < your_ages < 46:
                if your_ages >= 45:
                    after = after_replace(day_num_cal, month_num_cal, now_day, now_month)
                    if int(after) == 0:
                        output.set("Здравствуйте, " + str(initials) + ". До срока замены паспорта более года. На данный момент вам не стоит беспокоиться по этому поводу.")
                    elif int(after) <= 90:
                        count = - (int(after) - 90)
                        output.set("Здравствуйте, " + str(initials) + ". На данный момент вам " + str(your_ages) + " лет. " + "Если вы до сих пор не поменяли паспорт, сделайте это в ближайшем МФЦ. У Вас осталось " + str(count) + " дней на замену. Если вы не поменяете паспорт в течении этого времени, на Вас будет наложен штраф.")
                    else:
                        count = int(after) - 90
                        output.set("Здравствуйте, " + str(initials) + ". На данный момент вам " + str(your_ages) + " лет. " + "Если вы до сих пор не поменяли паспорт, сделайте это в ближайшем МФЦ. У вас просрочка в " + str(count) + " дней. Не забудьте оплатить штраф.")

                else:
                    before = before_replace(day_num_cal, month_num_cal, year_num_cal, now_day, now_month, your_ages)
                    if before == 0:
                        output.set("С днём рождения, " + str(initials) + "! На данный момент вам " + str(
                            your_ages + 1) + " лет. " + "Поменяйте паспорт в течении следующих 90 дней.")
                    else:
                        output.set("Здравствуйте, " + str(initials) + ". На данный момент вам " + str(
                            your_ages) + " лет. " + "До замены паспорта осталось " + str(before) + " дней.")
            else:
                output.set("Здравствуйте, " + str(
                    initials) + ". До срока замены паспорта более года. На данный момент вам не стоит беспокоиться по этому поводу.")



    else:
        errmsg_name.set("Некорректные данные")

check = (window.register(validate_username), "%P")

errmsg_name = StringVar()
errmsg_date = StringVar()

entry_name = Entry(window, validate="key", validatecommand=check, width=40)

lbl_error_name = Label(foreground="red", textvariable=errmsg_name, wraplength=250)
lbl_error_date = Label(foreground="red", textvariable=errmsg_date, wraplength=250)

lbl_date = Label(window, text="Дата рождения: ")

cal = DateEntry(window, selectmode='day', background="#AAA")

btn_calculation = Button(window, text="Произвести рассчет", relief=GROOVE, command=test1)

output = StringVar()
output.set("Здесь будет результат")
lbl_output = Label(window, textvariable=output, wraplength=250)

lbl_description.grid(row=0, column=0, columnspan=2)
lbl_input.grid(row=1, column=0, columnspan=2)
lbl_name.grid(row=2, column=0, sticky=W, padx=10)
entry_name.grid(row=2, column=1, sticky=W)
lbl_error_name.grid(row=3, column=1, columnspan=1, sticky=W)
lbl_date.grid(row=4, column=0, columnspan=1, sticky=W, padx=10)
cal.grid(row=4, column=1, sticky=W)
lbl_error_date.grid(row=5, column=1, columnspan=1, sticky=W)
btn_calculation.grid(row=6, column=0, columnspan=2, sticky=N, pady=30)
lbl_output.grid(row=7, column=0, columnspan=2)
window.mainloop()
