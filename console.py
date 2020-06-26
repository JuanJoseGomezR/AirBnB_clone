#!/usr/bin/python3
"""Console for HBNB
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """command processor"""
    
    prompt = "(hbnb)"
    
    classes = {"User", "BaseModel", "Place",
               "State", "Amenity", "City", "Review"}
    
    def do_create(self, line):
        """create command"""
        if line is None:
            print("** class name missing **")
        ##else:
            ###Continue###
            pass
            ##else:
                ##print("** class doesn't exist **")
    
    def do_show(self, line):
        """show command"""
        if line is None:
            print("** class name missing **")
        else:
            pass

    def do_EOF(self, line):
        """end of file"""
        return True
    
    def do_quit(self, line):
        """exit command"""
        return True

    def do_destroy(self, line):
        """destroy command"""
        if line is None:
            print("** class name missing **")
        else:
            pass
    
    def do_all(self, line):
        """self command"""
    
    def update(self, line):
        """update command"""
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()