from nicknames import *

def main():
    ng = NicknameGenerator()
    
    while True: 
        name = raw_input("Enter a name: ").title()
        nickname = ng.gen_nickname(name)
        if nickname:
            print("Your nickname is {} the {}".format(name,nickname))
        else:
            print("Sorry {}, I don't know how to pronounce your name".format(name))
        again = raw_input("Go again? ")
        if again.lower() in ['no','n']:
            break 

if __name__ == "__main__":
    main()
