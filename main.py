from tkinter import *
import re
from tkcalendar import DateEntry

window = Tk()
window.title("Когда менять паспорт")
window.geometry('400x550+760+250')

frame_input = Frame(border=1, background='red')
lbl_description = Label(window,
                        text="Данная программа поможет Вам рассчитать через какой промежуток времени Вам нужно поменять паспорт",
                        wraplength=390, justify=CENTER, padx=10, pady=10)
lbl_input = Label(window, text="Для этого Вам необходимо ввести свои ФИО и дату рождения", wraplength=390,
                  justify=CENTER, padx=10, pady=10)
lbl_name = Label(frame_input, text="ФИО: ", wraplength=390, padx=10, pady=0, background="#FFCDD2")
# entry_name = Entry()


def validate_username(username):
    result = re.match("[а-яА-ЯёЁ ]+$", username) is not None
    if not result and len(username) <= 50:
        errmsg.set("Используйте только кириллицу")
        # print("Ошибочный символ: " + str(result) + " " + username)
    else:
        errmsg.set("")
        # print("Верный символ: " + str(result) + " " + username)
    return result


check = (window.register(validate_username), "%P")

errmsg = StringVar()

entry_name = Entry(frame_input, validate="key", validatecommand=check, width=50)
lbl_error = Label(foreground="red", textvariable=errmsg, wraplength=250, background="#FFCDD2")

# lbl_entry = Label(window, textvariable=entry_name, wraplength=390, padx=10, pady=0, background="#FFCDD2")

frame_date = Frame(border=1, background='green')
lbl_date = Label(frame_date, text="Дата рождения: ", padx=30, background="#FFCDD2")

cal = DateEntry(frame_date, selectmode='day', year=2022, month=12, day=17, background="#b8b8b8")

frame_calculation = Frame(border=1, background='blue')
btn_calculation = Button(frame_calculation, text="Произвести рассчет", relief=GROOVE)

frame_calculation2 = Frame(border=1, background='red')
btn_calculation2 = Button(frame_calculation2, text="а")

lbl_description.grid(row=0, column=0)
lbl_input.grid(row=1, column=0)
lbl_name.grid(row=2, column=0)
entry_name.grid(row=2, column=1)
frame_input.grid(row=2, column=2)
lbl_error.grid(row=0, column=0)
lbl_date.grid(row=0, column=0)
frame_date.grid(row=0, column=0)
cal.grid(row=0, column=0)
btn_calculation.grid(row=0, column=0)
frame_calculation.grid(row=0, column=0)
btn_calculation.grid(row=0, column=0)
frame_calculation2.grid(row=0, column=0)

# lbl_description.pack(side=TOP)
# lbl_input.pack(side=TOP)
# lbl_name.pack(side=LEFT)
# entry_name.pack(side=LEFT)
# frame_input.pack(side=TOP)
# lbl_error.pack(side=TOP)
# lbl_date.pack(side=LEFT)
# frame_date.pack(side=LEFT, anchor=N)
# cal.pack(side=TOP)
# btn_calculation.pack()
# frame_calculation.pack(side=TOP)
# btn_calculation2.pack()
# frame_calculation2.pack(side=TOP)



# lbl_entry.pack()
# entry_name.pack()
window.mainloop()
