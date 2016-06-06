# std.py for C++ython

import sys


PY_VERSION = sys.version_info[0]
PY_PRINT = ("print(%s)" if PY_VERSION == 3 else "print %s")
PY_PRINT_SUB = ("print(%s % (%s))" if PY_VERSION == 3 else "print %s % (%s)")
PY_PRINT_NO_NEWLINE = ("print(%s, end=\"\")" if PY_VERSION == 3 else "print %s,")
PY_PRINT_SUB_NO_NEWLINE = ("print(%s % (%s), end=\"\")" if PY_VERSION == 3 else "print %s % (%s),")


class data:
    pass


class CppInput:
    def __rshift__(self, other):
        exec("""
data.%s = input()
        """ % other)
        return self


class CppOutput:
    def __lshift__(self, other):
        exec(PY_PRINT_NO_NEWLINE % ("\"\"\"" + other + "\"\"\""))
        return self


cin = CppInput()
i = cin
cout = CppOutput()
o = cout
endl = '\n'
l = endl
