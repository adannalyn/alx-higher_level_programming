#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    for strips in text.split('\n'):
        print(strips.strip())
