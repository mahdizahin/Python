#update

tpl=(1,2,3,4,5)

lst = list(tpl) #converting in list
lst.append(6)

tpl2=tuple(lst)
print(type(tpl2),tpl2)