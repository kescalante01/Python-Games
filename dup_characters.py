
string ='ABCDbFEfGIg'

unique_letters = ''
dup_count = 0
string = string.lower()
for letter in string:
    if letter in unique_letters:
        dup_count +=1
        print("this is a duplicate letter", letter,'\n',  "We have this many unique duplicates", dup_count)
    elif letter not in unique_letters:
        unique_letters += letter
        print("this is a unique letter", letter)



