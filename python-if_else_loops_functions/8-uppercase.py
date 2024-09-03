#!/usr/bin/python3

def uppercase(str):
    result = ""
    
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char

    print(result)
