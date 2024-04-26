#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), None)
    return (len(sentence), sentence[0])


if __name__ == "__main__":
    pass
