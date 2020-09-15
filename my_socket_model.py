# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/15 0015 上午 11:39
# Tool ：PyCharm

import socket
import threading

class My_Socket():

    __local_server=''

    __conn=''

    __PKT_BUFF_SIZE=10240

    def __init__(self,ip='0.0.0.0',port=50505,buff_size = 10240,debug=True):
        self.send_log('Event: init class ...')
        self.__PKT_BUFF_SIZE = buff_size

        if self.is_port_free(ip,port):
            threading.Thread(target=self.listen, args=(ip, port)).start()
        else:
            self.send_log('本地端口:{} 被占用'.format(local_port))
            exit()

    def __del__(self):
        try:
            self.__conn.close()
            self.__local_server.close()
            self.__PKT_BUFF_SIZE = ''
            del __conn
            del __local_server
            del __PKT_BUFF_SIZE
        except:
            pass

    def is_port_free(self, ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((ip, int(port)))
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            s.close()

    def do(self,conn):
        for i in range(1,1000):
            self.send_info(conn,str(i)+'\r\n')

    def send_log(self,content):
        print (content)
        return

    def send_info(self,conn,info):
        def send(conn,info):
            try:
                if isinstance(info,str):
                    conn.send(('> '+info).encode('utf8'))
                if isinstance(info,(tuple,list)):
                    for i in info:
                        if isinstance(i, str):
                            conn.send(('info: '+i).encode('utf8'))
            except Exception as e:
                self.send_log('exit:{}'.format(e))

        threading.Thread(target=send, args=(conn,info)).start()

    def listen(self,ip,port):
        self.__local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__local_server.bind((ip, int(port)))
        self.__local_server.listen(5)

        self.send_log('Event: Starting listen  ' + ip + ':' + str(port) +'  ...')

        while True:

            try:
                (self.__conn, self.__addr) = self.__local_server.accept()

            except (KeyboardInterrupt, Exception) as e:
                self.send_log(e)
                self.__local_server.close()
                self.send_log('Event: Something is wrong or break.  Stop mapping service...')
                break
            self.send_log('Event: request  connect from %s:%d.' %self.__addr)

            self.send_info(self.__conn, '欢迎：\r\n< ')

            while True:
                data = True
                try:
                    data = self.__conn.recv(self.__PKT_BUFF_SIZE)
                except Exception:
                    self.send_log('Event: Connection closed.')
                    exit()

                try:
                    data=data.decode('utf-8')
                    data=data.replace('\r','').replace('\n','').replace('\t','').replace(' ','')
                except Exception as e:
                    print(data,e)
                    continue

                self.send_log('Event: <命令来自{}，内容为: {}'.format(str(self.__addr),data))
                self.send_info(self.__conn,'<命令来自{}，内容为: {} \r\n'.format(str(self.__addr),data))

                if data=='exit':
                    self.__conn.close()
                    self.send_log('Event: requset close from %s:%d.' % self.__addr)
                    break


                if  data=='do':
                    self.send_log('Event: 开始执行程序')
                    self.send_info(self.__conn, '开始执行程序'+'\r\n')
                    self.do(self.__conn)
                    self.send_log('Event: 程序执行结束')
                    self.send_info(self.__conn,'程序执行结束'+'\r\n')
                    continue

                else:
                    self.send_info(self.__conn,'命令错误，请重新输入\r\n< ')





My_Socket(port=50505)
