import sqlite3, math

class Delta:
    def __init__(self):
        self.name = "Delta"
        self.author = "Colin Daugherty"
        self.version = "0.1b"
        self.welcome = "Hello, my name is Delta, how may I help?"

    def mathFunctions(type, numbers):
        i = 0
        if type == "addition":
            for i in numbers:
                num = numbers[i]
                i += 1
                num += numbers[i]
            print(num)
        elif type == "multiplication":
            for i in numbers:
                num = numbers[i]
                i += 1
                num *= numbers[i]
            print(num)
        else:
            print("Type cannot be null")
