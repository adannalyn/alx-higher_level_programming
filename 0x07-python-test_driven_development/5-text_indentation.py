#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    alpha = ""
    for char in text:
        alpha += char
        alpha.strip()
        if char in ['.', '?', ':']:
            alpha += '\n\n'
    print(alpha.strip().lstrip(), end="")
