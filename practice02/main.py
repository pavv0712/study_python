from model_trip import Trip

command = ''
cities = list()


def Existcity(name):
    isExists = False

    for city in cities:
        if city.name == name:
            isExists = True

    return isExists  

def Inputint(message):
    text = None
    isnumber = False
    while isnumber == False:
        try:
            num = input(message)
            text = int(num)
            isnumber = True
        except:
            print('숫자를 입력하세요.')
    
    return text

def InputBool(message):
    
    isma = None
    ismarry = False
    while ismarry == False:
        text = input(message)
        
        if text.upper() == 'Y':
            isma = True
            ismarry = True

        elif text.upper() =='N':
            isma = False
            ismarry = True

        if ismarry == False:
            print('지정한대로 입력해주세요.')

    return isma  

def Search():
    print('검색중')
    for city in cities:
        print(city.name, city.age, city.year, city.ismarried)
    print('결과: 총 {0}건'.format(len(cities)))

def NewCity():
    
    isExists = True
    while isExists == True:
        name = input('도시를 입력해주세요.')
        isExists = Existcity(name)
        if isExists == True:
            print('중복')


    age = Inputint('나이')
    year = Inputint('제정년도')
    ismarried = InputBool('결혼 여부 Y/N')

    c = Trip(name, age, year, ismarried)
    cities.append(c)

def Save():
    f = open('c:/python/citylist.txt', 'w', encoding = 'utf8')

    for city in cities:
        f.write(city.writeline())    
    
    
    f.close()
    print('저장완료 총 {0}'.format(len(cities)))

def Load():

    cities.clear()
    f = open('c:/python/citylist.txt', 'r', encoding = 'utf8')
    
    for line in f.readlines():
        items = line.replace('\n', '').split(';')

        name = items[0]
        age = int(items[1])
        year = int(items[2])
        ismarried = bool(items[3])

        city = Trip(name, age, year, ismarried)

        cities.append(city)
    
    f.close()
    
    
while command.upper() != 'EXIT':
    command = input('명령어를 입력해주세요.\n(1: 추가, 2: 조회, 3: 저장, 4: 불러오기)')

    if command == '1':
        NewCity()
        
    elif command == '2':
        Search()
    elif command == '3':
        Save()
    elif command == '4':
        Load()


    

