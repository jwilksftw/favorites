import urllib2
import random
import smtplib

opener= urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

with open('favorites.txt') as f:
    content = f.readlines()


favs = random.choice(content)
print favs




outToFile = open('favoritesmail.txt', mode='w')
outToFile.write('Here is your daily favorite!\n')
outToFile.close()

outToFile = open('favoritesmail.txt', mode='a+')
outToFile.write(favs)
    
outToFile.close()

with open ("favoritesmail.txt", "r") as myfile:
    data=myfile.read()
fromaddr = 'jwilksftw@gmail.com'  
toaddrs  = 'jwilksftw@gmail.com'  
msg = data    
  
# Credentials (if needed)  
username = 'jwilksftw'  
password = 'zottoz000'  
  
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.ehlo()
server.starttls()
server.ehlo()  
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()

