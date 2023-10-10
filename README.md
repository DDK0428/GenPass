# GenPass
A simple way of generating password as the users requirements. 

# Requirements
python3

# how to run the script
python3 genpass.py len [optional arguments]

# Help
python3 genpass.py -h 

usage: generate passwords as required by the user<br>

positional arguments:<br>
  len                   define the length of the password

options:
  -h, --help            show this help message and exit
  -u, --upper           include upper case letters to the password
  -l, --lower           include lower case letters to the password
  -n, --number          include numbers to the password
  -s, --special         include special characters to the password
  -e <characters_to_exclude>, --exclude <characters_to_exclude>
                        exclude any characters
