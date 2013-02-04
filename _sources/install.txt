=========
Install
=========

This instruction is basically based on debian linux, Ubuntu.

Python3.x Install
========================
Pylatte is python3.x based framework. Therefore it is mandatory to install python3.x interpreter.

.. code-block:: bash

	$sudo apt-get install python3
	$python3
	
Current version is python3.2. so it is up to you if you install python3 or python3.2. After installing, check out whether it is installed or not.

pip Install
============
pip is a tool for installing and managing Python packages, such as those found in the Python Package Index. It's a replacement for easy_install.

you can download install file at http://pypi.python.org/pypi/pip/ and unzip the file and install.

.. code-block:: bash

	$sudo python3 setup.py install
	
pylatte Install
============

.. code-block:: bash

	$pip-3.2 install --upgrade pylatte
	
Check if the installation is complete or not
Execute python3.x interpreter

.. code-block:: bash

	$python3
	
Then, import Pylatte

.. code-block:: python
	
	import pylatte

If import is successful without any error message, congratulation! it is complete.
	
		
	