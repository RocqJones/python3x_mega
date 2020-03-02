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

### e) Error exception handling.
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

### f) Conditionals and inputs.
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

### g) Loops.
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
[map1](map1.png)

## 7.0 Website blocker.
* The program will pick listed websites and write on 'hosts' file which is on dir: 
- Linux >>> ```hosts_path = "/etc/hosts"
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

#### e) Creating python virstual environment and deploying the test website to a live server.
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
* [Specifying a Python Runtime](https://devcenter.heroku.com/articles/python-runtimes#supported-python-runtimes)
* We will use [Heroku](https://www.heroku.com/) which is a cloud platform as a service supporting several programming languages, in this case for Python. To install [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-cli) on Linux(Debian) distro use ```$ sudo snap install --classic heroku```
- **Login on terminal** - Open terminal on ```mywebdir``` directory and use ```heroku login``` to login.
- **Create app** - Run ```heroku create jonespyflaskdeploy```. Note that 'jonespyflaskdeploy' will be the domain name. Don't kill this terminal.
- **Check for parkages** - Use ```$ pip freeze``` on 'mywebdir' directory.
- **Create requirements** - See on 'mywendir'.
- **Create 'Procfile'** - On 'mywebdir' and it shouldn't have a any extension. This file will tell the heroku server to point to 'script.py' and point to object app.
- **Create runtime file** - Should be a txt file. The runtime changes you should confirm from [here](https://devcenter.heroku.com/articles/python-support#supported-runtimes).
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
