# créé par Colveri le 17/11/22
# Dernière màj par Colveri le 14/03/23

# changelog (à partir du 13/05/23) Maintenant accessible depuis GitHub (https://github.com/e-psi-lon/encyclopedie)
# Version retravaillée pour être plus facilement modifiable, maintenant seule version maintenue (encylopedie.py est
# obsolète et ne sera plus maintenue mais reste disponible sur GitHub dans les anciens commits (et encore maintenant
# ici car je laisse au cas où)) 

# Importer les libs
import math
import time
from ion import *
from kandinsky import fill_rect as drawRect, draw_string as drawTxt


# Detection de pression de touche custom pour éviter le spam
def kd(key):
    if keydown(key):
        while keydown(key):
            pass
        return True
    return False


# Fonction pour faire les menus de l'interface utilisateur
def menu(x, y, elements, col=(0, 0, 0), bg_col=(255, 255, 255)):
    kd(4)
    el_size, select, txt_size, draw = 25, 0, [0 for _ in range(len(elements))], 1
    while True:
        if kd(1):
            draw = 1
            select = max(0, select - 1)
        if kd(2):
            draw = 1
            select = min(len(elements) - 1, select + 1)
        if kd(0):
            draw = 1
            elem_type = elements[select][0]
            if elem_type == "sld":
                elements[select][-1] = max(elements[select][-1] - 1, elements[select][2][0])
            if elem_type == "lst":
                elements[select][-1] = max(elements[select][-1] - 1, 0)
        if kd(3):
            draw = 1
            elem_type = elements[select][0]
            if elem_type == "sld":
                elements[select][-1] = min(elements[select][-1] + 1, elements[select][2][1])
            if elem_type == "lst":
                elements[select][-1] = min(elements[select][-1] + 1, len(elements[select][2]) - 1)
        if kd(4) and elements[select][0] == "btn":
            break

        if draw:
            for nb, el in enumerate(elements):
                drawRect(x, y + el_size * nb, 10 * txt_size[nb], el_size, bg_col)
                slcted = 1 if nb == select else 0
                elem_type = el[0]
                name = el[1]
                val = el[-1]
                if elem_type == "btn":
                    disp_txt = name
                elif elem_type == "sld":
                    disp_txt = name + " : {}".format(val)
                elif elem_type == "lst":
                    disp_txt = name + " : {}".format(el[2][val])
                else:
                    disp_txt = "error"
                if slcted:
                    disp_txt = "> " + disp_txt
                txt_size[nb] = len(disp_txt)
                drawTxt(disp_txt, x, y + nb * el_size, col, bg_col)
                draw = 0
    return elements[select][1], {x[1]: x[-1] for x in elements if x[0] != "btn"}


# Fonction input mais custom pour fonctionner via une interface kandinsky et non la console
def cinput(x1, y1, x2, y2):
    value_to_edit = ""
    while True:
        if kd(KEY_ONE):
            value_to_edit = value_to_edit + "1"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_TWO):
            value_to_edit = value_to_edit + "2"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_THREE):
            value_to_edit = value_to_edit + "3"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_FOUR):
            value_to_edit = value_to_edit + "4"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_FIVE):
            value_to_edit = value_to_edit + "5"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_SIX):
            value_to_edit = value_to_edit + "6"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_SEVEN):
            value_to_edit = value_to_edit + "7"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_EIGHT):
            value_to_edit = value_to_edit + "8"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_NINE):
            value_to_edit = value_to_edit + "9"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_ZERO) and len(value_to_edit) != 0 and value_to_edit[0] != "-":
            value_to_edit = value_to_edit + "0"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if len(value_to_edit) == 0 and kd(KEY_MINUS):
            value_to_edit = value_to_edit + "-"
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_DOT) and ("." not in value_to_edit):
            value_to_edit = value_to_edit + "."
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_BACKSPACE) and len(value_to_edit) != 0:
            value_to_edit = value_to_edit[:len(value_to_edit) - 1]
            drawRect(x1, y1, x2 - x1, y2 - y1, (255, 255, 255))
            drawTxt(value_to_edit, x1, y1)
        if kd(KEY_OK) or kd(KEY_EXE):
            if "." in value_to_edit:
                return float(value_to_edit)
            elif len(value_to_edit) == 0:
                return 0
            else:
                return int(value_to_edit)


# Fonction pour les racines (j'ai pas encore trouvé d'autres moyens)
# TODO: Trouver une méthode plus adéquate
def racines():
    drawTxt("Résoudre l'équation ax^2+bx+c=0", 0, 0)
    drawTxt("a", 0, 30)
    a = 0
    while a == 0:
        a = cinput(x1=0, y1=70, x2=340, y2=90)
    drawRect(0, 70, 340, 20, (255, 255, 255))
    drawTxt("b", 0, 30)
    b = cinput(x1=0, y1=70, x2=340, y2=90)
    drawRect(0, 70, 340, 20, (255, 255, 255))
    drawTxt("c", 0, 30)
    c = cinput(x1=0, y1=70, x2=340, y2=90)
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return "Cette équation a pour delta :\n " + delta + "\n et pour racines : \n" + str(
            (-b + math.sqrt(delta)) / (2 * a)) + "\n" + str((-b - math.sqrt(delta)) / (2 * a))
    elif delta == 0:
        return "Cette équation a pour racine : \n" + str(-b / (2 * a))
    elif delta < 0:
        return "Cette équation n'a aucune \nracine réelle."


# Idem que ci dessus
def discriminant():
    drawTxt("Trouver le discriminant de\nl'équation ax^2+bx+c=0", 0, 0)
    drawTxt("a", 0, 40)
    a = 0
    while a == 0:
        a = cinput(x1=0, y1=70, x2=340, y2=90)
    drawRect(0, 70, 340, 20, (255, 255, 255))
    drawTxt("b", 0, 40)
    b = cinput(x1=0, y1=70, x2=340, y2=90)
    drawRect(0, 70, 340, 20, (255, 255, 255))
    drawTxt("c", 0, 40)
    c = cinput(x1=0, y1=70, x2=340, y2=90)
    return "Cette équation a pour\n" \
           "discriminant : " + str(b ** 2 - 4 * a * c)


# Dictionnaire qui définit tout les éléments de l'encyclopédie
encyclopedie = {
    "Sciences": {
        "info": "Sciences :",
        "Mathématiques": {
            "info": "Mathématiques :",
            "Équations": {
                "info": "Équations :",
                "Racines": {
                    "function_to_call": racines
                },
                "Discriminant": {
                    "function_to_call": discriminant
                },
                "Retour": {}

            },
            "Vecteurs": {
                "info": "Vecteurs :",
                "Norme": {
                    "function_to_call": lambda: "Permet de calculer la norme d'un vecteur"
                },
                "Coordonnées": {
                    "function_to_call": lambda: "Permet de calculer les coordonnées d'un vecteur"
                },
                "Retour": {}
            },
            "Retour": {}
        },
        "SVT": {
            "info": "SVT :",
            "La Cellule": {
                "info": "La Cellule :",
                "Théorie Cellulaire": {
                    "function_to_call": lambda: "Permet de connaitre la théorie cellulaire"
                },
                "Retour": {}
            },
            "Retour": {}
        },
        "Physique": {
            "info": "Physique :",
            "La Lumière": {
                "info": "La Lumière :",
                "Colorimétrie": {
                    "info": "Colorimétrie :",
                    "Synthèse additive": {
                        "function_to_call": lambda: "Permet de connaitre la synthèse additive"
                    },
                    "Synthèse soustractive": {
                        "function_to_call": lambda: "Permet de connaitre la synthèse soustractive"
                    },
                    "Retour": {}
                },
                "Retour": {}
            },
            "Retour": {}
        },
        "Chimie": {},
        "Retour": {}
    },
    "Littéraire": {
        "info": "Littéraire :",
        "Francais": {
            "info": "Francais :",
            "Quelque Chose": {},
            "Retour": {}
        },
        "Anglais": {
            "info": "Anglais :",
            "Quelque Chose": {},
            "Retour": {}
        },
        "Retour": {}
    },
    "Autres": {
        "info": "Autres :",
        "Anniversaires": {
            "info": "Anniversaires :",
            "Lycée": {
                "info": "Coco : 08/08/2005 \nFlo : 05/04/2006 \nLilian : 20/10/2006"
            }
        },
        "Machin": {},
        "Bidule": {},
        "Credits": {
            "info": "Credits :",
            "Developers": {
                "function_to_call": lambda: drawTxt(
                    "Colveri : developpeur principal \ne_psi_lon : developpeur secondaire", 0, 0)
            },
        },
        "Retour": {}
    },
    "Quitter": {}
}


def __init__():
    # Message d'ouverture + début script
    drawTxt("Bienvenue dans l'encyclopédie\nde Colveri.\nVous choisirez votre acces \nen utilisant\n les menus "
            "dédiés.\nAppuyez sur 1 ou OK pour\ncommencer ou HOME/RETOUR pour\nquitter", 0, 0)
    while True:
        if kd(KEY_ONE) or kd(KEY_OK):
            ouvrir = 1
            drawRect(0, 0, 340, 230, (255, 255, 255))
            break
        elif kd(KEY_BACK) or kd(KEY_HOME):
            ouvrir = 0
            break
    if ouvrir == 1:
        main()


def main():
    buttonInMenu = [["btn", app] for app in encyclopedie]  # Définition des différents boutons du prochain menu
    level = "encyclopedie/"  # Niveau de base dans l'encyclopédie (équivalent à dossier, sous-dossier), ici niveau 0
    level_content = encyclopedie  # Contenu du niveau (de base à l'entièreté de l'encyclopédie)
    while True:  # On boucle à l'infini
        drawRect(0, 0, 340, 230, (255, 255, 255))  # On réinitialise l'interface
        if "info" in level_content:  # On vérifie si il y a un champ info dans le niveau actuel
            drawTxt(str(level_content["info"]), 0, 0)  # Si oui on l'affiche
        else:
            drawTxt("Aller à :", 0, 0)  # Sinon on affiche un message de base
        choice = menu(0, 30, buttonInMenu)[0]  # Ici on prend le choix de l'utilisateur
        drawRect(0, 0, 340, 230, (255, 255, 255))  # Réinitialisation de l'interface (encore)
        indice = [i for i in range(len(buttonInMenu)) if buttonInMenu[i][1] == choice][
            0]  # En vrai ici un .index() devrait suffir mais ne tentons pas le diable
        if choice == "Retour":  # Si c'est retour
            levelsplit = level.split(
                "/")  # On divise level en une liste qui ressemble à ca, par exemple : ["encyclopedie", "Sciences",
            # "Mathématiques", ""]
            levelsplit = levelsplit[
                         1:-2]  # On enlève la partie encyclopédie l'élément vide et le précédent (on remonte d'un
            # niveeau) ce qui donne dans l'exemple précédent ["Sciences"]
            level = "encyclopedie/" + "/".join(
                levelsplit) + "/"  # On redéfinit level (dans l'exemple "encyclopedie/Sciences/")
            level_content = encyclopedie  # On revient au niveau 0 du contenu
            for levels in levelsplit:  # On boucle sur chaque élément de levelsplit
                level_content = level_content[levels]  # Et on précise à chaque itération
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[
                                                                              app]) != str]  # On refait la liste des
            # boutons du menu (si on vérifie le type c'est pour éviter de mettre les infos)
        elif choice == "Quitter":  # Si c'est quitter
            break  # On casse la boucle et bye bye
        elif "function_to_call" in level_content[buttonInMenu[indice][1]]:  # Si il y a une fonction à éxécuter (
            # uniquement au niveau le plus bas possible)
            # Le commentaire suivant est pour éviter que PyCharm m'affiche une erreur alors qu'au lancemment du script
            # tout fonctionne
            # noinspection PyCallingNonCallable
            result = level_content[buttonInMenu[indice][1]]["function_to_call"]()  # On l'éxécute et on récupère le
            # résultat
            drawTxt(result, 0, 0)  # On affiche
            time.sleep(5)  # On attends pour laisser le temps de lire
            level = "encyclopedie/"  # Retour au niveau 0
            level_content = encyclopedie  # Idem mais en terme de contenu
            buttonInMenu = [["btn", app] for app in encyclopedie]  # Et enfin pour les boutons du menu
        else:  # Si aucun des cas précédents, alors c'est qu'on descend d'un niveau ce qui donne
            if len(level_content[buttonInMenu[indice][1]]) == 0:  # Si la page est vide
                level = "encyclopedie/"  # On retourne au niveau 0
                level_content = encyclopedie  # Idem
                buttonInMenu = [["btn", app] for app in encyclopedie]  # Et voilà
            else:  # Si il y a du contenu (le seul autre cas possible)
                level = level + buttonInMenu[indice][
                    1] + "/"  # On ajoute au niveau le nom de l'élément (exemple : on est dans Sciences on va dans
                # SVT ça donne "encyclopedie/Sciences/SVT/")
                level_content = level_content[buttonInMenu[indice][1]]  # La même mais en terme de contenu
                buttonInMenu = [["btn", app] for app in level_content if
                                type(level_content[app]) != str]  # Et pour les boutons


if __name__ == "__main__":  # Verification qu'on n'est pas un module mais bien le fichier principal
    """try:  # On essaye de lancer le programme
        __init__()  # Voilà
        print("Fermeture de l'encyclopédie")  # Quand on fermera on aura ça
    except Exception as e:  # En cas d'erreur
        print("Erreur : " + str(
            e) + "\nMerci de le report sur https://github.com/e-psi-lon/encyclopedie/issues")  # On donne l'erreur et
        # on donne un endroit ou le report
        print("Fermeture de l'encyclopédie")  # Et on dit que l'encyclopedie est fermée"""
    __init__()
