triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
#print('')

#print ('* ')
#print ('* * ')
#print ('* * * ')

for number in range(triangle_height + 1):
    print((triangle_char + " ") * number)
