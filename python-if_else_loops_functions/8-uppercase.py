#!/usr/bin/python3

def uppercase(str):
    result = ""
    
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char

    print(result)

if uppercase == __import__('8-uppercase').uppercase:
    uppercase("best")
    uppercase("Best School 98 Battery street")
