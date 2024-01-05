with open("plik.txt") as file:
    print("coś tu robimy, pewnie jakaś pętla po liniach")

# otwarcie i zwrócenie (w zmiennej file) referencji do wskazanego pliku.
my_file = open("plik.txt", "r")

# odczytanie i zwrócenie całego pliku jako jednego stringa, razem ze znakami newline
my_file.read()

# odczytuje i zwraca linię tekstu, razem z końcowym newline (\n).
# Jeśli zwrócony jest pusty string, osiągnięty jest koniec pliku.
my_file.readline()

# odczytuje cały plik i zwraca go jako listę stringów razem z newline na końcu
my_file.readlines()

# można iterować po pliku. Odczyta każdą linię, przypisze do line i wykona statement.
for line in my_file:
    print(line)

# zapisuje stringa do pliku i zwraca liczbę zapisanych znaków
my_file.write("jakiś string dodawany do pliku")

# zamyka plik. OBOWIĄZKOWE.
my_file.close()

# Przykład - obliczenie linii w pliku

count = 0
with open("plik.txt", "r") as f:
    while f.readline():
        count += 1

