# Logs Analysis Project
### A tool that generating informative summary from logs of newspaper website.  
####  Logs Analysis Project done by Mohammed Alsubhi as part of [Udacity's Full Stack Developer Nanodegree](https://sa.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
### Introduction
This tool coded using [python](https://www.python.org/) to:

 1. Connect to database.
 2. Execute queries.
 3. Analysis results.
 4. Format and print informative reports.
 
 This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
 
 1. **What are the most popular three articles of all time?**
 2. **Who are the most popular article authors of all time?**
 3. **On which days did more than 1% of requests lead to errors?**

### Requirements:
|Requirement| Version
|--|--|
| Python | [2.7](https://www.python.org/) |
| Psycopg2 | [2.7.5](http://initd.org/psycopg/download/) |
| PostgreSQL| [9.5.14](https://www.postgresql.org/download/) |
| Vagrant| [2.2.0](https://www.vagrantup.com/downloads.html) |
| VirtualBox| [5.1.38](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) |

### Instructions:
After achieve all previous requirements:

 

 1. Clone or direct download [ud-Logs-Analysis](https://github.com/MH-Alsubhi/ud-Logs-Analysis) repository.
 2. Download [Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  and extract it, you will find file called `newsdata.sql`.
 3. copy `newsdata.sql` file to [ud-Logs-Analysis](https://github.com/MH-Alsubhi/ud-Logs-Analysis) folder.
 4. Navigate to [ud-Logs-Analysis](https://github.com/MH-Alsubhi/ud-Logs-Analysis) folder.
 5. Open CLI (cmd,pwoershell,bash ..etc) in same folder to run Vagrant VM Machine by using this command:
 ```
$ vagrant up
```
You should see something like this: 

    $ vagrant up                                                                              
    Bringing machine 'default' up with 'virtualbox' provider...                               
    ==> default: Checking if box 'bento/ubuntu-16.04' is up to date...                        
    ==> default: Clearing any previously set forwarded ports...                               
    ==> default: Clearing any previously set network interfaces...                            
    ==> default: Preparing network interfaces based on configuration...                       
        default: Adapter 1: nat                                                               
    ==> default: Forwarding ports...                                                          
        default: 8000 (guest) => 8000 (host) (adapter 1)                                      
        default: 8080 (guest) => 8080 (host) (adapter 1)                                      
        default: 5000 (guest) => 5000 (host) (adapter 1)                                      
        default: 22 (guest) => 2222 (host) (adapter 1)                                        
    ==> default: Running 'pre-boot' VM customizations...                                      
    ==> default: Booting VM...                                                                
    ==> default: Waiting for machine to boot. This may take a few minutes...                  
        default: SSH address: 127.0.0.1:<port>                                                  
        default: SSH username: vagrant                                                        
        default: SSH auth method: private key                                                 
    ==> default: Machine booted and ready!                                                    
    ==> default: Checking for guest additions in VM...                                        
    ==> default: Mounting shared folders...                                                   
        default: /vagrant => <your Vagrant path>                   
    ==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
    ==> default: flag to force provisioning. Provisioners marked to run always will still run.

 6. After that connect to VM Machine using SSH by using this command:

```
$ vagrant ssh
```
You should see something like this: 

    $ vagrant ssh                                                    
    Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-75-generic x86_64)
                                                                     
     * Documentation:  https://help.ubuntu.com                       
     * Management:     https://landscape.canonical.com               
     * Support:        https://ubuntu.com/advantage                  
                                                                     
    6 packages can be updated.                                       
    0 updates are security updates.                                  
                                                                     
                                                                     
    The shared directory is located at /vagrant                      
    To access your shared files: cd /vagrant                         
    Last login: Sun Nov  4 13:08:04 2018 from 10.0.2.2               
    vagrant@vagrant:~$      

                                         

 7. cd to shared folder(a folder that your system and VM Machine shared) which called `/vagrant`
    using this command:

```
$ cd /vagrant
```
8. cd to project folder inside shared folder which called `/ud-Logs-Analysis` using this command:
 ```
 $ cd /ud-Logs-Analysis
```

 9. Load data from file to local database using this command:
 ```
 $ psql -d news -f newsdata.sql
```

10. Run `Logs-Analysis.py` file to start the tool using this command:
```
$ python Logs-Analysis.py
```
The result based on the current data will be like this:

    Most popular three articles of all time:-
    1- Candidate is jerk, alleges rival - 338647 Views
    2- Bears love berries, alleges bear - 253801 Views
    3- Bad things gone, say good people - 170098 Views
    
    Most popular article authors of all time:-
    1- Ursula La Multa - 507594 Views
    2- Rudolf von Treppenwitz - 423457 Views
    3- Anonymous Contributor - 170098 Views
    4- Markoff Chaney - 84557 Views
    
    Days which more than 1% of requests lead to errors:-
    July 17, 2016 - 2.26% errors 


### To stop VM Machine:

 1. If you still connected to VM Machine using ssh close connection by using this command:
 ```
$ exit
```
You should see something like this:

    vagrant@vagrant:~$ exit
    logout
    Connection to 127.0.0.1 closed.
2. then use this command to stop VM Machine:
```
$ vagrant halt
```
You should see something like this:
~~~
$ vagrant halt
==> default: Attempting graceful shutdown of VM...
~~~

### To restart VM Machine:
```
$ vagrant reload
```
