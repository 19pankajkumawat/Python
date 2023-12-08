# f = open('main.txt','rb')    rb means text so in binary form
# print(f)                     a  means we can write new text in file without remove before text
# text = f.read()
# print(text)
# f.close()


# this pro. is used to write in a file
# f = open('main.txt','w')      main.txt (file name)   w (function name)
# print(f)
# text = f.write('great')
# print(text)
# f.close()


# when we try to open a file they do not exist in our pc so this program create a new file
# f = open('main.txt3','w')
# print(f)
# text = f.read()
# print(text)
# f.close()
# this program is create a new file when the same name file did not exist

g = open('main.txt','a')
g.write('hello gyanni')