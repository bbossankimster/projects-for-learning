# Projects for learning

The main object is to get experience in different types of Python application:

-   console application

-   Web application

-   bot application

-   RESTfull API application

# Getting Started

Clone repositary, activate env (if you want) and install requirements:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/bbossankimster/projects-for-learning.git
cd projects-for-learning
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Project 1. Network pinger

You can run simple ICMP ping from console, Telegram bot or Web application (by
API or from simple Text field)

## Console pinger application

Console pinger application is example of using `subprocess` and `pythonping`
modules

Application based on `subprocess` module:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python learning.py -app console_pinger -lib subprocess -host 8.8.8.8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application based on `pythonping` module:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python learning.py -app console_pinger -lib pythonping -host 8.8.8.8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead 8.8.8.8 you can put your host/IP to ping.

# 
