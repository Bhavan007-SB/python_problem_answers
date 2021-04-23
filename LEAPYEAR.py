Year = int(input())   #get year from user

if(((Year % 400 == 0) or
    (Year % 100 !=0)) and    #Formula to find leap year
    (Year % 4 == 0)):
  print("{Year} is a Leap Year ".format)
else:
  print("{Year} is not a Leap Year".format)   #format do variable subsitutions
   

