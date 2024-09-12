#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char  in text:
        result += char
        if char in ".,?:":
            result += "\n\n"
    print(result)
