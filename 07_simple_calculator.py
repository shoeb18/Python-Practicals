class calculator:
    userinput1 = 0
    userinput2 = 0
    result = 0
    
    def oncalc(self):
        self.userinput1 = int(input("Enter the first Number : "))
        self.userinput2 = int(input("Enter the second Number : "))
        
        choice = input("Select operation (-,+,/,*) : ")
        
        if choice == '-':
            self.result = (self.userinput1 - self.userinput2)
        elif choice == '+':
            self.result = (self.userinput1 + self.userinput2)
        elif choice == '/':
            self.result = (self.userinput1 / self.userinput2)
        elif choice == '*':
            self.result = (self.userinput1 * self.userinput2)
            
        print("The result is :",self.result)
        
calc = calculator()
calc.oncalc()