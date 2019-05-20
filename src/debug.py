import time

start = time.time()

def printElapsedTime(prefix=None):
    print((prefix + ' ' if prefix else '') + str(time.time() - start))
