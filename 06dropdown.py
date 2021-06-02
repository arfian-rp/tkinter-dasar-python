from tkinter import *

def dropdown():
    print('hasil dari menu tsb')

root=Tk()
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label='file',menu=submenu)
submenu.add_command(label='new project',comand=dropdown())

root.mainloop()