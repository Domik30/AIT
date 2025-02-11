
l4 = [4, 15, 8, 12]

# # l2 = list(map(lambda a:a*a, l))

# # print(l2)

# # x = lambda a: a*a-9

# # x(6)
# # print(x(6))


# # l = [5, 4, 9, 7, 6]

# # l2 = list(map(lambda str(a) + "Kč", l))

# # print(l2)


# l3 = filter(lambda a : a<10, l)


l4 = list(map(lambda a: str(a) + 'Kc', filter(lambda a:a<10, l4)))
print(list(l4)) 