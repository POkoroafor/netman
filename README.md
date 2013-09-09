this program is built to allow a server to monitor several networked devices 
updating a database with the status' of said devices to a database as well as 
collecting network data on the device for the use of troubleshooting for the 
network administrator. this will allow the network admin to more efficiently 
bring the network back online. the system will also be allowed to create ticket
events to have the network admin bring the devices online as well as 
deprioritizing the events when devices come back up on their own.







###Requirements:
## Twisted Framework - Event Driven Network Framework
https://github.com/twisted/twisted

## TXmongo 
https://github.com/oubiwann/txMongoModel

## Redis-py
https://github.com/andymccurdy/redis-py


##Later : 

# Django Framework  will be added for the GUI client 
https://github.com/django/django
https://github.com/treeio/treeio


##Fabric - Simple, Pythonic remote execution and deployment.
 https://github.com/fabric/fabric

##Sshuttle - Transparent proxy server. VPN. Forwards over ssh Supports DNS tunneling.
 https://github.com/apenwarr/sshuttle

##Tablib - Python Module for Tabular Datasets in XLS, CSV, JSON, YAML, etc.
 https://github.com/kennethreitz/tablib

##Diamond
 https://github.com/BrightcoveOS/Diamond




### Features wanted of the program


## Server

Monitor device states and check-ins

Update database with check-in data

Update device states in database 

Activly attempt to contact database when network device goes down

Create event with ticket to correct outages

Set ticket priorities corrisponding to network state

Collect outage and network data when devices come back online

Log all events on server

Thread process for each device being monitored

Schedule activity for each device

Updates stored ip address for device if change made
## Client
Connect to server and update with network status at scheduled intervoles

Update device state if server cannot be contacted after so many attempts

Device collects network data when outage occurs (stored in local database)

Make network outage data available to server when connected to server

Updates dns with server if ip address changes

# GUI

Display netowrk alerts and activities

Manage Tickets for down sites or new projects

Manage expendatures for projects and tickets 

Manage payments and fees for customers

Manage Invintory for each site and 
