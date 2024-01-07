from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, " Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("User name: ")
    pwd = input("Password: ")

    # add to the end of file or create a new one
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def manage_passwords():
    while True:
        mode = input(
            "Would you like to add a new password or view an existing one? Press q to quit ").lower()
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue


def check_master_password():
    input_pwd = input("Please, enter your master password (press q to quit): ")
    with open('master_password.txt', 'r') as f:
        for line in f.readlines(0):
            master_pwd = line.rstrip()
            decrypt_master_pwd = fer.decrypt(master_pwd.encode()).decode()
            if input_pwd == "q":
                break
            elif input_pwd == decrypt_master_pwd:
                manage_passwords()
            else:
                print("Your master password is incorrect, please try again")
                check_master_password()


check_master_password()
