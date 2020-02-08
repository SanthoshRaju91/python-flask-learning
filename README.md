# python-flask-learning

1. Setting up a virtualenv, so that the packages installed does not conflict with the system packages. We have to work in isolation, when working with python.

    Installing virtualenv in linux

    `sudo apt-get install virtualenv`

    Installing virtualenv in Mac with homebrew

    `brew install virtualenv`

2. Creating a virtualenv with python3 as the python executable.

    `virtualenv --python=python3 venv`

    For compatibilty reasons the venv folder will not be committed to project repository.

3. Activate virtualenv before running any python related commands or working on the project itself.

    `source venv/bin/activate`

4. Install application package dependencies with pip install, for sharing the packages dependencies of the project we include them in `requirements.txt` file and install them with the below command

    `pip install -r requirements.txt`


Forms without a proper redirect, might result in resubmission. Resulting in calking the same api again. If there was a client data tthat needs to saved to database this will cause duplication of records in the database.

So redirection should be encouraged.

Cookies are un encrypted, so use sessions always

5. Using python-dotenv for environment configurations.

    .flaskenv is not committed to the git because of sensitive information, so create one with the below content

    ```
    FLASK_APP='app.py'
    FLASK_ENV='development'
    SECRET_KEY='<with your secret key>'
    ```
