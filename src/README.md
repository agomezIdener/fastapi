# Before first deploy 

1. Create a virtual environment: We will use the venv module that comes with Python to create a virtual environment. This environment is a self-contained directory tree that includes a Python installation and any packages you install while the environment is active. This allows you to isolate your project's dependencies from other Python projects on the same machine.

python -m venv venv

2. Activate the virtual environment: The command to do this will depend on your operating system

.\venv\Scripts\activate

3. Install the project dependencies: The dependencies for your project are listed in the requirements.txt file. You can use pip, the Python package installer, to install these dependencies

pip install -r requirements.txt

