from tkinter import *
from tempconv import ConvetTemp

window = Tk()
window.title("Temperature Convertor")
window.config(padx=25, pady=25)



#Temp input
user_temp = Entry(width=10,font=('Arial', 18))
user_temp.grid(column=0, row=1)
temp_convt = ConvetTemp(user_temp)

# Celsius
cels_input = Button(text='Celsius', command=temp_convt.cel_convt)
cels_input.grid(column=1, row=0)
cels_output = Label(text='Celsius')
cels_output.grid(column=2, row=0)

#Farhanite
farh_input = Button(text='Fahrenheit', command=temp_convt.far_convt)
farh_input.grid(column=1, row=1)
farh_output = Label(text='Fahrenheit')
farh_output.grid(column=2, row=1)

#Kelvin
kelv_input = Button(text='Kelvin', command=temp_convt.kel_convt)
kelv_input.grid(column=1, row=2)

kelv_output = Label(text='Kelvin')
kelv_output.grid(column=2, row=2)

window.mainloop()
