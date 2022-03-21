import datetime
import AgeFinding
def Current_Date():
    
    Current_Date = datetime.date.today()
    split_Current_date = str(Current_Date)
    split_Current_date = split_Current_date.split('-')
    
    return split_Current_date

def BirthDate():
    print("Enter Your Birth Date in 'YYYY-MM-DD' this formate.")
    birthdate = input()
    
    split_birthdate = birthdate.split('-')
    
    return split_birthdate

def Calculation():
    
    split_Current_date = Current_Date()
    split_birthdate = BirthDate()
    
    current_year = int(split_Current_date[0])
    birth_year = int(split_birthdate[0])
    
    Age = current_year - birth_year         #Age Find
    

    current_month = int(split_Current_date[1])
    birth_month = int(split_birthdate[1])
    remaining_month = current_month - birth_month   
    
    
    current_days = int(split_Current_date[2])
    birth_days = int(split_birthdate[2])
    remaining_days = current_days - birth_days  
    temp_Week = remaining_days/7

    Months = (Age * 12) + remaining_month   #month find
    
    
    remaining_week = remaining_month * 4.34524
    Weeks = (Age * 52.18) + remaining_week + temp_Week  #week Find


    days = Weeks * 7    #days Find
    
    AgeFinding.Display(Age,Months,Weeks,days)      #Calling to display function.
