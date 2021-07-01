from pyowm import OWM
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Прогноз погоды")
root.geometry("600x400")
owm = OWM('5f7824a443dbc21ce8769e57ca5fe2bd')
Label(root, text="Прогноз погоды", font="Consolas 15 bold", bg="white").pack(pady=10)
Label(root, text="Укажите название города: ", font="Consolas 11 bold", bg="white").pack(pady=10)

a = Entry(root, width=40)
a.pack()
Label(root, text="Температура °С: ", font="Consolas 11 bold", bg="white").pack(pady=10)
b = Entry(root, width=40)
b.pack()

def temp():
    place = a.get()
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    messagebox.showinfo("Weather", f'В городе {place} температура {temp} °С')
    b.insert(0, temp)

def details():
    place = a.get()
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    w.wind()
    w.humidity()
    w.rain()
    w.heat_index()
    print(w)
    messagebox.showinfo("Weather", w)

Button(root, text="Узнать температуру", command=temp).pack(pady=10)

root.mainloop()


