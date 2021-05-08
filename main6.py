"""
Opposite The Word

This script serves the feature of creating opposite version (reverse) of any word and then display it to you. The script is written in Python3, and intended for beginners to learn.

Author : Nikhil Raj Pandey (https://github.com/NikhilRajPandey/)
Created on : - December 2, 2018

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 8, 2021

Changes made in last modification :
1. Changed the old lengthy algorithm with the newer way of reversing the word.
2. Added commented docs, and cleaned the code and its structure.

Authors contributed to this script (Add your name below if you have contributed) :
1. Nikhil Raj Pandey (github:https://github.com/NikhilRajPandey/, email:nikhilrajpandey1@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Defining the reverse function to get a reversed form of an string entered. The function takes one parameter (argument) : string. Pass the string which you want a reverse of to this function while calling it.
reverse = lambda string : string[::-1]

def main():
    # Asking the user to enter the string (word)
    string = input('Enter a word : ')
    
    # Displaying the opposite of the word on the console screen
    print(f'[ The reverse of the entered word is "{reverse(string)}" ]')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses the CTRL+C key combo, then we exit

        exit()
    except Exception as e:
        # If there are any errors encountered during the process, then we display the error message on the console screen

        print(f'\n[ Error : {e} ]')

# Older version of the source code :
# ----
# _over = False
# while _over != True:
#     print("q for exit")
#     _list = input("Word:")
#     if _list == "q":
#         _over = True
#     else:
#         _return = ""
#         _list2 = []
#         i = -1

#         for words in _list:
#             _list2.append(words)

#         for _words in _list2:
#             _return = _return + _list2[i]
#             i = i - 1
#         print(_return)
# ----
