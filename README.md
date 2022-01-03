# Nmap Online (CrowdStrike Takehome Project)

Web application that uses user input to perform Nmap scans

## Disclaimers (Please Read)

This project uses the Django Web Framework, so there is third party library code within this project that I do not wish to take credit for. The business logic, of course, is my own. 

The CSS is also borrowed from public sources, because I do not intend to showcase front end design skills with this project. I did make some minor modifications to the css. **Credit to: https://github.com/thelearn-tech/hacker-theme**

## Installation (Linux)

These steps assume Python3 is already installed and you are running on an Linux. We will also assume that you already have a MySQL server running somewhere.

1. Clone this repo
2. Install django:
   1. check if django is already installed: ```python -m django --version```
   2. if not, install it. ```python -m pip install Django```
3. Install mysql client:  
   ```sudo apt-get install python3-dev default-libmysqlclient-dev build-essential``` # Debian / Ubuntu  
   or  
   ```sudo yum install python3-devel mysql-devel``` # Red Hat / CentOS  
   then  
   ```pip install mysqlclient```
4. Enter your database information and credentials into the Database section of NmapWeb/settings.py file. Then uncomment the lines:  
   ```
       DATABASES = {
        'default': {
    #        'ENGINE': 'django.db.backends.mysql',
    #        'NAME': 'YOURDATABASENAME',
    #        'USER': 'YOURUSERNAME',
    #        'PASSWORD': 'YOURPASSWORD',
    #        'HOST': 'YOURHOSTNAME',
            'PORT': '3306',
        }
    }
   ```
## Running the Application 

1. Run the server: ```python3 manage.py runserver```
2. By default the server runs on localhost:8000. This can be changed in settings.py
3. Access via browser:  
   ![image](https://user-images.githubusercontent.com/16928672/147896607-1262671d-55f2-4c63-a1c5-434f98be9301.png)

