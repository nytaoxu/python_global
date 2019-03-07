letters = ['a', 'b', 'c']

# add
letters.append('x')
letters.insert(0, 'y')
letters.insert(17, 'z')

# remove
letters.pop()
letters.pop(1)
letters.append('c')
letters.remove('c')
del(letters[0])
del letters[1]
letters.clear()

print(letters)
print(len(letters))
