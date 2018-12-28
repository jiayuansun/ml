from tkinter import *
from tkinter import ttk
import sqlite3





def main():
    window = Tk()
    
    window.title("Ahelper")
    window.geometry('800x200') 

    tab_control = ttk.Notebook(window)
 
    tab1 = ttk.Frame(tab_control)
 
    tab2 = ttk.Frame(tab_control) 
    tab_control.add(tab1, text='First') 
    tab_control.add(tab2, text='Second')


    btn = Button(tab1, text="Click Me") 
    btn.grid(column=6, row=2)

    height = 5
    width = 3
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = Entry(tab1, text="")
            b.grid(row=i, column=j)

    tab_control.pack(expand=1, fill='both')

    window.mainloop()

if __name__=="__main__":
    main()