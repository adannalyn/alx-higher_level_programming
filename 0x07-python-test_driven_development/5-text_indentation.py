#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    n = '.\n\n'
    o = '?\n\n'
    p = ':\n\n'
    text = text.replace('.', n).replace('?', o).replace(':', p)
    print()
    for strips in text.split('\n'):
        print(strips.strip())
