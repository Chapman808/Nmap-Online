# Nmap Online

Web application that uses user input to perform an Nmap SYN scan against ports 1-1000. 

## Details

This project uses the Django Web Framework, so there is third party library code within this project that I do not wish to take credit for. 
The CSS is also borrowed from public sources. **Credit to: https://github.com/thelearn-tech/hacker-theme**

## Demo

If you merely want to check out a demo of the application, visit the following link. I deployed the application in AWS under my own domain name:
http://nmap.chapman.sh/
NOTE: Please contact me for an API key to demo the application


On the back end, the service is running on port 8000. An Nginx reverse proxy server exposes the application publicly on port 80. The application connects to a MYSQL database hosted in AWS.

## Installation (Linux)

These steps assume Python3 is already installed and you are running on an Linux. We will also assume that you already have a MySQL server running somewhere.

1. Clone this repo
2. Install django and related dependendies:
   1. check if django is already installed: ```python -m django --version```
   2. if not, install it. ```python -m pip install Django```
   3. install django rest framework dependencies: ```python -m pip install djangorestframework``` and ```python -m pip install djangorestframework-api-key```
3. Install mysql client:  
   ```sudo apt-get install python3-dev default-libmysqlclient-dev build-essential``` # Debian / Ubuntu  
   or  
   ```sudo yum install python3-devel mysql-devel``` # Red Hat / CentOS  
   then  
   ```python -m pip install mysqlclient```
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
5. Update the API Key in settings.py with a new value:  
```API_KEY_SECRET = 'SECRET_VALUE' #CHANGE THIS```
   
7. Migrate database changes: ```python manage.py migrate```


## Running the Application 

1. Run the server: ```python3 manage.py runserver```
2. By default the server runs on localhost:8000. 
3. Access via browser:  
   ![image](https://user-images.githubusercontent.com/16928672/147989547-d3e67c4b-b8d4-4a72-a92b-90b099b6ffbd.png)

## Interacting with the REST API

Nmap Online includes a REST API to view past scans for a given hostname. 

**Supported Response Codes:** 200, 400  
**Returns:** JSON Array  
**Endpoints:**  
  - Past Scans (GET):
     - **Path:** /api/scans/
     - **Required Query parameter:** _host_
     - **Example:** /api/scans/?host=localhost

      **Example response (200 OK):**

      ```[{"model": "nmap.nmapresult", "pk": 9, "fields": {"host": "127.0.0.1", "ports": "[\"631/open/tcp//ipp///\"]", "timestamp": "2022-01-03T15:51:32.625Z"}}, {"model": "nmap.nmapresult", "pk": 11, "fields": {"host": "127.0.0.1", "ports": "[\"631/open/tcp//ipp///\"]", "timestamp": "2022-01-03T16:01:58.961Z"}}, {"model": "nmap.nmapresult", "pk": 12, "fields": {"host": "127.0.0.1", "ports": "[\"631/open/tcp//ipp///\"]", "timestamp": "2022-01-03T16:02:06.580Z"}}]```


