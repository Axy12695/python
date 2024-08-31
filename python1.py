def find_max_and_min(arr):
    if not arr:
        return None, None

    maxe = mine = arr[0]
    for val in arr[1:]:
        if val > maxe:
            maxe = val
        elif val < mine:
            mine = val

    return maxe, mine


# 示例使用
arr = list(input("请输入数组：").split())
maxe, mine = find_max_and_min(arr)
print(f"Max element is {maxe}, Min element is {mine}")