list_names = ['Esperanza', 'Sandra', 'Luis', 'Camilo']

for name in list_names:
    print(name,'with length', len(name))
    if len(name) >= 5:
        print('name longer than 5')
    if 'n' in name or 'N' in name:
        print('With "n" or "N".')
    
while len(list_names) > 0:
    list_names.pop()
    print(list_names)
