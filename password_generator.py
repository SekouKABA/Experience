from  tkinter import *
from random import randint, choice
import string
from turtle import right

def generate_password():
    password_min =6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    alea=randint(password_min,password_max)
    password = "".join(choice(all_chars) for i in range(alea))
    password_entry.delete(0,END)
    password_entry.insert(0,password)



window = Tk()
window.title("Générateur de mot de passe")
window.geometry("700x630")
window.config(bg="#4065A4")
frame = Frame(window,bg="#4065A4")
# creation d'image
width = 400
height =500
image = PhotoImage(file="mot-de-passe (1).png").zoom(35).subsample(32)
canvas = Canvas(frame,width=width, height=height, bg="#4065A4", bd =0,highlightthickness=0)
canvas.create_image(width/2, height/2, image = image)
canvas.grid(row=0, column=0, sticky=W)
right_frame = Frame(frame,bg="#4065A4")
sub_title =Label(right_frame,text="Mot de passe", font=("Helvetica",20),bg="#4065A4",fg="white").pack()
password_entry= Entry(right_frame,
                font=("Helvetica",20), bg ="#4065A4",fg="white")
password_entry.pack()
geneerate_password_button=Button(right_frame, text ="Generer", font=("Helvetica",20), bg ="#4065A4",fg="white", 
                            command=generate_password)
geneerate_password_button.pack()

right_frame.grid(row=0,column=1, sticky=W)

frame.pack(expand=YES)


# creation d'une barre de menu
menu_bar=Menu(window)
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Nouveau", command = generate_password)
menu_bar.add_cascade(label="Fichier",menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()