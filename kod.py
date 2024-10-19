memes={"lol":"komik bir şeye verilen cevap",
       "cringe":"garip ya da utandırıcı bir şey",
       "rofl":"bir şakaya karşılık cevap",
       "sheesh": "onaylamamak",
       "creepy":"korkunç"}
word=input("kelime girin").lower()
if word in memes.keys():
    print(memes[word])
else:
    print("kelime yok")
