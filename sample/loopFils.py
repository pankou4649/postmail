import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from configparser import ConfigParser  
from time import strftime,localtime

conf = ConfigParser()  
conf.read('conf.ini') 
sendAddress=conf['mail']['mailaddress']
password=conf['mail']['password']
fromAddress =conf['mail']['fromAddress']
toAddress = conf['mail']['toAddress']
smtp = conf['mail']['smtp']
port = conf['mail']['port']
base =conf['log']['logdir']

noerrsubject=conf['mail']['noerrsubject']
errocd=conf['mark']['errocd']
jumpcd=conf['mark']['jumpcd']




def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    finalbodyText=""
    nowydm=strftime('%Y%m%d',localtime())
    for finame in findAllFile(base):
        
        finamearr = finame.split('-')
        
        if finamearr[0]==nowydm:
            print(finame)
            finalbodyText=finalbodyText+readFile(base,finame)
    if finalbodyText=="":
        subject=noerrsubject
    else:
        subject=conf['mail']['subject']           
    sendmail(subject,finalbodyText)
def readFile(dir_path,file_name):
        

    bodyText=""
    file_path = os.path.join(dir_path, file_name)
    
    with open(file_path,encoding="utf-8") as f:
        line = f.readline()
        while line:
            if errocd in line:
                if jumpcd in line:
                    pass
                else:
                    print (line)
                    bodyText=bodyText+line+"\n"
            line = f.readline()
    return bodyText
                
def sendmail(subject,bodyText):
   

    
    smtpobj = smtplib.SMTP(smtp, port)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)
    
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()
    
    smtpobj.send_message(msg)
    smtpobj.close()
    print ("mail is sended.")

if __name__ == '__main__':
    main()