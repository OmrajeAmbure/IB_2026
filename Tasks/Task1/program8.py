# Age Calculations
barthyear = int(input("Enter your birth year: "))
currentyear = int(input("Enter the current year: "))
if barthyear>=1900 and barthyear<=3000:
    approximate_year = currentyear-barthyear
    print(f"Your Are {approximate_year} Year Old")
else:
    print("Enter Correct Year...!")


