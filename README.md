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

    