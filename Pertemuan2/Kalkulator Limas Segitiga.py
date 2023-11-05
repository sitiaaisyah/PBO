import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    alas = float(txtalas.get())
    t_limas = float(txttinggi_limas.get())
    t_segitiga = float(txttinggi_segitiga.get())

    L = (alas * t_limas) / 2 + 3 * (0.5 * alas * t_segitiga)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    alas = float(txtalas.get())
    t_limas = float(txttinggi_limas.get())
    t_segitiga = float(txttinggi_segitiga.get())

    V = (alas ** 2 * t_segitiga) / 6

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas Permukaan dan Volume Limas Segitiga")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Siti Aisyah") 
nama.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5,)

# Label Alas
alas = Label(frame, text="Alas :") 
alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Limas
t_limas = Label(frame, text="Tinggi Limas :")
t_limas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Prisma
t_segitiga = Label(frame, text="Tinggi Segitiga :")
t_segitiga.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Alas 
txtalas = Entry(frame)
txtalas.grid(row=1, column=1)

#Textbox Tinggi Segitiga
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=2, column=1)

# Textbox Tinggi Prisma
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=3, column=1)

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