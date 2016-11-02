input_string = "first_line   "
unicode_string = u'unicode_string'
raw_string = r'S:\nfdfd/fdfd/'
splitted_string = input_string.split('.')

print("Raw string" + raw_string)
print(splitted_string)

print('Formatted string {0} {1}'.format('first_str', 'second_str'))
print(str.format('Another format variant {} {} {}'.format('first', 'second', 'third')))


print(input_string.capitalize())
print(input_string.encode('utf-8').decode('utf-8'))

print(input_string.index('i'))
print(input_string.isdigit())
print(input_string.rstrip())
print(input_string.replace('i', 'W'))
