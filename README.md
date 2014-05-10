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

Notes:
------
You will still need to enter captcha. This library will provide you with the image for captcha. <font color="red">You **MUST NOT** develop any form of automatic captcha bypass.</font>
