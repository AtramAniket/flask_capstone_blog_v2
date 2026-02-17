import os
import smtplib
from dotenv import load_dotenv

class Contact:

    def __init__(self, sender_name, sender_address, message_content) -> None:

        load_dotenv()
        self.sender_address = sender_address
        self.subject = f"Contact request from {sender_name}"
        self.message_content = message_content
        self.app_passwd = os.getenv("APP_PSSWD")
        self.reciepient_address = os.getenv("RECIEPIENT_ADDRESS")
    
    def test(self) -> None:
        print(f"Sneding message to {self.sender_address}\nMessage:{self.message_content}")

    def send_message(self) -> None:

        with smtplib.SMTP("smtp.gmail.com") as connection:

            connection.starttls()

            connection.login(user = self.sender_address, password = self.app_passwd)
            
            connection.sendmail(from_addr = self.sender_address, to_addrs = self.reciepient_address, msg = f"Subject:{self.subject}\n{self.message_content}")