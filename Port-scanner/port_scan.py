#!/usr/bin/env python
# coding: utf-8

# In[4]:


import socket


Common_TCP_ports = [
    21, 22, 23, 25, 53, 80, 88, 110, 135, 139,
    143, 161, 389, 443, 445, 587, 993, 995,
    1433, 3306, 3389, 8080
]

Common_UDP_ports = [
    53, 67, 69, 88, 123, 135, 161, 389, 3389
]

# Common network ports and their typical services:
# 21: FTP, 22: SSH, 23: Telnet, 25: SMTP, 53: DNS, 67: DHCP server, 69: TFTP,
# 80: HTTP, 88: Kerberos, 110: POP3, 123: NTP, 135: RPC endpoint mapper,
# 139: NetBIOS, 143: IMAP, 161: SNMP, 389: LDAP, 443: HTTPS, 445: SMB,
# 587: SMTP (submission), 993: IMAPS, 995: POP3S, 1433: MS SQL, 3306: MySQL,
# 3389: RDP, 8080: HTTP alternative/proxy

#local_ip = input("Enter target ip: ") #originally user input determined the scan legacy*
#print(Target_ip)

#WAS GLOBAL, MOVED INTO FUNCTIONS
#local_ip = socket.gethostbyname(str(socket.gethostname())) #automatically grabs device IP address
#print(f"scanning ports @: {local_ip}")

def tcp_scan(ip=socket.gethostbyname(str(socket.gethostname()))):
    #local_ip = socket.gethostbyname(str(socket.gethostname())) #automatically grabs device IP address

    TCP_Open_ports = []

    for port in Common_TCP_ports:
        is_open = False
        TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #^^THIS ONLY CHECKS TCP^^ WILL BE UPDATED TO CHECK UDP ASWELL
        output = TCP_socket.connect_ex((ip,port))
        if output == 0:
            is_open = True
            print(f"Port {port} is open")
            TCP_Open_ports.append(port)
        else:
            print(f"Port {port} is closed or filtered")
        TCP_socket.close()
    #print(f"The following TCP ports are open: {TCP_Open_ports}") #will be fed as output to AI or ML later

    return TCP_Open_ports

def udp_scan(ip=socket.gethostbyname(str(socket.gethostname()))):
    #local_ip = socket.gethostbyname(str(socket.gethostname())) #automatically grabs device IP address

    UDP_Open_ports = []
    UDP_OF_ports = []

    for port in Common_UDP_ports:
        UDP_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        try: 
            UDP_socket.sendto(b'',(ip,port))
            UDP_socket.settimeout(2)
            data, address = UDP_socket.recvfrom(1024)
        except ConnectionResetError:
            print("Connection reset: No Active Connection: Port is closed")
            data = None
        except socket.timeout:
            print("Connection is open|filtered")
            UDP_OF_ports.append(port)
            data = None
        if data:
            print(f"Port {port} is open")
            UDP_Open_ports.append(port)
        UDP_socket.close()

    #if UDP_Open_ports != []:
            #print(f"The following UDP ports are open: {UDP_Open_ports}") #will be fed as output to AI or ML later

    #if UDP_OF_ports != []:
            #print(f"The following UDP ports are open|filtered: {UDP_OF_ports}") #will be fed as output to AI or ML later

    return UDP_Open_ports, UDP_OF_ports


def full_scan():

    #TAKE IN USER INPUT
    print('Enter an ip address or leave empty to scan your own:')
    ip = input()
    if (ip == ''):
        ip = socket.gethostbyname(str(socket.gethostname()))


    #RUN SCANS AND CAPTURE RETURN VALUES
    udp_open, udp_of = udp_scan(ip)
    tcp_open = tcp_scan(ip)

    return {
    "UDP_OPEN": udp_open,
    "UDP_OF": udp_of,
    "TCP_OPEN": tcp_open
    }

    #"UDP Open : " + UDP_Open_ports, "UDP OF : " + UDP_Open_ports, "TCP Open : " + TCP_Open_ports


#udp_scan()
#tcp_scan()
#full_scan()




# In[12]:


type(socket.gethostbyname(str(socket.gethostname())))


# In[ ]:





# In[ ]:




