#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    my_app create_room <room_type> <room_name>...
    my_app add_person <name> <category> [<need_accomodation>]
    my_app (-i | --interactive)
    my_app (-h | --help | --version)


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import cmd
import sys
from docopt import docopt, DocoptExit
from dojo import Dojo
from models.person import Fellow, Staff
#from models.room import Office, Living_space
dojo = Dojo()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            #We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class MyInteractive (cmd.Cmd):
    welcome = 'Welcome to the dojo'
    prompt = welcome

    @docopt_cmd
    def do_create_room(self, arg):
        """
        usage:
            my_app create_room <room_type> <room_name>...
        """
        name =arg['<room_name>']
        type_of_room = arg['<room_type>']

        create_room_status = dojo.create_room(name, type_of_room)
        if create_room_status == 'Invalid':
            print(create_room_status)
            return



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Done')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
