#import needed modules
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

camera = PiCamera() #setup camera

GPIO.setmode(GPIO.BCM) #setup camera button
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True: #infinite loop that takes button input, takes image, and send email
    input_state = GPIO.input(4) #button input
    if input_state == False:
        camera.start_preview() #preview image
        time.sleep(5) #show 5 seconds
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        print("Image Taken!")
        time.sleep(0.2)
        name = input("Please Type Your Name:\n") #keyboard input fot peron's name
        mail_content = name + ' Has Arrived at the Security Checkpoint.\n Please Review for Approval.'
        #email addresses and password
        address = 'wmoore4180@gmail.com'
        password = '4180password'
        securityAddr = 'wtmoore6@gmail.com'
        #Setup MIME
        message = MIMEMultipart()
        message['From'] = address
        message['To'] = securityAddr
        message['Subject'] = 'Security Checkpoint Notification: ' + name
        message.attach(MIMEText(mail_content, 'plain')) #add subjectand body
        with open('/home/pi/Desktop/image.jpg', 'rb') as f:
            #get image as .jpg type
            mime = MIMEBase('image', 'jpg', filename='image.jpg')
            #header data
            mime.add_header('Content-Disposition', 'attachment', filename='image.jpg')
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            
            mime.set_payload(f.read()) #read image file
            encoders.encode_base64(mime) #encode
            
            message.attach(mime) #add object to mime

        #Create SMTP to send email
        session = smtplib.SMTP('smtp.gmail.com', 587) #using gmail
        session.starttls()
        session.login(address, password) #login with address and password
        text = message.as_string()
        session.sendmail(address, securityAddr, text) #send email
        session.quit() #cleanup
        print('Email Sent to Secuity Officer.')
        os.remove('/home/pi/Desktop/image.jpg') #remove image from local device