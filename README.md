# python3x_mega
Learn Python3x programming from the basics all the way to creating your own, powerful scripts, web apps and games.

## 1.0 Major basics.
### a) Strings.
#### String Literals
* String literals in python are surrounded by either single quotation marks, or double quotation marks.
```
print("Hello")
```
* Assign string to a variable.
```
a = "Hello"
print(a)
```
##### Multiline string.
```
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
ut labore et dolore magna aliqua."""
print(a)
```
#### String Array.
* Get the character at position 1.
```
a = "Hello, World!"
print(a[1])
```
#### Slicing.
* You can return a range of characters by using the slice syntax.
```
b = "Hello, World!"
print(b[2:5])
```
#### Negative Indexing.
* Get the characters from position 5 to position 1, starting the count from the end of the string
```
b = "Hello, World!"
print(b[-5:-2])
```

### b) List.
List is a collection which is ordered and changeable. Allows duplicate members.
```
my_list = ["apple", "banana", "cherry"]
print(my_list)
```
* Access item.
```
my_list = ["apple", "banana", "cherry"]
print(my_list[1])
```
* Negative indexing.
```
my_list = ["apple", "banana", "cherry"]
print(my_list[-1])
```
* **Range of Indexes.** You can specify a range of indexes by specifying where to start and where to end the range.
```
list_of_fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list_of_fruits[2:5])
```

### c) Tuple.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
```
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
```

### d) Dictionary.
Dictionary is a collection which is unordered, it consists of **keys** and **values**.
```
car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car_dict)
```
* Accessing Items through:
**keys** -> ```x = car_dict["model"]```, and also through 
**values** -> ```x = car_dict.get("model")```

### e) Sets
A set is a collection which is unordered, it consists of **keys** and **values** but doesnot allow duplication

### f) Error exception handling.
It is possible to write programs that handle selected exceptions.
#### ValueError.
```
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```
#### 'except' handling.
* The try statement works as follows.
```
class B(Exception):
    pass
    
class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
#### The try … except statement with an optional else clause.
```
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### g) Conditionals and inputs.
* 'if' - Declears a condition.
* 'elif' - If the previous conditions were not true, then try this condition.
* 'else' - Catches anything which isn't caught by the preceding conditions.
```
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

### h) Loops.
#### i. for loop
* A 'for' loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

#### ii. while loop
* 'while' loop can execute a set of statements as long as a condition is true.
```
i = 1
while i < 6:
  print(i)
  i += 1
```

#### loops with multiple list.
* Map. Iterate on both lists in parallel
```
a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']
for x, y in map(None, a, b):
    print(x, y)
```

* Zip. Built-in function zip also lets you iterate in parallel
```
a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']
for x, y in zip(a, b):
    print(x, y)
```

## 2.0 File handling.
Refers to creating, reading, updating, and deleting files.
* **r** - Read - Default value. Opens a file for reading, error if the file does not exist.
* **a** - Append - Opens a file for appending, creates the file if it does not exist.
* **w** - Write - Opens a file for writing, creates the file if it does not exist.
* **x** - Create - Creates the specified file, returns an error if the file exists.
### a) Opening and reading files.
```
f = open("demofile.txt", "r")
print(f.read())
```

### b) Opening and writting files.
```
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```

#### Date and time.
```
import datetime

x = datetime.datetime.now()
print(x)
```

## 3.0 Commandline interactive dictionary.
* This is the first application. Building a commandline interactive dictionary which can predict words that matches a word with a typo by prompting similar words to the typed one.
* Follow guide.txt on '3.0 App1:Building_Interactive_Dict' directory.

## 4.0 Data analysis with Pandas.
Installation requirements are as follows. Note this is for Linux(Debian) users.
```
sudo apt-get install python3-pandas
pip install geocode
```

## 5.0 Numpy.
NumPy is a Python package which stands for 'Numerical Python'. It is the core library for scientific computing, which contains a powerful n-dimensional array object. Requirements are...
```
pip install numpy
pip install opencv-python
```
* Numpy dimensions with images.
* Stacking and splitting.

## 6.0 Webmaps with python folium.
For this section you will need to install folium as ```pip3 install folium``` on terminal.
Example:
```
>>> import folium
>>> map = folium.Map(location=[-3.401530, 38.555789], zoom_start=40)
>>> map
<folium.folium.Map object at 0x7f263b7a4b00>
>>> map.save("Map1.html")
```
* This will create 'Map1.html' that you can run on browser.
[map1](6.0App2:Creating_Webmaps_with_Folium/map1.png)

## 7.0 Website blocker.
* The program will pick listed websites and write on 'hosts' file which is on dir: 
- Linux >>> ```hosts_path = "/etc/hosts"```
- Windows >>> ```C:\Windows\System32\drivers\etc\hosts```
* The program will send the domains with start block time and end block time.

## 8.0 Building website with Python and Flask.
**Flask** is a python framework that has all tools and templates to build a website.
#### a) Install flask
```
pip install flask
```

#### b) Create first website.
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here!"

if __name__ == "__main__":
    app.run(debug=True)
```
* Run the above code on terminal as ```$ python3 script.py``` and run generated link on the browser.

#### c) Returning a HTML template.
* Use ```render_template``` from Flask. Ckeck the source-code at 'Returning_HTML_Template' directory.

#### d) Structure. 
```
root_dir/
    static/     /* Styling css, images and javascript goes in this dir */
    templates/  /* All '.html' files to be rendered goes to this dir */
    script.py
```

#### e) Creating python virtual environment and deploying the test website to a live server.
* Install virtual environment ```pip install virtualenv``` . The best practice is to create the virtual env before creating the project.
* On the root directory of project structure put all previous folders and files in one folder 'mywebdir' and create an virtual environment by running ``` $ python3 -m venv virtual``` command.
* Now the project structure will be like:
```
root_dir/
    mywebdir/
        static/
            css/
                main.css
                style.css
                styleform.css
        templates/
            layout.html
            home.html
            about.html
        script.py
        ...
    virtual/
        bin/
        include/
        lib/
        lib64/
        share/
        pyvenv.cfg
```
* We will use [Heroku](https://www.heroku.com/) which is a cloud platform as a service supporting several programming languages, in this case for Python. To install [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-cli) on Linux(Debian) distro use ```$ sudo snap install --classic heroku```
- **Login on terminal** - Open terminal on ```mywebdir``` directory and use ```heroku login``` to login.
- **Create app** - Run ```heroku create jonespyflaskdeploy```. Note that 'jonespyflaskdeploy' will be the domain name. Don't kill this terminal.
- **Check for parkages** - Use ```$ pip freeze``` on 'mywebdir' directory.
- **Create requirements** - See on 'mywendir'.
- **Create 'Procfile'** - On 'mywebdir' and it shouldn't have a any extension. This file will tell the heroku server to point to 'script.py' and point to object app.
- **Create runtime file** - Should be a txt file. For the runtime changes you should confirm from [here](https://devcenter.heroku.com/articles/python-support#supported-runtimes).
- **Initialize Git** - Go back and proceed from step 'b' which is step 5 in ```heroku_guide.txt```.
- **Add project files in .git repo** - Run ```$ git add .```
- **Commit changes** - ```$ git commit -m "first commit"```
- **Tell heroku which app we're working on** - ```$ heroku git:remote --app jonespyflaskdeploy```. So everything you do is applied to the domain.
- **Push changes** - ```$ git push heroku master```

* Now open browser and run link: https://jonespyflaskdeploy.herokuapp.com/ or ```$ heroku open```

The project structure should look like:
```
root_dir/
    mywebdir/
        static/
            css/
                main.css
                style.css
                styleform.css
        templates/
            layout.html
            home.html
            about.html
        Procfile
        requirements.txt
        runtime.txt
        script.py
    virtual/
```
**NOTE:** The complete [heroku deployment guide text file will be found here.](https://github.com/RocqJones/python3x_mega/blob/master/8.0App4:Website_with_Python_and_Flask/heroku_guide_8.4.txt)

## 9.0 Graphical User Interface with Tkinter.
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit. Import the Tkinter module.

## 10.0 Python with SQLite and PostgreSQL Databases.
* **SQLite** - It's portal type of database, meaning the user doesn't need to install the database to run a program. SQLite uses ```sqlite3``` Python library. 
* **PostgresSQL** - USed by python to communicate wide range of data between databse servers and browsers or other apps. PostgresSQL uses ```psycopg2``` Python library. This must be installed.

### SQLite Database steps.
1. Connect to database.
2. Create a cursor object.
3. Write an SQL query.
4. Close database connection.
```
def create_db_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
```
### PostgreSQL Psycopg2 steps.
**1. [Installation](https://www.postgresql.org/download/) in Linux(Debian)**
```
$ sudo apt-get install postgresql postgresql-contrib libpq-dev python3-dev
$ pip install psycopg2
```
* To confirm installation on Linux Debian run ```$ sudo -u postgres psql -c "SELECT version();"```
* Check if the Postgres database is truly initialized: ```$ pg_isready```
* To make sure that the service is up and running fine, run the following command
```
systemctl status postgresql
```
* For Window users use [Precompiled python Libraries](https://www.lfd.uci.edu/~gohlke/pythonlibs/) to install psycopg2.

**2. PostgreSQL Roles and Authentication Methods.**
PostgreSQL handles database access permissions using the concept of roles. **A role** can represent a database user or a group of database users.
* PostgreSQL supports a number of most commonly used authentication methods which are:
**a. Trust.** With this method, the role can connect without a password, as long as the criteria defined in the ```pg_hba.conf``` are met.
**b. Password.** A role can connect by providing a password. The passwords can be stored as ```scram-sha-256 md5``` and ```password``` (clear-text).
**c. Ident.** This method is only supported on TCP/IP connections. Works by obtaining the client’s operating system user name, with an optional user name mapping.
**d. Peer.** Same as Ident but it is only supported on local connections.
* The postgres user is typically used only from the local host and it is recommended not to set the password for this user.
* **Useful systemctl commands to manager the Postgres service under systemd.**
```
$ systemctl start postgresql
$ systemctl restart postgresql
$ systemctl stop postgresql
$ systemctl reload postgresql 		#this reloads the service configuration
```

**3. Securing and Configuring PostgreSQL Database.**
By default, the Postgres uses the concept of roles to manage database access permissions and database roles are conceptually completely separate from operating system users.
* The Postgres system user account is not protected using a password, to secure it, you can create a password using the **passwd utility**.
```
$ sudo passwd postgres
```
* Postgres role (or administrative database user) is not secured by default. You also need to secure it with a **password**.
```
$ su - postgres
$ psql -c "ALTER USER postgres WITH PASSWORD 'securepass_here';"
```

**4. Configuring Client Authentication.**
The main Postgres configuration file is located at ```/etc/postgresql/11/main/postgresql.conf```. Postgres uses two other manually-edited configuration files, which control client authentication.
* Configure md5 password authentication for client authentication.
```
$ sudo nano /etc/postgresql/11/main/pg_hba.conf
```
Look for the following line and change the authentication method from ```peer``` to ```md5``` as shown below:
```
# "local" is for Unix domainsocket connections only
local   all             all                                     md5
```
* Save the changes in the file and exit it. Then apply the recent changes by restarting the Postgres service as follows.
```
$ systemctl restart postgresql
```

**5. Creating a New Database and Database Role/User in PostgreSQL.**
First, switch to the postgres account and open the Postgres shell as follows.
```
$ su - postgres
$ psql
```
* To create a database called “test_db” run the following SQL command.
```
# CREATE DATABASE test_db;
```
* Then create a database user (a role with login rights) who will manage the new database as follows. This assumes login function by default.
```
# CREATE USER test_user WITH ENCRYPTED PASSWORD 'postgre123';
```
* Grant privilages.
```
# GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;
```
* To connect to the test_db as the user test_user, run the following command.
```
psql -d  test_db  -U test_user
```
* List databases: ```postgres=# \l or \list```
* Switching Databases: ```postgres=# \c test_db```
* Listing Tables: ```test_db=# \dt```
* To view running servers: ```netstat -nlt```
* To initialize a server: ```psql -h 0.0.0.0 -U postgres```. Replace 0.0.0.0 with e.g 127.0.0.1

## 11.0 Django.
* [Installation](https://www.djangoproject.com/download/): ```$ pip install Django==3.0.4``` and check version to see if it's installed ```$ django-admin.py --version```.
### Creating project.
Whether you are on Windows or Linux, just get a terminal or a cmd prompt and navigate to the place you want your project to be created, then use this code
```
$ django-admin startproject myproject
```
* This will create a "myproject" folder with the following structure −
```
myproject/
   manage.py            # The project's local django-admin for interacting with your project via command line
   myproject/           # python packages of your project.
      __init__.py       # treat this folder as package
      settings.py       # project settings
      urls.py           # All links of your project and the function to call
      wsgi.py           # If you need to deploy your project over WSGI.
```
Django also supports:
* MySQL (django.db.backends.mysql)
* PostGreSQL (django.db.backends.postgresql_psycopg2)
* Oracle (django.db.backends.oracle) and NoSQL DB
* MongoDB (django_mongodb_engine)
### Running the project
* To run project: ```$ python manage.py runserver```. You should have something like;
```
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 16, 2020 - 06:49:24
Django version 3.0.4, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
* If you experience issues run ```$ python manage.py migrate``` that should resolve the issue and run the project again.
### Create an Application.
* In main “myproject” folder, the same folder then manage.py:
```
$ python manage.py startapp myapp
```
* Django creates a “myapp” folder with the application structure:
```
myapp/
   __init__.py      # Make sure python handles this folder as a package
   admin.py         # Helps you make the app modifiable in the admin interface
   models.py        # This is where all the application models are stored.
   tests.py         # This is where your unit tests are.
   views.py         # This is where your application views are.
```
* At this point it's set up follow on source code '11.1' on '11.0Django' directory.
* **To create superuser do:** ```$ python manage.py createsuperuser```

## 12.0 Desktop database bookstore store application.
A program that stores book information:
* Title, Author
* Year, ISBN

User can View, Search, Add entry, Update entry, delete, and close app.

##### Requirements.
* Tkinter and sqlite3 database.

#### 12.3 Bank Account with OOP
* This program makes you understand disciplines of using OOP (Object Oriented Programming).
* It covers classes, functions, and inheritance.
* Program functionality include: **Checking bank balance, deposit, withdraw, transfer to other account.**

#### 12.4 OOP glossary
The program covers:
* Classes.
* Object instances.
* Instance variable.
* Class variable

## 13.0 Python image and video processing with OpenCV (Open-source Computer Vision) library.
It is learning computer vision in Python.
* [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) - It is a field that deals with acquiring and processing images and it makes decisions based on them. So you pass an image and the computer tries to understand the image and it can tell you how many faces are in the image.
#### 13.1 Loading, resizing, and writting image.
This script loads an image, resizes it, display on a window and the writes to a new file.
#### 13.2 Script that resizes all images.
The loop reads each image, resizes, displays,waits for the user input key, closes the window once the key is pressed and then writes the resized image under the existing file name together with the "resized_" prefix. The script resizes all images in a directory to 100x100.
#### 13.3 Face detection.
I will use front face cascades for this section and if you need more cascades check them [here.](https://github.com/Itseez/opencv/tree/master/data/haarcascades)
#### 13.4 Capturing video.
This program appreciates [VideoCapture()](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html) method that triggers video capture using a webcam.

## 14.0 Webcam motion detector.
* I will create a motion detector that records when an object passes infront of a computer camera. 
* The program will record the start time and end time of an object and draw a graph that shows how the motion was detected. 
