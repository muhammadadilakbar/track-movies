"""
This script uses Google Sheets API to fetch a spreadsheet.
It fetches the movie bluray release date and parses it using Python datetime module.
If parsed date matches today, it sends a notification to email address.
Assumptions: The machine has mail server like Postfix set up.
Tested on: Ubuntu 20.04, Python 3.8.10
"""

import ezsheets, os
from datetime import datetime, date
from mysql_connect import NOTIFY_EMAIL, SPREADSHEET

spreadSheet = ezsheets.Spreadsheet( SPREADSHEET )

sheet1 = spreadSheet.sheets[0]
rows = sheet1.getRows()
i = 1 # 0 is header row
go = True
while go:
    movieName = rows[i][0]
    if movieName == '':
        go = False
    else:
        estimatedBlurayReleaseDate = datetime.strptime( rows[i][1], "%m/%d/%Y" ).date()
        today = date.today()
        if estimatedBlurayReleaseDate == today:
            emailBody = rows[i][0] + " Bluray is out"
            commandLine = 'echo "' + emailBody + '" | mail -s "Blueray is out" "' + NOTIFY_EMAIL + '"'
            print( "Now sending email" )
            os.system( commandLine )
        i = i + 1