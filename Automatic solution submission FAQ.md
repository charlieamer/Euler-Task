Automatic solution submission FAQ
=================================

What is Automatic solution submission ?
---------------------------------------
> Euler-Task will automaticly try to find your source, extract it's content and submit it to thread so that others can discuss your solution.

How do I enable this feature ?
------------------------------
> Put threadText = 'Default' or any other custom message (see bellow) in order to turn this feature on. For example:
```python
EulerTask('Username', 'Password', threadText = 'Default')
```

What about my username and password information ?
-------------------------------------------------
> Others **will not** see your username and password as code is filtered out before sending to thread.

Can I put my custom message in thread ?
---------------------------------------
> **Yes**, when initializing EulerTask object, put threadText = "Your text". Put '%s' in place where you want your code to be. For example:
```python
EulerTask('Username', 'Password', threadText = "Check out my awesome code: %s")
```

Can I force resubmit my code to thread although I already solved the task ?
---------------------------------------------------------------------------
> **No**, but you will be able to do so soon.