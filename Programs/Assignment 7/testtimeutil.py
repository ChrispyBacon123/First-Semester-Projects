# Statement coverage for validate function

"""
>>> import timeutil
>>> timeutil.validate("5 21 a.m.")
False
>>> timeutil.validate("111:20 p.m.")
False
>>> timeutil.validate("03:35 a.m.")
False
>>> timeutil.validate("15:35 g.m.")
False
>>> timeutil.validate("20:1 p.m.")
False
>>> timeutil.validate("11:01 p.m.")
True

"""
import doctest
doctest.testmod(verbose = True)