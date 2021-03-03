# -*- coding: utf-8 -*-
# tcp mapping created by zl at 2020-09-11

import socket
import threading

class PortMapper():
    # 接收数据缓存大小
    __PKT_BUFF_SIZE=10240

    def __init__(self,remote_ip,remote_port,local_ip='0.0.0.0',local_port=3390,buff_size = 10240,debug=True):
        self.send_log('Event: init class ...')
        self.__PKT_BUFF_SIZE = buff_size

        if self.is_port_free(local_port):
            threading.Thread(target=self.tcp_mapping, args=(remote_ip, remote_port, local_ip, local_port)).start()
        else:
            self.send_log('本地端口:{} 被占用'.format(local_port))
            exit()

    def is_port_free(self, port,ip='0.0.0.0'):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((ip, int(port)))
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            s.close()

    # 端口映射函数
    def tcp_mapping(self,remote_ip, remote_port, local_ip, local_port):
        local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_server.bind((local_ip, local_port))
        local_server.listen(5)

        self.send_log('Event: Starting mapping service on ' + local_ip + ':' + str(local_port) + ' to ' +  remote_ip+':'+str(remote_port) +'  ...')

        while True:
            try:
                (local_conn, local_addr) = local_server.accept()
            except (KeyboardInterrupt, Exception):
                local_server.close()
                self.send_log('Event: Something is wrong or break.  Stop mapping service...')
                break

            threading.Thread(target=self.tcp_mapping_request, args=(local_conn, remote_ip, remote_port)).start()

            self.send_log('Event: Receive mapping request from %s:%d.' % local_addr)

        return

    # 调试日志封装
    def send_log(self,content):
        print (content)
        return

    # 单向流数据传递
    def tcp_mapping_worker(self,conn_receiver, conn_sender):
        while True:
            try:
                data = conn_receiver.recv(self.__PKT_BUFF_SIZE)
            except Exception:
                self.send_log('Event: Connection closed.')
                break

            if not data:
                self.send_log('Info: No more data is received.')
                break

            try:
                conn_sender.sendall(data)
            except Exception:
                self.send_log('Error: Failed sending data.')
                break

            # send_log('Info: Mapping data > %s ' % repr(data))
            self.send_log('Info: Mapping > %s -> %s > %d bytes.' % (conn_receiver.getpeername(), conn_sender.getpeername(), len(data)))

        conn_receiver.close()
        conn_sender.close()

        return

    # 端口映射请求处理
    def tcp_mapping_request(self,local_conn, remote_ip, remote_port):
        remote_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            remote_conn.connect((remote_ip, remote_port))
        except Exception:
            local_conn.close()
            self.send_log('Error: Unable to connect to the remote server.')
            return

        threading.Thread(target=self.tcp_mapping_worker, args=(local_conn, remote_conn)).start()
        threading.Thread(target=self.tcp_mapping_worker, args=(remote_conn, local_conn)).start()

        return


# 主函数
if __name__ == '__main__':
    print('written by 张磊')
    print('开始转发。。')
    PortMapper('192.168.1.251', 11223)

    # threading.Thread(target=PortMapper, args=('192.168.1.251', 11223)).start()
    # threading.Thread(target=PortMapper, args=('192.168.1.251', 808,'0.0.0.0',801)).start()

