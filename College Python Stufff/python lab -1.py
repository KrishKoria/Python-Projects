import decimal
import keyword
from decimal import *
print(keyword.kwlist)

print(1.1+2.2)
print(Decimal(1.1+2.2))
print(decimal.getcontext().prec)
a = Decimal(1.1+2.2)
print(f"{a: .2f}")
