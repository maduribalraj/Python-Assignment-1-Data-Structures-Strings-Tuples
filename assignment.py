Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> >>> string1 = "Hello "
... ... name = input("Enter your Name: ")
... ...
... ... result = string1 + name
... ... print(result)
... ...
... Enter your Name: maduri balraj
... Hello maduri balraj
... >>> string1 = "Hello "
... ... name = input("Enter your Name: ")
... ...
... ... result = string1 + name
... ... string3 = ", welcome to Python programming"
... ...
... ... result = result + string3
... ... print(result)
... ...
... Enter your Name: maduri balraj
... Hello maduri balraj, welcome to Python programming
... >>> text = "Hello Maduri Balraj, welcome to Python programming"
... ...
... ... print(text[0])
... ...
... H
... >>> text = "Hello Maduri Balraj, welcome to Python programming"
... ...
... ... print(text[-1])
... ...
... g
... >>> text = "Hello Maduri Balraj, welcome to Python programming"
... ...
... ... print(text[:5])
... ...
... Hello
... >>> text = "Hello Maduri Balraj, welcome to Python programming"
... ...
... ... print(text[-11:])
... ...
... programming
... >>> gnimmargorp nohtyP ot emoclew ,jarlaB irudaM olleH
...   File "<python-input-11>", line 1
...     gnimmargorp nohtyP ot emoclew ,jarlaB irudaM olleH
...                 ^^^^^^
... SyntaxError: invalid syntax
... >>> text = "Hello Maduri Balraj, welcome to Python programming"
... print(text[::-1])
...
gnimmargorp nohtyP ot emoclew ,jarlaB irudaM olleH
>>> text = "Hello Maduri Balraj, welcome to Python programming"
...
... print(text[29:35])
...
to Pyt
>>> text = "Hello Maduri Balraj, welcome to Python programming"
...
... print(text[32:38])
...
Python
>>> strM = "Python beginner tutorial"
... print(strM.upper())
...
PYTHON BEGINNER TUTORIAL
>>> strM = "Python beginner tutorial"
... print(strM.lower())
...
python beginner tutorial
>>> strM = "Python beginner tutorial"
... print(strM.count("t"))
...
3
>>> strM = "Python beginner tutorial"
... print(strM.replace("Python", "Machine Learning"))
...
Machine Learning beginner tutorial
>>> tuple1 = (10, 20, 30)
... tuple2 = (40, 50, 60)
...
... print(tuple1)
... print(tuple2)
...
(10, 20, 30)
(40, 50, 60)
>>> tuple1 = (10, 20, 30)
... tuple2 = (40, 50, 60)
...
... t_combine = tuple1 + tuple2
...
... print(t_combine)
...
(10, 20, 30, 40, 50, 60)
>>> tuple1 = (10, 20, 30)
... tuple2 = (40, 50, 60)
...
... t_combine = tuple1 + tuple2
... repeated_tuple = t_combine * 3
...
... print(repeated_tuple)
...
(10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60)
>>> print(t_combine[2])
30
>>>
>>> print(t_combine[:3])
(10, 20, 30)
>>>
>>> print(t_combine[-3:])
(40, 50, 60)
SyntaxError: invalid syntax
