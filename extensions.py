x = input("What is the filename ").casefold()
if x.endswith(".gif"):
    print(".gif")
elif x.endswith(".jpg"):
    print(".jpg")
elif x.endswith(".jpeg"):
    print(".jpeg")
else:
    print("application/octet-stream")








# def FileSavings():

#         x = input("what file extension ")

#         x = x.casefold()

#         if x == ".gif" or x == ".jpg" or x == ".jpeg" or x == ".png" or x == ".pdf" or x==".txt" or x == ".zip":

#             x= x.replace(".", "")

#             print("image/" + x)

#         else: print("application/octet-stream")



# FileSavings()













# <!-- In a file called extensions.py, implement a program that prompts the user for the name
#  of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, 
# in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, 
# output application/octet-stream instead, which is a common default. -->






