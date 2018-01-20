# Define 5 words in english to spanish.
# Door - puerta
# brother - hermano
# store - almacenar
# food - comida
#
# The end program : input an english sentence - output a spanish translation of the relevant words.

# word = str(input('Enter a word in the english dictionary: '))
# t_word =''
english_dict = {'door':'puerta', 'brother': 'hermano', 'store': 'almacenar', 'food': 'comida'}
# if word in english_dict:
#     print(english_dict[word])
# else:
#     print(word)
sentence = 'The door to the store is held open by my brother'
t_sentence = ''
for word in sentence.split():
    if word in english_dict:
        t_sentence = t_sentence + english_dict[word] + ' '
    else:
        t_sentence = t_sentence + word + ' '
print(sentence)
print(t_sentence)