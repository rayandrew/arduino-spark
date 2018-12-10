import smtplib

import logging

from settings import \
    EMAIL_USER, \
    EMAIL_PASSWORD, \
    EMAIL_HOST, \
    EMAIL_PORT

KWARGS_REQUIRED = ["host", "port", "email"]

logging.debug("[Email] Connecting to SMTP Server")

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASSWORD)

logging.debug("[Email] SMTP Server Successfully Connected")


def send_email(to, message):
    logging.debug("[Email] Sending a message from " +
                  EMAIL_USER + " to " + to)
    server.sendmail(EMAIL_USER, to, message)
    logging.debug("[Email] Sending message succeed!")


# class Email():
#     def __init__(self, **kwargs):
#         if all(key in KWARGS_REQUIRED for (key, value) in kwargs.items()):
#             raise ValueError("Args host, port, and email not found!")

#         self.host = kwargs.get("host")
#         self.port = kwargs.get("port")
#         self.email = kwargs.get("email")

#         # Connecting to SMTP Server
#         logging.debug("[Email] Connecting to SMTP Server")

#         self.server = smtplib.SMTP(kwargs["host"], kwargs["port"])
#         self.server.starttls()
#         self.server.login(self.email, kwargs.get("password"))

#         logging.debug("[Email] SMTP Server Successfully Connected")

#     def send_message(self, to, message):
#         logging.debug("[Email] Sending a message from " +
#                       self.email + " to " + to)
#         self.server.sendmail(self.email, to, message)
#         logging.debug("[Email] Sending message succeed!")

#     def __del__(self):
#         logging.debug("[EMAIL] Ending email session")
#         self.server.quit()
#         logging.debug("[EMAIL] Ending email session succeed")
