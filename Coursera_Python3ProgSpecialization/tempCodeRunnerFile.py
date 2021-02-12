addition_str_lst = addition_str.split("+")
print(addition_str_lst)
print(len(addition_str_lst))

for i in range(0, len(addition_str_lst)):
    addition_str_lst[i] = int(addition_str_lst[i])
    addition_int_lst = addition_str_lst
print(addition_int_lst)
    
sum_val = 0

for item in addition_int_lst:
    sum_val = sum_val + item
    item += 1
    
print(sum_val)