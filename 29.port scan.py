#!/bin/py
#   -*-coding:utf-8-*-
import sys
import subprocess
import socket
import threading
import time

class PortScanner:

    # default ports to be scanned
    # or put any ports you want to scan here!
    #__port_list = [1,3,6,9,13,17,19,20,21,22,23,24,25,30,32,37,42,49,53,70,79,80,81,82,83,84,88,89,99,106,109,110,113,119,125,135,139,143,146,161,163,179,199,211,222,254,255,259,264,280,301,306,311,340,366,389,406,416,425,427,443,444,458,464,481,497,500,512,513,514,524,541,543,544,548,554,563]
    __port_list=list(range(1,65500))
    # default thread number limit
    __thread_limit = 2000
    # default connection timeout time inseconds
    __delay = 6
    """
    Constructor of a PortScanner object

    Keyword arguments:
    target_ports -- the list of ports that is going to be scanned (default self.__port_list)
    """
    def __init__(self, target_ports = None):
        # If target ports not given in the arguments, use default ports
        # If target ports is given in the arguments, use given port lists
        if target_ports is None:
            self.target_ports = self.__port_list
        else:
            self.target_ports = target_ports


    """
    Return the usage information for invalid input host name. 
    """
    def __usage(self):
        print('python Port Scanner v0.1')
        print('please make sure the input host name is in the form of "something.com" or "http://something.com!"\n')


    """
    This is the function need to be called to perform port scanning

    Keyword arguments:
    host_name -- the hostname that is going to be scanned
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def scan(self, host_name, message = ''):

        if 'http://' in host_name or 'https://' in host_name:
            host_name = host_name[host_name.find('://') + 3 : ]

        print('*' * 60 + '\n')
        print('start scanning website: ' + str(host_name))

        try:
            server_ip = socket.gethostbyname(str(host_name))
            print('server ip is: ' + str(server_ip))

        except socket.error as e:
            # If the DNS resolution of a website cannot be finished, abort that website.

            #print(e)
            print('hostname %s unknown!!!' % host_name)

            self.__usage()

            return {}

            # May need to return specificed values to the DB in the future

        start_time = time.time()
        output = self.__scan_ports(server_ip, self.__delay, message)
        stop_time = time.time()

        print('host %s scanned in  %f seconds' %(host_name, stop_time - start_time))

        print('finish scanning!\n')

        return output


    """
    Set the maximum number of thread for port scanning

    Keyword argument:
    num -- the maximum number of thread running concurrently (default 1000)
    """
    def set_thread_limit(self, num):
        num = int(num)

        if num <= 0 or num > 50000:

            print('Warning: Invalid thread number limit! Please make sure the thread limit is within the range of (1, 50,000)!')
            print('The scanning process will use default thread limit!')

            return

        self.__thread_limit = num


    """
    Set the time out delay for port scanning in seconds

    Keyword argument:
    delay -- the time in seconds that a TCP socket waits until timeout (default 10)
    """
    def set_delay(self, delay):

        delay = int(delay)
        if delay <= 0 or delay > 100:

            print('Warning: Invalid delay value! Please make sure the input delay is within the range of (1, 100)')
            print('The scanning process will use the default delay time')

            return

        self.__delay = delay


    """
    Print out the list of ports being scanned
    """
    def show_target_ports(self):
        print ('Current port list is:')
        print (self.target_ports)


    """
    Print out the delay in seconds that a TCP socket waits until timeout
    """
    def show_delay(self):
        print ('Current timeout delay is :%d' %(int(self.__delay)))


    """
    Open multiple threads to perform port scanning

    Keyword arguments:
    ip -- the ip address that is being scanned
    delay -- the time in seconds that a TCP socket waits until timeout
    output -- a dict() that stores result pairs in {port, status} style (status = 'OPEN' or 'CLOSE')
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def __scan_ports_helper(self, ip, delay, output, message):

        '''
        Multithreading port scanning
        '''

        port_index = 0

        while port_index < len(self.target_ports):

            # Ensure that the number of cocurrently running threads does not exceed the thread limit
            while threading.activeCount() < self.__thread_limit and port_index < len(self.target_ports):

                # Start threads
                thread = threading.Thread(target = self.__TCP_connect, args = (ip, self.target_ports[port_index], delay, output, message))
                thread.start()
                port_index = port_index + 1


    """
    Controller of the __scan_ports_helper() function

    Keyword arguments:
    ip -- the ip address that is being scanned
    delay -- the time in seconds that a TCP socket waits until timeout
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def __scan_ports(self, ip, delay, message):

        output = {}

        thread = threading.Thread(target = self.__scan_ports_helper, args = (ip, delay, output, message))
        thread.start()

        # Wait until all port scanning threads finished
        while (len(output) < len(self.target_ports)):
            continue

        # Print openning ports from small to large
        for port in self.target_ports:
            if output[port] == 'OPEN':
                print(str(port) + ': ' + output[port] + '\n')

        return output



    """
    Perform status checking for a given port on a given ip address using TCP handshake

    Keyword arguments:
    ip -- the ip address that is being scanned
    port_number -- the port that is going to be checked
    delay -- the time in seconds that a TCP socket waits until timeout
    output -- a dict() that stores result pairs in {port, status} style (status = 'OPEN' or 'CLOSE')
    message -- the message that is going to be included in the scanning packets, in order to prevent
        ethical problem (default: '')
    """
    def __TCP_connect(self, ip, port_number, delay, output, message):
        # Initilize the TCP socket object
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCP_sock.settimeout(delay)


        # Initilize a UDP socket to send scanning alert message if there exists an non-empty message
        if message != '':
            UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDP_sock.sendto(str(message), (ip, int(port_number)))

        try:
            result = TCP_sock.connect_ex((ip, int(port_number)))
            if message != '':
                TCP_sock.sendall(str(message))

            # If the TCP handshake is successful, the port is OPEN. Otherwise it is CLOSE
            if result == 0:
                output[port_number] = 'OPEN'
            else:
                output[port_number] = 'CLOSE'

            TCP_sock.close()

        except socket.error as e:

            output[port_number] = 'CLOSE'
            pass

site=("192.168.1.1")
a=PortScanner()
a.scan(site)