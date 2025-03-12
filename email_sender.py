import smtplib
from email.message import EmailMessage

class sendEmail:

    SUBJECT = "HELLO"
    BODY = "HELLO WORD"
    RECEIVER = "receiver@gmail.com"  # Enter actual email to receive the email

    @staticmethod
    def email_alert(subject,body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        user = "sender@gmail.com" # enter email to send the text or create a new one
        msg['from'] = user
        password = "password" # Generate a password

        print("connecting")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user,password)
        print("login ")
        server.send_message(msg)
        server.quit()

        print("Email sent successfully!")


