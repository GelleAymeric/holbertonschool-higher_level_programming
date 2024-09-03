#!/usr/bin/python3

def print_last_digit(str):
    print(abs(str) % 10, end="")
    return (abs(str) % 10)

uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")