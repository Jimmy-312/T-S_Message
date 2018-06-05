from ftplib import FTP                 
#ftp.cmd("/")
filename="message.txt"
ip="192.168.1.104"
user,password='jimmy','312312'
bs=1024**3
def ftp(op,var=0):
    try:
        ftp=FTP()                        
        ftp.set_debuglevel(2)
        ftp.connect(ip,21)     
        ftp.login(user,password)      
        #print(ftp.getwelcome())
        if op=='r':
            with open(filename,"r+b") as t:
                ftp.retrbinary("RETR message.txt",t.write,bs)
            with open(filename,'rb') as f:
                m=str(f.read().decode())
        elif op=='s':
            var="%"+var
            content=bytes(var.encode())
            #print(content)
            with open(filename,'ab') as f:
                f.write(content)
            file_h=open(filename,"rb")
            ftp.storbinary("STOR message.txt",file_h,bs)
            m='Successful.'
        ftp.set_debuglevel(0)             
        ftp.quit()
        return m
    except:
        return 'err'
