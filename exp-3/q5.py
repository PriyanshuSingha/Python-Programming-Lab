sub1 = int(input("enter the marks:"))
sub2 = int(input("enter the marks:")) 
sub3 = int(input("enter the marks:"))
sub4 = int(input("enter the marks:"))
sub5 = int(input("enter the marks:"))

percentage = (sub1+sub2+sub3+sub4+sub5/250)*100
if percentage >= 90 and <= 100 :
    print("The grade is O")
elif percentage >= 80 and <=90 :
    print("the grade is E")    
elif percentage >= 70 and <=80 :
    print("the grade is E")
elif percentage >= 60 and <=70 :
    print("the grade is E")
elif percentage >= 50 and <=60 :
    print("the grade is E")
else:
    print("the grade is F")
                                    