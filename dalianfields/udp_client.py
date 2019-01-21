
from socket import *
import logging

def anheng_udp_client(mesg_list):


    try:
        ADDR = ("192.168.109.140", 514)
        udpCliSock = socket(AF_INET, SOCK_DGRAM)
        #udpCliSock.bind(("10.74.154.21", 5140))
        logging.warning("udp client send syslog number is " + str(len(mesg_list)))
        for syslog in mesg_list:
            udpCliSock.sendto(syslog, ADDR)
        udpCliSock.close()
    except Exception as e:
        logging.error("anheng_udp_client except {0}".format(e), exc_info=True)


if __name__ == "__main__":
    str1 = "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    str2 = "sfdsdfdadfadfadfa"
    list1 = [str1, str2]
    anheng_udp_client(list1)