==============================
Frequently Asked Questions
==============================

General
========
Why did you guys decied to make python3-based web framework?
	One day we read Linux Journal Dec. 2010 issue. Then we found out there are an interesting article. The article is about programming languages on top 10. Actually, python is not a popular language in Korea, but python was best on the rank. so we wander why python is popular in the world.
	
	In this reason, we decieded to study the newest python, python3. whild we're studying it, we realized there is no web framework based on only python3 (without 2to3). Finally, we are developing Pylatte as a open source project.

Using Pylatte
===============

| When i try start the pylatte server with commend "python latteServerStart.py", and i saw some error:
| Traceback (most recent call last): 
| File "C:\Users\jianxing\git\jianxingqiao-microq\pylatte_git\src\latteServerStart.py", 
| line 1, in <module> import latteSocketServer 
| File "C:\Users\jianxing\git\jianxingqiao-microq\pylatte_git\src\latteSocketServer.py", 
| line 9, in <module> import pylToPy File "C:\Users\jianxing\git\jianxingqiao-microq\pylatte_git\src\pylToPy.py",
| line 1, in <module> import ply.lex as lex ImportError: No module named ply.lex

	If you install PLY(Python Lex-Yacc) module, you will be solve this problem.

Developing Pylatte
====================
Not frequently asked yet.