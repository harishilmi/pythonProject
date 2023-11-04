import re

with open('show_version.txt') as ver_data:
    ver_output = ver_data.read()

'''compile'''

my_pattern = re.compile((r"(cisco)\.(\w+)"))
result = my_pattern.search(string=ver_output)
print(result)
print(result.group(0))
print(result.group(1))
print(result.group(2))
