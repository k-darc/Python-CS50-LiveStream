#use Speller, otherwise it won't run, python speller.py holmes.txt form Lecture 5. Total time is about 1.90 seconds in Python.
worlds = set()

def check(word):
    return word.lower() in worlds

def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return len(words)

def unload(): # upload isn't needed in Python. Python manages memory for you, there is no Malloc, freeing or pointers
    return True

# Total in C is about 0.42 seconds.