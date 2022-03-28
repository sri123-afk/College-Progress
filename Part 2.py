# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019357    
  
# Date: 28/11/2020

#References

#Programiz.com. 2020. Python List (With Examples). [online] Available at: <https://www.programiz.com/python-programming/list> [Accessed 23 November 2020].
#W3schools.com. 2020. Python Try Except. [online] Available at: <https://www.w3schools.com/python/python_try_except.asp> [Accessed 23 November 2020].
#Python, R., 2020. Python "While" Loops (Indefinite Iteration) – Real Python. [online] Realpython.com. Available at: <https://realpython.com/python-while-loop/> [Accessed 23 November 2020].

# Created a list to make the user enter in values only in the list.
B=[0,20,40,60,80,100,120]
print(B,"Only use the numbers inside the list")
while True: # Creating a while loop to make the program run multiple times until the user enters the correct output.
    try:
        credit_pass=int(input("Please enter your credits at pass :")) # Asking the user to input the credits for pass, fail and defer.
        if credit_pass not in B: # Making the user enter the values only on the list and out of the list will be given as out of range.
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
        total=credit_pass+credit_defer+credit_fail # Adding all the pass, defer and fail numbers.
        if total !=120: # After adding the total if the total is not equal to 120 the output will be total incorrect like 121 or more than that will give the user total incorrect.
            print("Total incorrect")
            continue
        if credit_pass==120: # If the credit is equal to 120 the user will get a output of progress and break the program.
            print("Progress")
            print("______________________________________________________")
            print("______________________________________________________")
            break
        if credit_pass==100: # If the credit is equal to 100 the user will get a ouput of module trailer even if the user enters 20 for credit_defer or credit_fail.
            print("Progress (module trailer)")
            print("______________________________________________________")
            print("______________________________________________________")
            break
        if credit_fail<=60 : # If the credit is less than equal to 60 the output will be module retriever even if the user enters 60 as defer too.
            print("Do not Progress – module retriever")
            print("______________________________________________________")
            print("______________________________________________________")
            break
        if credit_fail>=80: # If the credit is more than equal to 80 the ouput will be exclude even if the user enters 100 also.
            print("Exclude")
            print("______________________________________________________")
            print("______________________________________________________")
            break
    except ValueError: # After the code reads the inside the try if the user enters any other characters other than numbers the output will be enter the integer.
        print("please enter a integer")
        
        


