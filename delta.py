import sqlite3, math

class __default_function_option__:
    def __repr__(self):return "<no default>"

__default_function_option__ = __default_function_option__()

class Delta:
    def __init__(self):
        pass

    def timeKeeper(startstop=__default_function_option):
        if startstop == True:
            start_time = time.time()
        elif startstop == False:
            elapsed_time = str(time.time() - start_time)
            return elapsed_time
        else:
            print("unrecognized option passed")

    def helper():
        def helper(clearoptional=__default_function_option__):
        if clearoptional == __default_function_option__:
            version = "0.1b"
            author = "Colin Daugherty"
            name = "Delta"
            print("%s v%s created by %s \n NOTE: This is a very experimental AI, many things will change" % (name, version, author))
            query = input("%s: How may I be of assistance?\n ")
            return query
        elif clearoptional == "clear":
            # for windows
            if os.name == 'nt':
                _ = os.system('cls')

            # for mac and linux(here, os.name is 'posix')
            else:
                _ = os.system('clear')
        else:
            print("Unexpected parameter given-\nParameter given: %s\nParameter expected: default" % (clearoptional))


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

    def run(alwaysRunoptional=True):
        deltaInit = Delta.helper()
        deltaKeyword = Delta.determineKeyword(deltaInit)
        print(deltaKeyword)
        if alwaysRunoptional == True:
            Delta.run()
        elif alwaysRunoptional == False:
            print("Shutting down...")
            time.sleep(15)
            exit()
        elif alwaysRunoptional == "AskFirst":
            deltaAskRun = input("Would you like to run Delta again?: ")
            deltaConfirmRun = Delta.determineKeyword(deltaAskRun)
            if deltaConfirmRun == True:
                Delta.run("AskFirst")
            else:
                print("Shutting down...")
                time.sleep(15)
                exit()

    def init():
        startUp = input("__how should i run delta__")
        if startUp == "AskFirst":
            Delta.run("AskFirst")
        elif startup == "":
            Delta.run()
        elif startup == "False":
            Delta.run(False)
        else:
            print("invalid response, running in default always on mode")
            time.sleep(5)
            Delta.run()


    if __name__ == "__main__":
        Delta.run()
