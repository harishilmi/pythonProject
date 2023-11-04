import re

with open('show_version.txt') as ver_data:
    ver_output = ver_data.read()


my_pattern = r"Version.+\d"
re_output = re.search(pattern=my_pattern, string=ver_output)
print(re_output)
print(re_output.group(0))

print('*' * 30)
version_output = re_output.group(0)

print(f"{'IOS Version'.ljust(18)}: {version_output}")