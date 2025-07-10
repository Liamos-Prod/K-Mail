import time
import smtplib
import ssl
from email.mime.text import MIMEText
from utilities.password import PASSWORD_prog_kanabae
from .mail_content import html_content
from contact_functions.gs_contact_manager import get_data_dict

email_sender = 'yourEMail'
email_sender_name = 'yourUsername'
email_psw = YourPassword


def construct_mail(email_receiver, html_content,receiver_dict):
    em = MIMEText(html_content, 'html')
    em['From'] = email_sender_name
    receiver_name = get_sender_name(email_receiver,receiver_dict)
    print("Please wait...")
    em['To'] = email_receiver
    em['Subject'] = html_content.split('<title>')[1].split('</title>')[0]

    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_psw)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print(f"// ------ E-MAIL SENT TO {receiver_name} ------ //")

def replace_name_in_html(html_content, name):
    correct_content = html_content.replace("<<PRENOM>>"," " + name)
    return correct_content

def get_sender_name(email_receiver,receiver_dict):
    for email,name in receiver_dict.items():
        if email == email_receiver:
            return name

def send_mail(receiver_dict,html_content) :
    for receiver_email in receiver_dict.keys():
        print("// ------ PROCESSING NEXT E-MAIL ------ // ")
        modified_content = replace_name_in_html(html_content, get_sender_name(receiver_email,receiver_dict))
        construct_mail(receiver_email, modified_content,receiver_dict)
        time.sleep(40)
    