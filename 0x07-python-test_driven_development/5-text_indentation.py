#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    n = '\n\n'
    text = text.replace('.', '.'n).replace('?', '?'n).replace(':', ':'n)
    print()
    for strips in text.split('\n'):
        print(strips.strip())
