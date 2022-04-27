# SMR's Final Project

This project aims to compare the performance of two Languages Models by using SPARQL queries
This project has 2 main sections
1. Statistics page

    This page consists of 2 queries from wikidata along with a predicate that will then be sent to two language models to get the results
    the way it works is, 
    the first query is the question query, this is the query you want to use to get the data from wikidata

2. Playground page


## Requirements

For installing the software, you need to have access to the internet
and have python 3 installed.

To check if you have python 3 installed, type the following command in the Terminal:

```shell
$ python3 -V
```
You should get a result like this:
```shell
Python 3.6.13
```

If you don't have python 3 installed, please visit this [page](https://www.python.org/downloads/).

We will use the package manager [pip](https://pip.pypa.io/en/stable/) for our installations.


## Installation

1. Download the zip file from Github
2. Unzip the project
3. Open Terminal and navigate to the project's directory
4. It is highly recommended to use a virtual environment, to do this do:
```shell
$ python3 -m venv <name_of_your_environment>
$ source <name_of_your_environment>/bin/activate
```
5. And to make sure everything is up to date, do:
```shell
$ pip install --upgrade pip
```
6. Install all the required libraries
```shell
$ pip install -r requirements.txt
```
7. Apply the changes to the project
```shell
$ python mysite/manage.py migrate
```
8. Run the server
```shell
$ python mysite/manage.py runserver
```
* This will automatically launch a web server on the [Localhost](http://127.0.0.1:8000) port 8000.
* If the port is already in use, use the following command and specify the new port (recommended: 3000, 8080)
```shell
$ python mysite/manage.py runserver <new_port>
```
9. Open your prefered browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

10. Enjoy!


## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


for testing mac users
selenium
1. Open terminal
2. Navigate to the path where your chromedriver file is located
3. Execute the below command
4. 1. sudo cp chromedriver /usr/local/bin
5. 2. xattr -d com.apple.quarantine chromedriver


