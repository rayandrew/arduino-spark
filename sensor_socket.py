import sys
import socket
import json
import time
import random
import serial

import logging

from signal import signal, SIGPIPE, SIG_DFL

from settings import \
    SOCKET_HOST, \
    SOCKET_PORT, \
    ARDUINO_PORT, \
    ARDUINO_BAUDRATE

# Stop program if sigpipe detected
signal(SIGPIPE, SIG_DFL)


logging.basicConfig(filename="logger_socket.log", level=logging.DEBUG)


class SensorSocket():
    def __init__(self, host, port):
        logging.debug("[SOCKET] Initializing Socket")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        logging.debug("[SOCKET] Socket Initialized")

        print("Listening on port : ", str(SOCKET_PORT))

        self.socket.listen(5)

    def send_data(self, data):
        logging.debug("[SOCKET] Sending Data to Socket")
        conn, _ = self.socket.accept()

        try:
            conn.send(data.encode())
            logging.debug("[SOCKET] Sending Data to Socket Succeed")
        except BaseException as e:
            print("Error: %s" % str(e))

    def __del__(self):
        self.socket.close()


if __name__ == "__main__":
    try:
        logging.debug("[MAIN] Connecting to Arduino Serial")
        arduinoData = serial.Serial(
            port=ARDUINO_PORT, baudrate=ARDUINO_BAUDRATE)

        sensor_socket = SensorSocket(SOCKET_HOST, SOCKET_PORT)

        while(True):
            stri = arduinoData.readline().decode("utf-8")
            # sensor_socket.send_data(str(random.uniform(1.5, 8.0))) # debugging only
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nBye bye :(")
        sys.exit()
