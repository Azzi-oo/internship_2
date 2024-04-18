def long_word(words):
    max_length = 0
    longing_word = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longing_word = word
    return longing_word


def long_word_2(words):
    length = 0
    long_word = ""
    i = 0
    while i < len(words):
        if len(words[i]) > length:
            length = len(words[i])
            long_word = words[i]
        i += 1
    return long_word
