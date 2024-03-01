def a(lst, element):
    count_removed = 0
    while element in lst:
        lst.remove(element)
        count_removed += 1
    return count_removed
my_list = [1, 2, 3, 2, 4, 2,2, 5]
element = 2
removed_count = a(my_list, element)
print("لیست پس از حذف عنصر {}: {}".format(element, my_list))
print("تعداد عناصر حذف شده: {}".format(removed_count))
