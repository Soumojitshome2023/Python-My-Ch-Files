import time
capital_char= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

def fun(p,c):
    for i in capital_char:
        time.sleep(0.1)
        print(p+i)
        if (i == c):
            break;
    
text = 'HELLO SOUMOJIT'

n = 0;
while n < len(text) :
    fun(text[0:n],text[n])
    n+=1 
    