print('Hello, Django girls!')
a = 2 + 3
print(a)

# コメント行

name = 'Sonja'


# hi()関数
# 関数は、関数定義の後に呼び出す必要がある
def hi(name):
	print('Hi ' + name + '!')


girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
	hi(name)
	print('Next girl')

# rangeの2つ目の引数はリストに含まれない
for i in range(1, 6):
	print(i)

