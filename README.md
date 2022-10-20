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
 Text ASCII Credits: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=pw%20gator
=------------------------------------------------------------------------------=""")

usage: pwgator word [-h] [-n NUMBER] [-l LENGTH] [-c CHARACTERS] [-x] [-a]
                    [-f]

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        number of passwords to generate
  -l LENGTH, --length LENGTH
                        length of the password (4-300 characters, default: 8)
  -c CHARACTERS, --characters CHARACTERS
                        characters to use in the password ([s]ymbols,
                        [n]umbers, [l]owercase, [u]ppercase, [s]ymbols,
                        default: snlu)
  -x, --similar         exclude similar characters (i, l, L, 1, and !)
  -a, --ambiguous       exclude ambiguous characters ({}[]()/'"!,;:>,.)
  -f, --letter          ensure the first character is a letter
  
usage: pwgator check [-h] [-p PASSWORD] [-m MINIMUM] [-u] [-l] [-n] [-s]

options:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        password to check
  -m MINIMUM, --minimum MINIMUM
                        minimum number of characters
  -u, --uppercase       upper case letter
  -l, --lowercase       lower case letter
  -n, --number          has a number
  -s, --symbol          has a symbol