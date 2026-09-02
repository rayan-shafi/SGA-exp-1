Percentage = float(input("Input your Percentage: "))

if Percentage >= 90.00:
    print("Remarks- Excellent")

elif 75.00 <= Percentage <= 89.99:
    print("Remarks- Very Good")

elif 60.00 <= Percentage <= 74.99:
    print("Remarks- Good")

elif 40.00 <= Percentage <= 59.99:
    print("Remarks- Average")

elif Percentage <= 39.99:
    print("Remarks- Fail")