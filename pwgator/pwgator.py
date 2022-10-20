# Useful Resources:
# https://realpython.com/python-f-strings/
# https://docs.python.org/3/library/argparse.html
# https://www.youtube.com/watch?v=-Sgw-6a1HjU
# this did not work with powershell but still useful
# https://stackabuse.com/how-to-print-colored-text-in-python/
# this worked with powershell
# https://www.devdungeon.com/content/colorize-terminal-output-python#install_colorama
# https://stackoverflow.com/questions/61492538/how-do-i-scrape-a-randomly-generated-sentence-from-this-website
# https://realpython.com/python-typer-cli/

__app_name__  = "pwgator"
__version__   = "0.1.0"
__author__    = "Jerald Bledsoe"

import argparse
import sys
import random
import time
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
    
    # Generate Password
    # Subparser for creating passwords with the keyword 'word'
    word_parser = subparsers.add_parser('word', help='Generate password.')
    
    # Argument which allows the user to generate multiple passwords to choose from.
    word_parser.add_argument('-n', '--number', type=int, default=1, help='number of passwords to generate')

    # Argument which allows the user to choose different lengths (4-300 characters).
    word_parser.add_argument('-l', '--length', type=pass_length, default=8, help='length of the password (4-300 characters, default: %(default)s)')
    
    # Argument which allows the user to select different types of characters (symbols, numbers, lower case, upper case).
    word_parser.add_argument('-c', '--characters', type=character_options, default='snlu', help='characters to use in the password ([s]ymbols, [n]umbers, [l]owercase, [u]ppercase, [s]ymbols, default: %(default)s)')
    
    # Argument to exclude similar characters (such as i, l, L, 1, and !).
    word_parser.add_argument('-x', '--similar', action='store_true', help='exclude similar characters (i, l, L, 1, and !)')
    
    # Argument to exclude ambiguous characters (such as {}[]()/\'"!,;:>,.).
    word_parser.add_argument('-a', '--ambiguous', action='store_true', help='exclude ambiguous characters ({}[]()/\'"!,;:>,.)')
    
    # Argument to ensure the first character is a letter.
    word_parser.add_argument('-f', '--letter', action='store_true', help='ensure the first character is a letter')
    
    # Password Check
    # Subparser for creating passwords with the keyword 'check'
    word_parser = subparsers.add_parser('check', help='Password Check.')
    
    # Argument which gets the string input of the password to check.
    word_parser.add_argument('-p', '--password', type=str, help='password to check')
    
    # Argument which allows the user to see if the password has a minimum number of characters.
    word_parser.add_argument('-m', '--minimum', type=int, default=1, help='minimum number of characters')
    
    # Argument which allows the user to see if the password has at least one uppercase letter.
    word_parser.add_argument('-u', '--uppercase', action='store_true', help='upper case letter')
    
    # Argument which allows the user to see if the password has at least one lowercase letter.
    word_parser.add_argument('-l', '--lowercase', action='store_true', help='lower case letter')
    
    # Argument which allows the user to see if the password has at least one number.
    word_parser.add_argument('-n', '--number', action='store_true', help='has a number')
    
    # Argument which allows the user to se if the password has at least one special character.
    word_parser.add_argument('-s', '--symbol', action='store_true', help='has a symbol')
    
    # If the user does not provide any arguments, print the help message.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args(argv)
    
    print("""
=------------------------------------------------------------------------------=   
                                      __            
        ____ _      __   ____ _____ _/ /_____  _____
       / __ \ | /| / /  / __ `/ __ `/ __/ __ \/ ___/
      / /_/ / |/ |/ /  / /_/ / /_/ / /_/ /_/ / /    
     / .___/|__/|__/   \__, /\__,_/\__/\____/_/     
    /_/               /____/  

                     _.---._     .---.
            __...---' .---. `---'-.   `.
    ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
    -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
    ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
        ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
            ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
        jgs   ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                        ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~

=------------------------------------------------------------------------------=
 This ASCII pic can be found at: https://asciiart.website/index.php?art=animals/reptiles/aligators
 Text Credits: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=pw%20gator
=------------------------------------------------------------------------------=""")
    
    # If the user enters word command
    if args.command == 'word':
 
        # Generate a password based on number of passwords, length, characters, with options to exclude similar characters, 
        # exclude ambiguous characters, and ensure the first character is a letter.
        print("Generating Password(s)..")
        for i in range(args.number):
            password = generate_password(args.length, args.characters, args.similar, args.ambiguous, args.letter)
        
            # Check to see if colorama is installed.
            try:
                import colorama
                from colorama import Fore, Style
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
        print("=------------------------------------------------------------------------------=")
                
    # If the user enters check command
    if args.command == 'check':
        
        password = args.password
        
        # Get a count of options to adjust minimum password length.
        # This is to ensure that the minimum length is not less than the number of options.
        count = 0
        if args.uppercase: count += 1
        if args.lowercase: count += 1
        if args.number: count += 1
        if args.symbol: count += 1
        if len(password) < count: print("Error: Password is too short for the supplied options.")
        else:
            # Check to see if colorama is installed.
            try:
                import colorama
                from colorama import Fore, Style
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
            
                rgb_Password = colorize_text(password)
                rgb_Green = Fore.GREEN + Style.BRIGHT
                rgb_Red = Fore.RED + Style.BRIGHT
                rgb_Clear = Style.RESET_ALL
            
            # Otherwise let's just do vanilla output.
            except ImportError:   
                rgb_Password = password
                rgb_Green = ''
                rgb_Red = ''
                rgb_Clear = ''
                   
            print("Password: " + rgb_Password)
            print("=------------------------------------------------------------------------------=")
                    
            # Establish responses and adjust formatting.
            response_min   = ['| Checking password meets minimum length...          | ', ' [Null]']
            response_upper = ['| Checking password contains uppercase characters... | ', ' [Null]']
            response_lower = ['| Checking password contains lowercase characters... | ', ' [Null]']
            response_num   = ['| Checking password contains numbers...              | ', ' [Null]']
            response_char  = ['| Checking password contains special characters...   | ', ' [Null]']
        
            # Check to see if the password meets the minimum length requirement.
            if args.minimum < len(password): response_min[1] = rgb_Green + '[Success!]' + rgb_Clear
            else: response_min[1] = rgb_Red + '[Failure!]' + rgb_Clear
            print(response_min[0], end="")
            time.sleep(1)
            print(response_min[1])
                    
            # Check to see if the password contains uppercase characters.
            if args.uppercase:
                if any(char.isupper() for char in password): response_upper[1] = rgb_Green + '[Success!]' + rgb_Clear
                else: response_upper[1] = rgb_Red + '[Failure!]' + rgb_Clear
                print(response_upper[0], end="")
                time.sleep(1)
                print(response_upper[1])
                
            # Check to see if the password has at least one lowercase letter.
            if args.lowercase:
                if any(char.islower() for char in password): response_lower[1] = rgb_Green + '[Success!]' + rgb_Clear
                else: response_lower[1] = rgb_Red + '[Failure!]' + rgb_Clear
                print(response_lower[0], end="")
                time.sleep(1)
                print(response_lower[1])
                        
            # Check to see if the password has at least one number.
            if args.number:
                if any(char.isdigit() for char in password): response_num[1] = rgb_Green + '[Success!]' + rgb_Clear
                else: response_num[1] = rgb_Red + '[Failure!]' + rgb_Clear
                print(response_num[0], end="")
                time.sleep(1)
                print(response_num[1])

            # Check to see if the password has at least one special character.
            if args.symbol:
                if any(not char.isalnum() for char in password): response_char[1] = rgb_Green + '[Success!]' + rgb_Clear
                else: response_char[1] = rgb_Red + '[Failure!]' + rgb_Clear
                print(response_char[0], end="")
                time.sleep(1)
                print(response_char[1])

                print("=------------------------------------------------------------------------------=")