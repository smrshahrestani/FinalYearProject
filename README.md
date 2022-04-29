# SMR's Final Project


## Project Overview

The main idea behind this project is to compare the performance of two different AI-Language Models and see which one gives a better result in sentence completion tasks.

The app uses Wikidata's database as a source for evaluating the Language Models.
The way it retrieves the data is by using the SPARQL query language.
The app starts by getting two SPARQL queries as input from the user, along with an incomplete sentence that will be sent to and completed by two Language Models.

In the final stage, the app uses two different methods to evaluate the two Language Models with the answers retrieved from the Wikidata by comparing their similarities.
The first evaluation method is a strict string comparison, which uses the "Gestalt Pattern Matching" Algorithm to evaluate the answers.
The second method uses an AI-Language Model that tries to understand the sentence and score them based on its understanding of the sentences.

It is good to keep in mind that the result of the Language Model can vary every time. Also, the correctness of the results is not guaranteed. Language Model's behaviour highly relies on the way it was trained. The data that the Language Model was trained on also has a huge factor in its behaviour. So this project will use two different Language Models that were trained differently.
The two language models used are OpenAi: text-davinci-002, which is a Generative Pre-trained Transformer (GPT)
and HuggingFace: bert-base-uncased, that is a Masked language modelling (MLM)

At the end of the project, the app will give two individual scores for each sentence and an average score for both Language Models. The user then uses this result to evaluate the Language Models performance.

The second part of the app (Playground) is designed for getting the information that an endpoint might not have.
This part of the project also works with the SPARQL query language.
It queries the inputted query and sends the query result along with an incomplete sentence to be finished to the Language Models.
This section of the app also uses the same Language Models as the previous section.


----------------------------------------------------------------

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

----------------------------------------------------------------

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

----------------------------------------------------------------


## Testing


The app uses Chrome for testing, so users are required to download the Chrome on their PC if they are willing to run the functional tests(using selenium)

1. After ensuring that Chrome is installed, open a new Terminal and navigate to the projects directory.

2. Make sure the virtual environment in activated. If you haven't created one, go to step 4 in the Installation.

3. To run the tests, the server should be up and running. To run the server use a different Terminal and follow step 8 in the Installation.

then run the following command: 

```shell
$ python mysite/manage.py test webapp
```