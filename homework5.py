immutable_var = [1, 3], 6, 'Клоун', "Town", True
immutable_var_1 = (1, [3, 6], False, 'Клоун', "Town", True)
immutable_var_2 = tuple([[1, 3, 6], 'Клоун', False, "Town", True])
immutable_var_3 = tuple([1, 3, 6, 'Клоун', [False, "Town", True], 'war'])
print(immutable_var)
print(immutable_var_1)
print(immutable_var_2)
print(immutable_var[0])
print(immutable_var_2[0][1])
print(immutable_var_2[3])
print(immutable_var_3[4][0])

#  immutable_var[1] = 8  # ошибка кортеж не поддерживает обращение по элементам
immutable_var[0][1] = 34
print(immutable_var)
immutable_var_3[4][1] = 'Много'
print(immutable_var_3)

mutable_list = ["15", "56", "165", "Red", "sort"]
print(mutable_list)
print(mutable_list[3])
mutable_list[1] = "Coffee"
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend("new")
print(mutable_list)
mutable_list.extend(["new", 3])
print(mutable_list)
mutable_list.remove("e")
print(mutable_list)
print("popcorn" in mutable_list)
print("sort" in mutable_list)
print("popcorn" not in mutable_list)
print("sort" not in mutable_list)
print(mutable_list[0:8])
print(mutable_list[0:8:3])