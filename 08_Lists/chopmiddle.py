def chop(some_list):
    some_list.pop()
    del some_list[0]
    return None

def middle(some_list):
    # Less efficient way until I noticed I could just use the previous function:
    # new_list = list()
    # for i in range(len(some_list)):
    #     if i == 0 or i == range(len(some_list)):
    #         continue
    #     newlist.append(some_list[i])
    chop(some_list)
    return some_list

example = ["Lentejas", "Hamburguesas", "Albaricoques", "Broccoli"]

print(example)
print(middle(example))