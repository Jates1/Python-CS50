# name = input("camelcase:")
# length = len(name)
# lst_strng = list(name)
# for i in range (length):
#     if lst_strng[i].isupper():
#         lst_strng[i] = "_"
#     else:
#         lst_strng[i] = lst_strng[i].lower()
# lst_strng = "".join(lst_strng)
# print("Snakecase:", lst_strng)


def camel():
    inp = input("please input variable name in camerl case ")
    #inp = [char for char in inp]
    inp = list(inp)
    print(inp)
    A = []
    for i in inp:
        if i.isupper():
            A.append('_')
            A.append(i.lower())
        else:
            A.append(i)

    print(''.join(A))
camel()