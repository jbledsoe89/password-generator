# Useful Resources:
# https://realpython.com/python-f-strings/
# https://docs.python.org/3/library/argparse.html
# https://www.youtube.com/watch?v=-Sgw-6a1HjU
# this did not work with powershell but still useful
# https://stackabuse.com/how-to-print-colored-text-in-python/
# this worked with powershell
# https://www.devdungeon.com/content/colorize-terminal-output-python#install_colorama
# https://stackoverflow.com/questions/61492538/how-do-i-scrape-a-randomly-generated-sentence-from-this-website


import argparse
import sys
import random
from typing import Optional
from typing import Sequence


# Ensure the length is between 4-300 characters.
def pass_length(s: str) -> int:
    try:
        value = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got: {s!r}')
    
    if value < 4 or value > 300:
        raise argparse.ArgumentTypeError(f'invalid length expected 4-300, got: {value}')
    
    return value

# Use only s, n, l, u options for now.
def character_options(s: str) -> str:
    valid_chars = 'snlu'
    for char in s:
        if char not in valid_chars:
            raise argparse.ArgumentTypeError(f'invalid character: {char!r}')
    return s

# Generate a password based on length, characters, with options to exclude similar characters, exclude ambiguous characters, and ensure the first character is a letter.
def generate_password(length: int, characters: str, exclude_similar: bool, exclude_ambiguous: bool, first_letter: bool) -> str:  
    char_list = []
    
    # Add symbols to the list of characters.
    if 's' in characters:
        char_list.extend('!@#$%^&*()_+-=[]{}|;:,.<>?')
    
    # Add numbers to the list of characters.
    if 'n' in characters:
        char_list.extend('0123456789')
    
    # Add lowercase letters to the list of characters.
    if 'l' in characters:
        char_list.extend('abcdefghijklmnopqrstuvwxyz')
    
    # Add uppercase letters to the list of characters.
    if 'u' in characters:
        char_list.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Remove similar characters from the list of characters.
    if exclude_similar:
        char_list = [char for char in char_list if char not in 'il1!0o']
    
    # Remove ambiguous characters from the list of characters.
    if exclude_ambiguous:
        char_list = [char for char in char_list if char not in '{}[]()/\'"!,;:>,.']
    
    # Generate a password.
    password = ''
    for i in range(length):
        
        # Change first character into a letter if letter flag is enabled.
        if first_letter and i == 0:
            if 'l' in characters and 'u' not in characters:
                password = random.choice('abcdefghijklmnopqrstuvwxyz')
            if 'u' in characters and 'l' not in characters:
                password = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            else:
                password = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        # Otherwise let's do our thing.
        else:
            password += random.choice(char_list)
    
    return password

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    
    # Sub-Commands
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True
    
    # Subparser for creating passwords with the keyword 'word'
    word_parser = subparsers.add_parser('word', help='Generate password.')
    
    # Argument which allows the user to generate multiple passwords to choose from.
    word_parser.add_argument('-n', '--number', type=int, default=1, help='number of passwords to generate')

    # Argument which allows the user to choose different lengths (4-300 characters).
    word_parser.add_argument('-l', '--length', type=pass_length, default=4, help='length of the password (4-300 characters, default: %(default)s)')
    
    # Argument which allows the user to select different types of characters (symbols, numbers, lower case, upper case).
    word_parser.add_argument('-c', '--characters', type=character_options, default='snlu', help='characters to use in the password ([s]ymbols, [n]umbers, [l]owercase, [u]ppercase, [s]ymbols, default: %(default)s)')
    
    # Argument to exclude similar characters (such as i, l, L, 1, and !).
    word_parser.add_argument('-x', '--similar', action='store_true', help='exclude similar characters (i, l, L, 1, and !)')
    
    # Argument to exclude ambiguous characters (such as {}[]()/\'"!,;:>,.).
    word_parser.add_argument('-a', '--ambiguous', action='store_true', help='exclude ambiguous characters ({}[]()/\'"!,;:>,.)')
    
    # Argument to ensure the first character is a letter.
    word_parser.add_argument('-f', '--letter', action='store_true', help='ensure the first character is a letter')      
    
    # If the user does not provide any arguments, print the help message.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args(argv)
    
    # Generate a password based on number of passwords, length, characters, with options to exclude similar characters, exclude ambiguous characters, and ensure the first character is a letter.
    for i in range(args.number):
        password = generate_password(args.length, args.characters, args.similar, args.ambiguous, args.letter)
        
        # Check to see if colorama is installed.
        try:
            import colorama
            from colorama import Fore, Back, Style
            colorama.init()
            
            # Color text based on yellow for uppercase, blue for lowercase, green for numbers, and magenta symbols.
            def colorize_text(text: str) -> str:
                colorized_text = ''
                for char in text:
                    if char.isupper():
                        colorized_text += Fore.YELLOW + Style.BRIGHT + char + Style.RESET_ALL
                    elif char.islower():
                        colorized_text += Fore.BLUE + Style.BRIGHT + char + Style.RESET_ALL
                    elif char.isdigit():
                        colorized_text += Fore.GREEN + Style.BRIGHT + char + Style.RESET_ALL
                    else:
                        colorized_text += Fore.MAGENTA + Style.BRIGHT + char + Style.RESET_ALL
                return colorized_text
            
            print(colorize_text(password))
            
        # Otherwise let's just do vanilla output.
        except ImportError:   
            print(password)
        
# Main Code
if __name__ == '__main__':
    exit(main())