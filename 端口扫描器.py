import socket
import threading
import time
import os
import re
from tqdm import tqdm
import os

def get_ip_scan():#用于主机扫描
    while True:
        a = input('请选择输入的是域名还是IP(域名用1表示，IP用2表示,输入3退出): ')
        if a == '1':
            while True:
                    host = input('请输入域名：')
                    temp = os.popen('ping '+host)
                    temp = temp.read()

                    if temp.find('找不到') != -1:#find()未找到返回-1
                        print('无法连接该网址,请重新输入：')
                        continue
                    else:
                        temp = temp.split('[')
                        temp = temp[1].split(']')
                        result = temp[0]
                        print('该域名对应IP是：', result)
                        break
        elif a == '2':
            while True:
                ip = input('请输入IP地址：')
                temp = os.popen('ping '+ip)
                if temp.find('找不到') != -1:  # find()未找到返回-1
                    print('无法连接该IP,请重新输入：')
                    continue
                else:
                    print('该IP对应的主机存活')
                    break
        elif a == '3':
            break
        else:
            print('输入不符合要求，请重新输入')
while True:
    a = input('输入1调用主机发现，输入2调用端口扫描,输入3结束程序: ')
    if a == '1':
       get_ip_scan()
    elif a == '2':
        while True:
            a = input('请输入要查询的是IP还是网址域名：(ip用1表示，网址域名用2表示): ')
            if a == '1':
                ip = input('请输入IP：')
                break
            elif a == '2':
                host = str(input('请输入您要扫描的网址域名：'))
                ip = socket.gethostbyname(host)
                # 或者调用get_ip_scan()
                print('对应IP是：', ip)
                break
            else:
                print('您输入的不符合要求，请重新输入')
                continue
        port_list = []
        flag = 0  # 任务数

        print('开始端口扫描')
        t = time.time()  # 用于记录程序运行时间


        def scan(port):  # 扫描端口，确定是否打开
            global flag
            flag = flag + 1  # 开始扫描，任务数加一
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 检测代码
            sk.settimeout(1)
            try:
                sk.connect((ip, port))
                port_list.append(port)
            except Exception:
                pass
            sk.close()
            flag = flag - 1  # 任务结束，任务数减一


        threads = []

        for i in tqdm(range(0, 65535)):  # 65535
            thread = threading.Thread(target=scan, args=[i])
            threads.append(thread)
            thread.start()
            while flag >= 200:  # 如果任务数量大于200就等待0.1秒
                time.sleep(0.1)
        thread.join()
        print('扫描结束')
        print('开放端口：', port_list)
        print('运行时间：', time.time() - t)

    elif a == '3':
        print('欢迎再次使用')
        break
    else:
        print('您输入的不符合要求，请重新输入')
        continue
