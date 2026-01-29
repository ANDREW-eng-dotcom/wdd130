Project Title:Employee Shift Scheduler and Validator
Date generated:2025-12-10(Current Date)
..............................................
1.Project Overview
..............................................
This project is a command-line utility written in python designed to mange employee work shifts defined within a standard Comma-Separated Values (CSV) file.the primary goal is to ensure data integrity by validating shift schedules for overlaps and providing an essential summary of total hours worked per employee weekly.The entire implementation uses only built-in python standard libraries.
.....................................
2. Features Implemented
.................................
the program includes three core functions as requested:
- load_employee_data(filepath):
*Reads data from a specified CSV file.
*Parses raw string dates and times int python"datetime" objects for easier manipulation.
*Handles basic error checking (File Not Found,value errors in parsing).

-'validate_no_overlap(shifts)':
*checks the loaded shifts for conflicts.
*groups shifts by employee and dare.
*ensures that for any given employee on a single day,one shift does not start before a previous shift has ended.
*prints conflict details if na overlap is found.
-'calculate_weekly_hours(shifts,start_of_week_date)':
*calculates the total duration worked by each employee within a specific 7 day per period.
*outputs a summary in hours(float format).
...............................
3.technologies used
...............
-programming Language :python 3.x
-Libraries Used:
*'csv':For reading standard CSV file formats.
*'datetime':for handling all date,time,and duration calculations('datetime','time delta','date','strp time')
*'collections':Specifically 'default dict' for efficient dat structuring(group shifts by employee/date).
................................
4.data file format:
the program expects a CSV file named 'employee_shifts.csv' in the same directory as  the script, with the following exact headers:
'EmployeeName,Date,StartTime,EndTime'
example row:'John Doe,2025-12-01,09:00,17:00'
B.how to run:
1.ensure both the python script ('shift_manger.py') and the data file('employee_shifts.csv')
2.Open a terminal or command prompt.
3.Navigate to the directory containing the files.
Run the scripts using the command:
"python shift_manager.py"
......................................
5.Limitations and future Enhancements
...........................................
Limitations:
-The current validation only checks for overlaps * within* a single calender day .multi-day(e.g.,shifts running past midnight) are not currently handled by the 'validate_no_overlap' logic as structured.
-the program assumes a perfect input format based on the specific headers.
-the target week for calculation is hardcoded in the 'main()' function.

future enhancements:
Add support for shifts that span midnight.
implement robust command-line argument parsing to specify the input  filename,or the target calculation week dynamically ,
expand validation rues (e.g., ensuring minimum break times between shifts,checking for maximum weekly hours )