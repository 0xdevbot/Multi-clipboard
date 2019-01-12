# Multi-clipboard

<see usage below>
  
This script will allow you to use the terminal to maintain multiple things on the clipboard, the db file will be saved wherever you save the script, this can be chaged if you change line 3 of the file from:


SAVE_FILE = shelve.open('MULTI_SAVE') -> SAVE_FILE = shelve.open('PATH_TO_FOLDER/MULTI_SAVE')




```
USAGE: Python multi [Action] [var]
            Action:
             -s     [VAR]       saves whatever is currently in on your clipboard to the VAR
             -d     [VAR]       del anything stored to VAR
             -clear [n/a]       del entire db file
             -c     [VAR]       copies anything stored under VAR in DB file
             -p     [VAR]       prints anything saved to VAR
             -P     [n/a]       prints entire db file
             -k     [n/a]       prints all available VAR

            VAR                 var to store clipboard data under

            ERRORS:
            KeyError            KeyError: KEY NOT FOUND
                                VAR input not saved to db file, could be caused if you try to recall a VAR that was -d or
                                if the db file was del (at which point all VAR would be -d)

            IndexError          IndexError: EXPECTED AT LEAST 1/2 ARG RECEIVED X
