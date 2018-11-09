saya = input( 'masukkan berat badan anda' )
teman = input( 'masukkan berat badan teman' )
saya = int(saya)
teman = int(teman)
hasil1 = (saya- teman)
hasil2 = (teman-saya)
if teman > saya:
      kategori = 'kamu lebih ringan' ,abs(hasil1), 'kg dari teman kamu'
elif teman < saya:
      kategori = 'kamu lebih berat' ,abs(hasil2), 'kg dari teman kamu'
else:
      kategori = 'berat kamu sama dengan teman kamu '
print('{}'.format(kategori))