from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

ans_cont = 0

num_1 = float(input("Enter first number: "))

calc_count = False
while not calc_count:

    per_op = input("""+\n-\n*\n/\nPick a Operation: """)

    num_2 = float(input("Enter Second Number: "))

    op = operations[per_op]

    ans = op(num_1, num_2)

    ans_cont = ans

    print(f"{num_1} {per_op} {num_2} = {ans}")

    # print(ans_cont)

    cont = input(f"Type 'y' to Calculate with {ans_cont}, or Type 'n' to start a New Calculation: ").lower()

    if cont == 'y':
        calc = False
        num_1 = ans_cont

    elif cont == 'n':
        calc = True




