marks=int(input("Enter your marks (0-100)"))

if marks >= 90:
    grade= "A"
elif marks >=75 and marks < 90: # 'and' ensures both conditions are true
    grade= "B"
elif marks >=50 and marks < 75:
    grade= "C"
elif marks <50 and marks >=0: 
    grade= "F"
else:
    print("invalid input")
 #when you want to use = as a logical operator (in conditions, not in assignment) then use double == .Single = is only for assigning values.
print("Your grade is:", grade)    

# != means not equal to