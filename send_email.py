import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, subject, text_content):
  port = 465  # For SSL
  sender_email = ""
  password = ''
  server = smtplib.SMTP_SSL("smtp.gmail.com", port)
  server.login(sender_email, password)
  
  message = MIMEMultipart('related')
  message['Subject'] = subject
  message['From'] = sender_email
  message['To'] = receiver_email
  
  text = MIMEText(text_content, 'html')
  message.attach(text)
  
  image_path = "/Users/yoonjae/github/send_mail_press/profile.png"
  fp = open(image_path, 'rb')
  image = MIMEImage(fp.read(), name=os.path.basename(image_path))
  fp.close()
  
  image.add_header('Content-ID', '<image>')
  message.attach(image)
  
  server.sendmail(sender_email, [receiver_email], message.as_string())
  server.quit()
  
def main():
  send_email("", "", "")
  
if __name__ == '__main__':
  main()