from operasi_matematika import operasiMatematika
import unittest

class testOperasi(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self):
        self.operasi = operasiMatematika(10,5)
        
    def test_penjumlahan(self):
        self.operasi.penjumlahan()
        hasil = self.operasi.nilai
        self.assertEqual(hasil, 10+5)
        
    def test_pengurangan(self):
        self.operasi.pengurangan()
        hasil = self.operasi.nilai
        self.assertEqual(hasil, 10-5)

    def test_perkalian(self):
        self.operasi.perkalian()
        hasil = self.operasi.nilai
        self.assertEqual(hasil, 10*5)
        
    def test_pembagian(self):
        self.operasi.pembagian()
        hasil = self.operasi.nilai
        self.assertEqual(hasil, 10/5)
        
    # Uji kasus ketika b adalah nol
    def test_pembagian_by_zero(self):
        with self.assertRaises(ValueError):
            self.operator = operasiMatematika(10,0)
            self.operator.pembagian()  
            
    def tearDown(self):
        self.operasi.nilai = 0
    
if __name__ == '__main__':
    unittest.main()