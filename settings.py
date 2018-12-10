import os
import logging

from dotenv import load_dotenv

load_dotenv(verbose=True)

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_DESTINATION = os.getenv("EMAIL_DESTINATION")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
NOTIFICATION_MESSAGE = os.getenv("NOTIFICATION_MESSAGE")

SOCKET_HOST = os.getenv("SOCKET_HOST")
SOCKET_PORT = int(os.getenv("SOCKET_PORT"))
ARDUINO_PORT = os.getenv("ARDUINO_PORT")
ARDUINO_BAUDRATE = int(os.getenv("ARDUINO_BAUDRATE")) if os.getenv(
    "ARDUINO_BAUDRATE") else 9600

WATER_LEVEL_THRESHOLD = float(os.getenv("WATER_LEVEL_THRESHOLD")) if os.getenv(
    "WATER_LEVEL_THRESHOLD") else 5.00
