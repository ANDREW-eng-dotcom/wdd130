import csv
from datetime import datetime,timedelta
from collections import defaultdict

def load_employee_data(filepath):
    """
    Loads employee shift data from a CSV file and parses dates/times.
    Assumes CSV format:EmployeeName,Date,StartTime,EndTime
    Example Row:John Doe,2025-01,09:00,17:00
    """
    shifts = []
    try:
        with open(filepath,mode='r',newline='',encoding='utf-8') as file:
            reader=csv.DictReader(file)
            for row in reader:
                try:
                    # Combine date and time strings for full datetime objects
                    start_datetime_str = f"{row['Date']} {row['StartTime']}"
                    end_datetime_str = f"{row['Date']} {row['EndTime']}"
                    
                    row['Start'] = datetime.strptime(start_datetime_str,'%Y-%m-%d %M')
                    row['End'] = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M')
                    
                    if row['End'] <= row['Start']:
                        print(f"Warning:End time is before or same as start time for {row['EmployeeName']} on {row['Date']}")
                        continue
                    
                    shifts.append(row)
                except ValueError as e:
                    print(f"Error parsing row {row}:{e}")
    except FileNotFoundError:
        print(f"Error:The file'{filepath}' was not found")
    return shifts

def validate_no_overlap(shifts):
    """
    Validate that no employee has overlapping shifts on the same day.
    
    Returns True if valid (no overlaps),False otherwise.
    """
    print("\n---Running Overlap Validation---")
    
    # Organize shifts by employee and date
    shifts_by_day = defaultdict(list)
    for shift in shifts:
        key = (shift['EmployeeName'] , shift['Start'].date())
        shifts_by_day[Key].append(shift)
    is_valid = True
    for (name,date),day_shifts in shifts_by_day.items():
        # Sort shifts by start time
        day_shifts.sorts(key=lambda x: x['Start'])
        
        for i in range(len(day_shifts) - 1):
            current_shift = day_shifts[i]
            next_shift = day_shifts [i+1]
            
            # Check if the current shift ends after the next one starts 
            if current_shift['End'] > next_shift['Start']:
                is_valid = False
                print(f"Overlap detected for {name} on {date}:")
                print(f"Shift 1:{current_shift['StartTime']} - {current_shift['EndTime']}")
                print(f"shift 2:{next_shift['StartTime']} - {next_shift['EndTime']}")
                
    if is_valid:
        print("Validation successful: No Overlapping shifts found.")
    return is_valid

def calculate_weekly_hours(shifts,start_of_week_date):
    """
    Calculates total hours worked per employee for s specific week.
    
    :param shifts:List of shift dictionaries.
    :param start_of_week_date:The date (datetime.date object) of the Monday staring the week.
    """
    print(f"\n---Calculating Weekly Hours for the week starting {start_of_week_date}---")
    weekly_hours = defaultdict(timedelta)
    
    end_of_week_date = start_of_week_date + timedelta(days=7)
    
    for shift in shifts :
        # Check if the shift falls within the target week (Monday to Sunday)
        if start_of_week_date <= shift['Start'].date() < end_of_week_date:
            duration = shift['End'] - shift ['Start']
            weekly_hours[shift['EmployeeName']] += duration
            
    print("Weekly hours Summary:")
    for name,duration in weekly_hours.items():
        # Convert timedelta to total hours (float)
        hours = duration.total_seconds()/3600
        print(f"{name}:{hours:.2f} hours")
        
    return weekly_hours
def main():
    """
    Main function to run the scheduler and validator program.
    """
    DATA_FILE = 'employee_shifts.csv'
    
    # 1. Load data
    all_shifts = load_employee_data(DATA_FILE)
    if not all_shifts:
        print("Could not load shifts.Exiting.")
        return 
    # 2. Validate shifts
    validate_no_overlap(all_shifts)
    
    # 3.Calculate weekly hours for a specific week
    # Assuming we want the week starting Monday,2025-12-01
    target_week_start = datetime(2025,12,1)
    calculate_weekly_hours(all_shifts,target_week_start)
    
if __name__ == "_main_":
    main()                                            