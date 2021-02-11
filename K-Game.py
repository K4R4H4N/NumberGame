import random
import sys
print("""_______________________________________
|    SAYI              TAHMİN          |    EXTREME
|              OYUNU                   |
|--------------------------------------|               MOD 
|    V1.4                     2021     |
|                 K4R4H4N              |       1.5
|              |  /                    |
|              | /                     |
|              | \                     |
|              |  \  •                 |
________________________________________""")
print(" ~ Sayı Tahmin Oyunu V1.5 Extreme Mod~\n\"Sayı Tahmin Etme\" oyununa hoşgeldiniz. \n \nAmacınız bilgisayarın 1-100 arasında tuttuğu sayıyı tahmin etmek.Lütfen sayı yerine harf girmeyin. Deneme hakkınız bilgisayar tarafından rastgele seçilir. İyi Şanslar...\n")
wer=  input("Size nasıl hitap edelim ?: ")
input("\nHerşey yüklendi ! Enter'a basarak başlayabilirsin.")

change = random.randint(6,10)
number = random.randint(1,100)
sayi=int(input("""-------------------------------------
 0-100 arasında bir sayı tahmin 👇 et:
------------------------------- """))
while change > 0:	
	if change ==1:
		print("\n-------------------------------\nBilgisayarın tuttuğu sayı: ",number,"\n  Bilemedin. Tekrar denemeye hazırmısın ? :( \n ------------------------------")
	if change ==1:		
		break
	if change ==2 :
		print("\nDİKKAT ET",wer,"! SON HAKKIN !!!")
	if sayi > number :
		change -=1
		print("\nKalan deneme hakkın: ",change,"\n")
		sayi= int(input("Daha küçük bir sayı girin: "))		
	if sayi == number :
		  print("""           |   ------------------------	  |	  
	   |  Tebrikler!""", wer, """Kazandın!!! |
	   |   ------------------------   |""")
		  sys.exit()
		
	elif sayi < number :
			change -=1
			print("\nKalan deneme hakkın:",change,"\n")
			sayi= int(input("Daha BÜYÜK bir sayı girin: "))
