# rpi_irrigation_system
Irrigation system project implemented using a raspberry pi zero w

This is meant to be run using a crontab owned by root. 

- the bash script contains an execution command to run the python program "irrigator.py"
- the bash script is set as executable by anyone (chmod 777)
- bash script was included in root's crontab to run every sunday at 6PM 
