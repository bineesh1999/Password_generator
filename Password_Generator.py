import random
choices = ['!', '#', '$', '%', '&', '(', ')', '*', '+','0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("Welcome to the Random Password Generator!")
length = int(input("Length Of The Password : "))

def pass_word():
    password = []
    for i in range(length):
        password = password + [random.choice(choices)]

    print(f"Your Password is : {''.join(password)}")
    print("------------------------------------------")
    global reset
    reset = input("Try Again  Y/N : ").upper()
    if reset == "N":
        print("Thanks For Using Random Password Generator")
pass_word()
while reset =="Y":
    pass_word()


