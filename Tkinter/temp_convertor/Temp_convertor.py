from tkinter import *


def cel_convt():
    # convert temp
    cels = float(user_temp.get())
    conv_farh = round((1.8 * cels) + 32, 2)
    conv_kelv = round(cels + 273.15, 2)
    cels_output.config(text=f'{cels} °C')
    farh_output.config(text=f'{ conv_farh} °F')
    kelv_output.config(text=f'{conv_kelv} °K')


def far_convt():
    farh = float(user_temp.get())
    conv_cels = round((farh - 32) * 0.5556, 2)
    conv_kelv = round(conv_cels + 273.15, 2)
    cels_output.config(text=f'{conv_cels} °C')
    farh_output.config(text=f'{farh} °F')
    kelv_output.config(text=f'{conv_kelv} °K')

def kel_convt():
    kelvh = float(user_temp.get())
    conv_cels = round(kelvh - 273.15, 2)
    conv_farh = round((1.8 * conv_cels) + 32, 2)
    cels_output.config(text=f'{conv_cels} °C')
    farh_output.config(text=f'{ conv_farh} °F')
    kelv_output.config(text=f'{kelvh} °K')



window = Tk()
window.title("Temperature Convertor")
window.config(padx=25, pady=25)

# Celsius
user_temp = Entry(width=10,font=('Arial', 18))
user_temp.grid(column=0, row=1)

cels_input = Button(text='Celsius', command=cel_convt)
cels_input.grid(column=1, row=0)

cels_output = Label(text='Celsius')
cels_output.grid(column=2, row=0)

#Farhanite

farh_input = Button(text='Fahrenheit', command=far_convt)
farh_input.grid(column=1, row=1)

farh_output = Label(text='Fahrenheit')
farh_output.grid(column=2, row=1)

#Kelvin


kelv_input = Button(text='Kelvin',command=kel_convt)
kelv_input.grid(column=1, row=2)

kelv_output = Label(text='Kelvin')
kelv_output.grid(column=2, row=2)

window.mainloop()
