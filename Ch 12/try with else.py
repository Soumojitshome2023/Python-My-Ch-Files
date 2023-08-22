try:
    i = int(input("Enter a number: "))
    c = 2*i

except Exception as e:
    print(e)

else:                             # try: complete hole else: kaj korbe, nahole korbe na.
    print("We were successful")