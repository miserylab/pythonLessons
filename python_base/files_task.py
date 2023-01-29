fw = open('doc/file4.txt', 'a', encoding='utf-8')
i = 0
i = sum(1 for line in open('doc/file4.txt', 'r')) + 1
fw.write('Привет' + ' ' + str(i) + ' раз(a)' + '\n')
fw.close()

fr = open('doc/file4.txt', 'r', encoding='utf-8')
print(fr.read())
fr.close()
