def return_10():
    return 10

def add(num1 , num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
     return string1 + string2

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)

def number_to_full_month_name(month):
    months = ["January" , "Febuarary", "March", "April","May", "June", "July","August","September","October","November","December"]
    return months[month -1]

def number_to_short_month_name(month):
    months = ["Jan","Feb", "Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    return months[month -1]