random_file = open("GRY", "r")

for info in random_file.readlines():
    print(info)
random_file.close()

random_file = open("GRY","a")
random_file.write("\nI have a pencil.")
random_file.close()

random_file1 = open("GRY1","w")