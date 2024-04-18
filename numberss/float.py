from numpy import array
import textwrap
y=array([0, 1])

try:
    bool(y)
except ValueError as exc:
    print("\n".join(textwrap.wrap(str(exc))))
