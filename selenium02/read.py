from model_soccer import Soccer


f = open('c:python/soccer_list.txt', 'r', encoding='utf8')

for line in f.readlines():
    print(line)


f.close()