from tkinter import *
from tkinter import messagebox
import os
import socket
import threading
import time
from tqdm import  tqdm

def Main_window():  # 创立主窗口，需要设置的功能的选项按钮
    main_window = Tk()
    main_window.title('端口扫描器')
    main_window.geometry('250x75+500+200')
    Label(main_window, text='欢迎使用端口扫描器，请选择功能', width=30, height=2, bg='white',
          font=('宋体', 10), ).grid(row=1, column=1, columnspan=2, sticky=NSEW)
    Button(main_window, text='主机发现', command=zhuji_window).grid(row=2, column=1, sticky=NSEW)
    Button(main_window, text='端口扫描', command=Port_window).grid(row=2, column=2, sticky=NSEW)
    main_window.mainloop()


def zhuji_window():  # 创建主机发现功能的窗口 需要设置输入域名或者IP的按钮
    zhuji_window = Tk()
    zhuji_window.title('主机发现')
    zhuji_window.geometry('250x75+600+250')
    Label(zhuji_window, text='欢迎使用主机发现，请选择输入方式', width=30, height=2, bg='white',
          font=('宋体', 10), ).grid(row=1, column=1, columnspan=2, sticky=NSEW)
    Button(zhuji_window, text='域名', command=Zhuji_yuming_window).grid(row=2, column=1, sticky=NSEW)
    Button(zhuji_window, text='IP', command=Zhuji_ip_window).grid(row=2, column=2, sticky=NSEW)
    zhuji_window.mainloop()


def Zhuji_yuming_window():  # 创建主机——域名的窗口  此处需要实现功能的展示 需要标签-域名 entry输入文本  Button 确认按钮  resultText输出文本
    zhuji_yuming_window = Tk()
    zhuji_yuming_window.geometry('300x50+600+300')
    zhuji_yuming_window.title('主机发现_域名')
    Label(zhuji_yuming_window, text='域名：').grid(row=0, column=0, sticky=NSEW)
    v1 = StringVar()
    v1.set('None')
    Entry(zhuji_yuming_window, textvariable=v1,font = ('楷体',15)).grid(row=0, column=1, rowspan=3, sticky=NSEW)
    Button(zhuji_yuming_window, text='确定', command=lambda :Zhuji_yuming_comfirm(v1.get())).grid(row=0, column=4, sticky=NSEW)

    # yuming_text = Text(zhuji_yuming_window,width = 30,height=10,font = ('楷体',15)).grid(row=0, column=1, rowspan=3, sticky=NSEW)
    #Button(zhuji_yuming_window, text='确定', command=lambda :Zhuji_yuming_comfirm(yuming_text)).grid(row=0, column=4, sticky=NSEW)

    zhuji_yuming_window.mainloop()

def Zhuji_yuming_comfirm(v1):  # 用于确认输入的主机域名 运行代码，把结果输入至resul_text文本框中
    host = str(v1)
    print('传递过来的host = ',host)  # 后台监控传递过来的host
    if host == 'None':
        messagebox.showinfo('message','您还没有输入域名')
    else:
        ip=Zhuji_yuming_scan(host)
        messagebox.showinfo('message',ip)

def Zhuji_yuming_scan(host):
    messagebox.showinfo('message','正在运行，请等待....(点击确定继续等待)')
    temp = os.popen('ping ' + host)
    temp = temp.read()

    if temp.find('找不到') != -1:  # find()未找到返回-1
        a = '无法连接该域名(或该域名的主机不存活),请重新输入域名'
    else:
        temp = temp.split('[')
        temp = temp[1].split(']')
        result = temp[0]
        a = '该域名(主机存活)对应IP是：'+ str(result)
    print(a) # 通过后台监控结果
    return a



def Zhuji_ip_window():
    zhuji_ip_window = Tk()
    zhuji_ip_window.geometry('300x50+600+300')
    zhuji_ip_window.title('主机发现_IP')
    Label(zhuji_ip_window, text='IP：').grid(row=0, column=0, sticky=NSEW)
    v2 = StringVar()
    v2.set('None')
    Entry(zhuji_ip_window, textvariable=v2,font = ('楷体',15)).grid(row=0, column=1, rowspan=3, sticky=NSEW)

    Button(zhuji_ip_window, text='确定', command=lambda :Zhuji_ip_comfirm(v2.get())).grid(row=0, column=4, sticky=NSEW)

    zhuji_ip_window.mainloop()

def Zhuji_ip_comfirm(v2):  # 用于确认输入的主机域名 运行代码，把结果输入至resul_text文本框中
    host = str(v2)
    print('传递过来的ip = ',host)
    if v2 == 'None':
        messagebox.showinfo('message','您还没有输入ip')
    else:
        ip=Zhuji_ip_scan(host)
        messagebox.showinfo('message',ip)


def Zhuji_ip_scan(host):
    messagebox.showinfo('message','正在运行，请等待....(点击确定继续等待)')
    temp = os.popen('ping ' + host)
    temp = temp.read()

    if temp.find('找不到') != -1:  # find()未找到返回-1
        a = '无法连接该IP(或该IP主机不存活),请重新输入IP'
    else:
        a = '该IP主机存活'
    print(a)
    return a

def Port_window():  # 创建端口视频功能的窗口
    port_window = Tk()
    port_window.title('端口扫描')
    port_window.geometry('250x75+600+250')
    Label(port_window, text='欢迎使用端口扫描，请选择输入方式', width=30, height=2, bg='white',
          font=('宋体', 10), ).grid(row=1, column=1, columnspan=2, sticky=NSEW)
    Button(port_window, text='域名', command=Port_yuming_window).grid(row=2, column=1, sticky=NSEW)
    Button(port_window, text='IP', command=Port_ip_window).grid(row=2, column=2, sticky=NSEW)
    port_window.mainloop()

def Port_yuming_window():  # 创建主机——域名的窗口  此处需要实现功能的展示 需要标签-域名 entry输入文本  Button 确认按钮  resultText输出文本
    port_yuming_window = Tk()
    port_yuming_window.geometry('300x50+600+300')
    port_yuming_window.title('端口扫描_域名')
    Label(port_yuming_window, text='域名：').grid(row=0, column=0, sticky=NSEW)
    # Label(port_yuming_window, text='开始端口：').grid(row=1, column=0, sticky=NSEW)
    # Label(port_yuming_window, text='结束端口：').grid(row=1, column=2, sticky=NSEW)

    v1 = StringVar()
    v1.set('None')
    # v2 = StringVar()
    # v2.set('None')
    # v3 = StringVar()
    # v3.set('None')

    Entry(port_yuming_window, textvariable=v1,font = ('楷体',15)).grid(row=0, column=1, columnspan=3, sticky=NSEW)
    # Entry(port_yuming_window, textvariable=v2,font = ('楷体',15)).grid(row=1, column=1, sticky=NSEW)
    # Entry(port_yuming_window, textvariable=v3,font = ('楷体',15)).grid(row=1, column=3, sticky=NSEW)
    Button(port_yuming_window, text='确定', command=lambda :Port_yuming_comfirm(v1.get())).grid(row=0, column=4,rowspan=2, sticky=NSEW)
    port_yuming_window.mainloop()


def Port_yuming_comfirm(host):  # 用于确认输入的主机域名 运行代码，把结果输入至resul_text文本框中
    try:
        ip = socket.gethostbyname(str(host))
        print('传递过来的host = ',host)  # 后台监控传递过来的host
        print('对应的IP是：',ip)
        Port_scan(ip)
    except:
        print('域名不符合要求')
        messagebox.showinfo('message','域名不符合要求(或者域名不存在)')


def Port_ip_window():
    port_ip_window = Tk()
    port_ip_window.geometry('300x50+600+300')
    port_ip_window.title('端口扫描_IP')
    Label(port_ip_window, text='IP：').grid(row=0, column=0, sticky=NSEW)
    # Label(port_ip_window, text='开始端口：').grid(row=1, column=0, sticky=NSEW)
    # Label(port_ip_window, text='结束端口：').grid(row=1, column=2, sticky=NSEW)

    v1 = StringVar()
    v1.set('None')
    # v2 = StringVar()
    # v2.set('None')
    # v3 = StringVar()
    # v3.set('None')

    Entry(port_ip_window, textvariable=v1,font = ('楷体',15)).grid(row=0, column=1, columnspan=3, sticky=NSEW)
    # Entry(port_ip_window, textvariable=v2,font = ('楷体',10)).grid(row=1, column=1, sticky=NSEW)
    # Entry(port_ip_window, textvariable=v3,font = ('楷体',10)).grid(row=1, column=3, sticky=NSEW)
    Button(port_ip_window, text='确定', command=lambda :Port_ip_comfirm(v1.get())).grid(row=0, column=4,rowspan=2, sticky=NSEW)
    port_ip_window.mainloop()

def Port_ip_comfirm(ip):  # 用于确认输入的主机域名 运行代码，把结果输入至resul_text文本框中
    print('输入的IP是：',ip)
    Port_scan(ip)

port_list = []#用于记录开放的端口
def Scan_functiom(ip,port):  # 扫描端口，确定是否打开
    global flag
    flag = 0
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



def Port_scan(ip):
    messagebox.showinfo('message','开始扫描，点击确定后继续等待一会...')
    threads=[]
    t=time.time()
    for i in tqdm(range(1,65535)):  # 65535
        thread = threading.Thread(target=Scan_functiom, args=[ip,i])
        threads.append(thread)
        thread.start()
        while flag >= 200:  # 如果任务数量大于200就等待0.1秒
            time.sleep(0.1)
    thread.join()
    print('port_list = ',port_list)
    messagebox.showinfo('message','开放的端口有：'+str(port_list)+'\n所使用的时间为：'+str(time.time()-t)+'秒')  #此处port_list以及time.time()-t要用str转格式，不然此messagebox无法显示



Main_window()
