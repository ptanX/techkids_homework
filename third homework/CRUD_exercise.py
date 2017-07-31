our_items = ['T-Shirt', 'Sweater']
while 1:
    input_option = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if input_option.upper() == 'C':
        new_item = input('enter new == items:')
        our_items.append(new_item)
        print('Our items:', end = '')
        for i in range(len(our_items)):
            if i == len(our_items)-1:
                print(our_items[i], end='\n')
            else:
                print(our_items[i], end=', ')
    elif input_option.upper() == 'R':
        print('Our items:', end = ' ')
        for i in range(len(our_items)):
            if i == len(our_items)-1:
                print(our_items[i], end='\n')
            else:
                print(our_items[i], end=', ')
    elif input_option.upper() == 'U':
        position = int(input('Update position? '))
        if position >= len(our_items):
            print('Index out of range items, please try again')
        else:
            new_item = input('New items? ')
            our_items[position] = new_item
            for i in range(len(our_items)):
                if i == len(our_items)-1:
                    print(our_items[i], end='\n')
                else:
                    print(our_items[i], end=', ')
        
    elif input_option.upper() == 'D':
        position = int(input('Delete position? '))
        if position >= len(our_items):
            print('Index out of range items, please try again')
        else:
            our_items.pop(position)
            for i in range(len(our_items)):
                if i == len(our_items)-1:
                    print(our_items[i], end='\n')
                else:
                    print(our_items[i], end=', ')
    else:
        print('your input letter must be in the FUCKING four letters "C,R,U,D"')
        
