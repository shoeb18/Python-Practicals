def reverse_str(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1

s = input("Enter the string : ")
print("The original string : "+s)      
print("The reverse string : "+reverse_str(s))