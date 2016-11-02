input_string = "input"
output_string = "output"
final_string = input_string + output_string

multiplied_output_string = output_string * 3

print(final_string)
print(multiplied_output_string)


print(id(input_string))
print(id(output_string))
print(id(final_string))

print('\nIndex Operations')
print(final_string[0])
print(final_string[-1])
print(final_string[-2])

print('\nList Operations(slices)')
print(final_string[0::])
print(final_string[::])
print(final_string[1::])
print(final_string[1:-1])
print(final_string[::-1])
print(final_string[::2])
print(final_string[slice(None, None, 2)])
print(len(final_string))
