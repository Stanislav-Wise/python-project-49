#!/usr/bin/env python3

from brain_games import cli


def main():
    cli.print_hello()
    name = cli.welcome_user()
    print(cli.welcome_user(name))


if __name__ == '__main__':
    main()
