from ftplib import FTP                 
#ftp.cmd("/")
filename="message.txt" 
bs=1024**3
print(bs)
def receive():
    ftp=FTP()                        
    ftp.set_debuglevel(2)
    ftp.connect("192.168.1.104",21)     
    ftp.login("jimmy","312312")      
    #print(ftp.getwelcome())           
    with open(filename,"r+b") as t:
        ftp.retrbinary("RETR message.txt",t.write,bs)
    with open(filename,'rb') as f:
        m=str(f.read().decode())
    ftp.set_debuglevel(0)             
    ftp.quit()
    return m    
    
def send(con):
    con="%"+con
    ftp=FTP()                        
    ftp.set_debuglevel(2)
    ftp.connect("192.168.1.104",21)     
    ftp.login("jimmy","312312")      
    content=bytes(con.encode())
    #print(content)
    with open(filename,'ab') as f:
        f.write(content)
    file_h=open(filename,"rb")
    ftp.storbinary("STOR message.txt",file_h,bs)
    ftp.set_debuglevel(0)             
    ftp.quit()
    return

#send('gggggggggggggggggggggggggggggggggggggggggggggg')
