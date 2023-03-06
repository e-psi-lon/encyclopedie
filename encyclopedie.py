#créé par Colveri le 17/11/22
#Dernière màj par e_psi_lon le 01/02/23

#changelog (à partir du 24/01/23)
# Maintenant accessible depuis GitHub (https://github.com/e-psi-lon/encyclopedie)
# IMPORTS MODULES

import math
import time
from ion import *
from kandinsky import fill_rect as drawRect, draw_string as drawTxt



# Pour faire une meilleure interface


def menu(x,y,elements,col=(0,0,0),bg_col=(255,255,255)):
  def kd(x):
    if keydown(x):
      while keydown(x):pass
      return True
    return False
  kd(4)
  el_size,select,txt_size,draw=25,0,[0 for i in range(len(elements))],1
  while True:
    if kd(1):
      draw=1
      select=max(0,select-1)
    if kd(2):
      draw=1
      select=min(len(elements)-1,select+1)
    if kd(0):
      draw=1
      type=elements[select][0]
      if type=="sld":elements[select][-1]=max(elements[select][-1]-1,elements[select][2][0])
      if type=="lst":elements[select][-1]=max(elements[select][-1]-1,0)
    if kd(3):
      draw=1
      type=elements[select][0]
      if type=="sld":elements[select][-1]=min(elements[select][-1]+1,elements[select][2][1])
      if type=="lst":elements[select][-1]=min(elements[select][-1]+1,len(elements[select][2])-1)
    if kd(4) and elements[select][0]=="btn":
      break

    if draw:
      for nb,el in enumerate(elements):
        drawRect(x,y+el_size*nb,10*txt_size[nb],el_size,bg_col)
        slcted=1 if nb==select else 0
        type=el[0]
        name=el[1]
        val=el[-1]
        if type=="btn":disp_txt=name
        elif type=="sld":disp_txt=name+" : {}".format(val)
        elif type=="lst":disp_txt=name+" : {}".format(el[2][val])
        else : disp_txt="error"
        if slcted: disp_txt="> "+disp_txt
        txt_size[nb]=len(disp_txt)
        drawTxt(disp_txt,x,y+nb*el_size,col,bg_col)
        draw=0
  return elements[select][1],{x[1]:x[-1] for x in elements if x[0]!="btn"}

# Fonction detection touches
def cinput():
  value_to_edit=""
  while True:
    if keydown(KEY_ONE):
      value_to_edit = value_to_edit+"1"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_ONE): pass
    if keydown(KEY_TWO):
      value_to_edit = value_to_edit+"2"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_TWO): pass
    if keydown(KEY_THREE):
      value_to_edit = value_to_edit+"3"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_THREE): pass
    if keydown(KEY_FOUR):
      value_to_edit = value_to_edit+"4"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_FOUR): pass
    if keydown(KEY_FIVE):
      value_to_edit = value_to_edit+"5"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_FIVE): pass
    if keydown(KEY_SIX):
      value_to_edit = value_to_edit+"6"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_SIX): pass
    if keydown(KEY_SEVEN):
      value_to_edit = value_to_edit+"7"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_SEVEN): pass
    if keydown(KEY_EIGHT):
      value_to_edit = value_to_edit+"8"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_EIGHT): pass
    if keydown(KEY_NINE):
      value_to_edit = value_to_edit+"9"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_NINE): pass
    if keydown(KEY_ZERO) and len(value_to_edit)!=0 and value_to_edit[0]!="-":
      value_to_edit = value_to_edit+"0"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_ZERO): pass
    if len(value_to_edit)==0 and keydown(KEY_MINUS):
      value_to_edit = value_to_edit+"-"
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_MINUS): pass
    if keydown(KEY_DOT) and (not "." in value_to_edit):
      value_to_edit = value_to_edit+"."
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_DOT): pass
    if keydown(KEY_BACKSPACE) and len(value_to_edit)!=0:
      value_to_edit = value_to_edit[:len(value_to_edit)-1]
      drawRect(0,70,340,20,(255,255,255))
      drawTxt(value_to_edit,0,70)
      while keydown(KEY_BACKSPACE): pass
    if (keydown(KEY_OK) or keydown(KEY_EXE)):
      while keydown(KEY_OK) or keydown(KEY_EXE): pass
      if "." in value_to_edit:
        return float(value_to_edit)
      elif len(value_to_edit)==0:
        return 0
      else:
        return int(value_to_edit)


# DEF COMMANDES


# Maths
class Sciences:
  def __init__(self):
    drawTxt("Sciences :",0,0)
    Rangee = menu(0,30,[["btn","Mathématiques"],["btn","SVT"],["btn","Physique"],["btn","Chimie"],["btn","Retour"]])[0]
    drawRect(0,0,340,230,(255,255,255))
    if Rangee=="Mathématiques":
      Sciences.Maths()
    if Rangee=="SVT":
      Sciences.SVT()
    if Rangee=="Physique":
      Sciences.Physique
    if Rangee=="Retour":
      Main.colonne()
  class Physique():
    def __init__(self):
      Chapitre=menu(0,30,[["btn","ICIIIIIIIIIIIII"],["btn","Retour"]])[0]
      if Chapitre=="ICIIIIIIIIIIIII":
        drawTxt("! EN COURS DE CONSTRUCTION !",0,0)
        drawRect(0,0,340,230,(255,255,255))
        time.sleep(2)
      if Chapitre=="Retour":
        Sciences()
  class Maths:
    def __init__(self):
      drawTxt("Mathématiques :",0,0)
      Chapitre = menu(0,30,[["btn","Équations"],["btn","Vecteurs"],["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Équations":
          Sciences.Maths.Equation()
      elif Chapitre=="Vecteurs":
          Sciences.Maths.Vecteurs()
      elif Chapitre=="Retour":
        Sciences()
    class Equation:
      def __init__(self):
        drawTxt("Mathématiques/Équations :",0,0)
        Theme = menu(0,30,[["btn","Discriminant"],["btn","Retour"]])[0]
        drawRect(0,0,340,230,(255,255,255))
        if Theme=="Discriminant":
          drawRect(0,0,340,230,(255,255,255))
          drawTxt(Sciences.Maths.Function.discriminant(),0,0)
          drawRect(0,0,340,230,(255,255,255))
          time.sleep(3)
        if Theme=="Retour":
          Sciences.Maths()
    class Vecteurs:
      def __init__():
        pass
    class Function:
      def discriminant():
        drawTxt("Résoudre l'équation ax^2+bx+c=0",0,0)
        drawTxt("a",0,30)
        a=0
        while a==0: a=cinput()
        drawRect(0,70,340,20,(255,255,255))
        drawTxt("b",0,30)
        b=cinput()
        drawRect(0,70,340,20,(255,255,255))
        drawTxt("c",0,30)
        c=cinput()

        delta=b**2-4*a*c
        if delta>0:
          x1=-(-b**2+math.sqrt(delta))/(2*a)
          x2=-(-b**2-math.sqrt(delta))/(2*a)
          return "Cette équation à delta :\n "+delta+"\n et pour racines : \n"+str(x1)+"\n"+str(x2)
        if delta==0:
          x=-b/(2*a)
          return "Cette équation à pour racine : \n"+str(x)
        if delta<0:
          return "Cette équation n'à aucune \nracine réelle."


  # SVT

  class SVT:
    def __init__(self):
      drawTxt("SVT :",0,0)
      Chapitre = menu(0,30,[["btn","La Cellule"],["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="La Cellule":
        drawTxt("SVT/La Cellule",0,0)
        Theme = menu(0,30,[["btn","Théorie Cellulaire"],["btn","Retour"]])[0]
        drawRect(0,0,340,230,(255,255,255))
        if Theme=="Théorie Cellulaire":
          drawTxt(self.TheorieCellulaire(),0,0)
          time.sleep(5)
          drawRect(0,0,340,230,(255,255,255))
        if Theme=="Retour":
          drawTxt("SVT :",0,0)
          Chapitre = menu(0,30,[["btn","La Cellule"],["btn","Retour"]])[0]
          drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Retour":
        Main.colonne()

    def TheorieCellulaire(self):
      return "- Tout organisme vivant est\ncomposé d'une ou plusieurs\ncellules \n- La cellule est l'unité de\nstructure et de fonction du\nvivant \n- Toute cellule provient d'une\nautre cellule par division\ncellulaire"

  # Chimie
  class Chimie:
    def __init__(self) -> None:
      drawTxt("Chimie :",0,0)
      Chapitre = menu(0,30,[["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Retour":
        Sciences()

class Litteraire:
  def __init__(self):
    drawTxt("Litteraire :",0,0)
    Rangee = menu(0,30,[["btn","Francais"],["btn","Anglais"],["btn","Retour"]])[0]
    drawRect(0,0,340,230,(255,255,255))
    if Rangee=="Francais":
      Litteraire.Francais()
    if Rangee=="Anglais":
      Litteraire.Anglais()
    if Rangee=="Retour":
      Main.colonne()
  class Francais:
    def __init__(self):
      drawTxt("Litteraire/Francais :",0,0)
      Chapitre=menu(0,30,[["btn","Quelque Chose"],["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Quelque Chose":
        drawTxt("Quelque Chose :",0,0)
        Theme=menu(0,30,[["btn","Retour"]])[0]
        drawRect(0,0,340,230,(255,255,255))
        if Theme=="Retour":
          Litteraire()
  class Anglais:
    def __init__(self):
      drawTxt("Litteraire/Anglais :",0,0)
      Chapitre=menu(0,30,[["btn","Quelque Chose"],["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Quelque Chose":
        drawTxt("Quelque Chose :",0,0)
        Theme=menu(0,30,[["btn","Retour"]])[0]
        drawRect(0,0,340,230,(255,255,255))
        
      if Chapitre=="Retour":
        Litteraire()

class Autres:
  def __init__(self):
    drawTxt("Autres :",0,0)
    Rangee = menu(0,30,[["btn","Anniversaires"],["btn","Machin"],["btn","Bidule"],["btn","Credits"],["btn","Retour"]])[0]
    drawRect(0,0,340,230,(255,255,255))
    if Rangee=="Anniversaires":
      drawTxt("Autres/Anniversaires :",0,0)
      Chapitre=menu(0,30,[["btn","Lycée"],["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Lycée":
        drawTxt("Coco : 08/08/2005 \nFlo : 05/04/2006 \nLilian : 20/10/2006",0,0)
        time.sleep(2)
        drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Retour":
        Autres()
    if Rangee=="Credits":
      drawTxt("Autres/Credits :",0,0)
      Chapitre=menu(0,30,[["btn","Developers"],["btn","Retour"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Developers":
        drawTxt("Dev principal : Colveri \nDev secondaire : e_psi_lon",0,0)
        time.sleep(2)
        drawRect(0,0,340,230,(255,255,255))
      if Chapitre=="Retour":
        Autres()

    if Rangee=="Retour":
      Main.colonne()
class Main:
  def __init__(self):
    drawTxt("Bienvenue dans l'encyclopédie\nde Colveri.\nVous choisirez votre acces \nen utilisant\n les menus dédiés.\nAppuyez sur 1 ou OK pour\ncommencer ou HOME/RETOUR pour\nquitter",0,0)
    while True:
      if keydown(KEY_ONE) or keydown(KEY_OK):
        ouvrir = 1
        drawRect(0,0,340,230,(255,255,255))
        break
      elif keydown(KEY_BACK) or keydown(KEY_HOME):
        break
    if ouvrir==1 :
      Main.colonne()
  def colonne():
    """Permet de choisir où aller"""
    Colonne=""
    while Colonne!="Quitter":
      drawTxt("Aller à :",0,0)
      Colonne = menu(0,30,[["btn","Sciences"],["btn","Littéraire"],["btn","Autres"],["btn","Quitter"]])[0]
      drawRect(0,0,340,230,(255,255,255))
      if Colonne=="Sciences":
        Sciences()
      if Colonne=="Autres":
        Autres()
      if Colonne=="Littéraire":
        Litteraire()
      if Colonne=="Quitter":
        pass



try:
  Main()
  print("Exiting Program")
except:
  print("Bug Detected") 