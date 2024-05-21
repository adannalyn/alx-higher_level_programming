#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indented_text = ""

    for char in text:
        indented_text += char

        if char in ".?:":
            print(indented_text.strip() + "\n")
            indented_text = ""

    if indented_text:
        print(indented_text.strip(), end="")
