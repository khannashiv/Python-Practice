## Approach 0 : Without using __init__.py file || Working  for me.

# from mypackage import math_ops, string_ops

# print(math_ops.mul(2,3))
# print(math_ops.sub(2,3))
# print(math_ops.div(2,3))

# print(string_ops.shout("wow"))
# print(string_ops.whisper("listen"))

## Approach 1 : Absolute imports & making use of __init__.py file altough commented out since we are using absolute path || Working for me. ||  Running python file directly from the directory where file exists i.e python test_package.py

# Test-1 | Working .

from mypackage.math_ops import mul, sub
from mypackage.string_ops import shout, whisper

print(mul(3, 7))
print(sub(7,2))
print(shout("wow"))

# Test-2 | Working .

from modules_packages.mypackage.math_ops import div
print(div(1,2))

# Summary:
    # Absolute imports (e.g. from mypackage.math_ops import mul) || python test_package.py or python -m test_package || Tested with Test-1
    # python -m modules_packages.test_package --> Tested with Test-2
    # Relative imports not worked for me.



   