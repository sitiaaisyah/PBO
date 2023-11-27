import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    a_segitiga = float(txtalas_segitiga.get())
    t_segitiga = float(txttinggi_segitiga.get())
    t_prisma = float(txttinggi_prisma.get())

    L = (a_segitiga * t_prisma) + 2 * (0.5 * a_segitiga * t_segitiga)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    a_segitiga = float(txtalas_segitiga.get())
    t_segitiga = float(txttinggi_segitiga.get())
    t_prisma = float(txttinggi_prisma.get())

    V = 0.5 * a_segitiga * t_segitiga * t_prisma

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas Permukaan dan Volume Prisma Segitiga")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Siti Aisyah") 
nama.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5,)

# Label Alas Segitiga
a_segitiga = Label(frame, text="Alas Segitiga :") 
a_segitiga.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga
t_segitiga = Label(frame, text="Tinggi Segitiga :")
t_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Prisma
t_prisma = Label(frame, text="Tinggi Prisma :")
t_prisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Alas Segitiga
txtalas_segitiga = Entry(frame)
txtalas_segitiga.grid(row=1, column=1)

#Textbox Tinggi Segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1)

# Textbox Tinggi Prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume : ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry (frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()