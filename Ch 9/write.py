with open("khetu.txt", "w") as f:
    f.write(" How are you? ")

print("Done ")


with open("khetu.txt", "a") as f:   #append mode
    f.write(" Hello ")

print("Done ")