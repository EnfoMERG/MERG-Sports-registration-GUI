from customtkinter import *
from PIL import Image

imgPillow = Image.open("C:\\Users\\TUFFTHYMEZ\\Desktop\\Python\\GUI UX\\Tkinter\\MERG Gui\\MERG Pillow.PNG")

def end():
    fenster.destroy()

fenster = CTk()
fenster.geometry("900x700")
fenster.title("MERG Sports")
fenster.configure(bg="#474448")

optChoice = ["Light Mode", "Dark Mode"]  # OptionMenu btn mit light/dark-mode 

def optionmenu_callback(choice):
    if choice == "Dark Mode":
        set_appearance_mode("dark")
        change_text_color("#BBCEF9")
    else:
        set_appearance_mode("light")
        change_text_color("#474448")

def change_text_color(color):
    lbAcErstellen.configure(text_color=color)
    lbSchonReg.configure(text_color=color)
    btLogin.configure(text_color=color)
    entName.configure(text_color=color)
    entEmail.configure(text_color=color)
    entPW.configure(text_color=color)

set_appearance_mode("light")

optionmenu = CTkOptionMenu(fenster, values=optChoice, command=optionmenu_callback, fg_color="#F57449",button_color="#F57449", text_color="#141204", font=("Comic Sans MS", 13))
optionmenu.place(x=760, y=29)

lbPillow = CTkLabel(master=fenster,text="", image=CTkImage(dark_image=imgPillow, light_image=imgPillow,size=(100,100)) )
lbPillow.place(relx=0, rely=0.05)

lbOrangeBlock = CTkLabel(master=fenster, text="",bg_color="#F57449",width=900)
lbOrangeBlock.grid(row=0)

lbAcErstellen = CTkLabel(master=fenster, text="Account Erstellen", text_color="#474448", font=("Comic Sans MS", 30))
lbAcErstellen.place(relx=0.5, rely=0.2, anchor="center")

lbSchonReg = CTkLabel(master=fenster, text="Schon registriert?", text_color="#474448", font=("Comic Sans MS", 15))
lbSchonReg.place(relx=0.5, rely=0.3, anchor="center")

btLogin = CTkButton(master=fenster, text="Login", text_color="#474448", font=("Comic Sans MS", 15), fg_color="transparent", width=20, hover_color="#F57449")
btLogin.place(relx=0.6, rely=0.3, anchor="center")

entName = CTkEntry(master=fenster, placeholder_text="Name", text_color="#474448",font=("Comic Sans MS", 15))
entName.place(relx=0.5, rely=0.4, anchor="center")

entEmail = CTkEntry(master=fenster, placeholder_text="e-mail", text_color="#474448",font=("Comic Sans MS", 15))
entEmail.place(relx=0.5, rely=0.5, anchor="center")

entPW = CTkEntry(master=fenster, placeholder_text="Passwort", text_color="#474448",font=("Comic Sans MS", 15))
entPW.place(relx=0.5, rely=0.6, anchor="center")

entPW = CTkEntry(master=fenster, placeholder_text="Geburtstag TT.MM.JJJJ", text_color="#474448",font=("Comic Sans MS", 11))
entPW.place(relx=0.5, rely=0.7, anchor="center")

fenster.mainloop()