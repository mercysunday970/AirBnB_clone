#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb) '
    class_list = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass
def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel.
        Exceptions:
            =>If the class name is missing, print ** class name missing **
                (ex: $ create)
            =>If the class name doesn’t exist, print ** class doesn't exist **
                (ex: $ create MyModel)
        """

        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            if arg[0] not in self.class_list:
                raise NameError

            new_inst = eval(arg[0])()
            new_inst.save()
            print(new_inst.id)

        except NameError:
            print("** class doesn't exist **")

        except SyntaxError:
            print("** class name missing **")

    def do_show(self, args):
        """  Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        Exceptions:
        => If the class name is missing, print ** class name missing **
            (ex: $ show)
        => If the class name doesn’t exist, print ** class doesn't exist**
            (ex: $ show MyModel)
        => If the id is missing, print ** instance id missing **
            (ex: $ show BaseModel)
        => If the instance of the class name doesn’t exist for the id,
            print ** no instance found **
            (ex: $ show BaseModel 121212)
        """
        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            if len(arg) < 2:
                raise IndexError()
            if arg[0] not in self.class_list:
                raise NameError()

            obj = storage.all()

            obj_key = arg[0] + "." + arg[1]

            if obj_key in obj:
                print(obj[obj_key].to_dict()["id"])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        Note:
            => If the class name is missing, print ** class name missing **
                (ex: $ destroy)
            => If the class name doesn’t exist, print ** class doesn't exist **
                (ex:$ destroy MyModel)
            => If the id is missing, print ** instance id missing **
                (ex: $ destroy BaseModel)
            => If the instance of the class name doesn’t exist for the
                id, print ** no instance found **
                (ex: $ destroy BaseModel 121212)
        """

        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            if len(arg) < 2:
                raise IndexError()
            if arg[0] not in self.class_list:
                raise NameError()

            obj = storage.all()

            obj_key = arg[0] + "." + arg[1]

            if obj_key in obj:
                del obj[obj_key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
    def do_all(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel.
        Exceptions:
            =>If the class name is missing, print ** class name missing **
                (ex: $ create)
            =>If the class name doesn’t exist, print ** class doesn't exist **
                (ex: $ create MyModel)
        """
        args = line.split()
        if len(args) == 0:
            content = models.storage.all()
            value_list = []
            for key in content.keys():
                value = content[key]
                value_list.append(str(value))
            print(value_list)
        else:
            if args[0] == "BaseModel":
                content = models.storage.all()
                value_list = []
                for key in content.keys():
                    value = content[key]
                    value_list.append(str(value))
                print (value_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")

        if len(args) > 0:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(args) == 3:
                            print("** value missing **")
                        else:
                            if len(args) >= 4 and args[0] == "BaseModel":
                                # reload the private attribute __object of the FileStorage class
                                FileStorage().reload()
                                # get all the content of the __object using the all function
                                content = FileStorage.all(FileStorage)
                                value_input = "{}.{}".format("BaseModel", args[1])
                                if content.get(value_input) is None:
                                    print("** no instance found **")
                                else:
                                    # obtain the BaseModel from the json file using the id
                                    obj = content[value_input]
                                    # convert the obj to dictionary using the to_dict function in the BaseModel class
                                    obj_to_dict = obj.to_dict()

                                    # convert the attribute and value to a string
                                    key = str(args[2])
                                    value = str(args[3])

                                    # update the existing dictionary(BaseModel)
                                    obj_to_dict[key] = value

                                    # convert the dictionary back to a BaseModel
                                    new_base_model = BaseModel(**obj_to_dict)
                                    # save to updated the updated_at attribute
                                    new_base_model.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
