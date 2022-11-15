class my_class:
    def formula(self, num):
        sum = 0
        while (num != 0):
            sum = sum + int(num % 10)
            num = int(num/10)
        return sum
    
obj = my_class()
print("The sum is :",obj.formula(512))