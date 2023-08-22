s = {1, 2, 5, 1, 3, 9, 6, 15, 16, 17, 55, 22, 5, 9, 6}

print(s)        #Output:> {1, 2, 3, 5, 6, 9, 15, 16, 17, 22, 55}


s.discard(10)
print(s)        #Output:> {1, 2, 3, 5, 6, 9, 15, 16, 17, 22, 55}
s.remove(10)
print(s)        #Output:> Error 

# J ta set ar modhe nei seta remove korte chaile error asbe, but 
# J ta set ar modhe nei seta discard korte chaile error asbe naaaaa..

