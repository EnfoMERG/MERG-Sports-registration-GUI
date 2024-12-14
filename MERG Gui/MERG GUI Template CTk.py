
from tkinter import ttk
from customtkinter import *

options = ["KB", "MB", "GB", "GiB"]

def ende():
    fenster.destroy()

fenster = CTk()
fenster.title("Byte-Rechner") 
fenster.configure(bg="#474448")
fenster.wm_geometry( '400x350' )

def umrechnen():
    try:
        zahl = float(etEingabe.get())
        einheit = combobox.get()
        if einheit == "GB":
            lbAusgabe["text"] = zahl * 0.000000001, "GB"
        elif einheit == "GiB":
            lbAusgabe["text"] = zahl * 0.000000000931323, "GiB"
        elif einheit == "MB":
            lbAusgabe["text"] = zahl * 0.000001, "MB"
        elif einheit == "KB":
            lbAusgabe["text"] = zahl * 0.001, "KB"
    except:
        lbAusgabe["text"] = "keine Zahl!"


etEingabe = CTkEntry(fenster)                            
etEingabe.grid(row=0, column=1,sticky="w", padx=5, pady=5)

lbEingabe = CTkLabel(fenster, text="Angabe in Byte :")          
lbEingabe.grid(row=0, column=0, sticky="w", padx=5, pady=5)

lbUmrechnen = CTkLabel(fenster, text="Umrechnen zu :" )          
lbUmrechnen.grid(row=1, column=0, sticky="w", padx=5, pady=5)

combobox = ttk.Combobox(fenster, values= options)
combobox.grid(row=1 ,column=1, sticky="W", padx=5, pady=5)

buEquals = CTkButton(fenster, text=" = ", command=umrechnen, corner_radius=30, fg_color="#F57449", hover_color="#BBCEF9")   
buEquals.grid(row=3, column=0, sticky="w", padx=5, pady=5)

lbAusgabe = CTkLabel(fenster, text="" )                  
lbAusgabe.grid(row=3, column=1, sticky="w", padx=5, pady=5 )

fenster.mainloop()