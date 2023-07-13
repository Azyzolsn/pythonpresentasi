name = "John Doe"
age = 23

print("my name is " + str(name) + " I'm " + str(age) + " years old")
# output : my name is John Doe. I'm 23 years old

friends = ["Nolan", "Mary", "Abby", "Nolan", "Abby"]
friends = list(set(friends))
# hilangkan nama yang terduplikasi hanya dengan satu baris kode

name = "jOhn DoE"
# buatlah fungsi untuk menyelesaikan permasalahan di bawah.
print(name.upper())
# output: JOHN DOE
print(name.lower())
# output: john doe
print(name.capitalize())
# output: John Doe

first_numbers = [9, 7, 10, 7, 10]

# dapatkan total nilai baris angka diatas
total = sum(first_numbers)
print("Total: ", total)

# dapatkan nilai yang paling maksimal dan minimal dari baris angka di atas
maximum = max(first_numbers)
minimum = min(first_numbers)
print("Maximum: ", maximum)
print("Minimum: ", minimum)

# berapa banyak angka yang bisa dibagi 2
habis_bagi_2 = sum(1 for num in first_numbers 
                   if num % 2 == 0)
print("Count divisible by 2: ", habis_bagi_2)

# buat lah baris ganjil menjadi dikali 2 dan baris genap ditambah 4
modif = [num * 2 
         if num % 2 != 0 
         else num + 4 
         for num in first_numbers]
print("Modified numbers: ", modif)
#perkalian silang
first_numbers = [9, 7, 10, 7, 10]
second_numbers = [2, 3]

# Lakukan perkalian silang antara baris angka pertama dengan baris angka kedua
result_number = [[x * y for y in second_numbers] for x in first_numbers]

print(result_number)

# Jumlahkan nilai berdasarkan posisi barisnya
result = [sum(row) for row in result_number]

print(result)
# berapa banyak angka yang sama muncul di dalam baris angka tersebut
count_duplicates = len(first_numbers) - len(set(first_numbers))
print("Count of duplicates: ", count_duplicates)

#palindrome
def palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

print(palindrome("kodok"))

print(palindrome("katak"))

print(palindrome("ab"))






