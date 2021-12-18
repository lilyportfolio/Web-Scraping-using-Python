========================================================================
README
========================================================================


SETUP


The application has drivers included for the source code to run. However, if you face any issues due to incompatibility of the driver with your OS, please follow the below steps.


Install geckodriver and chromedriver from the following locations


Geckodriver: https://github.com/mozilla/geckodriver/releases


Chromedriver: https://chromedriver.chromium.org/downloads


Settings
Change the path in setup_driver.py to match the chromedriver path on your PC as 
follows -


driver_path = <driver_path>


Install modules -
selenium - to scrape live webpage
PySimpleGUI - to be able to use GUI
slatek3 - to parse resume
bs4 - parse website
json - parse website
selenium - parse website
itertools




Please run the main.py


**********************************************************************************************
Input I:         User Resume in .pdf format
Input II:        Desired role from the dropdown list
Output:         List of courses missing from the user’s resume to be acquired by the user 
                       in order to get the desired role 
***********************************************************************************************