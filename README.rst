==============================================
Socratease SDK in a Django Project
==============================================

A Django project which shows the working of the Socratease SDK.

Installation
============

Install Python 3.8 or higher

Create and enter a virtual environment

::

    python3 -m venv virtualenv
    source virtualenv/bin/activate

Install pip

::

    curl https://bootstrap.pypa.io/get-pip.py | python
    pip install setuptools --upgrade


To run this example install the python packages required by executing the following command:

::

    $ pip install -r requirements.txt

Run application
===============

::

    $ python manage.py runserver

Then, if you go to the URL http://127.0.0.1:8000/ in your web browser, and you see
Your Home Page on the screen, you know everything is working as expected.

Once the project is up and running, you can go to the URL http://127.0.0.1:8000/assessments/cms/home to see how the
Socratease SDK works. You can change the parameters in the .env file and see how they affect the SDK.