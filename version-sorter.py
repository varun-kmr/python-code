def f(list):
    #  split each element into a list of ints. Then use it as key to sort
    list.sort(key=lambda version: [int(temp) for temp in version.split('.')], reverse=True)
    return list


version_list = ["3.9.5", "4.3.11", "8.1.2", "4.3.6", "4.5.6"]
sorted_result = f(version_list)
print(sorted_result)
