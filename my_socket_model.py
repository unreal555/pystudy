# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/15 0015 上午 11:39
# Tool ：PyCharm

import socket
import threading
import time


class My_Socket():
    __username__ = 'admin'
    __pwd__ = 'admin'
    __local_server=''
    __addr=''
    __conn=''
    __PKT_BUFF_SIZE=10240
    __user_stat=[]


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

    def __init__(self,ip='0.0.0.0',port=50505,buff_size = 10240,debug=True):
        self.send_log('Init class ...')
        self.__PKT_BUFF_SIZE = buff_size

        if self.is_port_free(ip,port):
            threading.Thread(target=self.server, args=(ip, port)).start()
        else:
            self.send_log('本地端口:{} 被占用'.format(local_port))
            exit()

    def server(self, ip, port):
        self.__local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__local_server.bind((ip, int(port)))
        self.__local_server.listen(1)

        self.send_log('Starting listen  ' + ip + ':' + str(port) + '  ...')

        while True:

            try:
                (self.__conn, self.__addr) = self.__local_server.accept()
                self.__conn.settimeout(30)

            except Exception as e:
                self.send_log(e)
                self.__local_server.close()
                self.send_log('Something is wrong or break.  Stop mapping service...')
                break
            self.send_log('Request connect from %s:%d.' % self.__addr)

            self.user_check()

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



    def do(self):
        for i in range(1,100):
            time.sleep(1)
            self.send_info(str(i)+'\r\n')

    def send_log(self,content):
        print ('Event: ',content)
        return

    def send_info(self,info):
        def work(info):
            try:
                if isinstance(info,str):
                    self.__conn.send((info).encode('utf8'))
            except Exception as e:
                self.send_log('socket已断开，但是程序仍在输出，断开原因为:{}'.format(e))

        threading.Thread(target=work, args=(info,)).start()

    def send_in_mark(self):
        self.send_info(info='> \r\n')

    def send_out_mark(self):
        self.send_info(info='< ')

    def recive(self):
        while True:
            data = ''
            try:
                data = self.__conn.recv(self.__PKT_BUFF_SIZE)
            except Exception:
                self.send_log('Connection from {} closed.'.format(self.__addr))
                self.__conn.close()
                break
            try:
                data = data.decode('utf-8')
                data = data.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
            except Exception as e:
                print(data, e)
                continue
            if data == '':
                continue

            if data==None:
                continue

            return data

    def talk(self):
        while True:

            data=self.recive()

            if data==None:
                self.__conn.close()
                break

            self.send_log('命令来自{}，内容为: {}'.format(str(self.__addr), data))
            self.send_info('< 命令来自{}，内容为: {} \r\n'.format(str(self.__addr), data))

            if data == 'exit':
                self.__conn.close()
                self.send_log('Requset close from %s:%d.' % self.__addr)
                self.__conn.close()
                break

            if data == 'do':
                self.send_log('开始执行程序')
                self.send_info('开始执行程序' + '\r\n')
                self.do()
                self.send_log('程序执行结束')
                self.send_info('程序执行结束' + '\r\n> ')
                self.__conn.close()
                break

            else:
                self.send_info('> 命令错误，请重新输入\r\n< ')

    def user_check(self):

        if self.__addr[0] in self.__user_stat:
            self.send_info('> 欢迎：\r\n')
            self.send_out_mark()
            threading.Thread(target=self.talk).start()



        else:
            try:
                self.send_info('> 请输入用户名:')
                username = self.recive()
                self.send_info('> 请输入密码:')
                psw = self.recive()
                self.send_log(username + ':' + psw)
                self.send_log(str(self.__user_stat))
            except Exception as e:
                self.send_log(e)

            if username==self.__username__ and  psw==self.__pwd__:
                self.__user_stat.append(self.__addr[0])
                self.send_info('> 欢迎：\r\n')
                self.send_out_mark()
                threading.Thread(target=self.talk).start()
            else:
                self.send_log('user psw wrong')
                self.__conn.close()

My_Socket(port=50505)
