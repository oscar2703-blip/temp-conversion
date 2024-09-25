from tkinter import*
import tkinter.font as font
window = Tk()

def convert():
    temp_celsius = celsius_value.get()
    if(temp_celsius.replace(".",'',1).isdigit()):
        error_msg.grid_forget()
        temp_fahrenheit = (float(temp_celsius)*9/5) + 32
        output_fahrenheit.config(text = "Temperature in farhenheit: " + str(temp_fahrenheit))
    else:
        error_msg.grid(row=1, column=1)

window.title("Celsius to Fahrenheit Converter")
description = Label(text = "Celsius -> Fahrenheit", font = font.Font(size = 20), fg = "")
description.pack()