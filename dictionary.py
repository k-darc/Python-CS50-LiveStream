#use Speller, otherwise it won't run
worlds = set()

def check(word):
    return word.lower() in worlds

def load(dictionary):
    while open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return  len(words)

def unload(): # upload isn't needed in Python. Python manages memory for you, there is no Malloc, freeing or pointers
    return True