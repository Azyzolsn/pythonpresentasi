# Input data 
nama = input('Masukan nama anda : ')
kelas = input('Masukan kelas anda : ')
mtk = input('masukan nilai Matematika anda : ')
indo = input('masukan nilai Bahasa Indonesia anda : ')
inggris = input('Masukan nilai Bahasa Inggris anda : ')

# Pengolahan data
total_nilai = int(mtk) + int(indo) + int(inggris)
nilai_rata_rata = (int(mtk )+ int(indo) + int(inggris)) / 3

# Output data
print('================================================================================')
print('Nama : ' + str(nama))
print('kelas :  ' + str(kelas))
print('=================================================================================')
print('Nilai Matematika : ' + str(mtk))

if int(mtk) >= 70 :
    print('Status : Nilai memenuhi KKM')
else : 
    print('Status : Nilai tidak memenuhi KKM')
    
print('Nilai Bahasa Indonesia : ' + str(indo))

if int(indo) >= 70 :
    print('Status : Nilai memenuhi KKM')
else : 
    print('Status : Nilai tidak memenuhi KKM')

print('Nilai Bahasa Inggris : ' + str(inggris))

if int(inggris) >= 70 :
    print('Status : Nilai memenuhi KKM')
else :
    print('Status : Nilai tidak memenuhi KKM')
    
print('Total Nilai : ' + str(total_nilai))
print('Nilai rata-rata : ' + str(nilai_rata_rata))

if nilai_rata_rata >= 70 :
    print('Anda lulus ')
else : 
    print('Anda dinyatakan tidak lulus')
