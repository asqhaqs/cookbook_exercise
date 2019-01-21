from socket import *



def reciver():
    ADDR = ("10.74.154.21", 514)

    udpSocket=socket(AF_INET,SOCK_DGRAM)

    udpSocket.bind(ADDR)

    recvData = udpSocket.recvfrom(1024)

    print(recvData)

    udpSocket.close()

if __name__ == "__main__":


    reciver()