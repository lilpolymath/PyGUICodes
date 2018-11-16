from socket import *

sequence = 0
done = "0"
connectMag = "connect"
serverName = "Favour-PC" #Name of the PC
serverPort = 12000

opp = ""
oppPort = ""

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(connectMag, (serverName,serverPort))
msg = clientSocket.recv(1024)
print msg
while done == "0":
	confirmP = clientSocket.recv(1024)
	print confirmP
	opp = clientSocket.recv(1024)
	print opp
	oppPort = int(clientSocket.recv(1024))

	done = "1"

clientSocket.close()