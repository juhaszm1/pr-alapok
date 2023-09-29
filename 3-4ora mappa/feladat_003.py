#  feladat_003
# dk9 95-oldal

print(f'udv neked!')
evek_szama = input('hany eves vagy? ')
evek_szama = int(evek_szama)

if evek_szama == 0:
    print(f"meg nem szulettes meg")
elif evek_szama < 6:
    print(f"{evek_szama} eves vagy meg nem jarsz altalanos iskolaba")
elif evek_szama >= 6 and evek_szama <= 14:
    print(f"{evek_szama} eves vagy altalanos iskolaba jarsz")
elif evek_szama >= 14 and evek_szama <= 65:
    print(f"{evek_szama} tanulsz vagy dolgozol")

else:
    print(f" {evek_szama} eves vagy nyugdijas")

#else:
   #print(f"egy ev mulva {evek_szama+1} eves leszel")
   #print(f"nem altalanos iskolaba jarsz")
