"""               _                                    
     __ _      __| |     __ _      _ _ _      ____     
    / _` |    / _` |    / _` |    | ` ` |    / __/     
   | (_| |   | (_| |   | (_| |    | | | |    \__ \     
    \__,_| ⍟ \__,_|▄⍟▄\__,_|█⍟▄|_|_|_| ⍟ /___/ ⍟  
                   ███           ███                   
                 ███               ███                 
                ██                   ██                
                         ▄▄█▄▄                         
               ▄       ███───███       ▄               
              ███     ███──█──███     ███              
               ▀       ██──▄──██       ▀               
                         ▀▀█▀▀                         
                ██                   ██                
                 ███               ███                 
    Automated Decentralization And Management System   
                    ▀▀▀█████████▀▀▀                    
"""

import os
import sys
import subprocess

from sys import platform
import manager
import installer
from time import sleep
from display import clear_screen
from colours import colours
from splash import splash
    
PATH = os.getcwd()      # A.D.A.M.S. Directory

if platform == "linux":
    from getch import getch as getch
    DATA_PATH = os.getcwd() + '/data/'      # Linux directory format
elif platform == "win32":
    from msvcrt import getch as getch
    DATA_PATH = os.getcwd() + '\data\\'     # Windows directory format

if os.geteuid() != 0:
    subprocess.call(['sudo', './adams'], cwd=PATH)
    sys.exit()


class main:

    menu_title = ""     # Initialize string: menu_title
    menu_options = {}   # Initialize array: menu_options
    menu_prompt = ""    # Initialize string: menu_prompt
    
    def __init__(self):
        clear_screen()
        self.set_menu("MAIN")
        self.main_menu()
    #################################################### END: __init__()

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
    #################################################### END: get_input(prompt)

    def print_header(self):
        clear_screen()  # Clear console window
        print(colours().title("\n\t" + self.menu_title[1] + "\n\n"))   # Print menu title
    #################################################### END: print_header()

    def print_options(self):
        for key, value in self.menu_options.items():
            if str(key) == 'SPACE':
                print()
            else:
                print("\t    " + colours().cyan(str(key)) + ": " + str(value))
        print()
    #################################################### END: print_options()

    def set_menu(self, menu_id):
        global menu_title
        global menu_options
        
        if menu_id.upper() == "MAIN":   # If Main menu requested do the following
            self.menu_title = ["MAIN", 
                          "A.D.A.M.S."]
                          
            self.menu_options = {"1" : "Install", 
                            "2" : "Configuration",
                            "SPACE" : "", 
                            "Q" : "Quit"}
    #################################################### END: set_menu(menu_id)

    def main_menu(self):
        self.set_menu("MAIN")
        
        try:
            while True:
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1" or user_input.upper() == "I":
                    #subprocess.run(["sudo", "python3", "modules/installer.py"], check=True)
                    installer.cli()
                elif user_input.upper() == "2" or user_input.upper() == "C":
                    #subprocess.run(["sudo", "python3", "modules/manager.py", self.POWERDNS_CONF_PATH], check=True)
                    manager.cli()
                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    clear_screen()    # Clear console window
                    sys.exit(0)
        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            self.main_menu()
    #################################################### END: main_menu()

if __name__ == '__main__':
    splash()
    main()
#################################################### END: __main__