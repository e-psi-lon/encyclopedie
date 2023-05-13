# créé par Colveri le 17/11/22
# Dernière màj par Colveri le 14/03/23

# changelog (à partir du 13/05/23) Maintenant accessible depuis GitHub (https://github.com/e-psi-lon/encyclopedie)
# Version retravaillée pour être plus facilement modifiable, maintenant seule version maintenue (encylopedie.py est
# obsolète et ne sera plus maintenue mais reste disponible sur GitHub dans les anciens commits (et encore maintenant
# ici car je laisse au cas où)) IMPORTS MODULES

import math
import time
from ion import *
from kandinsky import fill_rect as drawRect, draw_string as drawTxt


# Pour faire une meilleure interface

def kd(key):
    if keydown(key):
        while keydown(key):
            pass
        return True
    return False


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


def cinput():
    value_to_edit = ""
    while True:
        if kd(KEY_ONE):
            value_to_edit = value_to_edit + "1"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_TWO):
            value_to_edit = value_to_edit + "2"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_THREE):
            value_to_edit = value_to_edit + "3"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_FOUR):
            value_to_edit = value_to_edit + "4"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_FIVE):
            value_to_edit = value_to_edit + "5"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_SIX):
            value_to_edit = value_to_edit + "6"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_SEVEN):
            value_to_edit = value_to_edit + "7"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_EIGHT):
            value_to_edit = value_to_edit + "8"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_NINE):
            value_to_edit = value_to_edit + "9"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_ZERO) and len(value_to_edit) != 0 and value_to_edit[0] != "-":
            value_to_edit = value_to_edit + "0"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if len(value_to_edit) == 0 and kd(KEY_MINUS):
            value_to_edit = value_to_edit + "-"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_DOT) and ("." not in value_to_edit):
            value_to_edit = value_to_edit + "."
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_BACKSPACE) and len(value_to_edit) != 0:
            value_to_edit = value_to_edit[:len(value_to_edit) - 1]
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_OK) or kd(KEY_EXE):
            if "." in value_to_edit:
                return float(value_to_edit)
            elif len(value_to_edit) == 0:
                return 0
            else:
                return int(value_to_edit)


encyclopedie = {
    "Sciences": {
        "info": "Sciences :",
        "type": "btn",
        "Mathématiques": {
            "info": "Mathématiques :",
            "type": "btn",
            "Équations": {
                "Discriminant": "Permet de calculer le discriminant d'une équation du second degré"
            },
            "Vecteurs": {
                "Norme": {
                    "Norme d'un vecteur": "Permet de calculer la norme d'un vecteur"
                },
                "Coordonnées": {
                    "Coordonnées d'un vecteur": "Permet de calculer les coordonnées d'un vecteur"
                }
            }
        },
        "SVT": {
            "La Cellule": {
                "Théorie Cellulaire": "Permet de connaitre la théorie cellulaire"
            }
        },
        "Physique": {
            "La Lumière": {
                "Colorimétrie": {
                    "Synthèse additive": "Permet de connaitre la synthèse additive",
                    "Synthèse soustractive": "Permet de connaitre la synthèse soustractive"
                }
            }
        },
        "Chimie": {}
    },
    "Littéraire": {
        "Francais": {
            "Quelque Chose": {}
        },
        "Anglais": {
            "Quelque Chose": {}
        }
    },
    "Autres": {
        "Anniversaires": {
            "Lycée": {
                "info": "Coco : 08/08/2005 \nFlo : 05/04/2006 \nLilian : 20/10/2006"
            }
        },
        "Machin": {},
        "Bidule": {},
        "Credits": {
            "Developers": {}
        }
    },
    "Quitter": {}
}


def __init__():
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
    drawRect(0, 0, 340, 230, (255, 255, 255))
    drawTxt("Aller à :", 0, 0)
    buttonInMenu = [["btn", app] for app in encyclopedie]
    level = "encyclopedie/"
    level_content = encyclopedie
    while True:
        drawRect(0, 0, 340, 230, (255, 255, 255))
        if "info" in level_content:
            drawTxt(level_content["info"], 0, 0)
        else:
            drawTxt("Aller à :", 0, 0)
        choice = menu(0, 30, buttonInMenu)[0]
        drawRect(0, 0, 340, 230, (255, 255, 255))
        indice = [i for i in range(len(buttonInMenu)) if buttonInMenu[i][1] == choice][0]
        drawRect(0, 0, 340, 230, (255, 255, 255))
        if choice == "Retour":
            levelsplit = level.split("/")
            levelsplit = levelsplit[1:-2]
            level = "encyclopedie/" + "/".join(levelsplit) + "/"
            level_content = encyclopedie
            for levels in levelsplit:
                level_content = level_content[levels]
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[app]) != str]
        elif choice == "Quitter":
            break
        elif "function_to_call" in level_content[buttonInMenu[indice][1]]:
            exec(level_content[buttonInMenu[indice][1]]["function_to_call"])
            level = "encyclopedie/"
            level_content = encyclopedie
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[app]) != str]
        else:
            level = level + buttonInMenu[indice][1] + "/"
            level_content = level_content[buttonInMenu[indice][1]]
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[app]) != str]


if __name__ == "__main__":
    __init__()
    """try:
        __init__()
        print("Fermeture de l'encyclopédie")
    except Exception as e:
        print("Erreur : " + str(e))
        print("Fermeture de l'encyclopédie")"""
