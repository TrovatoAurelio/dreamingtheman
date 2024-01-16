import math

class Studente():
  def __init__(self,nome,cognome,sezione):
    self.nome=nome
    self.cognome=cognome
    self.sezione=sezione

  def si_presenta(self):
    print("Mi chiamo "+self.nome+" "+self.cognome+" e vado nella sezione "+self.sezione)

studente1=Studente("Aurelio","Trovato","L")
studente1.si_presenta()
studente2=Studente("Stefano","Marzano","L")
studente2.si_presenta()

#si crei una classe che rappresenti un vettore. I suoi attributi sono le componenti cartesiane x e y. I metodi sono: uno che scriva il modulo del vettore, un secondo che sommi 2 vettori.


class Vettore:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def modulo(self):
    modulo=math.sqrt((self.x**2)+(self.y**2))
    return modulo

  def somma(self,vector2):
    somma_moduli=(math.sqrt((self.x**2)+(self.y**2)))+math.sqrt((vector2.x**2)+(vector2.y**2))
    return somma_moduli

  def somma_vettori(self,vector2):
    vettore_somma_x=self.x+vector2.x
    vettore_somma_y=self.y+vector2.y
    vettore_somma=[]
    vettore_somma.append(vettore_somma_x)
    vettore_somma.append(vettore_somma_y)
    return vettore_somma

vettore1=Vettore(3,4)
vettore2=Vettore(20,21)
print(Vettore.somma(vettore1,vettore2))
print(Vettore.somma_vettori(vettore1,vettore2))
print(Vettore.modulo(vettore1))