#1 Split in Half

#str = "bbbbbcaaaaa"
#print(str.split('c'))


#str = "bbbbbcaaaaa"
#mylist = ['bbbbb', 'aaaaa']
#print('-'.join(mylist))


#QUESTION #2 Unique Characters in Strip

def check_unique_chars(string):
    if string is None:
        return True
    for char in string:
        if string.count(char) > 1:

            return False
    return True


print(check_unique_chars("read"))


print(check_unique_chars("readr"))