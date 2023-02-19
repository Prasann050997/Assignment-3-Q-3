#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def up_low(x):      
    u = sum(1 for i in x if i.isupper())
    l = sum(1 for i in x if i.islower())
    print( "No. of Upper case characters : ", (u))
    print( "No. of lower case characters : ", (l))

up_low( 'The quick Brow Fox')