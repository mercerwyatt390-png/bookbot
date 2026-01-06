
def count_words(text): #Counts the number of words in the book
    words = text.split()
    return len(words)

def char_use(text): #Counts the total # of characters used
    char = {}
    for c in text:
        if c.lower() not in char:
            char[c.lower()] = 1
        else:
            char[c.lower()] += 1
    return char