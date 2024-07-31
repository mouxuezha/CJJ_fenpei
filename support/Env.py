# coding=UTF-8
from __future__ import division
import socket
import numpy as np

SIZE = 1024 * 1024*2
import json
import random
import re
import os

class Env():
    def __init__(self, IP, port):
        self._ip = IP
        self._port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SIZE)
        self.client.connect((self._ip, self._port))
        print("unfinished yet")