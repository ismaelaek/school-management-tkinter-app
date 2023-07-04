from Classes import *
from Functions import *
from datetime import date

while True:
    print(
        """
        #########################################
        #            Entrez Comme :             #
        #---------------------------------------#
        # 1 | Directuer                         #
        # 2 | Formatuer                         #
        # 3 | Stagaire                          #
        #---------------------------------------#
        # 0 | Quitter le programme              #
        #                                       #
        #########################################
        """
    )
    options=[0,1,2,3]
    utl=EntChoix(options,"Entrez votre choix :")
    if utl == 1:
        user=input("Entrez le nom d'utilisatuer : ")
        Pass=input("Entrez le mot de pass : ")
        fois=0
        while confirmeUtl(user,Pass,file_Drctr)==False:
            print("Nom d'utilisatuer ou mot de pass non valide !!")
            user=input("Entrez le nom d'utilisatuer : ")
            Pass=input("Entrez le mot de pass : ")
        while True:
            MenuDrctr()
            options=[0,1,2,3,4,5,6,7,8,9,10]
            choix=EntChoix(options,"Entrez votre choix :")
            if choix == 1:  
                AjouteFiliere()
            elif choix == 2:
                AjoutStg()
            elif choix == 3:
                AjoutFrmtr()
            elif choix == 4:
                AfficherStagaire()
            elif choix == 5:
                AfficherFormateurs()
            elif choix == 6:
                SupremeStg()
            elif choix == 7:
                SupremeFrmtr()
            elif choix == 8:
                AfficherNotes()
            elif choix == 9:
                Exportation()
            elif choix == 10:
                Importation()
            else:
                break
    elif utl == 2:
        cin=input("Entrez le CIN d'utilisatuer : ").upper()
        Pass=input("Entrez le mot de pass : ")
        while  confirmeUtl(cin,Pass,file_Frmtr)==False:
            cin=input("Entrez un CIN valide !!! : ")
            Pass=input("Entrez le mot de pass : ")
        while True:
            MenuFrmtr()
            options=[0,1,2,3]
            choix=EntChoix(options,"Entrez votre choix :")
            if choix == 1:
                AfficherStagaire()
            elif choix == 2:
                SaisirNotes()
            elif choix == 3:
                ConsulterNoteFr()
            else:
                print("Au revoir !!")
                break
    elif utl == 3:
        while True:
            MenuStg()
            options=[0,1,2]
            choix=EntChoix(options,"Entrez votre choix :")
            if choix == 1:
                Inscription()
            elif choix == 2:
                ConsulterNoteStgr()
            else:
                print("Au revoir !!")
                break
    elif utl == 0:
        break
    else:
        print("Choix non valide")

