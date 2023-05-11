import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Patient Admitted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="No Beds Available... \nTry Different department", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def admitpg(root,frame1,client_socket):

    root.title("Admit Patient")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Admit Patient", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "GENERAL\n\nGENERAL", variable = vote, value = "GENERAL", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"GENERAL",client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("i1.png")).resize((45,45),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "CARDIIAC\n\nCARDIIAC", variable = vote, value = "CARDIIAC", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"CARDIIAC",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("i2.png")).resize((35,48),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "DENTAL\n\nDENTAL", variable = vote, value = "DENTAL", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"DENTAL",client_socket) ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("i3.png")).resize((55,40),Image.ANTIALIAS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "NEURAL\n\nNEURAL", variable = vote, value = "NEURAL", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"NEURAL",client_socket)).grid(row = 5,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("i4.png")).resize((50,45),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nGYNO    \n nGYNO ", variable = vote, value = "GYNO", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"GYNO",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("i5.png")).resize((45,35),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
