# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019357    
  
# Date: 28/11/2020

#References
#W3schools.com. 2020. Python For Loops. [online] Available at: <https://www.w3schools.com/python/python_for_loops.asp#:~:text=A%20for%20loop%20is%20used,other%20object%2Dorientated%20programming%20languages.> [Accessed  23 November 2020].


B=[0,20,40,60,80,100,120]
print(B,"Only use the numbers inside the list")
# Creating variables to add the total number of outputs entered by the user as numbers.
a=0
b=0
d=0
e=0
while True:
    try:
        credit_pass=int(input("Please enter your credits at pass :"))
        if credit_pass not in B:
            print("Out of range")
            continue
        credit_defer=int(input("Please enter your credits at defer :"))
        if credit_defer not in B:
            print("Out of range")
            continue
        credit_fail=int(input("Please enter your credits at fail :"))
        if credit_fail not in B:
            print("Out of range")
            continue
        total=credit_pass+credit_defer+credit_fail
        if total !=120:
            print("Total incorrect")
            continue
        if credit_pass==120:
            print("Progress")
            a=a+1   # Since the variable starts with 0 when the user enters a progress value it adds automatically the histogram.       
            print("______________________________________________________")
            print("______________________________________________________")
        elif credit_pass==100:
            print("Progress (module trailer)")
            b=b+1
            print("______________________________________________________")
            print("______________________________________________________")
        elif credit_fail<=60 :
            print("Do not Progress – module retriever")
            d=d+1
            print("______________________________________________________")
            print("______________________________________________________")
        elif credit_fail>=80:
            print("Exclude")
            e=e+1
            print("______________________________________________________")
            print("______________________________________________________")
        c=input("Would you like to enter another data y/q:")                   # Asking the user enter further more records or not
        print("_________________________________________________")
        if c=="y":                                                                                  #If yes the user will have to type the credit pass, defer and fail results again to record.
            continue
        else:
            if c=="q":                                                                              # If no the user will be give a table of a histogram displaying how many outputs have come in numbers and stars.
                print("______________________________________________________")
                print("______________________________________________________")
                print("Horizontal Histogram")
                print("Progress",a," :",end=' ')  # Making the stars to print horizontally by using end='' and the progress output in one line.
                for i in range(a):
                    print("*",end='')
                print("\nTrailer",b,"     :",end=' ')
                for i in range(b):
                    print("*",end='')
                print("\nRetriever",d,":",end=' ')
                for i in range(d):
                    print("*",end='')
                print("\nExcluded",e,":",end=' ')
                for i in range(e):
                    print("*",end='')
                add=a+b+d+e                             # Making add variable in order to show the user how many inputs have they entered as in numbers.

                print()
                print(add,"outcomes in total.")
                print("______________________________________________________")
                print("______________________________________________________")
            break
    except ValueError:                 # After the code reads the inside the try if the user enters any other characters other than numbers the output will be enter the integer.
        print("please enter a integer") 


       
        

