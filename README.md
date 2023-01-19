# Port-scanner
端口扫描器
本次端口扫描器有非gui版本以及gui版本，其中gui版本的端口扫描器在可视化图形实现上，出现了一些无法解决的问题，这些问题将在   ***端口扫描器GUI版本***   提到

#### 端口扫描器非GUI版本

1. 进入之后运行程序
2. 根据需要运用的功能，即   **主机发现**  和   **端口扫描**
3. 输入1调用主机扫描，输入2调用端口扫描,输入3结束程序
4. 根据控制台的提示，依次进行输入即可



#### 端口扫描器GUI版本

1. 进入之后，运行即可

2. 进入之后根据需要点击按钮使用即可

3. 在**主机发现窗口**或者**端口扫描窗口**后**关闭端口扫描器窗口(即第一个窗口)**，再进行选择域名或者IP才可以正常运行功能（打开能正常运行的窗口，文本框默认内容是None，如果没有请确认上述步骤）（此涉及到一个一直没有解决的一个问题在下面详细叙述）

   

4. 控制台作为后台使用，会显示输入的网址域名host，以及IP，还有端口扫描的进程图

   

##### **GUI ：利用Tkinter出现的一些问题**

*下列问题描述中，可以把默认文本None的出现与否作为功能能否正常运行的标准*

其中的问题都只找到解决方法或者代替的办法，没有找到根本原因是为什么



问题1：在打开**端口扫描器窗口**和**主机发现窗口**或者**端口扫描窗口**后，**选择域名或者IP之后**出现的**新窗口**，文本框的**内容不是默认的None**，以及改变文本框的内容时，**程序无法实时更新文本框的内容**，导致功能运行失败

问题1解决办法：在**主机发现窗口**或者**端口扫描窗口**后**关闭端口扫描器窗口**，此时选择域名或者IP，打开的**新窗口**文本框有默认内容None，并且**功能能正常运行**





问题2：在**问题1解决方法的基础上**，打开的**第一个新窗口是正常运行**的（有默认文本None），但在不关闭第一个新窗口，再次点击域名或者IP出现的**第二个或多个新窗口**，没有默认文本None，即**功能无法正常运行**

问题2解决方法：此时只要把**第一个功能正常运行的窗口关闭**，重新点击域名或者IP，再次重新的**新窗口又是正常运行**的。当**不关闭此窗口**，再次点击域名或IP，**问题2将再次出现**。





问题3：

```python
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


```

在函数**Port_ip_window()**中，

**Button(port_ip_window, text='确定', command=lambda :Port_ip_comfirm(v1.get())).grid(row=0, column=4,rowspan=2, sticky=NSEW)**

若**将command=lambda :Port_ip_comfirm(v1.get())改成Port_scan(ip)**，程序运行会在扫描完之后卡死（未找到原因）



问题3解决方法：只需要引入一个函数**Port_ip_comfirm(ip)**作为过渡，就能解决这个问题





问题4：在非GUI版本时，扫描过程很慢，但是基本上不会漏端口

在GUI版本时，扫描过程很快，但端口扫描会重复，还会漏端口

（在测试同一个域名时，非GUI版本扫描345s，扫描的端口有12个，不重复，且答案正确，但是GUI版本扫描35s，扫描的端口只有3个，且有时候端口会重复）



问题4解决方法：暂时还未找到。
