:: This command will cd into the correct folder, activate your virtual environment,
:: set the correct commands for Flask and run it. 

:: Make sure to set location to location of repo before running
:: Also make sure that the virtual enviroment and all libraries are installed before running

cmd /k "cd C:\Users\jacob\Desktop\Twitter-Stat-Tracker\ && env\Scripts\activate.bat && set FLASK_APP=run.py && set FLASK_DEBUG=1 && py -m flask run"
