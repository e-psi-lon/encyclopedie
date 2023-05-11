encyclopedie = {
    "Sciences": {
        "info": "Choisissez parmi les différentes matières scientifiques",
        "Mathématiques": {
            "Équations": {
                "Racines": {
                    "info:":"Permet de calculer le/les racines d'une équation du second degré",
                    "function_to_call" : "def racines():\n\tdrawTxt(\"Résoudre l'équation ax^2+bx+c=0\", 0, 0)\n\tdrawTxt(\"a\",0,30)\n\ta = 0\n\twhile a == 0:\n\t\ta = cinput()\n\tdrawRect(0, 70, 340, 20, (255, 255, 255))\n\tdrawTxt(\"b\",0,30)\n\tb = cinput()\n\tdrawRect(0, 70, 340, 20, (255, 255, 255))\n\tdrawTxt(\"c\",0,30)\n\tc = cinput()\n\tdelta = b**2 - 4*a*c\n\tif delta > 0:\n\t\tx1 = -(-b**2 + math.sqrt(delta)) / (2*a)\n\t\tx2 = -(-b**2 - math.sqrt(delta)) / (2*a)\n\t\treturn \"Cette équation a pour delta :\\n \" + delta + \"\\n et pour racines : \\n\" + str(x1) + \"\\n\" + str(x2)\n\tif delta == 0:\n\t\tx = -b / (2*a)\n\t\treturn \"Cette équation a pour racine : \\n\" + str(x)\n\tif delta < 0:\n\t\treturn \"Cette équation n'a aucune \\nracine réelle.\""
                },
                "Discriminant": {
                    "info": "Permet de calculer le discriminant d'une équation du second degré",
                    # In one line using \n and \t
                    "function_to_call": "def discriminant():\n\tdrawTxt(\"Trouver le discriminant de l'équation ax^2+bx+c=0\", 0, 0)\n\tdrawTxt(\"a\",0,30)\n\ta = 0\n\twhile a == 0:\n\t\ta = cinput()\n\tdrawRect(0, 70, 340, 20, (255, 255, 255))\n\tdrawTxt(\"b\",0,30)\n\tb = cinput()\n\tdrawRect(0, 70, 340, 20, (255, 255, 255))\n\tdrawTxt(\"c\",0,30)\n\tc = cinput()\n\tdelta = b**2 - 4*a*c\n\treturn \"Cette équation a pour discriminant : \" + delta"
                },
                "Retour": {}
                
            },
            "Vecteurs": {
                "Norme": {
                    "Norme d'un vecteur": "Permet de calculer la norme d'un vecteur"
                },
                "Coordonnées": {
                    "Coordonnées d'un vecteur": "Permet de calculer les coordonnées d'un vecteur"
                }
            },
            "Retour": {}
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
        "Chimie": {},
        "Retour": {}
    },
    "Littéraire": {
        "Francais": {
            "Quelque Chose": {},
            "Retour": {}
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

def main():
    buttonInMenu = [["btn", app] for app in encyclopedie if type(encyclopedie[app]) != str]
    level = "encyclopedie/"
    level_content =  encyclopedie
    while True:
        print("Niveau : " + level)
        choice = int(input("Choix : "))
        if choice == len(buttonInMenu) - 1 and level != "encyclopedie/":
            levelsplit = level.split("/")
            levelsplit = levelsplit[1:-2]
            level = "encyclopedie/" + "/".join(levelsplit) + "/"
            level_content = encyclopedie
            for levels in levelsplit:
                level_content = level_content[levels]
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[app]) != str]
        if choice == len(buttonInMenu) - 1 and level == "encyclopedie/":
            break
        elif "function_to_call" in level_content[buttonInMenu[choice][1]].keys():
            exec(level_content[buttonInMenu[choice][1]]["function_to_call"])
            level = "encyclopedie/"
            level_content =  encyclopedie
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[app]) != str]
        else:
            level = level +  buttonInMenu[choice][1] + "/"
            level_content = level_content[buttonInMenu[choice][1]]
            buttonInMenu = [["btn", app] for app in level_content if type(level_content[app]) != str]
        

if __name__ == "__main__":
    main()