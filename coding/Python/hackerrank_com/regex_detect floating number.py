"""
^ says start of the expression.

[-+]? says it can start with either - or +.

[0-9] says any number from 0-9 can be followed after it.

* says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, even 0 times.

'.' is placeholder for any character.(for the answer it should be '\.' instead of '.' ; '\' is escape character. Because of this you can literally mean a dot in expression).

again[0-9] as explained earlier.

'+' says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, but atleast one time.

$ follows whichever thing it should come in the end.



r'^[+-]? says that the input start with + or -
[0-9]* says that the next char will be 0,1,2,3,4,5,6,7,8 or 9 the digit will be appear once or more.

. here \ is a skip char that is used for "." ,without using . compiler can't understand "." char

"[0-9]+$" says that the last digit will be at least one digit from 0,1,2,3,4,5,6,7,8,9 decimal digit. dolar sign is ending symbol.
 """

import re
for _ in range(int(input())):
    print( bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
