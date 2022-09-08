from tkinter import *
from turtle import left
import webbrowser

def lien():
    return webbrowser.open_new("http://matchendirect.fr")

window = Tk()
cadre=Frame(window,bg="#8FD7A5", bd=4)
cadre.pack(expand=YES)
window.title("Ma fenêtre")
window.geometry("600x400")
window.minsize(480,360)
window.iconbitmap("one-piece.ico")
window.config(background="#8FD7A5")


label_title = Label(cadre,text="BIENVENUE MES FRERES",bd="4",
                    font =("Arial",30), bg= "#8FD7A5",fg="white").pack()
label_subtitle=Label(cadre, text =" Je suis ravi de vous voir",
                    font=("Courrier",20), bg = "#8FD7A5", fg="white").pack()

myclick = Button(cadre, text="Pour voir les matches",
                font =("Arial",15), bg= "white",fg="#8FD7A5", command=lien).pack(pady=25, fill = X)



window.mainloop()