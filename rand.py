from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['$', '=', ',', "'", '"', '{', '}', '[', ']', '(', ')', '>', '<', '|', '_', '/', '\\', '~', '#', '@', '?', '%', '^', '&', '*', '-', '+', '!', '`', '.', ':', ';']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

all_char = letters[:] + symbols[:] + numbers[:]

let_num = letters[:] + symbols[:]

num_sym = numbers[:] + symbols[:]

sym_let = symbols[:] + letters[:]

def generate(sym_y_n, let_y_n, num_y_n, num_char):
    if sym_y_n == "yes" and let_y_n == "yes" and num_y_n == "yes":
        shuffle(all_char)
        password = ""
        for i in range(1, int(num_char) + 1):
            password = password + choice(all_char)
        return password
    elif sym_y_n == "no" and let_y_n == "yes" and num_y_n == "yes":
        shuffle(let_num)
        password = ""
        print(password)
        for i in range(1, int(num_char) + 1):
            password = password + choice(let_num)
        return password
    elif sym_y_n == "yes" and let_y_n == "no" and num_y_n == "yes":
        shuffle(num_sym)
        password = ""
        for i in range(1, int(num_char) + 1):
            password = password + choice(num_sym)
        return password
    elif sym_y_n == "yes" and let_y_n == "yes" and num_y_n == "no":
        shuffle(sym_let)
        password = ""
        for i in range(1, int(num_char) + 1):
            password = password + choice(sym_let)
        return password
    elif sym_y_n == "no" and let_y_n == "no" and num_y_n == "yes":
        shuffle(numbers)
        password = ""
        for i in range(1, int(num_char) + 1):
            password = password + choice(numbers)
        return password
    elif sym_y_n == "no" and let_y_n == "yes" and num_y_n == "no":
        shuffle(letters)
        password = ""
        for i in range(1, int(num_char) + 1):
            password = password + choice(letters)
        return password
    elif sym_y_n == "yes" and let_y_n == "no" and num_y_n == "no":
        shuffle(symbols)
        password = ""
        for i in range(1, int(num_char) + 1):
            password = password + choice(symbols)
        return password
    elif sym_y_n == "no" and let_y_n == "no" and num_y_n == "no":
        return "Try Again!"
    else:
        return "Error"