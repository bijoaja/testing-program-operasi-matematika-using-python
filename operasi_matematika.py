class operasiMatematika:
    def __init__(self, a,b) -> None:
        self.a = a
        self.b = b
        self.nilai = 0
        
    def penjumlahan(self):
        self.nilai = self.a + self.b
    
    def pengurangan(self):
        self.nilai = self.a - self.b
    
    def perkalian(self):
        self.nilai = self.a * self.b
    
    def pembagian(self):
        if self.b == 0:
            raise ValueError(f'Hasil operasi dari {self.a} / {self.b} = Tak Terhingga / Error')
        self.nilai = self.a / self.b


def hasil(operasi, bilangan_1, bilangan_2):
    hasil = operasiMatematika(bilangan_1,bilangan_2)

    if operasi == "1":
        operasi = "+"
        hasil.penjumlahan()
        
    elif operasi == '2':
        operasi = "-"
        hasil.pengurangan()
        
    elif operasi == '3':
        operasi = "*"
        hasil.perkalian()
        
    elif operasi == '4':
        operasi = "/"
        hasil.pembagian()
        
    else:
        return 'Tidak valid'
    hasil = hasil.nilai
    
    return f'Hasil operasi dari {bilangan_1} {operasi} {bilangan_2} = {hasil}'


def show():
    print('='*25)
    print('Operasi Matematika')
    print('1. Jumlah \t [+]')
    print('2. Kurang \t [-]')
    print('3. Kali \t [*]')
    print('4. Bagi \t [/]')
    print('=' * 25)
    operasi = input('Pilih operasi (1/2/3/4): ')
    bilangan_1 = eval(input('Masukkan bilangan pertama: '))
    bilangan_2 = eval(input('Masukkan bilangan kedua: '))
    print('=' * 25)
    print(hasil(operasi, bilangan_1, bilangan_2))

if __name__ == '__main__':
    show()