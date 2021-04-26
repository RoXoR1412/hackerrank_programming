from collections import OrderedDict
item_dict=OrderedDict()
for _ in range(int(input())):
    item,space,quantity=input().rpartition(' ')
    item_dict[item]=item_dict.get(item,0)+int(quantity)
for item,quantity in item_dict.items():
    print(item,quantity)
