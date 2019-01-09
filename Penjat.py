import random

dibuixPenjat = ["""

  +---+
  |   |
      |
      |
      |
      |
=========== """, """

  +---+
  |   |
  0   |
      |
      |
      |
=========== """, """

  +---+
  |   |
  0   |
  |   |
      |
      |
=========== """, """

  +---+
  |   |
  0   |
  |\  |
      |
      |
=========== """, """


  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========== """, """


  +---+
  |   |
  0   |
 /|\  |
   \  |
      |
=========== """, """

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========== """]
paraules = " gos gat ratoli fortnite casa esternocleidomastoideo sopar policia granota hotel mercedes hospital elefant bolígraf ximpanze mirall raspberry pernil nadal nevada caixa rotlle bossa escudella porta arduino python scratch".split()

def paraulaAleatoria(llistat):
    indexParaula = random.randint(0, len(llistat) -1)
    return llistat[indexParaula]

def displayPantalla(dibuixPenjat, lletresFaltants, lletresCorrectes, paraulaSecreta):
    print (dibuixPenjat[len(lletresFaltants)])
    
    blanks = "_" * len(paraulaSecreta)
    
    for i in range(len(paraulaSecreta)):
        if paraulaSecreta[i] in lletresCorrectes:
            blanks = blanks[:i] + paraulaSecreta[i] + blanks[i+1:]

    for lletra in blanks: print lletra, 

    print "\nLletres utilitzades:" ,
    for lletra in lletresFaltants: print lletra,
        
def encertar(jaEncertat):
    while True:
        print "\nEndevina una lletra"
        adivina = raw_input()
        adivina = adivina.lower()
        if len(adivina) != 1:
            print "Sisplau introdueix una lletra."
        elif adivina in jaEncertat:
            print "Ja has adivinat aquesta lletra, escull-ne una altra"
        elif adivina not in "abcçdefghijklmnopqrstuvwxyz":
            print "Només pots introduir LLETRES."
        else:
            return adivina

def tornaraJugar():
    print "Vols tornar a jugar?(si o no)"
    return raw_input().lower().startswith("s")

print "P E N J A T"
lletresFaltants = ""
lletresCorrectes = ""
paraulaSecreta = paraulaAleatoria(paraules)
jocAcabat = False


while True:
    displayPantalla (dibuixPenjat, lletresFaltants, lletresCorrectes, paraulaSecreta)

    adivina = encertar(lletresFaltants + lletresCorrectes)
    
    if adivina in paraulaSecreta:
        lletresCorrectes = lletresCorrectes + adivina
        TrobaTot = True
        for i in range(len(paraulaSecreta)):
            if paraulaSecreta[i] not in lletresCorrectes:
                TrobaTot = False
                break
    else:
        lletresFaltants = lletresFaltants + adivina
        TrobaTot = False
    if TrobaTot:
        print "Siii! La paraula secreta es " + paraulaSecreta + "! Has guanyat!!!"
        jocAcabat = True
    else:
        if len(lletresFaltants) == len(dibuixPenjat) -1:
            displayPantalla(dibuixPenjat, lletresFaltants, lletresCorrectes, paraulaSecreta)
            print "Has fet masses intents!\nDespres de " + str(len(lletresFaltants)) + " intents i " + str(len(lletresCorrectes)) + " encerts correctes, la paraula era " + paraulaSecreta + " "
            jocAcabat = True
            
    if jocAcabat:
        if tornaraJugar():
            lletresFaltants = ""
            lletresCorrectes = ""
            jocAcabat = False
            paraulaSecreta = paraulaAleatoria(paraules)
        else:
            break


















































    











































