import prompt


def print_hello():
    print('Welcome to the Brain Games!')


def enter_name():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    return f'Hello, {name}!'
