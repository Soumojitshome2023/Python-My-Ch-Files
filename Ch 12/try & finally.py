# Without Exit
try:
    i = int(input("Enter a number: "))
    c = 2*i 

except Exception as e:
    print(e)
                                          # Important Line

finally:                                  #____________(1)
    print("We are done")

print("Thanks for using the program")     #____________(2)
                                          # Programe exit na hole __(1)&__(2) same,2jon e kaj korbe e. 
                                    
print("_______________________________________________________________________________")
# With Exit 
try:
    i = int(input("Enter a number: "))
    c = 2*i 

except Exception as e:
    print(e)
    exit()                                # Important Line

finally:                                  # program exit hok, ba na hok, finally kaj korbe eee.
    print("We are done")

print("Thanks for using the program")     # programe exit hoa gele a ta  kaj korbe naaaa.. 
                                          # programe exit na hole a ta kaj korbe..

# finally mean:> Jai hok finally: run hobe eee.