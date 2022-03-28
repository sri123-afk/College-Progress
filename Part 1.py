# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019357    
  
# Date: 28/11/2020

#References
#W3schools.com. 2020. Python Conditions. [online] Available at: <https://www.w3schools.com/python/python_conditions.asp> [Accessed  23 November 2020].



credit_pass=int(input("Please enter your credits at pass :")) #Asking the user to enter a integer value to calculate the total result.
credit_defer=int(input("Please enter your credits at defer :"))
credit_fail=int(input("Please enter your credits at fail :"))
if credit_pass==120:   # If the credit is equal to 120 the user will get a output of progress and break the program.
    print("Progress")
    print("______________________________________________________")
    print("______________________________________________________")

elif credit_pass==100:  # If the credit is equal to 100 the user will get a ouput of module trailer even if the user enters 20 for credit_defer or credit_fail.
    print("Progress (module trailer)")
    print("______________________________________________________")
    print("______________________________________________________")
           
elif credit_fail<=60 :     # If the credit is less than equal to 60 the output will be module retriever even if the user enters 60 as defer too.
    print("Do not Progress – module retriever")
    print("______________________________________________________")
    print("______________________________________________________")
          
elif credit_fail>=80:    # If the credit is more than equal to 80 the ouput will be exclude even if the user enters 100 also.
    print("Exclude")
    print("______________________________________________________")
    print("______________________________________________________")
            

      
