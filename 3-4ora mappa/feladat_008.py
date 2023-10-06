# feladat_008

"""
kerjunk be ket egesz szamot szam1 szam2
hasonlitsuk ossze a ket szamot es irassuk ki 
hogy a szam1 szam2 kisebb mint a szam2
vagy szam2 kisebb mint a szam1
vagy a szam1 egyenlo szam2-vel
"""

szam1=input("Irj be egy szamot /szam1/ : ")
szam2=input("Irj be megegy szamot /szam2/ : ")
szam1=int(szam1)
szam2=int(szam2)

"""
if szam1 < szam2:
    print(f"a szam1 kisebb mint a szam2")
elif szam2 < szam1:
    print(f"a szam2 kisebb mint a szam1")
else:
    print(f"a szam1 egyenlo a szam2-vel")    
"""

"""
if szam1 < szam2:
    print(f"a szam1 kisebb mint a szam2")
if szam2 < szam1:
    print(f"a szam2 kisebb mint a szam1")
if szam1 == szam2:
    print(f"a szam1 egyenlo a szam2-vel")
"""


if szam1 < szam2:
    print(f"a szam1 kisebb mint a szam2")
elif szam2 < szam1:
    print(f"a szam2 kisebb mint a szam1")
elif szam1 == szam2:
    print(f"a szam1 egyenlo szam2")