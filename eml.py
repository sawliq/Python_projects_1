# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)   
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("snapcart55@gmail.com", "qwerty9876")  #sender's email and password
  
# message to be sent 
message = "hi i am your boss"
  
# sending the mail 
s.sendmail("snapcart55@gmail.com", "sawlstore2@gmail.com", message)    #sender_email , receiver's email
  
# terminating the session 
s.quit() 
