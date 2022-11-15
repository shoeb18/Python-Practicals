# initialize punctuation variable
punctuation = '''"'[]{}()-;:/,\<>.?@#$%^&*_~'''

# taking user input
user_str = input("Enter the string : ")

# removing punctuation from string
no_punc = ""

for char in user_str:
    if char not in punctuation:
        no_punc = no_punc + char

# displaying the string
print(no_punc)
