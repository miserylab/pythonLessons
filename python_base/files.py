
# fw = open('doc/file.txt', 'a')
# fw.write("Hello world\n")
# fw.close()


# var = input("Напищи что-нибудь : ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()


# a - запись новых данных в файл и помещение новых данных в конец файла
# w - запись новых данных в файл, но с удалением старых данных

fw = open('doc/file2.txt', 'w')
fw.write("privet")
fw.close()


fw = open('doc/file3.txt', 'w', encoding='utf-8')
fw.write("ававыа")
fw.close()


fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()

print(text)