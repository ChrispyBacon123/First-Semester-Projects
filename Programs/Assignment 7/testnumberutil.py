# Statement coverage for aswords function

"""
>>> import numberutil

>>> numberutil.aswords(0)
'zero'

>>> numberutil.aswords(8)
'eight'

>>> numberutil.aswords(70)
'seventy'

>>> numberutil.aswords(34)
'thirty four'

>>> numberutil.aswords(600)
'six hundred'

>>> numberutil.aswords(603)
'six hundred and three'

>>> numberutil.aswords(321)
'three hundred and twenty one'

>>> numberutil.aswords(350)
'three hundred and fifty'

"""
import doctest
doctest.testmod(verbose = True)