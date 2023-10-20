def koszont():
        print('Udv a fedelzeten')

koszont()
koszont()
koszont()

# -----------------------------------------------

# Eljárás definíciója
def koszont_nevvel(nev):
        print('Szia '+ nev +', üdv a fedélzeten!')

# Eljárás hívása    
koszont_nevvel('Ádám')

# -----------------------------------------------

def koszont_ket_nevvel(nev1, nev2):
	    #print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')
        print(f"Szia {nev1}, {nev2}!\nUdv a fedelzeten!")
koszont_ket_nevvel('Nóra', 'Ádám')

keresztnev1 = "Nóra"
keresztnev2 = "Ádám"
koszont_ket_nevvel('Nóra', 'Ádám' )
koszont_ket_nevvel(keresztnev1,keresztnev2)

# -----------------------------------------------

    