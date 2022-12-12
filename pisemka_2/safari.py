# Vaším úkolem bude vytvořit program, který bude uchovávat informace o zvířatech na safari
# Vytvořte třídu Safari, která bude obsahovat tyto vlastnosti:
#   animals (list[Animal]) - uchovává zvířata, která jsou na safari
# Vytvořte třídu Animal, která bude obsahovat tyto vlastnosti a metody
#   name (str) - jméno zvířete
#   species (str) - druh zvířete 
#   sex (str) - pohlaví (male, female)
#   info (Info) - stav zvířete
#   cure_animal(self): vylečí zvíře (nastaví info.illness na False)
#   mating(self, animal):
#       pokus o spáření dvou zvířat.
#       Pokud zvířata budou jiného druhu (self.species != animal.species), tak vyhoďtě výjimku dle své volby.
#       Pokud zvířata budou stejného pohlaví, tak vyhoďte také výjimku
#       Pokud jedno ze zvířat bude nemocné nebo už je březí, vyhoďte také výjimku
#       Pokud jsou zvířata od sebe vzdáleny více než 100 m, tak vyhoďte výjimku
#       Páření bude probíhat tak, že bude přibližně 33% šance na splození.
#       Pokud bylo páření úspěšné, nastavte self.info.gravid = True
#   distance(self, animal):
#       Funkce vrátí vzdálenost dvou zvířat podle polohy (self.info.location)
# Vytvořte třídu Info, která bude mít tyto vlastnosti:
#   illness (bool) - určuje zda je zvíře nemocné
#   gravid (bool) - určuje, zda je zvíře březí
#   location (tuple(latitude(float), longitude(float))) - souřadnice zvířat ve formě tuplu, který má dvě float souřadnice
#       V konstruktoru ověřte, že hodnoty souřadnic jsou v rozsahu WGS84. Pokud budou mimo rozsah, tak vyhoďte výjimku
# Pro každou třídu implementujte konstruktor __init__
# Pro každou třídu implementujte metodu __repr__
# Nakonec vytvořte ukázkový příklad, kde vytvoříte zvířata a Safari
