"""
10-1 Python学习笔记：在文本编辑器中新建一个文件
写几句话来总结一下你至此学到的Python知识
其中每一行都以“In Python you can”打头
将这个文件命名为learning_python.txt
并将其存储到为完成本章练习而编写的程序所在的目录中

编写一个程序，它读取这个文件，并将你所写的内容打印三次：
第一次打印时读取整个文件；
第二次打印时遍历文件对象；
第三次打印时将各行存储在一个列表中，再在with代码块外打印它们


"""
filename = 'file_text/learning_python'
learning = []

print("---读取整个文件---")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print("---遍历所有对象---")
with open(filename) as file_object:
    for i in file_object.readlines():
        print(i.strip())

print("---对象都加入列表---")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    learning.append(line.strip())

print(learning)
