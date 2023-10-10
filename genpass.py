import random
import string
from argparse import ArgumentParser, Namespace

parser = ArgumentParser(prog='password generator')
parser.usage = 'generate passwords as required by the user'

parser.add_argument('len', type=int, help='define the length of the password')
parser.add_argument('-u', '--upper', help='include upper case letters to the password', action='store_true')
parser.add_argument('-l', '--lower', help='include lower case letters to the password', action='store_true')
parser.add_argument('-n', '--number', help='include numbers to the password', action='store_true')
parser.add_argument('-s', '--special', help='include special characters to the password', action='store_true')
parser.add_argument('-e', '--exclude', help='exclude any characters', metavar='<characters_to_exclude>')

args: Namespace = parser.parse_args()


def generate_password(length: int = 10):
    character_sets = []
    if args.upper:
        character_sets.append(string.ascii_uppercase)
    if args.lower:
        character_sets.append(string.ascii_lowercase)
    if args.number:
        character_sets.append(string.digits)
    if args.special:
        character_sets.append(string.punctuation)

    if not any([args.upper, args.lower, args.number, args.special]):
        character_sets = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]

    random_string = ''.join(character_sets)

    if args.exclude:
        exclude_list = list(args.exclude.strip())
        for char_to_exclude in exclude_list:
            random_string = random_string.replace(char_to_exclude, '')

    password: str = ''.join(random.choice(random_string) for i in range(length))
    return password


print(generate_password(args.len))
