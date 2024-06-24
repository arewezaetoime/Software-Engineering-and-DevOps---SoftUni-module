def unique(n):
    copy_arr = n.copy()

    for i in range(0, len(n) + 1):
        if i + 1 == len(n):
            break

        if n[i] != n[i + 1]:
            continue
        else:
            copy_arr.pop(n[i])

        return copy_arr
    