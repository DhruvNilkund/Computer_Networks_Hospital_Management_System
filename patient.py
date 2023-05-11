import tkinter as tk
import socket
from tkinter import *
from VotingPage import admitpg

def establish_connection():
    host = '10.30.205.53'
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'

def taking_data_voter1(name,gender,zone,city,passw):
    client_socket1 = establish_connection()
    if(client_socket1 == 'Failed'):
        message = "Connection failed"
    message="9"+name+" "+gender+" "+zone+" "+city+" "+passw+" "
    client_socket1.send(message.encode()) #2
    message = client_socket1.recv(1024)
    vid = message.decode()
    client_socket1.close()
    return vid

def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        admitpg(root, frame1, client_socket)

    elif(message=="Patient Admitted"):
        message = "Patient admitted"
        failed_return(root,frame1,client_socket,message)

    elif(message=="Invalid Patient"):
        message = "Invalid patient"
        failed_return(root,frame1,client_socket,message)

    else:
        #message = "Server Error"
        #failed_return(root,frame1,client_socket,message)
        client_socket.close()
        sub = Button(frame1, text="Discharge", width=10, command = lambda: discharge_server(voter_ID, password))
        Label(frame1, text="").grid(row = 4,column = 0)
        sub.grid(row = 5, column = 3, columnspan = 2)

def discharge_server(voter_ID,password):
    client_socket1 = establish_connection()

    message ="8"+voter_ID + " " + password
    client_socket1.send(message.encode()) #2

    message = client_socket1.recv(1024) #Authenticatication message
    message = message.decode()
    client_socket1.close()

    # if(message=="Authenticate"):
    #     admitpg(root, frame1, client_socket)

    # elif(message=="Patient Admitted"):
    #     message = "Patient admitted"
    #     failed_return(root,frame1,client_socket,message)

    # elif(message=="Invalid Patient"):
    #     message = "Invalid patient"
    #     failed_return(root,frame1,client_socket,message)

    # else:
        
    #     failed_return(root,frame1,client_socket,message)



def Login(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Patient Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Patient Login", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Patient ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:   ", anchor="e", justify=LEFT).grid(row = 3,column = 0)

    Patient_ID = tk.StringVar()
    name = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = Patient_ID)
    e1.grid(row = 2,column = 2)
    e3 = Entry(frame1, textvariable = password, show = '*')
    e3.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=10, command = lambda: log_server(root, frame1, client_socket, Patient_ID.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         voterLogin(root,frame1)
