from tkinter import *
class ConvetTemp():
    def __init__(self, inp_temp):
        self.int_temp = inp_temp

    def cel_convt(self):
        # convert temp
        cels = float(self.int_temp)
        conv_farh = round((1.8 * cels) + 32, 2)
        conv_kelv = round(cels + 273.15, 2)

    def far_convt(self):
        farh = float(self.int_temp)
        conv_cels = round((farh - 32) * 0.5556, 2)
        conv_kelv = round(conv_cels + 273.15, 2)


    def kel_convt(self):
        kelvh = float(self.int_temp)
        conv_cels = round(kelvh - 273.15, 2)
        conv_farh = round((1.8 * conv_cels) + 32, 2)
