import smtplib
from email.message import EmailMessage
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Costache'
email['to'] = 'USERNAME@gmail.com'
email['subject'] = 'Ala bala portocala, ti a mancat maimuta cioara!'

email.set_content(html.substitute({'name': 'Andrew'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('USERNAME@gmail.com', 'PASSWORD')
    smtp.send_message(email)