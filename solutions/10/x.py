from termcolor import colored

print(colored('hello', 'red'), colored('world', 'green'))

for x in range(0, 10):
    if x % 2:
        print(colored(str(x), 'red'), end="")
    else:
        print(colored(str(x), 'green'), end="")

print()