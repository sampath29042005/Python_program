#write a program take inputs from the user and print the area,perimeter of rectangle,square,triangle,circle
#%%
# 1. Rectangle
print("--- Rectangle ---")
length = int(input("length of the rectangle: "))
width = int(input("width of the rectangle: "))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print(rect_area)  
print(rect_perimeter)
#%%
# 2. Square
print("--- Square ---")
side = int(input("side length of the square: "))
sq_area = side**2
sq_perimeter = 4 * side
print(sq_area)
print(sq_perimeter)
#%%
# 3. Triangle (using 3 sides and Heron's formula)
print("--- Triangle ---")
a = int(input("first side of the triangle: "))
b = int(input("second side of the triangle: "))
c = int(input("third side of the triangle: "))
 
#%%
# 4. Circle
print("--- Circle ---")
radius = float(input("the radius of the circle: "))
circle_area = 3.14 * (radius**2)
circle_circumference = 2 * 3.14 * radius
print(circle_area)
print(circle_circumference)

#%%
# shopping bill calculations

pen_price = 10
q1 = 5

book_price = 50
q2 = 3

file_price = 20
q3 = 5

bill = ((pen_price+q1)+(book_price+q2)+(file_price+q3)) 
print(bill)

#%%
# atm
ac_blance= float(input())
withdraw_amount= float(input())
av_blance = ac_blance - withdraw_amount
print(av_blance)


#%%
# student marks avg
sub1 = int(input("sub 1: "))
sub2 = int(input("sub 2: "))
sub3 = int(input("sub 3: "))
sub4 = int(input("sub 4: "))
sub5 = int(input("sub 5: "))

avg_marks = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print(avg_marks)

#%%
#salary
basic_salary = float(input("basic salary: "))
bonus = float(input("bonus amount: "))

final_salary = basic_salary + bonus
print(final_salary)

#%%
distance = float(input("distance (in km): "))
mileage = float(input("mileage (km per liter): "))
fuel_price = float(input("fuel price per liter: "))

total_fuel_cost = (distance / mileage) * fuel_price
print(total_fuel_cost)

#%%
# Chocolate Distribution
total_chocolates = int(input("Enter the total number of chocolates: "))
total_students = int(input("Enter the total number of students: "))

chocolates_per_student = total_chocolates // total_students
remaining_chocolates = total_chocolates % total_students

print(chocolates_per_student)
print(remaining_chocolates)

#%%
#Restaurant Bill Splitting
total_bill = float(input("total restaurant bill: "))
number_of_friends = int(input("number of friends: "))

amount_per_friend = total_bill / number_of_friends
print(amount_per_friend)

#%%
#Electricity Bill
units_consumed = float(input("units consumed: "))
price_per_unit = float(input("price per unit: "))

electricity_bill = units_consumed * price_per_unit
print(electricity_bill)

#%%
#Discount Calculation
original_price = float(input("original price: "))
discount_percentage = float(input("discount percentage: "))

discount_amount = (original_price * discount_percentage) / 100
final_price = original_price - discount_amount

print(final_price)

#%%
#Time Conversion
total_seconds = int(input("number of seconds: "))

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"{minutes} min  {remaining_seconds} sec ")

#%%
#Monthly Savings
monthly_salary = float(input("monthly salary: "))
monthly_expenses = float(input("monthly expenses: "))

monthly_savings = monthly_salary - monthly_expenses
print(monthly_savings)

#%%
# 
#%%