# HBNB
This is the console/command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a file storage.

## Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review
### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands
To start, navigate to the project folder and enter ./console.py in the shell.

#### Create
```create <class name>``` Ex: ```create BaseModel```

#### Show
```show <class name> <object id>``` Ex: ```show User my_id```

#### Destroy
```destroy <class name> <object id>``` Ex: ```destroy Place my_place_id```

#### All
```all``` or ```all <class name>``` Ex: ```all``` or ```all State```

#### Quit
```quit``` or ```EOF```

#### Help
```help``` or ```help <command>``` Ex: ```help``` or ```help quit```

Additionally, the console supports ```<class name>.<command>(<parameters>)``` syntax. Ex: ```City.show(my_city_id)```

### How to use it
#### Using the Console
The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```
Alternatively, to use the AirBnB console in interactive mode, run the file console.py by itself:
```
$ ./console.py
```
While running in interactive mode, the console displays a prompt for input:
```
$ ./console.py
(hbnb)
```
To quit the console, enter the command quit, or input an EOF signal (ctrl-D).
```
$ ./console.py
(hbnb) quit
$
$ ./console.py
(hbnb) EOF
$
```
