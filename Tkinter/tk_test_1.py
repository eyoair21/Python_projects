from tkinter import *



window = Tk()
window.title("Test GPU")
window.minsize(width=500,height=600)

my_label = Label(text='I am label',font=('Arial',24,'bold'))
my_label.pack()



def button_clicked():
   print(' I got Clicked')
   new_text = input.get()
   my_label.config(text= new_text)



#buttton
button = Button(text ='Generate', command=button_clicked)
button.pack()


input = Entry(width=10)
input.pack()


input.pack()





window.mainloop()
