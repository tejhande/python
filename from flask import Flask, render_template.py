import words

words_list = words.words()

d_words = [word for word in words_list if word.startswith('d')]

print(d_words)
