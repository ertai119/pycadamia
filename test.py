numbers = [1,2,4,5]

for x in numbers:
    if 2 < x < 4:
        print('found')
        break
else:
    print('not found')