year = int(input("Enter Year : "))
leapyear = False
if year%4 == 0 and (year%100 != 0 or  year%400 == 0):
   print("Leap Year")
else:
    print("Normal")
