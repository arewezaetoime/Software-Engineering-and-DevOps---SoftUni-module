
# def next_character(chars):
#     output = []
#     for char in chars:
#         print (char)

# next_character('abc')

n = [1, 1 , 2, 3, 3, 5]
# print(len(n.copy()))
# print(n.copy())
print(len(n))

def unique_elements(n):
    copy_arr = n.copy()
    
    for i in range(0, len(n) + 1):
        if i + 1 == len(n):
            break

        if n[i] != n[i+1]:
            continue
        else:
            copy_arr.pop(n[i])

    return copy_arr
    
print(unique_elements(n))

    
print(unique_elements(n))