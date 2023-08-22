a = input("Enter Number:> ")

try:
    a = int(a)
    if a >= 18:
        print("ok")
    else:
        print("No")

except Exception as e:
    print(f"Your input resulted in an error: {e}")
