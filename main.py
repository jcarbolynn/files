# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("file.txt") as file:
#   contents = file.read()
#   print(contents)

# error without adding mode = "w" bc by default python opens files as read only
# with open("file.txt", mode="w") as file:
#   file.write("\nHoooray!")

# # mode = "a" to append instead of overwrite
# with open("file.txt", mode="a") as file:
#   file.write("\nI like noodles")

# # if writing to a file that doesnt exist you will create one
# with open("new_file.txt", mode="a") as file:
#   file.write("New text.")

# with open("new_file_modew.txt", mode="w") as file:
#   file.write("New text again.")





# with open("data.txt", mode="w") as data:
#    data.write(str(0))

test_var = ""
with open("data.txt",mode="r") as data:
  test_var = data.read()

print(test_var)
print(type(test_var))
