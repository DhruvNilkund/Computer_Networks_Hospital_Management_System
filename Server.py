import socket
import threading
import dframe as df
from threading import Thread
from dframe import *
import dframe as df

lock = threading.Lock()

def client_thread(connection):

    data = connection.recv(1024)     #receiving voter details            #2

    #verify voter details
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    if(df.verify(log[0],log[1])):                                #3 Authenticate
        if(df.isEligible(log[0])):
            print('Patient Logged in... ID:'+str(log[0]))
            connection.send("Authenticate".encode())
        else:
            print('Patient admitted by ID:'+str(log[0]))
            connection.send("Patient Amitted".encode())
    else:
        print('Invalid patient')
        connection.send("Invalid patient".encode())


    data = connection.recv(1024)                                    #4 Get Vote
    print("patient admitted from ID: "+str(log[0])+"  Processing...")
    lock.acquire()
    #update Database
    if(df.vote_update(data.decode(),log[0])):
        print("patient admitted by voter ID = "+str(log[0]))
        connection.send("Successful".encode())
    else:
        print("patient admission update failed by voter ID = "+str(log[0]))
        connection.send("patient admission update Failed".encode())
                                                                        #5

    lock.release()
    connection.close()

def taking_data_voter1(name,gender,zone,city,passw):
    vid=df.taking_data_voter(name,gender,zone,city,passw)
    return vid

def voting_Server():

    serversocket = socket.socket()
    host = '10.30.203.53'
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())   ### 1
        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
