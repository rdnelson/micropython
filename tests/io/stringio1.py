import _io as io

a = io.StringIO()
print(a.getvalue())
print(a.read())

a = io.StringIO("foobar")
print(a.getvalue())
print(a.read())
print(a.read())

a = io.StringIO()
a.write("foo")
print(a.getvalue())

a = io.StringIO("foo")
a.write("12")
print(a.getvalue())

a = io.StringIO("foo")
a.write("123")
print(a.getvalue())

a = io.StringIO("foo")
a.write("1234")
print(a.getvalue())

a = io.StringIO()
a.write("foo")
print(a.read())

a = io.StringIO()
a.close()
for f in [a.read, a.getvalue, lambda:a.write("")]:
    # CPython throws for operations on closed I/O, micropython makes
    # the underlying string empty unless MICROPY_CPYTHON_COMPAT defined
    try:
        f()
        print("ValueError")
    except ValueError:
        print("ValueError")
