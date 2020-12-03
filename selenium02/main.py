from selenium import webdriver
from model_soccer import Soccer



driver = webdriver.Chrome()
driver.get('file:///C:/python/htmltable01/index.html')

table = driver.find_element_by_xpath('//table')

trs = table.find_elements_by_xpath('.//tr')

soccer_list = list()


for tr in trs:
    tds = tr.find_elements_by_xpath('.//td')
    tdlength = len(tds)

    if tdlength == 0:
        continue
    if tdlength == 1:
        continue

    rank = int(tds[0].text)
    name = tds[1].text
    score = int(tds[2].text)
    nation = tds[3].text
    team = tds[4].text

    
    s = Soccer(rank, name, score, nation, team)

    soccer_list.append(s)

print('{0}건'.format(len(soccer_list)))

# for sl in soccer_list:
#     print(sl.rank, sl.name, sl.score, sl.nation, sl.team)


# f = open('c:/python/soccer_list.txt', 'w', encoding='utf8')

# for sl in soccer_list:
#     line = '{0};{1};{2};{3};{4}\n.'.format(sl.rank, sl.name, sl.score, sl.nation, sl.team)
#     f.write(sl.Saveline())

# f.close()  


f = open('c:/python/soccer_list.txt', 'r', encoding='utf8')

for line in f.readlines():
    items = line.replace('\n', '').split(';')

    rank = int(items[0])
    name = items[1]
    score = int(items[2])
    nation = items[3]
    team = items[4]

    soccer = Soccer(rank, name, score, nation, team)

    soccer_list.append(soccer)

f.close()







    
