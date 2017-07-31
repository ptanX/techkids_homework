sheep_list = [25,371, 130, 204, 219, 272, 124, 445, 47, 51]
total_money = 0
for i in range(4):
    print('MONTH {0}'.format(i+1))
    print('One Fucking month has passed, here are my sheep')
    print('Hello my nam is ptanx, and they are my FUCKING sheep list:\n')
    print(sheep_list)
    print("Now biggest has size {0} lets shear it".format(str(max(sheep_list))))
    sheep_list[sheep_list.index(max(sheep_list))] = 8
    print("After shearing here are my Fucking Sheep:\n" + str(sheep_list))
    sheep_list[sheep_list.index(8)] = 58
    
print('My flock size is total: {0}'.format(sum(sheep_list)))
print('i would get: {0}$'.format(sum(sheep_list)*20))
