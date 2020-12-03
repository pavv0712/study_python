from model_hero import HeroModel

heroes = list()

# heroes.append(HeroModel('hulk','미국',23))
# heroes.append(HeroModel('ironman','미국',34))
# heroes.append(HeroModel('hawkeye','미국',55))
# heroes.append(HeroModel('loki','미국',66))
# heroes.append(HeroModel ('thor','미국',77))
# heroes.append(HeroModel('captain','미국',88))
# heroes.append(HeroModel('vision','미국',99))


# f = open('c:/python/heroes.txt', 'w', encoding='utf8')

# for h in heroes:
#      f.write(h.Writeline())

# f.close()

newheroes = list()

f = open('c:/python/heroes.txt', 'r', encoding='utf8')
for line in f.readlines():
     strHero = line.replace('\n','')

     herolines = strHero.split(';')
     nation = herolines[0]
     name = herolines[1]
     age = int(herolines[2])
     ishero = bool(herolines[3])
    
     hero = HeroModel(name, nation, age, ishero)
     newheroes.append(hero)
f.close()


def Existhero(name):
    isExist = False
    
    for hero in newheroes:
        if hero.name == name:
            isExist = True

    return isExist
    



command =''
while command.upper() != 'EXIT':
    command = input('명령어를 입력해주세요.')

    if command =='1':
        name = input('추가할 영웅명을 입력요망.')


        if Existhero(name)  == True:
            print('중복. {0}'.format(name))
        else:
            nation = input('국가: ')
            age = int(input('나이: '))
            newHero = HeroModel(name, nation, age, True)
            newheroes.append(newHero)
            print('등록완료. {0}'.format(name))
    elif command == '2':
        for hero in newheroes:
            hero.showprofile()
    elif command == '3':
        f = open('c:/python/heroes.txt', 'w', encoding='utf8')

        for h in newheroes:
             f.write(h.Writeline())
        f.close()
    elif command == '4':
        f = open('c:/python/heroes.txt', 'r', encoding = 'utf8')
        for line in f.readlines():
         strHero = line.replace('\n','')

         herolines = strHero.split(';')
         nation = herolines[0]
         name = herolines[1]
         age = int(herolines[2])
         ishero = bool(herolines[3])
    
         hero = HeroModel(name, nation, age, ishero)
         newheroes.append(hero)
        f.close()



           

   
