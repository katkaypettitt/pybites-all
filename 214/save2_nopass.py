def countdown():
    """Write a generator that counts from 100 to 1"""
    t = 100
    while True:
        yield t
        t -= 1