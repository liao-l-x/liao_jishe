from django.test import TestCase

# Create your tests here.
hierarchy_list = {
    (1, "畜牧中心"),
    (2, "畜牧公司"),
    (3, "养殖场"),
    (4, "畜舍")
}
for i in hierarchy_list:
    print(i)
print(type(hierarchy_list),hierarchy_list.get(2))