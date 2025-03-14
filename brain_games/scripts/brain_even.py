#!/usr/bin/env python3
from brain_games import cli


def main():
    cli.print_hello()
    name = cli.enter_name()
    print(cli.welcome_user(name))


if __name__ == '__main__':
    main()
