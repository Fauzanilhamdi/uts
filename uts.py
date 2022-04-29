#nomor 1
nilai = [4,5,3,7,9,6,8,1,2,10]
nilai.sort()
print(nilai)

#nomor 2
print('----------------------------------------------------')
print('menentukan nilai dan ujian dengan bahasa python')
print('----------------------------------------------------')

nilai = int(input('silahkan masukkan nilai: '))

if nilai >= 90 :
    print('anda mendapatkan nilai A')
elif nilai >= 80 :
    print('anda mendapatkan nilai B+')
elif nilai >= 75 :
    print('anda mendapatkan nilai B')
elif nilai >= 70 :
    print('anda mendapatkan nilai C+')
elif nilai >= 65 :
    print('anda mendapatkan nilai C')
elif nilai >= 60 :
    print('anda mendapatkan nilai D')
elif nilai >= 50 :
    print('anda mendapatkan nilai E')
elif nilai <= 40:
    print('anda mendapatkan nilai F')

#nomor 3
suhu = input('masukkan suhu nya : ')
if suhu <= 25:
    print('suhu lebih rendah daripada 25')
#nomor 4
nama_lengkap = input('masukkan nama : ')
jeniskelamin = input('masukkan jenis kelamin anda : ')
NIM = input('masukkan nim anda : ')
jurusan = input('masukkan jurusan: ')

print('selamat datang %s jenis kelamin %s nim anda %s dari jurusan %s' % (nama_lengkap,jeniskelamin,NIM,jurusan)) 