import flet as ft

def main(page: ft.Page):
    page.title = "Calkulator Luas Tanah"

    def btn_click(e):
        Panjang_Tanah.value = int(Panjang_Tanah.value)
        Lebar_Tanah.value = int(Lebar_Tanah.value)
        if not Panjang_Tanah.value:
            Panjang_Tanah.error_text = "Mohon masukkan nilai!"
            page.update()
        else:
            Luas = Panjang_Tanah.value * Lebar_Tanah.value
            if Lebar_Tanah.value < 9999 and Lebar_Tanah.value >= 1 :
                dlg = ft.AlertDialog(
                    title=ft.Text(f"Luas Tanah Anda Adalah {Luas}!"), on_dismiss=lambda e: print("Dialog dismissed!"))
                page.dialog = dlg
                dlg.open = True 
                page.update()
            else:
                Lebar_Tanah.error_text = "Masukkan nilai dari 1-9999 !"
                page.update()

    Panjang_Tanah = ft.TextField(label="Panjang_Tanah")
    Lebar_Tanah = ft.TextField(label="Lebar_Tanah")
    

    page.add(Panjang_Tanah, Lebar_Tanah, ft.ElevatedButton("hitung!", on_click=btn_click))

ft.app(main)