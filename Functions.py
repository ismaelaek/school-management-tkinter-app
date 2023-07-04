import csv
from Classes import *
from datetime import *
import secrets
from prettytable import PrettyTable
ListFiliere,List_Attend,ListStgr,ToutsModules,ListFrmtr,ListeNotes=[],[],[],[],[],[]


# ####################

# M1=Module("Web Dynamique",1,2,"PA122")
# M2=Module("Programtion en JavaScript",1,1,"PA457")
# M3=Module("Algorithmique et Python",1,2,"PA789")
# M4=Module("Web Statique",1,1,"PA123")
# LM=[M1,M2,M3,M4]

# for m in LM:
#     ToutsModules.append(m)
# DD=Filiere("Developpement Digital","DD",LM)
# GE=Filiere("Gestion Des Entreprises","GE",LM)

# F1=Formateur('CIN1','Errhmaoui','Hassan',date(1998,8,23),LM)
# F2=Formateur('CIN2','Biad','Moustapha',date(1998,8,23),LM)
# LFO=[F1,F2]
# for f in LFO:
#     ListFrmtr.append(f)

# LF=[DD,GE]
# for f in LF:
#     ListFiliere.append(f)
# S1=Stagaire("PA2215",1,"Aloui","Hassnae",date(1998,8,23),LF,11.66,12.5)
# S2=Stagaire("PA2245",2,"Benghaith","Mohamed",date(1999,6,15),LF,11.58)
# S3=Stagaire("PA2875",1,"El Arabi","Jaouad",date(2002,6,26),LF,14.74)
# S4=Stagaire("PA2645",1,"ES-Samlali","Jassmine",date(2000,10,16),LF,14.98)
# S5=Stagaire("PA2240",1,"Ahmed","Mohsen",date(2004,8,20),LF,14.42)


# LA=[S1,S2,S3,S4,S5]
# for s in LA:
#     List_Attend.append(s)

# N1=Note(1,"PA2215",12.5,17.75,15.00)
# N2=Note(2,"PA2215",19.5,19.75,18.00)
# N3=Note(3,"PA2215",17.5,19.25,18.00)
# N4=Note(4,"PA2215",18.5,18.75,19.00)

# N5=Note(1,"PA2875",10,11.50,12.00)
# N6=Note(2,"PA2875",10,10,18.00)
# N7=Note(3,"PA2875",11.75,15.25,14.00)
# N8=Note(4,"PA2875",18.5,18.75,19.00)

# LN=[N1,N2,N3,N4,N5,N6,N7,N8]
# for n in LN:
#     ListeNotes.append(n)


####################


DA=date(2022,6,6)
file_Drctr="AuthDirectuere.csv"
file_Frmtr="AuthFormateurs.csv"
file_Stgr="AuthStagaires.csv"
def MenuStg():
    print("""
        #########################################
        #                  Menu                 #
        #---------------------------------------#
        # 1 | Inscrir                           #
        # 2 | Consulter notes                   #
        # 0 | Deconnexion                       #
        #                                       #
        #########################################
        """)
    
def MenuFrmtr():
    print("""
        #########################################
        #                  Menu                 #
        #---------------------------------------#
        # 1 | Aficher La liste des stagaires    #
        # 2 | Saisir notes                      #
        # 3 | Consulter les notes               #
        # 0 | Deconnexion                       #
        #                                       #
        #########################################
        """)
    
def MenuDrctr():
    print("""
        ############################################
        #                    Menu                  #
        #------------------------------------------#
        # 1  | Ajouter une filière                 #
        # 2  | Ajouter un stagaire                 #
        # 3  | Ajouter un formatuer                #
        # 4  | Aficher La liste des stagaires      #
        # 5  | Aficher La liste des formatuers     #
        # 6  | Suppremer un stagaire               #
        # 7  | Suppremer un formatuers             #
        # 8  | Calculer et Afficher les notes      #
        # 9  | Exporter les données dans des CSVs  #
        # 10 | Importer les données                #
        # 0  | Deconnexion                         #
        #                                          #
        ############################################
        """)

# fonction pour verifier si un stagaire est deja existe
def ExisteStgr(List,C):
    for stg in List:
        if stg.CIN == C:
            return True
    return False

# fonction pour verifier si un formatuer est deja existe
def ExisteFrmtr(C):
    for frmtr in ListFrmtr:
        if frmtr.CIN == C:
            return True
    return False

# fonction pour verifier si un module existe ou non
def ExisteModule(nom_mod):
    for mdl in ToutsModules:
        if mdl.Nom == nom_mod:
            return True
    return False

# fonction pour verifier si une filiere existe ou non
def ExisteFiliere(nom_fil):
    for flr in ListFiliere:
        if flr.Nom == nom_fil:
            return True
    return False

#################################
# Gestion des erreurs

def EntChoix(options,msg):
    while True:
        try:
            choix = int(input(msg))
            if choix in options:
                return choix
            else:
                print("Choix non valide")
        except (ValueError):
            print("Entrée invalide. Veuillez entrer un entier.")
            
def EntNoteFloat(msg):
    while True:
        try:
            N = float(input(msg))
            if N > 0 and N < 20:
                return N
            else:
                print("La valuer donnée non valide ")
        except (ValueError):
            print("Entrée invalide !!")
def EntDate(min,max,msg):
    while True:
        try:
            N = int(input(msg))
            if N >= min and N <= max:
                return N
            else:
                print("La valuer donnée non valide ")
        except (ValueError):
            print("Entrée invalide !!")
##################################

# fonction pour confiremer l'utilisateur
def confirmeUtl(User, Pass, File):
    global UtlActuel
    f = open(File, 'r')
    reader = csv.reader(f)
    for ligne in reader:
        if len(ligne) == 2:
            U, P = ligne[:2]
            if U == User and P == Pass:
                UtlActuel = User
                return True
    return False

# fonction pour verifier si l'age de stagaire est entre 15ans et 30 ans
def VerifierAge(DN,DA):
    age = int((DA - DN).days / 365.25)
    if age  < 30 and age > 15:
        return True
    else:
        return False
    
#  fonction pour ajouter un filiere
def AjouteFiliere():
    nom=input("Entrez nom de filiere :").title()
    while ExisteFiliere(nom):
        print("Un filiere avec ce nom est deja existe !!")
        nom=input("Entrez nom de filiere :").title()
    abbr=input("Entrez l'abbr de filiere :").upper()
    listMods=[]
    F=Filiere(nom,abbr)
    idFil=F.getid()
    print("Entrez les modules de", nom)
    for i in range(3):
        print("Entrez nom de module N°",i+1,end=":")
        Nom_mod=input().title()
        Coeff=EntChoix([1,2,3,4],"Entrez le coeffeciant de module (Max : 4): ")
        mod=Module(Nom_mod,idFil,Coeff)
        listMods.append(mod)
        
        ToutsModules.append(mod)
    F.ListModules=listMods
    ListFiliere.append(F)
    print(nom,"a été ajouté avec succée")
    
# function pour tries les stagaires par rapport au notes de bac
def getnote(obj):
    return obj.BacNote
# fonction pour accepter des stagaige que sont dans la liste d'attent
def AjoutStg():
    if List_Attend == []:
        print("La liste d'attent est vide")
    else :
        if len(ListStgr) <= 50:
            List_Attend.sort(key=getnote,reverse=True)
            for stg in List_Attend :
                print(stg)
                print("\n 1 | Accepter \t 2 | Refuser")
                option=[1,2]  
                choix=EntChoix(option,"Votre decision : ")
                
                if choix == 1 :
                    ListStgr.append(stg)
                    print("Vous avez accepté",stg.Nom,stg.Prenom)
                    file="AuthStagaires.csv"
                    F=open(file,'a')
                    ECV=csv.writer(F)
                    Pass = secrets.token_hex(5)
                    ECV.writerow([stg.CIN, Pass])
                    F.close()
                else :
                    print("Vous avez refusé",stg.Nom,stg.Prenom)
            for stg in List_Attend:
                for stag in ListStgr:
                    if stg.CIN == stag.CIN :
                        List_Attend.remove(stg)
        else :
            print("La list de stagaires est insuffisant")
            
# fonction pour personaliser la languer d'une chain de characters
def StrSpaces(text, total_length):
    spaces_needed = max(0, total_length - len(text))
    filled_text = text + " " * spaces_needed
    return filled_text

# fonction pour afficher tout le module en form d'un Menu 
def afficherModules(List):
    print("#"*40)
    for mod in List:
        print("#",StrSpaces(str(mod.getid()),3),"|",StrSpaces(mod.Nom,30),"#")
    print("#"*40)
#  fonction pour entrez la date de naissance
def SaisirDateNai():
    print("Entrez la date de naissance :")
    jj=EntDate(1,31,"Le Jour :")
    mm=EntDate(1,12,"Le Mois :")
    aaaa=EntDate(1950,2015,"L'Anné :")
    DN=date(aaaa,mm,jj)
    return DN

# fonction pour a jouter un formateur
def AjoutFrmtr():
    cin=input("Enrtez la CIN de formateur :").upper()
    while ExisteFrmtr(cin) == True:
        print("Le formateur est deja existe")
        cin=input("Enrtez un autre CIN :")
    nom=input("Entrez le nom de formateur :").title()
    prenom=input("Entrez le prenom de formateur :").title()
    DN=SaisirDateNai()
    print("Choisissez le (s) module (s) que le formatuer enseignera :")
    Form=Formateur(cin,nom,prenom,DN)
    listModFrmtr=[]
    options=[]
    for mod in ToutsModules:
        options.append(mod.getid())
        
    NM=EntChoix([1,2,3],"Nombre de module que ce formateur va enseigner (Max : 3): ")
    afficherModules(ToutsModules)
    
    for i in range(NM):
        print("Module",i+1,":")
        NumMod=EntChoix(options,"Entrez l'id de module a ajouter :")
        for mod in ToutsModules:
            if mod.getid()==NumMod:
                listModFrmtr.append(mod)
    Form.Modules=listModFrmtr
    ListFrmtr.append(Form)
    print(nom,prenom,"a été ajouté avec succée")
    # enregestrer les infos d'acces de le formateur 
    file="AuthFormateurs.csv"
    F=open(file,'a')
    ECV=csv.writer(F)
    Pass = secrets.token_hex(5)
    ECV.writerow([cin, Pass])
    F.close()

# fonction pour afficher tout les 
# stagaire en from d'un tableau
def AfficherStagaire():
    if ListStgr==[]:
        print("*"*30)
        print("Aucan stagaire a afficher !!")
        print("*"*30)
    else :
        table=PrettyTable(["CIN","Nom","Prenom","Date de naissance","Note de bac","Filiere"])
        for stg in ListStgr:
            table.add_row([stg.CIN,stg.Nom,stg.Prenom,str(stg.DateNai),stg.BacNote,stg.NomFil()])
        print(table)
def AfficherFormateurs():
    if ListFrmtr == []:
        print("*"*30)
        print("Aucan formateur a afficher !!")
        print("*"*30)
    else:
        table=PrettyTable(["CIN","Nom","Prenom","Date de naissance","Modules"])
        for frmtr in ListFrmtr:
            table.add_row([frmtr.CIN,frmtr.Nom,frmtr.Prenom,str(frmtr.DateNai),frmtr.NomModules()])
        print(table)
def SupremeStg():
    CIN=input("Entrez CIN de stagaire a suppremer: ")
    while ExisteStgr(ListStgr,CIN)==False:
        print("Stagaire n'existe pas!!")
        CIN=input("Entrez CIN de stagaire valide: ")
    for stg in ListStgr:
        if CIN ==stg.CIN:
            ListStgr.remove(stg)
    print("un stagaire a été suppremé avec succée")
    
def SupremeFrmtr():
    CIN=input("Entrez CIN de  formateur a suppremer: ")
    while ExisteStgr(CIN)==False:
        print(" formateur n'existe pas!!")
        CIN=input("Entrez CIN de formateur valide: ")
    for frmtr in ListFrmtr:
        if CIN ==frmtr.CIN:
            ListFrmtr.remove(frmtr)
    print("un stagaire a été suppremé avec succée")

def RetUserByCIN(cin,List):
    for ele in List:
        if ele.CIN==cin:
            return ele
    
def RetModuleByID(id):
    for ele in ToutsModules:
        if ele.getid()==id:
            return ele

def CalculeNotes(cin):
    NoteGeneral = 0
    Coeff = 0
    for Note in ListeNotes:
        if cin == Note.CIN_stgr:
            NG = Note.MoyenModule()
            CO = RetModuleByID(Note.id_mod).Coeff
            NoteGeneral += NG * CO
            Coeff += CO
    if Coeff != 0:
        MoyenGenerale = round(NoteGeneral / Coeff, 2)
    else:
        MoyenGenerale = 0
    RetUserByCIN(cin, ListStgr).MoyGeneral = MoyenGenerale

def AfficherNotes():
    for stg in ListStgr:
        CalculeNotes(stg.CIN)
    
    table=PrettyTable(["CIN","Nom et Prenom","Filiere","Moyenne Generale"])
    for stg in ListStgr:
        table.add_row([stg.CIN,stg.Nom+" "+stg.Prenom,stg.NomFil(),stg.MoyGeneral])
    print(table)

def SaisirNotes():
    ModulesDeFrmtr=RetUserByCIN(UtlActuel,ListFrmtr).Modules
    afficherModules(ModulesDeFrmtr)
    options=[]
    for mod in ModulesDeFrmtr:
        options.append(mod.getid())
    choix=EntChoix(options,"Entrez le module que vous voullez saisir les notes :")
    module=RetModuleByID(choix)
    print("Vous avez choisé le module",module.Nom)
    fil=module.id_fil
    for stg in ListStgr:
        if stg.idFil == fil :
            print("Saisir le note de",stg.Nom)
            C1=EntNoteFloat("Entrez la note de 1ere controle :")
            
            C2=EntNoteFloat("Entrez la note de 2éme controle :")
            
            EFM=EntNoteFloat("Entrez la note de l'EFM :")
            
            N=Note(module.getid(),stg.CIN,C1,C2,EFM)
            ListeNotes.append(N)
            
def ConsulterNoteFr():
    ModulesDeFrmtr=RetUserByCIN(UtlActuel,ListFrmtr).Modules
    fils=set()
    for module in ModulesDeFrmtr:
        fils.add(module.id_fil)
    table=PrettyTable([["CIN","Nom et Prenom","Filiere","Moyenne Generale"]])
    for stg in ListStgr:
        if stg.idFil in fils:
            table.add_row([stg.CIN,stg.Nom+" "+stg.Prenom,stg.NomFil(),stg.MoyGeneral])
    print(table)
    
def retModByName(name):
    for mod in ToutsModules:
        if mod.Nom == name:
            return mod
        
def Inscription():
    DN=SaisirDateNai()
    DA=date(2023,9,10)
    if VerifierAge(DN,DA)== False :
        print("Vous ne peuvent pas iscrir !!")
    else:
        C = input("Entrez CIN: ").upper()
        while ExisteStgr(ListStgr,C) or ExisteStgr(List_Attend,C):
            print("Ce CIN est deja existe !!")
            C= input("Entrez votre CIN")
        N = input("Entrez votre nom: ").title()
        P = input("Entrez votre prnom: ").title()
        BacNote = EntNoteFloat("Enter la note de bac: ")

        options=[]
        print("########## LES FILIERES ##########")
        print("#"*40)
        for filiere in ListFiliere:
            options.append(filiere.getid())
            print("#",StrSpaces(str(filiere.getid()),3),"|",StrSpaces(filiere.Nom,30),"#")
        print("#"*40)
        
        fil = EntChoix(options,"Choiser une filiere: ")
        stagaire = Stagaire(C,fil, N, P, DN, ListFiliere, BacNote)
        List_Attend.append(stagaire)
        print("Vous avez inscré avec succée")
        # enregestrer les infos d'acces de le stagaire 
        

def ConsulterNoteStgr():
    cin=input("Entrez le CIN d'utilisatuer : ").upper()
    if ExisteStgr(cin):
        Pass=input("Entrez le mot de pass : ")
        if  confirmeUtl(cin,Pass,file_Stgr):
            print("Mon Notes:")
            table=PrettyTable(["Module","1er Control","2ém Control","EFM","Moyenne de module"])
            for note in ListeNotes:
                if note.CIN_stgr == UtlActuel:
                    module = RetModuleByID(note.id_mod)
                    table.add_row([module.Nom,note.PrControl,note.DeControl,note.EFM,round(note.MoyenModule(),2)])
            print(table)
        else:
            print("Mot de pass non valide!")
    else :
        print("Aucun stagire avec ce CIN !!")

def Exportation():
    File_filieres=open("Data/Filieres.csv","a")
    FilWriter=csv.writer(File_filieres, delimiter=",")
    for fil in ListFiliere:
        FilWriter.writerow([fil.Nom,fil.Abr])
        
    File_Modules=open("Data/Modules.csv","a")
    ModWriter=csv.writer(File_Modules, delimiter=",")
    for mod in ToutsModules:
        ModWriter.writerow([mod.getid(),mod.Nom, mod.id_fil,mod.Coeff,mod.CINFrmtr])
        
    File_Stagaires=open("Data/Stagaires.csv","a")
    StgWriter=csv.writer(File_Stagaires, delimiter=",")
    for stg in ListStgr:
        StgWriter.writerow([stg.CIN,stg.Nom, stg.Prenom,stg.DateNai,stg.idFil,stg.BacNote])
        
    stgAttent=open("Data/StgsEnAttent.csv","a")
    StgWriter=csv.writer(stgAttent, delimiter=",")
    for stg in List_Attend:
        StgWriter.writerow([stg.CIN,stg.Nom, stg.Prenom,stg.DateNai,stg.idFil,stg.BacNote])
        
    File_Formatuer=open("Data/Formateurs.csv","a")
    FrmtWriter=csv.writer(File_Formatuer, delimiter=",")
    for frmtr in ListFrmtr:
        FrmtWriter.writerow([frmtr.CIN,frmtr.Nom, frmtr.Prenom,frmtr.DateNai,frmtr.AfficheNomMods()])
        
    File_Notes=open("Data/Notes.csv","a")
    NoteWriter=csv.writer(File_Notes, delimiter=",")
    for note in ListeNotes:
        NoteWriter.writerow([note.id_mod,note.CIN_stgr,note.PrControl,note.DeControl,note.EFM,note.MoyenModule()])
    print("Touts le données ont été exporté avec succeé ")

def ImportDate(str):
    DNai = datetime.strptime(str, "%Y-%M-%d").date()
    return DNai

def Importation():
    with open("Data/Filieres.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 2:
                N, Abr = info[0], info[1]
                ListFiliere.append(Filiere(N, Abr))
    

    with open("Data/Modules.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 4:
                N, idfil, Coeff, CinF = info[0], info[1], info[2], info[3]
                ToutsModules.append(Module(N, int(idfil), int(Coeff), CinF))
                

    with open("Data/Stagaires.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                ListStgr.append(Stagaire(C, int(idF), N, P, DN, ListFiliere, BN))
    

    with open("Data/Notes.csv","r") as Notesfile:
        for line in Notesfile:
            info = line.strip().split(",")
            if len(info) == 5:
                idM,Cstg,C1,C2,EFM= info[0],info[1],info[2],info[3],info[4]
                ListeNotes.append(Note(int(idM),Cstg,float(C1),float(C2),float(EFM)))
    

    
    with open("Data/StgsEnAttent.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                List_Attend.append(Stagaire(C, int(idF), N, P, DN, ListFiliere, float(BN)))
    
    
    with open("Data/Formateurs.csv","r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 5:
                C,N,P= info[0],info[1],info[2]
                DN = ImportDate(info[3])
                NomMods=info[4].strip().split("-")
                NomMods = list(filter(lambda x: x != "", NomMods))
                listMods=[]
                for nom in NomMods:
                    mod=retModByName(nom.strip())
                    if mod.CINFrmtr == C:
                        listMods.append(mod)
                ListFrmtr.append(Formateur(C,N,P,DN,listMods))
    print("Touts le données valides ont été importés avec succeé ")
