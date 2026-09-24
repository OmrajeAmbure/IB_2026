print("--------------------------Elactricity Bill Calculations---------------------------")
print("Enter the Elactricity Bill Unit : ")
inp = int(input())
bill = 0
if inp > 0 and inp<=100:
    bill = inp*5;
elif inp > 100 and inp<=200:
    bill = inp*7;
elif inp > 200 and inp<=300:
    bill = inp*10;
elif inp>300:
    bill = inp*15;
else:
    print("Enter Valid Unit's")
    
print(f"Your Unit is {inp} \nTotal Bill is {bill}")
