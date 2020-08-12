class Command:

    def __init__(self):
            self.running = False
            self.command_list = ["exit : exits the command line"]

    def run(self):

        self.running = True

        if self.running == True :
            while self.running == True:
                val = input(">> ") 
                print(val.split())
                if "exit" in val.split():
                    quit()
                if "help" in val.split():
                    help()
        
    def quit():
        self.running = False
        return self.running

    def help(self):
        print(self.command_list)

    def exit(self):
        run = False
        return run