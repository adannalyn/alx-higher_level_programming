#!/usr/bin/python3
"""Line Break After a Punctuation Mark"""


def text_indentation(text):
    """Punctuation mark"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indented_text = ""
    i = 0
    while i < len(text):
        indented_text += text[i]
        if text[i] in {".", "?", ":"}:
            indented_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print("\n".join(line.strip() for line in indented_text.split("\n")))
