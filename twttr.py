
# word = input("What's you word?").casefold()
# # lstword = list(word)
# # for i in lstword:
# #     if lstword[i] == "a" or lstword[i] == "e" or lstword[i] == "u":
# #         lstword.replace()
# word1 = word.replace("e", "") 
# word1 = word1.replace("a", "")
# word1 = word1.replace("u", "")
# word1 = word1.replace("i", "")
# print(word1)

# def vowels():
#     inp = input("please input the text ").upper()
#     inp = [char for char in inp]

#     print(inp)
#     A = []
#     B= ["A", "E", "I", "O", "U"]

#     for i in inp:
#         for j in B:

#          if i != j:
#             print(i)
#             A.append(i)

#     print(''.join(A))


# vowels()



def vowels1():
    c = input("please input the text ").upper()
    vowels= ["A", "E", "I", "O", "U"]
    print(''.join([l for l in c if l not in vowels]));



vowels1()





#When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
# as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
#  implement a program that prompts the user for a str of text and then outputs that same text but 
# with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.