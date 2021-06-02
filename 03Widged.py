from tkinter import *

root = Tk()
satu = Label(root, text="Judul program", bg='red', fg='white')
dua = Label(root, text="keterangan", bg='purple', fg='white')
tiga = Label(root, text="Input", bg='blue', fg='black')

satu.pack()
dua.pack(fill=X)
tiga.pack(side=RIGHT, fill=Y)
root.mainloop()