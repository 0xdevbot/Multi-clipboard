import pyperclip, sys, shelve

SAVE_FILE = shelve.open('MULTI_SAVE')

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('IndexError: IndexError: EXPECTED AT LEAST 1/2 ARG RECEIVED ' + str(len(sys.argv) - 1)+'\n\n')
    print('''USAGE: Python multi [Action] [var]
            use -h for help
                    ''')
    sys.exit(0)

if sys.argv[1] == '-s':
    SAVE_FILE[str(sys.argv[2])] = pyperclip.paste()
elif sys.argv[1] == '-d':
    try:
        del SAVE_FILE[str(sys.argv[2])]
    except KeyError:
        print('KeyError: KEY NOT FOUND\n\n')
        print('''USAGE: Python multi [Action] [var]
                use -h for help
                        ''')
elif sys.argv[1] == '-clear':
    SAVE_FILE.clear()
    sys.exit(0)
elif sys.argv[1] == '-c':
    try:
        pyperclip.copy(SAVE_FILE[str(sys.argv[2])])
    except KeyError:
        print('KeyError: KEY NOT FOUND\n\n')
        print('''USAGE: Python multi [Action] [var]
        use -h for help
                ''')
elif sys.argv[1] == '-p':
    try:
        print(str(SAVE_FILE[str(sys.argv[2])]))
    except KeyError:
        print('KeyError: KEY NOT FOUND\n\n')
        print('''USAGE: Python multi [Action] [var]
                use -h for help
                        ''')
elif sys.argv[1] == '-P':
    print(str(SAVE_FILE))
elif sys.argv[1] == '-k':
    print(SAVE_FILE.keys())
elif sys.argv[1] == '-h':
    print('''USAGE: Python multi [Action] [var]
            Action:
             -s     [VAR]       saves whatever is currently in on your clipboard to the VAR
             -d     [VAR]       del anything stored to VAR
             -clear [n/a]       del entire db file
             -c     [VAR]       copies anything stored under VAR in DB file
             -p     [VAR]       prints anything saved to VAR
             -P     [n/a]       prints entire db file
             -k     [n/a]       prints all the available VAR

            VAR                 var to store clipboard data under

            ERRORS:
            KeyError            KeyError: KEY NOT FOUND
                                VAR input not saved to db file, could be caused if you try to recall a VAR that was -d or
                                if the db file was del (at which point all VAR would be -d)

            IndexError          IndexError: EXPECTED AT LEAST 1/2 ARG RECEIVED X
            ''')
else:
    print('UnknownArg\n\n')
    print('''USAGE: Python multi [Action] [var]
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
            ''')

SAVE_FILE.close()
sys.exit(0)

