Euler-Task
==========

Helping library for Project Euler in Python

This library will help you submit and read tasks from Project Euler more easily.
Very simple and easy to use.

Importing
---------
```python
from EulerTask import EulerTask
```

Installation
------------
For now, you need to download the library ZIP from Github (on right side, Download as ZIP), and extract it to the same folder your script is located (or from the current working directory of python terminal).
In future, there might be an easier way of installation (like pip).

Compatibility
-------------
This library is compatible with python 2.x and 3.x. Note however that for 3.x you'll need to use PILLOW instead of PIL, since PIL doesn't support 3.x.

Example:
--------
```python
#Submit solution:
EulerTask('username', 'password').setProblem(ProblemNumber).solve(MySolution)
#Print problem statement:
EulerTask('username', 'password').setProblem(ProblemNumber).printProblemStatement()
#Print problem statement and submit solution:
EulerTask('username', 'password').setProblem(ProblemNumber).printProblemStatement().solve(MySolution)
```

Dependencies:
-------------
* Mechanize (Python virtual browser)
* BeautifulSoup (Python html parser)

Optional dependencies:
* PIL (Python imaging library)
or
* PILLOW (PIL fork)

Notes:
------
You will still need to enter captcha. This library will provide you with the image for captcha. <font color="red">You **MUST NOT** develop any form of automatic captcha bypass.</font>
