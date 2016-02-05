# PythonEmailScript

Pulls .edu email addresses from text files placed in the 'place_input_files_here' directory and inserts them into a mysql database, table, and column specified at runtime. Created for use with Eta Kappa Nu Honor Society.

# Usage Instructions
1. You will need to download and install MySQL Connector for Python, which can be found here:
    https://dev.mysql.com/downloads/connector/python/. It will ask you to create an account if you do not already have one, but the account is free.

2. If you have a mac, or already have python installed, you can proceed to step 3. Otherwise, you will need to download and install python from here: https://www.python.org/downloads/. I'm using version 2.7.10.
    
3. Clone this repository to the desired directory. Run (in terminal)
    ```bash
    git clone https://github.com/gdscheele/PythonEmailScript.git
    ```
  
4. Run (in terminal)
      ```bash
      cd PythonEmailScript
      ```
5. Place text files containing emails into the 'place_input_files_here' directory.
6. Run (in terminal)
    
    ```bash
    python main.py
    ```
7. Follow the instructions given in the program. You will need to provide all the database information at runtime.
