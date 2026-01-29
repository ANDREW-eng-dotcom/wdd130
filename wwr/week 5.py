from cmath import e
import csv
from datetime import datetime,timedelta
from pickle import TRUE
def load_employee_data(filename="employees.csv"):
    """
    Reads employee data from a CSV file and returns a dictionary
    the CSV should have headers:employee_Id,name,max_hours
    """
    employees={}
    try:
        with open(filename,mode='r',newline='') as file:
            reader=CSV.DictReader(file)
            for row in reader:
                emp_id=int(row['employee_id'])
                employees[emp_id]={
                    'name':row['name'],
                    'max_hours':int(row['max_hours'])
                }
            expectValueError
        print(f"error{filename} not found.")
    except ValueError or e:
                print(f"Error reading{filename}:{e}.Check data formats.")
                return employees
    def calculate_weekly_hours(employees_id,schedule):
                """
                calculates the total hours worked by a specific employees in a given schedule
                """
                total_hours = 0 
                for shift in schedule:
                    if shift['employee-id']==employees-id:
                        #Calculate duration=end_time - start_time
                        duration= shift['end_time']-shift['start_time']
                        total_hours+=duration.total_seconds()/3600
                        return total_hours
                    def validate_schedule(employees,schedule):
                        """
                        Validates the entire schedule against maximum hours and overlapping shifts.
                        Returns true if valid,false otherwise,and prints error messages.
                        """
                        
                        is_valid=TRUE
                        
                        #1.Validate max_hours for each employee
                        for emp_id,data in employees.items():
                            hours=calculate_weekly_hours(emp_id,schedule)
                            if hours>data['max_hours']:
                                print(f"validation error:{data['name']} (ID{'emp_ids'}) is 
                                scheduled for"f"{hours:2f} hours,exceeding max of 
                                      {data['max_hours']}hours")
                                is_valid=False
                            #Optional:warn about under_scheduling if needed
                            #elif hours==0:
                            #print(f"warning:{data['name']}(ID{emp_id}) has no shifts,")
                        #2.Validate no overlapping shifts
                        #For a real scheduler,this check needs to be more robust for all employees and all shifts.
                        #We can perform a simpler check:no two shifts in the list can overlap for the same person.
                        for i, shift2 in enumerate(schedule):
                            for j,shift2 in enumerate(schedule):
                                if i!=j and shift1['employee_id'] == shift2['employee_id']:
                                    #check for overlap:shift 1 starts before shift 2 ends AND shift1 ends after shift2 starts
                                    if shift1['start_time']<shift2['end_time'] and shift1['end_time']>shift2['start_time']:
                                        print(f"validation error: Overlapping shifts for employee{shift1['employee_id']}.")
                                        print(f"shift1:{shift1['start_time'].strftime('%Y-%m-%d%H:%M')} to {"shift1" ['end_time'],"strftime"('%Y-%m-%d%H:%M')}"):
                                        print(f"shift2:{shift2['end_time'].strftime('%Y-%m-%d%H:%M')} to {shift2['endtime'].strftime(%Y-%m-%d%H:%M)}")
                                        
                                        is_valid=False
                                        
                                    return is_valid
                                #...Example Usage(main function)...
                                def main():
                                    """Main execution function to demonstrate the scheduler."""
                                    print("...Running Employee shift scheduler and validator...")
                                    
                                    #1.create a dummy employees file for demonstration.
                                    with open('employees.csv',mode='w',newline='') as file:
                                        writer=csv.writer(file)
                                        writer.writerow(['employee_id','name','max_hours'])
                                        writer.writerow(['101','Andrew','40'])
                                        writer.writerow(['102','Adrine','30'])
                                        writer.writerow(['103','Charlne','20'])
                                        
                                    #2.Load employee data
                                    employees_data=load_employee_data()
                                    print("\nLoaded Employees:" Employees_data)
                                    
                                #3.Define a simple schedule(using datetime objects).
                                #This example schedule shows a valid schedule and an overlap to demonstrate validation.
                                sample_schedule=[
                                    #Andrew's shifts(Total 35 hours-valid)
                                    {'employee_id':101,'start_time':datetime(2025,11,24,9,0),'end_time':datetime(2025,11,24,17,0)},#8hours
                                    {'employee_id':101,'start_time':datetime(2025,11,25,9,0),'end_time':datetime(2025,11,25,17,0)},#8hours
                                    {'employee_id':101,'start_time':datetime(2025,11,26,9,0),'end_time':datetime(2025,11,26,18,0)},#9hours
                                    {'employee_id':101,'start_time':datetime(2025,11,28,9,0),'end_time':datetime(2025,11,28,15,0)},#6hours
                                    {'employee_id':101,'start_time':datetime(2025,11,29,9,0),'end_time':datetime(2025,11,29,13,0)},#4hours
                                    
                                    #Adrine's shifts(Total 32 hours-invalid,exceeds 30 hours max)
                                    {'employee_id':102,'start_time':datetime(2025,11,24,9,0,),'end_time':datetime(2025,11,24,17,0)},#8hours
                                    {'employee_id':102,'start_time':datetime(2025,11,25,9,0),'end_time':datetime(2025,11,25,19,0)},#10hours
                                    {'employee_id':102,'start_time':datetime(2025,11,26,9,0),'end_time':datetime(2025,11,26,19,0)},#10hours
                                    {'employee_id':102,'start_time':datetime(2025,11,27,9,0),'end_time':datetime(2025,11,27,13,0)},#4hours
                                    
                                    #Charline's shifts(Demonstrate an overlap)
                                    {'employee_id':103,'start_time':datetime(2025,11,24,8,0),'end_time':datetime(2025,11,24,12,0)},
                                    {'employee_id':103,'start_time':datetime(2025,11,24,11,0),'end_time':datetime(2025,11,24,15,0)}#overlaps from 11:00 to 12:00
                                ]
                                
                                print("\nValidating sample schedule...")
                                
                                #4.validate the schedule
                                if validate_schedule(employees_data,sample_schedule):
                                    print("\nSchedule is VALID! Ready for deployment.")
                                else:
                                    print("\nSchedule is invalid.Please review the errors above.")
                                    
                        if_name_=="_main_"
                        main()                                   