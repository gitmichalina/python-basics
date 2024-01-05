import pickle

my_object = [1, 2, 3]

# zapisuje obiekt do pliku, ktory musi byc otwarty w trybie 'wb' (write binary
my_file = open("my_file.bin", "wb")
pickle.dump(my_object, my_file)
my_file.close()

# rekonstruuje obiekt zapisany do pliku, musi być ten plik otwarty w trybie 'rb'
my_file = open("my_file.bin", "rb")
reconstructed_object = pickle.load(my_file)
my_file.close()
print("zrekonstruowany obiekt", reconstructed_object)

# zapisuje obiekt w zmiennej jako string
string_from_my_object = pickle.dumps(my_object)
print("obiekt wyslany do stringa", string_from_my_object)

# rekonstruuje obiekt zapisany wczesniej w stringu
my_object_from_string = pickle.loads(string_from_my_object)
print("obiekt wyciagniety ze stringa", string_from_my_object)
