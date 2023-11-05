import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas():
    j = float(txtjari_jari.get())
    t = float(txtTinggi.get())
    gp = float(txtgaris_pelukis.get())

    L = pi * j * (j + gp)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    j = float(txtjari_jari.get())
    t = float(txtTinggi.get())
    gp = float(txtgaris_pelukis.get())

    v = (1/3) * pi * (j ** 2) * t
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas Permukaan dan Volume Kerucut")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Siti Aisyah") 
nama.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5,)

# Label jari-jari
j = Label(frame, text="Jari-Jari :") 
j.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
t = Label(frame, text="Tinggi :") 
t.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Label Garis Pelukis
gp = Label(frame, text="Garis Pelukis :") 
gp.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Textbox
txtjari_jari= Entry(frame)
txtjari_jari.grid(row=1, column=1, sticky=W, padx=5, pady=5)

#Textbox
txtTinggi= Entry(frame)
txtTinggi.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#Textbox
txtgaris_pelukis= Entry(frame)
txtgaris_pelukis.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label(frame, text="Volume : ")
Volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()