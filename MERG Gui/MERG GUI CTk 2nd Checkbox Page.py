from customtkinter import *
from PIL import Image

imgPillow = Image.open("C:\\Users\\TUFFTHYMEZ\\Desktop\\Python\\GUI UX\\Tkinter\\MERG Gui\\MERG Pillow.PNG")

def end():
    fenster.destroy()

fenster = CTk()
fenster.geometry("900x700")
fenster.title("MERG Sports")
fenster.configure(bg="#BBCEF9")

optChoice = ["Dark Mode", "Light Mode"]  # OptionMenu btn mit light/dark-mode 

def optionmenu_callback(choice):
    choise = optionmenu.get()
    if choice == "Dark Mode":
        set_appearance_mode("dark")
        change_text_color("#BBCEF9")
    else:
        set_appearance_mode("light")
        change_text_color("#474448")

def change_text_color(color):
    ckbLaufen.configure(text_color=color)
    ckbGewichtHeben.configure(text_color=color)
    ckbFahrrad.configure(text_color=color)
    ckbWandern.configure(text_color=color)
    ckbSchwimmen.configure(text_color=color)
    

set_appearance_mode("dark")

optionmenu = CTkOptionMenu(fenster, values=optChoice, command=optionmenu_callback, fg_color="#F57449",button_color="#F57449", text_color="#141204", font=("Comic Sans MS", 13))
optionmenu.place(x=760, y=29)

lbPillow = CTkLabel(master=fenster,text="", image=CTkImage(dark_image=imgPillow, light_image=imgPillow,size=(100,100)) )
lbPillow.place(relx=0, rely=0.05)

lbOrangeBlock = CTkLabel(master=fenster, text="",bg_color="#F57449",width=900)
lbOrangeBlock.grid(row=0)

ckbLaufen = CTkCheckBox(master=fenster, text="LAUFEN", text_color="#BBCEF9", font=("Comic Sans MS", 15))
ckbLaufen.place(relx=0.3, rely=0.3, anchor="w")

ckbGewichtHeben = CTkCheckBox(master=fenster, text="GEWICHTHEBEN", text_color="#BBCEF9", font=("Comic Sans MS", 15))
ckbGewichtHeben.place(relx=0.3, rely=0.37, anchor="w")

ckbFahrrad = CTkCheckBox(master=fenster, text="FAHRRADFAHREN", text_color="#BBCEF9",font=("Comic Sans MS", 15))
ckbFahrrad.place(relx=0.3, rely=0.44, anchor="w")

ckbSchwimmen = CTkCheckBox(master=fenster, text="SCHWIMMEN", text_color="#BBCEF9",font=("Comic Sans MS", 15))
ckbSchwimmen.place(relx=0.3, rely=0.51, anchor="w")

ckbWandern = CTkCheckBox(master=fenster, text="WANDERN", text_color="#BBCEF9",font=("Comic Sans MS", 15))
ckbWandern.place(relx=0.3, rely=0.58, anchor="w")

btnRegister = CTkButton(master=fenster, text="Registrieren", text_color="#141204",font=("Comic Sans MS", 18), fg_color="#F57449", hover_color="#BBCEF9")
btnRegister.place(relx=0.5, rely=0.8, anchor="center")

fenster.mainloop()