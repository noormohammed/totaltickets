# Do lots of things

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/noormohammed/totaltickets.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

### For running the django application

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd totaltickets
(env)$ python manage.py runserver
```
Open a browser and go to `http://127.0.0.1:8000/samples/`.


### For running the test cases
`coverage run manage.py test samples -v 2`


### Coverage report
`coverage report`
