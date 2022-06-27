import os

def gs(file):
    gs.list = []
    with open(file, 'r') as f:
        for line in f:
            gs.list.append(line)

def ge(list):
    counter = 0
    counter2 = 0
    test = 'MAC Address'
    for element in list:
        counter = counter + 1
        if element[0] == '8':
            http_title = ''
            for charecter in element[:len(test)]:
                http_title = http_title + charecter
            if http_title == test:
                print('-------------------------------------')
                print(element + ' is at line ' + str(counter))
                print('-------------------------------------')
         
            

gs("big.txt")
ge(gs.list)