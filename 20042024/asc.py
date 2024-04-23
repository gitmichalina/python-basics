import locale

print("résumé".encode("utf-8"))
# b'r\xc3\xa9sum\xc3\xa9'
print("El Niño".encode("utf-8"))
# b'El Ni\xc3\xb1o'

print(b"r\xc3\xa9sum\xc3\xa9".decode("utf-8"))
# résumé
print(b"El Ni\xc3\xb1o".decode("utf-8"))
# El Niño

print(locale.getpreferredencoding())
# cp1250