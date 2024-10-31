import random
saves = []
a = 'QWERTYUIOPASDFGHJKLZXCVBNM'
b = 'qwertyuiopasdfghjklzxcvbnm'
c = '1234567890'
d = '!@#$%^&*()_+{}:">?,./'
symbols = a + b + c + d
def main_menu():
    while True:
        print("Menu")
        print("1. Generate Random Pass")
        print("2. Generate by a certain num of symbols")
        print("3. Check saves")
        print("4. Exit")

        choice = input("\nChoose option: ")

        if choice == '1':
                generate_random_password()
        elif choice == '2':
                generate_variety_password()
        elif choice == '3':
                check_saves()
        elif choice == '4':
            print("Exiting from program")
            break
        else:
             print("error, retry.")
def generate_random_password():
    password = ''
    length = int(input("Enter the length: "))
    for i in range(length):
        password += random.choice(symbols)
    print(password)
    saves.append(password)
def generate_variety_password():
    password = ''
    for i in range(8):
        password += random.choice(symbols)
    print(password)
    saves.append(password)
def check_saves():
    if saves:
        for idx, password in enumerate(saves, start=1):
            print(f"{idx}. {password}")
    else:
        print("Empty")
main_menu()