# Unit-Testing

### setup

#### Install python on ubuntu
#### Clone the repo using the following command
    git clone git@github.com:Praful-Jain/Unit-Testing
#### Create a virtual environment 
    python3 -m venv name_of_evn 
#### Activate the virtual environment
    source path/to/env/bin/activate
#### Navigate to the project folder and install the requirements to the virtual environment
    pip install -r requirements.txt

### setup coverage.py
    
#### Install Coverage.py:
    pip install coverage

#### Run Tests with Coverage:
    coverage run -m unittest your_test_file.py

#### Generate Coverage Report:
    coverage report

#### Generate HTML Report (Optional):
    coverage html
