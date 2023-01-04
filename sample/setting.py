from tkinter import messagebox
from tkinter import *
import configparser




def save():
     strmail = mail.get()
     strpw = pw.get()
     strsubject = subject.get()
     strnoerrsubject = noerrsubject.get()
     strmfrom = mfrom.get()
     strto = to.get()
     strsmtp = smtp.get()
     strport = port.get()
     strlogdir = logdir.get()
     strerrocd = errocd.get()
     strjumpcd = jumpcd.get()


     #conf.add_section('mail')
     conf.set('mail','mailaddress',strmail)
     conf.set('mail','password',strpw)
     conf.set('mail','subject',strsubject)
     conf.set('mail','noerrsubject',strnoerrsubject)
     conf.set('mail','fromAddress',strmfrom)
     conf.set('mail','toAddress',strto)
     conf.set('mail','smtp',strsmtp)
     conf.set('mail','port',strport)
     #conf.add_section('log')
     conf.set('log','logdir',strlogdir)
     #conf.add_section('mark')
     conf.set('mark','errocd',strerrocd)
     conf.set('mark','jumpcd',strjumpcd)
     
     
     
     
     with open('conf.ini', 'w') as fw:
         conf.write(fw)
     messagebox.showinfo("setting","保存しました")

conf = configparser.ConfigParser()
conf.read('conf.ini') 
fsendAddress=conf['mail']['mailaddress']
fpassword=conf['mail']['password']
ffromAddress =conf['mail']['fromAddress']
ftoAddress = conf['mail']['toAddress']
fsmtp = conf['mail']['smtp']
fport = conf['mail']['port']
flogdir =conf['log']['logdir']
fsubject=conf['mail']['subject']
fnoerrsubject=conf['mail']['noerrsubject']
ferrocd=conf['mark']['errocd']
fjumpcd=conf['mark']['jumpcd']


root = Tk()
root.geometry('900x300')
root.title('設定')

mail = Label(root, text='メール')
pw = Label(root, text='パスワード')
subject = Label(root, text='エラー有件名')
noerrsubject = Label(root, text='エラー無件名')
mfrom = Label(root, text='from')
to = Label(root, text='to')
smtp = Label(root, text='SMTP')
port = Label(root, text='PORT')
logdir = Label(root, text='ログフォルダー')
errocd = Label(root, text='エラーコード')
jumpcd = Label(root, text='無視コード')


mail.place(x=5, y=10, width=100, height=20)
pw.place(x=200, y=10, width=100, height=20)
subject.place(x=350, y=10, width=100, height=20)
mfrom.place(x=500, y=10, width=100, height=20)
to.place(x=700, y=10, width=100, height=20)

noerrsubject.place(x=5, y=80, width=100, height=20)
smtp.place(x=150, y=80, width=100, height=20)
port.place(x=280, y=80, width=100, height=20)
logdir.place(x=400, y=80, width=100, height=20)
errocd.place(x=650, y=80, width=100, height=20)
jumpcd.place(x=750, y=80, width=100, height=20)


addr = StringVar(value=fsendAddress)
mail = Entry(root,textvariable=addr)
mail.place(x=5, y=30, width=180, height=20)

password = StringVar(value=fpassword)
pw = Entry(root,textvariable=password)
pw.place(x=200, y=30, width=130, height=20)

subjectxt = StringVar(value=fsubject)
subject = Entry(root,textvariable=subjectxt)
subject.place(x=350, y=30, width=130, height=20)

mfromtxt = StringVar(value=ffromAddress)
mfrom = Entry(root,textvariable=mfromtxt)
mfrom.place(x=500, y=30, width=180, height=20)

totxt = StringVar(value=ftoAddress)
to = Entry(root,textvariable=totxt)
to.place(x=700, y=30, width=150, height=20)

fnoerrsubjecttxt = StringVar(value=fnoerrsubject)
noerrsubject = Entry(root,textvariable=fnoerrsubjecttxt)
noerrsubject.place(x=5, y=100, width=130, height=20)

smtptxt = StringVar(value=fsmtp)
smtp = Entry(root,textvariable=smtptxt)
smtp.place(x=150, y=100, width=100, height=20)

porttxt = StringVar(value=fport)
port = Entry(root,textvariable=porttxt)
port.place(x=280, y=100, width=100, height=20)

logdirtxt = StringVar(value=flogdir)
logdir = Entry(root,textvariable=logdirtxt)
logdir.place(x=400, y=100, width=200, height=20)

errocdtxt = StringVar(value=ferrocd)
errocd = Entry(root,textvariable=errocdtxt)
errocd.place(x=650, y=100, width=100, height=20)

jumpcdtxt = StringVar(value=fjumpcd)
jumpcd = Entry(root,textvariable=jumpcdtxt)
jumpcd.place(x=800, y=100, width=100, height=20)


# 方法-直接调用 run1()
btn1 = Button(root, text='保存', command=save)
btn1.place(x=100, y=150, width=100, height=50)


root.mainloop()