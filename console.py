#!/usr/bin/python3
"""Console for HBNB
"""

import shlex
import cmd
import json
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """command processor
    """

    prompt = "(hbnb) "

    classes = ["BaseModel", "State", "City",
               "Amenity", "Review", "Place", "User"]

    def do_create(self, line):
        """create command
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        if line not in self.classes:
            print("** class doesn't exist **")
            return
        if line == self.classes[0]:
            new_obj = BaseModel()
        elif line == self.classes[1]:
            new_obj = State()
        elif line == self.classes[2]:
            new_obj = City()
        elif line == self.classes[3]:
            new_obj = Amenity()
        elif line == self.classes[4]:
            new_obj = Review()
        elif line == self.classes[5]:
            new_obj = Place()
        elif line == self.classes[6]:
            new_obj = User()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """show command
        """
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        # line = line.split()
        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        stor_obj = storage.all()
        if len(line) >= 1:
            for obj_d in stor_obj.keys():
                splite = obj_d.split(".")
                if splite[0] != line[0] or splite[1] != line[1]:
                    continue
                prnt_obj = stor_obj[obj_d]
                print(prnt_obj)
                return
        print("** no instance found **")

    def emptyline(self):
        """Empty File
        """
        return

    def do_EOF(self, line):
        """end of file
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_destroy(self, line):
        """destroy command
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        line = line.split()
        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        stor_obj = storage.all()
        obj_del = "{}.{}" .format(line[0], line[1])
        if obj_del in stor_obj:
            del(stor_obj[obj_del])
            storage.save()

    def do_all(self, line):
        """self command
        """
        if line not in self.classes and len(line) > 0:
            print("** class doesn't exist **")
            return
        stor_obj = storage.all()
        obj = []
        for obj_id in stor_obj.keys():
            if len(line) > 0:
                if obj_id.split(".")[0] != line:
                    continue
            obj.append(str(stor_obj[obj_id]))
        print(obj)

    def do_update(self, line):
        """update command
        """
        try:
            if not line:
                raise SyntaxError()
            #my_list = line.split()
            my_list = shlex.split(line)
            if my_list[0] not in self.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            if my_list[2] in v.__dict__:
                t = type(v.__dict__[my_list[2]])
                v.__dict__[my_list[2]] = t(my_list[3])
                v.save()
            else:
                try:
                    v.__dict__[my_list[2]] = eval(my_list[3])
                    v.save()
                except Exception:
                    v.__dict__[my_list[2]] = my_list[3]
                    v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
