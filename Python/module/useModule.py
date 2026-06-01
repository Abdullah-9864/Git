# # import module as md
# # print(md.person["name"])

# # import platform
# # print(platform.system())
# # print(dir(platform))


# from importlib.resources import path
# import os

# from sklearn import base


# f = open("demofile.txt", "r")
# print(f.read())
# f.close()

# f = open("demofile.txt", "w")
# f.write("This is new content")
# f.close()





# f = open("demofile.txt", "a")
# f.write("\nThis line is appended")
# f.close()

# f = open("demofile.txt", "r")
# print(f.read())
# f.close()



f = open("newfile.txt", "x")
f.write("Brand new file!")
f.close()


f = open("newfile.txt", "r")
print(f.read())
f.close()
