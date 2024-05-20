#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indented_text = ""
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            indented_text += text[i] + "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            indented_text += text[i]
            i += 1
    for line in indented_text.split("\n"):
        if line.strip():
            print(line.strip())
