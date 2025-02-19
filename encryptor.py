#!/usr/bin/python3
import sys

blocksize = 16

def loadMessage():
    message = ""
    with open("message.txt","r",encoding='utf-8') as file:
        for line in file:
            message += line
    while len(message) % blocksize != 0:
        message += '0'
    return message

def encode(chunk): #encodes a 16-character string into a 128-bit integer.
    start = 120 #start at highest bit position
    encoded = 0
    for c in chunk:
        encoded = encoded | (ord(c)<<start)
        start -= 8
    return encoded

def transmit(): #XOR encryption with incrementing IV

    # Test key
    key = 0xadbeefdeadbeefdeadbeef00

    iv = 0
    msg = loadMessage()
    #print("Message loaded:", msg)    #use to print text before encryption

    chunks = [msg[i:i+16] for i in range(0,len(msg), 16)]

    send = ''
    for chunk in chunks:
        iv = (iv+1) % 255
        curr_k = key+iv
        encoded = encode(chunk)
        enc = encoded ^ curr_k
        foo = hex(enc)[2:]
        while len(foo) != 32:
           foo = '0'+foo
        send += foo
    print(send)  #prints encrypted msg
    sys.exit(0)

if __name__=="__main__":
    transmit()
