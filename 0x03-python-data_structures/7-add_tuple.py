#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    
    result = tuple(tuple_a + tuple_b for tuple_a, tuple_b in zip(tuple_a,  tuple_b))
    
    print("{}".format(result))
    
    if __name__ == "__main__":
        pass