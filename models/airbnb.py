#!/usr/bin/python3


import cmd

class MyConsole(cmd.Cmd):
    '''
    a custom console command processor class.
    inherits from cmd.Cmd to provide an interactive shell
    with command processing capabilities
    '''
    pass
    
if __name__ == "__main__":
    '''
    executes the command loop if the script is ran in the main program
    '''
    MyConsole().cmdloop()    
