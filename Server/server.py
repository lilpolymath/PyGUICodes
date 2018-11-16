from socket import *
import threading


class roomThread(threading.Thread):

	#This is a thread that will handle matching 2 clients to each other
	def __init__(self, name, client1IP, clientIP, client2IP, client2P, port):
		threading.Thread.__init__(self)
		self.name = name
		self.client1 = (client1IP, client1P)
		self.client2 = (client2IP, client2P)
		self.port	 = port
		self.done	 = 0
		
		#For clints to communicate directly you need to send to each the other's
		#information which includes their IP addressand the port they are using to communicate
	def run(self):
		connectMag = str(self.port)
		playerNum  = 1
		sequence   = 0
		roomSocket = socket(AF_INIT, SOCK_DGRAM)
		roomSocket.bind(('', self.port))

		roomSocket.sendto(connectMag, self.client1)
		roomSocket.sendto(connectMag, self.client2)

		roomSocket.sendto(self.client2[0], self.client1)
		roomSocket.sendto(str(self.client2[1]), self.client)

		roomSocket.sendto(self.client1[0], self.client2)
		roomSocket.sendto(str(self.client1[1]), self.client)
		print "Done"

userID = 1
userList = ()
userPort = ()
roomID = 1
count = 0
client1  = ()
client2  = ()
done = 0
portNum = 12000
port = 12000
serverSocket = socket(AF_INIT, SOCK_DGRAM)
serverSocket.bind(('',portNum))

while True:
	connectReq, userAddr = serverSocket.recvfrom(1024)
	userlist += userAddr
	serverSocket.sendto(str(userID), userAddr)

	if userID%2 == 0 and .5*userID == roomID:
		pList = list(userList)
		port += 1
		room = roomThread(roomID, pList,[count], pList[count+1], pList[count+2], pList[count+3], port)
		room.start()
		count =+ 4
		roomID =+ 1
		print "Room created"
	userID += 1