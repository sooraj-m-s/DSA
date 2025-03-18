def binary_search(li, target):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == target:
            return True
        elif li[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def linear_search(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return True
    return False


li = [1, 2, 3, 4, 7, 9]
target = 7

if binary_search(li, target):
    print(f'Value {target} is found in the array.')
else:
    print(f'Value not in the array')


if linear_search(li, target):
    print(f'Value {target} is found in the array.')
else:
    print(f'Value not in the array')
