# importing all the useful libraries for the task 6
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
import subprocess

# sending the email to the person whose face is detected 
def sendMail(receiver_address , name):
    #The mail addresses and password
    sender_address = 'sender_email_here'
    sender_pass = getpass.getpass(prompt="Enter your password")
    
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'We have detected you and your name is:' + name
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("mail sent to the address")
    
    
    def aws_ec2_ebs():
    # AWS cli command for creating aws ec2 instance

    # first - creating the key-pair for the aws 
    subprocess.getoutput("aws ec2 create-key-pair --key-name aws_key")

    # second  - creating security group for our ec2 instance 
    subprocess.getoutput("aws ec2 create-security-group --group-name MyAWSSecurityGroup --description My AWS security group")

    # third  - creating/ launching an ec2 instance
    subprocess.getoutput("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name aws_key --security-group-ids sg-0d044f5752b4e9322")

    # fourth - creating an ebs volume in aws 
    subprocess.getoutput("aws ec2 create-volume --volume-type gp2  --size 1  --availability-zone  ap-south-1a")

    # fifth - Attaching the above created EBS volume to the instance
    subprocess.getoutput("aws ec2 attach-volume --volume-id vol-07cde9d02dea697d3 --instance-id i-0ef7886cf2396a580  --device /dev/sdf")
