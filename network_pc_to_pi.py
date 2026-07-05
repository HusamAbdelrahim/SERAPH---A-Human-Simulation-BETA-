# This is just a test 

import socket

def send_score(score):
    pi_ip = ""   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((pi_ip, 5000))
    s.send(str(score).encode())
    s.close()

send_score(300)   