from nicknames import *

def main():
    ng = NicknameGenerator()
    
    while True: 
        name = raw_input("Enter a name: ")
        nickname = ng.gen_nickname(name)
        print("Your nickname is {}".format(nickname))
        again = raw_input("Go again? ")
        if again.lower() in ['no','n']:
            break 

if __name__ == "__main__":
    main()
