# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 05.09.2022 


# working with lists
new_list = ["magic", "skill", "capability", "competence", "knowledge"]
for item in new_list: 
    print(item)















#%%



"""
# playing with lists.
friends = ["Iliyas", "Kirill", "Sultan", "Nurzhan"]
print(friends[0])
print(f"Hello, dear friends: {friends[0]}, {friends[1]}, {friends[2]}, {friends[3]}")

    
print("\nAppending new elements:")
some_list = ["item1", "item2", "item3"]
some_list.append("item4")
print(some_list)

# damn, that's quite interesting!
# some_list = some_list.append("item4") doesn't work!
# while simply some_list.append("item4") works... 

# working with changing the items on the list
print("\n")
some_list[0] = "ITEMA"
print(some_list)


# inserting elements: basically like list[item_count] = new_item_name
print("\nInserting new elements:")
some_list.insert(3, "item3_new")
print(some_list)
# now it adds for the third place: item3_new
some_list[0], some_list[-2], some_list[-1] = "item1", "item4", "item5" 
for i in some_list: 
    print(i)


# popping is opposite to appending. 
print(f"\nOld List: {some_list}")
some_list.pop()
print(f"Updated List with Pop: {some_list}")

#not only popping taking the value from the list but also can assign. 
print("\nnot only popping taking the value from the list but also can assign".title())
print(f"Current list: {some_list}")
emitted_value = some_list.pop(-1)
print(f"Updated List without the last item: {some_list}")
print(f"Emitted value: {emitted_value}")


# removing items only with certain value name
print("\nremoving items only with cetrain value name".title())
print(f"Our current list: {some_list}")
removed_item = some_list.remove("item1")
print(f"Updated list without the removed item {removed_item}")
print(f"Remaining items on the list: {some_list}")

# sorting lists
print("\nsorting lists using .sort()".title())
int_list = [3, 5, 2, 4, 1]
int_list.sort()
print(int_list)

#sorting temporarily
print("\nsorting temporarily using sorted()".title())
int_list = [3, 5, 2, 4, 1]
print(f"{int_list}")
print(sorted(int_list))

#finding the length of the list
print("\nfinding the length of the list".title())
print(f"The length of the 'int_list' is {len(int_list)}")
"""




#%% 

"""
print("Languages: \n\tPython, \n\tC++, \n\tJS")

text = "people "
print(text)
text = text.rstrip()
print(text)
"""



#%%
# some last code
"""
a = "hello, world!"
print(a.title())
print(a.upper())
print(a.lower())

first_name="alisher"
last_name="temirlanov"
full_name=f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")
"""


