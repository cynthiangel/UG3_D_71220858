curahhujan = input('Masukkan nilai curah hujan\t: ').lower().split(' ')


a = ('Curah hujan 0 artinya Cuaca Terang/Berawan' if curahhujan[0] == 'terang/berawan' else(print('Curah hujan 0.5-20 artinya Curah hujan ringan' if curahhujan[0] == 'hujan ringan' else(print('Curah hujan 21-50 artinya Curah hujan sedang' if curahhujan[0] == 'hujan sedang' else(print(' Curah hujan 51-100 artinya Curah hujan lebat' if curahhujan[0] == 'hujan lebat' else(print('Curah hujan diatas 100 artinya Curah hujan ekstrem' if curahhujan[0]=='hujan ekstrem'))))))))
print(a)