# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019357    
  
# Date: 28/11/2020

#References

#loops?, h. and Bem, M., 2020. How Do I Make "*" Print Vertically On Python Loops?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops?answertab=votes#comment93456895_53285993> [Accessed 23 November 2020].



B=[0,20,40,60,80,100,120]
top=["Progress:","Trailer:", "Retriver:",  "Excluded"]   # The list is created in order to make words stay in same line so the ouput can be printed vertically.
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
            a=a+1 # Since the variable starts with 0 when the user enters a progress value it adds automatically the histogram.
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
        c=input("Would you like to enter another data y/q:")                        # Asking the user enter further more records or not.
        print("_________________________________________________")
        if c=="y":                                                                                              # If yes the user will have to type the credit pass, defer and fail results again to record.
            continue
        else:
            if c=="q":                                                                                          # If no the user will be give a table of a histogram displaying how many outputs have come in numbers and stars.
                print("______________________________________________________")
                print("______________________________________________________")
                print("Vertical Histogram")
                top=["|Progress|"+str(a),"|Trailer|"+str(b), "|Retriver|"+str(d),  "|Excluded|"+str(e)]   # The list is created in order to make words stay in same line so the ouput can be printed vertically and the integer is being converted to string in order to join the variables with the list.
                print('  '.join(top))                                                                     # Joining the attribute at the top will remove the brackets and the inverted commas will make the histogram even more better.
                for i in range(max(a, b, d, e)):# Setting a range to add progress,trailer,retriever and exclude to enter the total outputs and stars to the user in a vertical method.
                    print("        {0}               {1}                 {2}                   {3}". format(    # This is being used because the number 0 to 3 represents to count the a,b,d,e one by one and in the order of the top and the alingment as well.
                        "*" if i < a else " ",
                        "*" if i < b else " ",
                        "*" if i < d else " ",
                        "*" if i < e else " ",
                        ))                        
                add=a+b+d+e                                                                         # Making add variable in order to show the user how many inputs have they entered as in numbers.
                print("\n")
                print(add,"outcomes in total.")
                print("______________________________________________________")
                print("______________________________________________________")
            break
    except ValueError:                    # After the code reads the inside the try if the user enters any other characters other than numbers the output will be enter the integer.
        print("please enter a integer")
