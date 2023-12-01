worlds = set()

def check(word):
    return word.lower() in worlds

def load(dictionary):
    while open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return  len(words)