import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nehal Ahuja'
email['to'] = 'surbhiranjan0507@gmail.com'
email['subject'] = 'You won 10,00000 dollars!'

email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('nehalahuja5@gmail.com', 'hpjuly_5')
	smtp.send_message(email)
	print("all good boss!")

# 'x' = 'your email from which mail has to be sent'
# 'y' = 'your email's password'
# 'a' = 'your name'
# 'b' = 'email id, to which mail has to be sent'
# Also, the name Tintin can be modified as per the requirement
