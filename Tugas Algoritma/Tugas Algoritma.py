nama = (input('MASUKAN NAMA :'))
umur = int(input('MASUKAN UMUR :'))
berat_badan = int(input('MASUKAN BERAT BADAN :'))
tinggi_badan = int(input('MASUKAN TINGGI BADAN :'))
nilai_ujian = float(input('MASUKAN NILAI UJIAN :'))

hasil= "SELAMAT ANDA LOLOS ADMINISTRASI TARUNA POLRI" if (umur>=17 and umur <=23 and berat_badan >= 50 and tinggi_badan >=165 and nilai_ujian >=75) else "ANDA TIDAK LOLOS ADMINITRASI TARUNA POLRI"

print(hasil)