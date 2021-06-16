import tkinter as tk
from decimal import *
btn_width = 4
btn_height = 1


def onclick():
    exit()


def summation():
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, Decimal(first_entry.get()) + Decimal(second_entry.get()))


def subtraction():
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, Decimal(first_entry.get()) - Decimal(second_entry.get()))


def multiplication():
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, Decimal(first_entry.get()) * Decimal(second_entry.get()))


def power():
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, Decimal(first_entry.get()) ** Decimal(second_entry.get()))


def delete_all_entries():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)


def persent():
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, Decimal(first_entry.get()) / 100 * Decimal(second_entry.get()))


def division():
    answer_entry.delete(0, tk.END)
    if Decimal(second_entry.get()) == 0:
        answer_entry.insert(0, 'Division error(zero division)')
    else:
        answer_entry.insert(0, Decimal(first_entry.get()) / Decimal(second_entry.get()))


win = tk.Tk()
win.title('Maybe some calc?')
win.geometry('210x400')
ext_btn = tk.Button(win, command=onclick, text='Exit')
ext_btn.place(x=10, y=350)
first_entry = tk.Entry(win, width=25)
first_entry.place(x=10, y=0)
second_entry = tk.Entry(win, width=25)
second_entry.place(x=10, y=40)
plus_btn = tk.Button(win, command=summation, text='+', width=btn_width, height=btn_height)
plus_btn.place(x=10, y=90)
minus_btn = tk.Button(win, command=subtraction, text='-', width=btn_width, height=btn_height)
minus_btn.place(x=60, y=90)
mult_btn = tk.Button(win, command=multiplication, text='*', width=btn_width, height=btn_height)
mult_btn.place(x=110, y=90)
division_btn = tk.Button(win, command=division, text='/', width=btn_width, height=btn_height)
division_btn.place(x=160, y=90)
del_btn = tk.Button(win, command=delete_all_entries, text='CE', width=btn_width, height=btn_height)
del_btn.place(x=10, y=60)
power_btn = tk.Button(win, command=power, text='**', width=btn_width, height=btn_height)
power_btn.place(x=10, y=120)
persent_btn = tk.Button(win, command=persent, text='%', width=btn_width, height=btn_height)
persent_btn.place(x=60, y=120)
answer_frame = tk.Frame(win, width=190, height=40, relief='ridge', borderwidth=10, bg='red')
answer_frame.place(x=10, y=150)
answer_entry = tk.Entry(win, width=28)
answer_entry.place(x=20, y=160)
tk.mainloop()
