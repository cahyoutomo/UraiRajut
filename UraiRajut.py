#SOAL 3, UraiRajut

class UraiRajut:                                     #Buat suatu class dengan nama UraiRajut dimana di dalamnya terdapat 2 function
    
    def urai(self,kata) :                            #Buat suatu function dengan nama urai yang berisi 2 parameter (self dan kata)
        hasil = ''                                   #Terdapar variabel hasil yang kosong, nantinya untuk menampung hasil iterasi dari for loop
        for i in range (len(kata)+1):                #For loop sebanyak i terhadap panjang kata yang ditambah 1 (yg pertama untuk membuat row(print ke bawah))
            for j in range(i) :                      #For loop sebanyak j terhadap i (yg kedua untuk membuat column(print samping))
                hasil += kata[j]                     #variabel hasil akan ditambahkan oleh isi dari kata di index ke j
                                                     #apabila kata=Code (contoh soal), nanti iterasinya jadi C CC CCo CCoC CCoCo..... CCoCodCode
        return hasil                                 #terminasi function dan return ke hasil
    
    def rajut(self,kata2):                             #Buat suatu function dengan nama rajut yang berisi 2 parameter (self dan kata2)                             
        hitung_kata = len(kata2)                       #Menghitung panjang data pada variabel kata2
        kapital = sum(1 for c in (kata2) if c.isupper()) #Variabel kapital untuk mencari huruf kapital yang ada pada variabel kata2 dengan for loop dimana terdapat kondisi if untuk huruf kapital

        hapus = hitung_kata-kapital                    #Variabel hapus untuk mencari berapa jumlah huruf yang akan dihapus nantinya
                                                       #Berdasar contoh, kata yg benar adalah yg diakhir, variabel hapus digunakan untuk menghitung berapa huruf yang ada sebelum kata terakhir
        hasil = kata2[hapus:hitung_kata]               #Variabel hasil untuk membuat hasilnya (variabel kata2 dicetak dari index ke-hapus sampai index ke-hitung_kata)
        return hasil                                   #Terminasi function dan return ke hasil
       

func = UraiRajut()                                     #Panggil kelas UraiRajut()

#Function urai dan parameternya
print(func.urai('Code'))
print(func.urai('Python'))
print(func.urai('Purwadhika'))

#Function rajut dan parameternya
print(func.rajut('CCoCodCode'))
print(func.rajut('PPyPytPythPythoPython'))
print(func.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))