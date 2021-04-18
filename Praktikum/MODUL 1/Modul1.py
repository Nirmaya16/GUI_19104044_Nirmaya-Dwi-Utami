Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 9
>>> id(x)
140716398618656
>>> y = 9
>>> id(y)
140716398618656
>>> x = 9
>>> id(x)
140716398618656
>>> y = 12
>>> id(y)
140716398618752
>>> x = 9
>>> id(x)
140716398618656
>>> y = 9
>>> id(y)
140716398618656
>>> del y
>>> y
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x
9
>>> id(x)
140716398618656
>>> x = True
>>> id(x)
140716398335824
>>> posisi = (300,300)
>>> posisi
(300, 300)
>>> 
>>> Posisi
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Posisi
NameError: name 'Posisi' is not defined
>>> a = 1; b = 2; c =3
>>> print(a); print(b); print(c)
1
2
3
>>> x = 9
>>> if isinstance(x,int)and \
   x > 0 and \
   x % 2 == 1:
	print("%d adalah bilangan bulat ganjil positif" %x)
	9 adalah bilangan bulat ganjil positif
	
SyntaxError: invalid syntax
>>> x = 9
>>> if isinstance(x,int)and \
 x > 0 and \
 x % 2 == 1:
    print("%9 adalah bilangan bulat ganjil positif" %x)
9 adalah bilangan bulat ganjil positif
SyntaxError: invalid syntax
>>> print("Pemrograman GUI") +
SyntaxError: invalid syntax
>>> print("Pemrograman GUI" +
      "dengan Python dan PyQt")
Pemrograman GUIdengan Python dan PyQt
>>> data = [
100,
200,
300
]
>>> kamus = {
'one':'satu',
'two':'dua',
'three':'tiga'
}
>>> data
[100, 200, 300]
>>> kamus
{'one': 'satu', 'two': 'dua', 'three': 'tiga'}
>>> x = 9
>>> if isinstance(x,int)and \
 x > 0 and \
 x % 2 == 1:
    print("%d adalah bilangan bulat ganjil positif" %x)

    
9 adalah bilangan bulat ganjil positif
>>> # bilangan biner
>>> a = 0b1001
>>> # bilangan oktal
>>> b = 0o23
>>> # bilangan heksadesimal
>>> c = 0x2f
>>> a
9
>>> b
19
>>> c
47
>>> a = True
>>> type(a)
<class 'bool'>
>>> int(a)
1
>>> a = 15
>>> id(a)
140716398618848
>>> a += 5
>>> a
20
>>> id(a)
140716398619008
>>> a = 123.456
>>> a
123.456
>>> a * 2
246.912
>>> s1 = 'pemrograman pythhon'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman
... python 3'''
>>> 
>>> s1 = 'pemrograman python'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman
... python 3'''
>>> s1[0], s1[1],ArithmeticError s1[2]
SyntaxError: invalid syntax
>>> s1 = 'pemrograman python'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman python 3'''
SyntaxError: multiple statements found while compiling a single statement
>>> s1 = 'pemrograman python'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman
... python 3'''
SyntaxError: multiple statements found while compiling a single statement
>>> s1 = 'pemrograman python'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman python 3'''
SyntaxError: multiple statements found while compiling a single statement
>>> s1 = 'pemrograman python'
>>> s2 = 
KeyboardInterrupt
>>> s1 = 'pemrograman python'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman
... python 3'''
>>> s1[0], s2[1], s3[2]
('p', 'e', 'm')
>>> 
>>> data = 'p001\tspidol\t\t9000\np002\tpensil\t\t6000'
>>> print(data)
p001	spidol		9000
p002	pensil		6000
>>> 
>>> data = '\tharga\n' + data
>>> print(data)
	harga
p001	spidol		9000
p002	pensil		6000
>>> 
>>> s1 = 'python'
>>> s2 = 'PYTHON'
>>> s1 == s2
False
>>> s1 != s2
True
>>> s1 < s2
False
>>> s1 > s2
True
>>> s1 <= s2
False
>>> s1 >= s2
True
>>> 
>>> s = 'Pemrograman Python dan PyQt'
>>> s1 = s[0:11]
>>> s1
'Pemrograman'
>>> len(s1)
11
>>> 
>>> s = s[:11]
>>> s = s[:8]
>>> s = 'Pemrograman Python dan PyQt'
>>> s1 = s[:11]
>>> s[:8]
'Pemrogra'
>>> s = 'Pemrograman Python dan PyQt'
>>> s = s[:11]
>>> s = s[:8]
>>> s = s[8:]
>>> s = s[0:11:2]
>>> s = s[0:11:1]
>>> s = s[0:11:3]
>>> s
''
>>> 
>>> len(s)
0
>>> 
>>> print(s)

>>> s = s[:11]
>>> s = s[:8]
>>> s = s[8:]
>>> s = s[0:11:2]
>>> s = s[0:11:1]
>>> s = s[0:11:3]
SyntaxError: multiple statements found while compiling a single statement
>>> s = 'Pemrograman Python dan PyQt'
>>> s1 = s[:8]
>>> s1
'Pemrogra'
>>> s1 = s[8:]
>>> s1
'man Python dan PyQt'
>>> s1 = s[:11]
>>> s1
'Pemrograman'
>>> s1 = s[0:11:2]
>>> s1
'Pmormn'
>>> s1 = s[0:11:1]
>>> s1
'Pemrograman'
>>> s1 = s[0:11:3]
>>> s1
'Prra'
>>> 
>>> s = 'balonku ada %d, kempes %d tinggal %f' %(5,1,4,5)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    s = 'balonku ada %d, kempes %d tinggal %f' %(5,1,4,5)
TypeError: not all arguments converted during string formatting
>>> s = 'balonku ada %d, kempes %d tinggal %f' %(5,1,4.5)
>>> s
'balonku ada 5, kempes 1 tinggal 4.500000'
>>> 
>>> list = ['balon, 'budi', 'ada', 5]
	
SyntaxError: invalid syntax
>>> list = ['balon', 'budi', 'ada', 5]
>>> for item in list:
	print(item)

	
balon
budi
ada
5
>>> extend(['rupa-rupa'])
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    extend(['rupa-rupa'])
NameError: name 'extend' is not defined
>>> balon['0'] = nyawa
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    balon['0'] = nyawa
NameError: name 'nyawa' is not defined
>>> del['balon']
SyntaxError: cannot delete literal
>>> 