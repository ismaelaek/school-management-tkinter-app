from tkinter import *
from tkinter import ttk,messagebox
from Classes import *
from Functions import *
from datetime import *
import time
import secrets


file_Drctr="AuthDirectuere.csv"
file_Frmtr="AuthFormateurs.csv"
file_Stgr="AuthStagaires.csv"

def MenuPrincipale(fen,frame=None):
    if frame:
        frame.destroy()
    LogFrame=Frame(fen)
    LogFrame.pack()
    MsgLog=Label(LogFrame, text="Entrer comme :", font="Bahnschrift 16 bold", fg="#22B9A8")
    MsgLog.pack(pady=10)
    optionsLog=["Directeur","Formateur","Stagiaire"]
    for i in range(len(optionsLog)):
        if i==1:
            bg="#1199B7"
        else:
            bg="#22B9A8"
        BT = Button(LogFrame, text=optionsLog[i].upper(), font="times 20 bold ", fg="white", bg=bg,width=25,
                    command= lambda a=i : OperationLog(fen, LogFrame, optionsLog[a]))
        BT.pack(pady=10)
    Exit = Button(LogFrame, text="Quitter", font="times 20 bold ", fg="white", bg="#ffa245",width=15,
                    command= exit, border=0)
    Exit.pack(pady=25)

def OperationLog(fen, FM, opt):
    FM.destroy()
    if opt == "Directeur":
        afficherFrameConnexion(fen, opt)
    elif opt == "Formateur":
        afficherFrameConnexion(fen, opt)
    else:
        afficherFrameConnexion(fen, opt)

def afficherFrameConnexion(fen, opt,frame=None):
    if frame:
        frame.destroy()
    frameLogin = Frame(fen, padx=5, pady=5)
    frameLogin.pack(pady=10)
    labelMsg=Label(frameLogin, text="Merci de connexion d'abord !", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=2)
    if opt=="Stagiaire":
        formLogin(frameLogin,fen,opt)
        
        labeInsc = Label(frameLogin, text=" Vous n'avez inscré ? ", font="Bahnschrift 16 bold", fg="#22B9A8",width=30)
        labeInsc.grid(row=6, column=0,columnspan=2, pady=5)
        
        Inscrir = Button(frameLogin, text="Inscrir", font="times 16 bold", width=34 ,fg="white", bg="#22B9A8",command= lambda : inscrptionFrame(frameLogin,fen,opt))
        Inscrir.grid(row=7, column=0, columnspan=2, pady=5)
    else:
        formLogin(frameLogin,fen,opt)
        
        
def formLogin(frameLogin,fen,user):
    global entUser, entPass
    labeUser = Label(frameLogin, text="Nom d'utilisateur : ", font="Times 12")
    labeUser.grid(row=1, column=0, pady=5, sticky=NW)
    
    entUser = Entry(frameLogin,font="times 20 ", width=30, border=0)
    entUser.grid(row=2, column=0,columnspan=2,pady=5, sticky=NW)
    
    labePass = Label(frameLogin, text="Mot de pass : ", font="Times 12")
    labePass.grid(row=3, column=0, pady=5, sticky=NW)
    
    entPass = Entry(frameLogin,font="times 20 ", width=30, border=0, show="*")
    entPass.grid(row=4, column=0,columnspan=2, pady=5, sticky=NW)
    
    annuler = Button(frameLogin, text="Annuler", font="times 16 bold",width=15 , fg="white", bg="#ffa245",command=lambda : MenuPrincipale(fen,frameLogin))
    annuler.grid(row=5, column=0,pady=5)
    
    connex = Button(frameLogin, text="Connexion", font="times 16 bold", width=15 ,fg="white", bg="#22B9A8", command=lambda : Connexion(fen,frameLogin,user))
    connex.grid(row=5, column=1, pady=5)
    
def inscrptionFrame(frame,fen,opt):
    global entCIN,entNom,entPrenom,entNotBac,entJrNai,entMsNai,entAnNai,entFil,frameInsc
    frame.destroy()
    frameInsc=Frame(fen)
    frameInsc.pack()
    labelMsg=Label(frameInsc, text="Inscription !", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    labeCIN = Label(frameInsc, text="C I N : ", font="Times 12")
    labeCIN.grid(row=1, column=0, pady=3, sticky=NW)
    
    entCIN = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entCIN.grid(row=2, column=0,columnspan=3,pady=3, sticky=NW)
    
    labeNom = Label(frameInsc, text="Nom : ", font="Times 12")
    labeNom.grid(row=3, column=0,columnspan=3, pady=3, sticky=NW)
    
    entNom = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entNom.grid(row=4, column=0,columnspan=3, pady=3, sticky=NW)
    
    labePrenom = Label(frameInsc, text="Prénom : ", font="Times 12")
    labePrenom.grid(row=5, column=0,columnspan=3, pady=3, sticky=NW)
    
    entPrenom = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entPrenom.grid(row=6, column=0,columnspan=3, pady=3, sticky=NW)
    
    labeNotBac = Label(frameInsc, text="La note de bac : ", font="Times 12")
    labeNotBac.grid(row=7, column=0,columnspan=3, pady=3, sticky=NW)
    
    entNotBac = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entNotBac.grid(row=8, column=0,columnspan=3, pady=3, sticky=NW)
    
    labeDateNai = Label(frameInsc, text="Date de naissance (jj/mm/aaaa) : ", font="Times 12")
    labeDateNai.grid(row=9, column=0,columnspan=3, pady=3, sticky=NW)
    
    entJrNai = Entry(frameInsc,font="times 20 ", width=9, border=0)
    entJrNai.grid(row=10, column=0, pady=3, sticky=NW)
    
    entMsNai = Entry(frameInsc,font="times 20 ", width=9, border=0)
    entMsNai.grid(row=10, column=1, padx=5, pady=3, sticky=NSEW)
    
    entAnNai = Entry(frameInsc,font="times 20 ", width=9, border=0)
    entAnNai.grid(row=10, column=2, pady=3, sticky=SE)
    
    labeFil = Label(frameInsc, text="Choisissez une filiere : ", font="Times 12")
    labeFil.grid(row=11, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFil=ttk.Combobox(frameInsc,width=30,font="times 20 ",values=FiliersValide())
    entFil.grid(row=12, column=0, columnspan=3, pady=3, sticky=NSEW)
    
    Inscrir = Button(frameInsc, text="Inscrir", font="times 16 bold", width=36 ,fg="white", bg="#22B9A8", command=lambda:Inscription(fen))
    Inscrir.grid(row=13, column=0, columnspan=3, pady=5)
    
    Annuler = Button(frameInsc, text="Annuler", font="times 16 bold", width=36 ,fg="white", bg="#ffa245", command=lambda:afficherFrameConnexion(fen, opt,frameInsc))
    Annuler.grid(row=14, column=0, columnspan=3, pady=5)

###################
def FiliersValide():
    fils=[]
    for fil in ListFiliere:
        fils.append(fil.Nom)
    return fils

###################
def ErrDate(min,max,val):
    try: 
        Age=int(val)
        if int(Age) > max or int(Age)< min:
            messagebox.showerror("Erruer","Date Entrée non valide !!")
        else:
            return int(Age)
    except (ValueError):
            messagebox.showerror("Erruer","Saisir un nombre !!")

def ErrInt(val):
    try: 
        INT=int(val)
        return int(INT)
    except (ValueError):
            messagebox.showerror("Erruer","Saisir un nombre !!")

def ErrNote(val):
    try: 
        Not=float(val)
        if float(Not) > 20 or float(Not)< 0:
            messagebox.showerror("Erruer","Note entrée non valide !!")
        else:
            return float(Not)
    except (ValueError):
            messagebox.showinfo("Attention","Saisir un nombre !!")
###################

def Inscription(fen):
    L=[entCIN,entNom,entPrenom,entNotBac,entJrNai,entMsNai,entAnNai,entFil]
    for i in L:
        if i.get()=="":
            messagebox.showinfo("Attention","Merci de remplir touts les champs !!")
            return 
    jj=ErrDate(1,31,entJrNai.get())
    mm=ErrDate(1,12,entMsNai.get())
    aa=ErrDate(1900,2023,entAnNai.get())
    if jj and mm and aa and ErrNote(entNotBac.get()):
        DN=date(aa,mm,jj)
        if not VerifierAge(DN,DA):
            messagebox.showinfo("Attention","Vous ne peuvent pas inscrir !!")
            MenuPrincipale(fen,frameInsc)
        else:
            CIN=entCIN.get().upper()
            if ExisteStgr(ListStgr, CIN ) or ExisteStgr(List_Attend, CIN ):
                messagebox.showerror("Erreur","Un stagaire avec ce CIN est deja exist !!")
                return 
            Nom=entNom.get().title()
            Prenom=entPrenom.get().title()
            NotBac=ErrNote(entNotBac.get())
            if NotBac>=10:
                for fil in ListFiliere:
                    if fil.Nom == entFil.get():
                        id_fil=fil.getid()
                        break
                List_Attend.append(Stagaire(CIN,id_fil,Nom,Prenom,DN,ListFiliere,NotBac))
                messagebox.showinfo("Attention","Vous avez inscré avec succée !! \n Merci d'attent le confirmation..")
                MenuPrincipale(fen,frameInsc)
            else:
                messagebox.showerror("Erruer","La note entrée invalide")

def Connexion(fen,frame,user):
    global UtlActuel
    # "or" for a while 
    if user == "Directeur" and confirmeUtl(entUser.get(),entPass.get(),file_Drctr):
        UtlActuel=entUser.get().upper()
        frame.destroy()
        fenDrctr(fen)
    elif user == "Formateur" and confirmeUtl(entUser.get().upper(),entPass.get(),file_Frmtr):
        UtlActuel=entUser.get().upper()
        frame.destroy()
        fenFrmtr(fen)
    elif user == "Stagiaire" and confirmeUtl(entUser.get().upper(),entPass.get(),file_Stgr):
        UtlActuel=entUser.get().upper() 
        frame.destroy()
        fenStgr(fen)
    else:
        messagebox.showerror("Erreur","Le nom d'utilisatuer ou mot de pass non valide !!")
        entPass.delete(0,END)
        entPass.focus()

def fenDrctr(fen,frame=None):
    if frame :
        frame.destroy()
    frameDrctr = Frame(fen, padx=5, pady=5)
    frameDrctr.pack(pady=10)
    MsgLog=Label(frameDrctr, text="ADMINSTARTION", font="Bahnschrift 16 bold", fg="#22B9A8")
    MsgLog.grid(row=0,column=0,columnspan=3)
    optionsD = [
        "Ajouter une filière",
        "Ajouter un stagiaire",
        "Ajouter un formateur",
        "Afficher les stagiaires",
        "Afficher les formateurs",
        "Supprimer un stagiaire",
        "Supprimer un formateur",
        "Calculer les notes",
        "Exporter les données",
        "Importer les données",
        "Déconnexion"
    ]
    n = 1
    for i in range(len(optionsD)):
        if i == len(optionsD)-1:
            button = Button(frameDrctr, text=optionsD[i].upper(), font="times 12 bold ", fg="white", bg="#ffa245",width=53,command=lambda: MenuPrincipale(fen,frameDrctr))
            button.grid(row=n, column=i % 3 , columnspan=2, padx=5, pady=10)
        else:
            button = Button(frameDrctr, text=optionsD[i].upper(), font="times 12 bold ", fg="white", bg="#22B9A8",width=25,
                            command=lambda a=i: OperationD(fen, frameDrctr, optionsD[a]))
            button.grid(row=n, column=i % 3 , padx=5, pady=10)
        if i % 3 == 2:
            n = n + 1

def OperationD(fen, fdr, x):
    fdr.destroy()
    framOperDrctr = Frame(fen, padx=5, pady=5)
    framOperDrctr.pack(pady=10)
    if x == "Ajouter une filière":
        AjouFilFrame(fen,framOperDrctr)
    elif x =="Ajouter un stagiaire":
        ValiderStg(fen, framOperDrctr)
    elif x =="Ajouter un formateur":
        AjouFormFrame(fen,framOperDrctr)
    elif x =="Afficher les stagiaires":
        afficherListeStagiaires(fen,framOperDrctr)
    elif x =="Afficher les formateurs":
        afficherListeFormateurs(fen,framOperDrctr)
    elif x =="Supprimer un stagiaire":
        frameDeSupprission(fen,framOperDrctr,x)
    elif x =="Supprimer un formateur":
        frameDeSupprission(fen,framOperDrctr,x)
    elif x =="Calculer les notes":
        Calcule(fen)
    elif x =="Exporter les données":
        Exportation(fen,framOperDrctr)
    elif x =="Importer les données":
        Importation(fen,framOperDrctr)


#######################################
# Les frames et les operations de directuer

def AjouFilFrame(fen,frame):
    global entNomFil,entAbbr,entNomMod1,entNomMod2,entNomMod3,entCoef1,entCoef2,entCoef3
    labelMsg=Label(frame, text="Ajouter une filiére !".upper(), font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid( row=0,column=0, columnspan=4)
    
    labeNomFil = Label(frame, text="Nom de filiere : ", font="Times 12")
    labeNomFil.grid(row=1, column=0, pady=5, sticky=NW)
    
    entNomFil = Entry(frame,font="times 20 ", width=30, border=0)
    entNomFil.grid(row=2, column=1,columnspan=3,pady=5, sticky=NW)
    
    labeAbbr = Label(frame, text="Abbreviation : ", font="Times 12")
    labeAbbr.grid(row=3, column=0, pady=5, sticky=NW)
    
    entAbbr = Entry(frame,font="times 20 ", width=30, border=0)
    entAbbr.grid(row=4, column=1,columnspan=3, pady=5, sticky=NW)
    
    labelMsg=Label(frame, text="Ajouter les modules de cette filiiere !".upper(), font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=5, column=0,  columnspan=4,pady=10)
    
    for i in range(3):
        labeNomMod = Label(frame, text=f"Module {i+1}:", font="Times 12")
        labeNomMod.grid(row=i+6, column=0, pady=10, sticky=NW)
        
        labeCoef = Label(frame, text="Coef :", font="Times 12")
        labeCoef.grid(row=i+6, column=2, pady=10, sticky=NW)
    # ***************
    entNomMod1 = Entry(frame,font="times 14 ", width=30)
    entNomMod1.grid(row=6, column=1,pady=10, sticky=NW)
    entCoef1 = Entry(frame,font="times 14 ", width=10 )
    entCoef1.grid(row=6, column=3,pady=10, sticky=NW)
    # ***************
    entNomMod2 = Entry(frame,font="times 14 ", width=30)
    entNomMod2.grid(row=7, column=1,pady=10, sticky=NW)
    entCoef2 = Entry(frame,font="times 14 ", width=10 )
    entCoef2.grid(row=7, column=3,pady=10, sticky=NW)
    # ***************
    entNomMod3 = Entry(frame,font="times 14 ", width=30)
    entNomMod3.grid(row=8, column=1,pady=10, sticky=NW)
    entCoef3 = Entry(frame,font="times 14 ", width=10 )
    entCoef3.grid(row=8, column=3,pady=10, sticky=NW)
    
    ajouFil = Button(frame, text="Ajouter", font="times 16 bold", width=20 ,fg="white", bg="#22B9A8",command= lambda : AjoutFil(frame,fen))
    ajouFil.grid(row=9, column=0, columnspan=2, pady=5)
    annuler = Button(frame, text="Annuler", font="times 16 bold",width=20 , fg="white", bg="#ffa245",command=lambda : fenDrctr(fen,frame))
    annuler.grid(row=9, column=2,pady=5,columnspan=2)

def AjoutFil(frame,fen):
    champs=[entNomFil,entAbbr,entNomMod1,entNomMod2,entNomMod3,entCoef1,entCoef2,entCoef3]
    for cham in champs:
        if cham.get()=="":
            messagebox.showinfo("Attention","Merci de remplir touts les champs !!")
            return 
    nom = entNomFil.get().title()
    if ExisteFiliere(nom):
        messagebox.showerror("Erruer","Cette filiere est deja existe !!")
        return
    abbr = entAbbr.get().upper()
    F = Filiere(nom, abbr)
    idFil = F.getid()
    Noms = [entNomMod1.get(), entNomMod2.get(), entNomMod3.get()]
    
    coef1,coef2,coef3=entCoef1.get(),entCoef2.get(),entCoef3.get()
    if ErrInt(coef1) and ErrInt(coef2) and ErrInt(coef3):
        Coefs = [coef1,coef2,coef3]
        listMods = []
        for i in range(3):
            mod = Module(Noms[i].title(), idFil, Coefs[i])
            listMods.append(mod)
            ToutsModules.append(mod)
            
        F.ListModules = listMods
        ListFiliere.append(F) 
        messagebox.showinfo("Info", "Filiere est bien ajouté !!")
        frame.destroy()
        fenDrctr(fen)
    else :
        return

########################################
def PrintStg(obj):
    return StrSpaces(obj.Nom,18) + StrSpaces(obj.Prenom,20) + StrSpaces(str(obj.BacNote),16) + StrSpaces(obj.NomFil(),30)
entete=StrSpaces("Nom",18) + StrSpaces("Prenom",20) + StrSpaces("Note Bac",16) + StrSpaces("Feliere",30)

def ValiderStg(fen, frame):
    global stgLables, AcceptBtns, RefuBtns
    frame.pack()
    if List_Attend == []:
        messagebox.showerror("Erreur", "La liste d'attente est vide")
        fenDrctr(fen,frame)
    else:
        if len(ListStgr) <= 50:
            List_Attend.sort(key=getnote, reverse=True)
            n = 0
            stgLables = []
            AcceptBtns = []
            RefuBtns = []
            annuler = Button(frame, text="Retour", font="times 14 bold",width=10 , fg="white", bg="#ffa245",command=lambda : fenDrctr(fen,frame))
            annuler.grid(row=0, column=0,pady=5,sticky="W")
            
            EntetLabl = Label(frame,text=entete, font="times 14",width=56,bg="white")
            EntetLabl.grid(row=1, column=0,columnspan=4,sticky="W")
            
            EntetLabl = Label(frame,text="Actions", font="times 14",width=20, bg="white")
            EntetLabl.grid(row=1, column=4,columnspan=2)
            for stg in List_Attend:
                if n%2==0:
                    bg="#faf4ee"
                else:
                    bg="#f2e4d7"
                frame.pack(padx=5, pady=5) 
                stgLabel = Label(frame, text=PrintStg(stg),font="times 14 ", bg=bg, width=56, pady=5)
                stgLabel.grid(row=n+2, column=0, columnspan=4, pady=2,sticky="W")
                stgLables.append(stgLabel)
                
                accept_button = Button(frame, text="Accepter",font="times 12 bold ", fg="white", bg="#22B9A8",width=10,
                                    command=lambda s=stg, index=n: AccepterStg(s, index))
                accept_button.grid(row=n+2, column=4,padx=5, pady=5)
                AcceptBtns.append(accept_button)
                
                reject_button = Button(frame, text="Refuser",font="times 12 bold ", fg="white", bg="#ffa245",width=10,
                                    command=lambda s=stg, index=n: RefuserStgr(s, index))
                reject_button.grid(row=n+2, column=5, pady=5)
                RefuBtns.append(reject_button)
                n += 1
                
def AccepterStg(stg, index):
    ListStgr.append(stg)
    yesno=messagebox.askyesno("Confirme",f"Êtes-vous sûr de vouloir accepter {stg.Nom} {stg.Prenom} ?")
    if yesno:
        file = file_Stgr
        with open(file, 'a') as f:
            Pass = secrets.token_hex(5)
            f.write(f"{stg.CIN},{Pass}\n")
        List_Attend.remove(stg)
        stgLables[index].grid_forget()
        AcceptBtns[index].grid_forget()
        RefuBtns[index].grid_forget()
    else:
        return

def RefuserStgr(stg, index):
    yesno=messagebox.askyesno("Confirme",f"Êtes-vous sûr de vouloir refuser Mohamed ? {stg.Nom} {stg.Prenom}")
    if yesno:
        List_Attend.remove(stg)
        stgLables[index].grid_forget()
        AcceptBtns[index].grid_forget()
        RefuBtns[index].grid_forget()
    else:
        return 
########################################
def RecupereNomModules(Liste):
    NomModules=[]
    for m in Liste:
        NomModules.append(m.Nom)
    return NomModules
########################################
def AjouFormFrame(fen,frame):
    global entFrmCIN,entFrmNom,entFrmPrenom,entFrmAnNai,entFrmMsNai,entFrmJrNai , listBoxMods
    labelMsg=Label(frame, text="Ajout d'un Formatuer !", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    labeFrmCIN = Label(frame, text="C I N : ", font="Times 12")
    labeFrmCIN.grid(row=1, column=0, pady=3, sticky=NW)
    
    entFrmCIN = Entry(frame,font="times 20 ", width=30, border=0)
    entFrmCIN.grid(row=2, column=0,columnspan=3,pady=3, sticky=NW)
    
    labeFrmNom = Label(frame, text="Nom : ", font="Times 12")
    labeFrmNom.grid(row=3, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFrmNom = Entry(frame,font="times 20 ", width=30, border=0)
    entFrmNom.grid(row=4, column=0,columnspan=3, pady=3, sticky=NW)
    
    labeFrmPrenom = Label(frame, text="Prénom : ", font="Times 12")
    labeFrmPrenom.grid(row=5, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFrmPrenom = Entry(frame,font="times 20 ", width=30, border=0)
    entFrmPrenom.grid(row=6, column=0,columnspan=3, pady=3, sticky=NW)

    labeFrmDateNai = Label(frame, text="Date de naissance (jj/mm/aaaa) : ", font="Times 12")
    labeFrmDateNai.grid(row=7, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFrmJrNai = Entry(frame,font="times 20 ", width=9, border=0)
    entFrmJrNai.grid(row=8, column=0, pady=3, sticky=NW)
    
    entFrmMsNai = Entry(frame,font="times 20 ", width=9, border=0)
    entFrmMsNai.grid(row=8, column=1, padx=5, pady=3, sticky=NSEW)
    
    entFrmAnNai = Entry(frame,font="times 20 ", width=9, border=0)
    entFrmAnNai.grid(row=8, column=2, pady=3, sticky=SE)
    
    labelMods = Label(frame, text="Choisissez le(s) module(s) que le formateur enseignera:", font="Times 12")
    labelMods.grid(row=9, column=0, columnspan=2, padx=5, pady=5)
    listBoxMods = Listbox(frame, selectmode=MULTIPLE, height=3, width=25)
    listBoxMods.grid(row=9, column=2, pady=3)

    for module in RecupereNomModules(ToutsModules):
        listBoxMods.insert(END, module)
    
    Inscrir = Button(frame, text="Ajouter", font="times 16 bold", width=36 ,fg="white", bg="#22B9A8", command=lambda:AjoutFrmtr())
    Inscrir.grid(row=11, column=0, columnspan=3, pady=5)
    
    Annuler = Button(frame, text="Annuler", font="times 16 bold", width=36 ,fg="white", bg="#ffa245", command=lambda:fenDrctr(fen,frame))
    Annuler.grid(row=12, column=0, columnspan=3, pady=5)
########################################
def AjoutFrmtr():
    L =[ entFrmCIN, entFrmNom, entFrmPrenom, entFrmAnNai, entFrmMsNai, entFrmJrNai]
    for i in L:
        if i.get()=="":
            messagebox.showinfo("Attention","Merci de remplir touts les champs !!")
            return 
    CinFrmtr=entFrmCIN.get().upper()
    if ExisteFrmtr(CinFrmtr):
        messagebox.showerror("Erreur", "Le formateur existe déjà")
        return
    
    NF=entFrmNom.get().title()
    PF=entFrmPrenom.get().title()
    if ErrDate(1,31,entFrmJrNai.get()) and ErrDate(1,12,entFrmMsNai.get()) and ErrDate(1900,2023,entFrmAnNai.get()):
        jj=ErrDate(1,31,entFrmJrNai.get())
        mm=ErrDate(1,12,entFrmMsNai.get())
        aa=ErrDate(1900,2023,entFrmAnNai.get())
        
        DNF=date(aa,mm,jj)
        Form=Formateur(CinFrmtr,NF,PF,DNF)
        
        selectedMods= listBoxMods.curselection()
        if len(selectedMods)>3:
            messagebox.showerror("Erreur", "Selecionnez trois modules au max !!")
        else:
            listModFrmtr=[]
            for mod in ToutsModules:
                for index in selectedMods:
                    if mod.Nom==listBoxMods.get(index):
                        mod.CINFrmtr=CinFrmtr
                        listModFrmtr.append(mod)
            Form.Modules=listModFrmtr
            ListFrmtr.append(Form)
            file = file_Frmtr
            with open(file, 'a') as f:
                Pass = secrets.token_hex(5)
                f.write(f"{CinFrmtr},{Pass}\n")
            f.close()
            messagebox.showinfo("info", f"{NF} {PF} est bien ajouté")
    else :
        return
########################################

def afficherListeStagiaires(fen, frame):
    Annuler = Button(frame, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenDrctr(fen,frame))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(frame, text="La liste des stagiares ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("CIN","Nom","Prenom","Date de Naissaance","Note de Bac","Filiere ")
    CodeC=('cin','nom','Prenom','Date de Naissaance','Note de Bac','Filiere ')
    TM=ttk.Treeview(frame,columns=CodeC,show='headings')
    for i in range(6):
        TM.column(CodeC[i],width=120,anchor='center')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
    for i in range(len(ListStgr)):
        TM.insert('','end',values=(f'{ListStgr[i].CIN}',f'{ListStgr[i].Nom}',f'{ListStgr[i].Prenom}',f'{ListStgr[i].DateNai}',f'{ListStgr[i].BacNote}',f'{ListStgr[i].NomFil()}'))
########################################
def afficherListeFormateurs(fen, frame):
    Annuler = Button(frame, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenDrctr(fen,frame))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(frame, text="La liste des fourmatuers ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("CIN","Nom","Prenom","Date de Naissaance","Modules")
    CodeC=('cin','nom','Prenom','Date de Naissaance','Modules')
    TM=ttk.Treeview(frame,columns=CodeC,show='headings')
    for i in range(5):
        TM.column(CodeC[i],width=150,anchor='center')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
    for i in range(len(ListFrmtr)):
        TM.insert('','end',values=(f'{ListFrmtr[i].CIN}',f'{ListFrmtr[i].Nom}',f'{ListFrmtr[i].Prenom}',f'{ListFrmtr[i].DateNai}',f'{ListFrmtr[i].AfficheNomMods()}'))
        
########################################
# supression 
def frameDeSupprission(fen,frame,x):
    global entCinSup
    if x == "Supprimer un stagiaire":
        msg="stagaire"
    else:
        msg="formatuer"

    labelMsg=Label(frame, text=f"Supression d'un {msg} !!", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)

    labelCIN = Label(frame, text=f"Entrez le CIN de {msg} à supprimer: ", font="Times 12")
    labelCIN.grid(row=1, column=0, pady=5, sticky=NW)
    
    entCinSup = Entry(frame,font="times 20 ", width=30, border=0)
    entCinSup.grid(row=2, column=0,columnspan=3,pady=15, sticky=NW)

    Supp = Button(frame, text="Supprimer", font="times 16 bold", width=36 ,fg="white", bg="#22B9A8", command= lambda: Supprimer(x))
    Supp.grid(row=11, column=0, columnspan=3, pady=5)
    
    Retour = Button(frame, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#ffa245", command=lambda:fenDrctr(fen,frame))
    Retour.grid(row=12, column=0, columnspan=3, pady=5)

def Supprimer(x):
    
    if entCinSup.get()=="" :
        messagebox.showerror("Erreur","Veuillez choisir un code")
    else:
        C=entCinSup.get().upper()
        if x == "Supprimer un stagiaire":
            if not ExisteStgr(ListStgr,C):
                messagebox.showerror("Erreur","Aucun stagaire avec ce CIN !!")
            else:
                for stg in ListStgr:
                    if stg.CIN==C:
                        yesno=messagebox.askyesno("Confirmation",f"Êtes-vous sûr de vouloir supprimer {stg.Nom} {stg.Prenom}?")
                        if yesno:
                            ListStgr.remove(stg)
                            messagebox.showinfo("Confirmation","Le stagiaire à été supprimé")
                        else :
                            return
        else:
            if not ExisteFrmtr(C):
                messagebox.showerror("Erreur","Aucun formatuer avec ce CIN !!")
            else:
                for frmtr in ListFrmtr:
                    if frmtr.CIN==C:
                        yesno=messagebox.askyesno("Confirmation",f"Êtes-vous sûr de vouloir supprimer {frmtr.Nom} {frmtr.Prenom} ?")
                        if yesno:
                            ListStgr.remove(frmtr)
                            messagebox.showinfo("Confirmation","Le formatuer à été supprimé")
                        else :
                            return

########################################
def Calcule(fen):
    if ListeNotes ==[]:
        messagebox.showerror("Non disponible","Les note sont pas encore disponibles !")
    else:
        for stg in ListStgr:
            CalculeNotes(stg.CIN)
        messagebox.showinfo("Operation terminé","Tout les note sont calculé avec succée")
    fenDrctr(fen)
########################################


def Importation(fen,frame):
    labelMsg=Label(frame, text="Importation des données ...", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    image = PhotoImage(file="img/transfering.gif")
    label =Label(frame, image=image)
    label.grid(row=2,column=0, pady=10)
    
    progress = ttk.Progressbar(frame, length=300)
    progress.grid(row=1,column=0, pady=10)
    
    def MiseAJourProgress(count, total):
        progress['value'] = (count / total) * 100
        frame.update_idletasks()
        frame.update()
        time.sleep(1)
    
    count = 0
    total = 6

    with open("Data/Filieres.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 2:
                N, Abr = info[0], info[1]
                ListFiliere.append(Filiere(N, Abr))
    
    count += 1
    MiseAJourProgress(count, total)
    with open("Data/Modules.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 4:
                N, idfil, Coeff, CinF = info[0], info[1], info[2], info[3]
                ToutsModules.append(Module(N, int(idfil), int(Coeff), CinF))
                
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/Stagaires.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                ListStgr.append(Stagaire(C, int(idF), N, P, DN, ListFiliere, BN))
    
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/Notes.csv","r") as Notesfile:
        for line in Notesfile:
            info = line.strip().split(",")
            if len(info) == 5:
                idM,Cstg,C1,C2,EFM= info[0],info[1],info[2],info[3],info[4]
                ListeNotes.append(Note(int(idM),Cstg,float(C1),float(C2),float(EFM)))
    
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/StgsEnAttent.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                List_Attend.append(Stagaire(C, int(idF), N, P, DN, ListFiliere, float(BN)))
    
    count += 1
    MiseAJourProgress(count, total)
    
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
        
    
    count += 1
    MiseAJourProgress(count, total)
    
    messagebox.showinfo("Importatation Terminé","Tous les données valides ont été importés avec succès")
    
    fenDrctr(fen,frame)


def Exportation(fen, frame):

    labelMsg=Label(frame, text="Exportation des Données ...", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    image = PhotoImage(file="img/transfering.gif")
    label =Label(frame, image=image)
    label.grid(row=2,column=0, pady=10)
    
    total = 6 
    count = 0 
    progress = ttk.Progressbar(frame, length=300)
    progress.grid(row=1,column=0, pady=10)

    def ExportProgress():
        nonlocal count
        count += 1
        progress['value'] = (count / total) * 100
        frame.update_idletasks()
        time.sleep(1)


    File_filieres = open("Data/Filieres.csv", "a")
    FilWriter = csv.writer(File_filieres, delimiter=",")
    for fil in ListFiliere:
        FilWriter.writerow([fil.Nom, fil.Abr])
    File_filieres.close()
    ExportProgress()

    File_Modules = open("Data/Modules.csv", "a")
    ModWriter = csv.writer(File_Modules, delimiter=",")
    for mod in ToutsModules:
        ModWriter.writerow([ mod.Nom, mod.id_fil, mod.Coeff, mod.CINFrmtr])
    File_Modules.close()
    ExportProgress()

    File_Stagaires = open("Data/Stagaires.csv", "a")
    StgWriter = csv.writer(File_Stagaires, delimiter=",")
    for stg in ListStgr:
        StgWriter.writerow([stg.CIN, stg.Nom, stg.Prenom, stg.DateNai, stg.idFil, stg.BacNote])
    File_Stagaires.close()
    ExportProgress()

    stgAttent = open("Data/StgsEnAttent.csv", "a")
    StgWriter = csv.writer(stgAttent, delimiter=",")
    for stg in List_Attend:
        StgWriter.writerow([stg.CIN, stg.Nom, stg.Prenom, stg.DateNai, stg.idFil, stg.BacNote])
    stgAttent.close()
    ExportProgress()

    File_Formatuer = open("Data/Formateurs.csv", "a")
    FrmtWriter = csv.writer(File_Formatuer, delimiter=",")
    for frmtr in ListFrmtr:
        FrmtWriter.writerow([frmtr.CIN, frmtr.Nom, frmtr.Prenom, frmtr.DateNai,frmtr.AfficheNomMods()])
    File_Formatuer.close()
    ExportProgress()

    File_Notes = open("Data/Notes.csv", "a")
    NoteWriter = csv.writer(File_Notes, delimiter=",")
    for note in ListeNotes:
        NoteWriter.writerow([note.id_mod, note.CIN_stgr, note.PrControl, note.DeControl, note.EFM, round(note.MoyenModule(),2)])
    File_Notes.close()
    ExportProgress()
    
    progress.destroy()
    messagebox.showinfo("Exportatation Terminé","Tous les données valides ont été exporté avec succès")
    fenDrctr(fen,frame)

########################################
########################################
########################################

def fenFrmtr(fen,frame=None):
    user=RetUserByCIN(UtlActuel,ListFrmtr)
    if frame:
        frame.destroy()
    frameFrmtr = Frame(fen, padx=5, pady=5)
    frameFrmtr.pack(pady=10)
    username=user.Nom+" "+user.Prenom
    MsgLog=Label(frameFrmtr, text=f"Bonjour {username}", font="Bahnschrift 16 bold", fg="#1199B7")
    MsgLog.grid(row=0,column=0,columnspan=2)
    optionsF = [
        "Saisir notes",
        "Consulter les notes",
        "Déconnexion"
    ]

    saisir = Button(frameFrmtr, text=optionsF[0].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=25,
                    command=lambda: OperationF(fen, frameFrmtr, optionsF[0]))
    saisir.grid(row=1, column=0 , padx=5, pady=10)
    
    consulte = Button(frameFrmtr, text=optionsF[1].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=25,
                    command=lambda : OperationF(fen, frameFrmtr, optionsF[1]))
    consulte.grid(row=1, column=1 , padx=5, pady=10)

    button = Button(frameFrmtr, text=optionsF[2].upper(), font="times 12 bold ", fg="white", bg="#EA5A4F",width=53,
                    command=lambda: MenuPrincipale(fen,frameFrmtr))
    button.grid(row=2, column=0 , columnspan=2, padx=5, pady=10)
    
def OperationF(fen, fdr, x):
    fdr.destroy()
    framOperFrmtr = Frame(fen, padx=5, pady=5)
    framOperFrmtr.pack(pady=10)
    if x == "Saisir notes":
        Saisirnotes(fen,framOperFrmtr)
    elif x == "Consulter les notes":
        ConsulteNoteFr(fen,framOperFrmtr)
        
def Saisirnotes(fen, frame):
    labelMsg=Label(frame, text="Saisir les notes !".upper(), font="Bahnschrift 16 bold", fg="#1199B7")
    labelMsg.grid( row=0,column=0, columnspan=4)

    LCM = Label(frame, text=f"Choisir le module que vous voulez saisir les notes ", font="Times 12")
    LCM.grid(row=1, column=0, pady=5, sticky=NW)

    ModulesDeFrmtr = RetUserByCIN(UtlActuel, ListFrmtr).Modules

    MC=ttk.Combobox(frame, font="Arial 18", values=RecupereNomModules(ModulesDeFrmtr))
    MC.grid(row=1, column=1, pady=5)

    BT = Button(frame, text="Entrez les Notes", font="times 16 bold", width=36 ,fg="white", bg="#1199B7", command=lambda: Valide(fen, frame ,MC.get()))
    BT.grid(row=2, column=0, columnspan=3, pady=5)

    
    Retour = Button(frame, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:fenFrmtr(fen,frame))
    Retour.grid(row=3, column=0, columnspan=3, pady=5)

def SelectStagiaireApartairNomModul(nom):
    Stagiaire = []
    for m in ToutsModules:
        if m.Nom==nom:
            for f in ListFiliere:
                if m.id_fil==f.getid():
                    for stg in ListStgr:
                        if stg.idFil== f.getid():
                            Stagiaire.append(stg)
                    return Stagiaire

def nameStg(obj):
    return StrSpaces(obj.CIN,16) + StrSpaces(obj.Nom,20) + StrSpaces(obj.Prenom,20)
entete2= StrSpaces("CIN",16) + StrSpaces("Nom",20) + StrSpaces("Prenom",20)


NotesSaisé=[]
def Valide(fen, frame, MC):
    frame.destroy()
    noteframe =Frame(fen, padx=5, pady=5)
    noteframe.pack(padx=5, pady=5)
    
    annuler = Button(noteframe, text="Retour", font="times 14 bold",width=10 , fg="white", bg="#EA5A4F",command=lambda : fenFrmtr(fen,noteframe))
    annuler.grid(row=0, column=0,pady=5,sticky="W")
    
    labelMsg=Label(noteframe, text="La liste des stagiaire".upper(), font="Bahnschrift 16 bold", fg="#1199B7")
    labelMsg.grid( row=1,column=0, columnspan=5,)
    
    EntetLabl = Label(noteframe,text=entete2, font="times 14",width=56,bg="white")
    EntetLabl.grid(row=2, column=0,columnspan=4,sticky="W",pady=10)
            
    EntetLabl = Label(noteframe,text="Action", font="times 14",width=20, bg="white")
    EntetLabl.grid(row=2, column=4,pady=10)
    listestagers=SelectStagiaireApartairNomModul(MC)
    n = 3
    
    for stg in listestagers:
        L=[stg.CIN,MC]
        if L not in NotesSaisé:
            if n%2==0:
                bg="#faf4ee"
            else:
                bg="#f2e4d7"

            LCM = Label(noteframe, text=nameStg(stg), font="Times 12",bg=bg,width=56 )
            LCM.grid(row=n, column=0, columnspan=4 , pady=5, sticky="W")
            
            saisirNote = Button(noteframe, text="saiser les notes",font="times 12 bold ", fg="white", bg="#1199B7", width=20 ,command=lambda s=stg : note_stagiaire(s, fen, noteframe,MC))
            saisirNote.grid(row=n, column=4,padx=5, pady=5)
            n+=1
            noteframe.update()

def note_stagiaire(s, fen, noteframe,MC):

    noteframe.destroy()
    frameNote = Frame(fen, padx=5, pady=5)
    frameNote.pack(padx=5, pady=5)

    labelMsg=Label(frameNote, text=f"Saiser les notes de stagaire {s.Nom} {s.Prenom} de module {MC} ", font="Bahnschrift 14 bold", fg="#1199B7")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    C1= Label(frameNote, text="la note de primier contrôle :", font="Times 12")
    C1.grid(row=1, column=0, pady=5, sticky=NW)
    
    Note1 = Entry(frameNote, font="times 20 ", width=36, border=0)
    Note1.grid(row=2, column=0,columnspan=3, pady=5,sticky=NSEW)
    
    C2= Label(frameNote, text="la note de duexieme contrôle :", font="Times 12")
    C2.grid(row=3,column=0, pady=5, sticky=NW)
    
    Note2 = Entry(frameNote, font="times 20 ", width=36, border=0)
    Note2.grid(row=4, column=0,columnspan=3,pady=5,sticky=NSEW)
    
    EFM= Label(frameNote,text="la note de l'examen de fin de module :", font="Times 12")
    EFM.grid(row=5, column=0, pady=5, sticky=NW)
    
    NoteEFM = Entry(frameNote, font="times 20 ", width=36, border=0)
    NoteEFM.grid(row=6, column=0,columnspan=3,pady=5,sticky=NSEW)
    
    BtnValider =Button(frameNote,text ="valider",command= lambda STG=s, C1=Note1, C2=Note2, EFM=NoteEFM, mod=MC: ValiderNoteEtudiant(STG,C1,C2,EFM,mod,fen, frameNote,MC),
    font="Times 17 ", bg="#1199B7", fg="white",width=36)
    BtnValider.grid(row=7, column=0, columnspan=3, pady=5,sticky=NSEW)
    
    Retour = Button(frameNote, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:Valide(fen,frameNote,MC))
    Retour.grid(row=8, column=0, columnspan=3, pady=5)


def ValiderNoteEtudiant(STG,C1,C2,EFM,mod,fen,frameNote,MC):
    for m in ToutsModules:
        if m.Nom==mod:
            IDMOD=m.getid()
    if (ErrNote(C1.get()) and ErrNote(C2.get()) and ErrNote(EFM.get())):
        yesno=messagebox.askyesno("Confirmation",f"Voulez vous affecter ces notes a {STG.Nom} {STG.Prenom} ?")
        if yesno:
            N=Note(IDMOD,STG.CIN,C1.get(),C2.get(),EFM.get())
            ListeNotes.append(N)
            NotesSaisé.append([STG.CIN,mod])
            messagebox.showinfo("Conformation",f"Vous avez saisé la note de {STG.Nom} {STG.Prenom} avec succe")
            Valide(fen,frameNote,MC)
        else:
            return
    else:
        return
    

def ConsulteNoteFr(fen, frame):
    labelMsg=Label(frame, text="Consulter les notes !".upper(), font="Bahnschrift 16 bold", fg="#1199B7")
    labelMsg.grid( row=0,column=0, columnspan=4)

    LCM = Label(frame, text=f"Choisir le module que vous voulez consulter les notes ", font="Times 12")
    LCM.grid(row=1, column=0, pady=5, sticky=NW)

    ModulesDeFrmtr = RetUserByCIN(UtlActuel, ListFrmtr).Modules

    MC=ttk.Combobox(frame, font="times 16", values=RecupereNomModules(ModulesDeFrmtr))
    MC.grid(row=1, column=1, pady=5)

    BT = Button(frame, text="Consulter", font="times 16 bold", width=36 ,fg="white", bg="#1199B7", command=lambda: AffichageNoteMod(fen, frame ,MC.get()))
    BT.grid(row=2, column=0, columnspan=3, pady=5)

    
    Retour = Button(frame, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:fenFrmtr(fen,frame))
    Retour.grid(row=3, column=0, columnspan=3, pady=5)
    
def AffichageNoteMod(fen,frame,mod):
    frame.destroy()
    FrameConNote=Frame(fen,padx=5, pady=5)
    FrameConNote.pack(pady=10)
    Annuler = Button(FrameConNote, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenFrmtr(fen,FrameConNote))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(FrameConNote, text=f"Les notes de module {mod} ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("CIN","Nom","Prenom","CONTROLE 1","CONTROLE 2","EFM")
    CodeC=('cin','nom','Prenom','CONTROLE 1','CONTROLE 2','EFM')
    TM=ttk.Treeview(FrameConNote,columns=CodeC,show='headings')
    for i in range(6):
        TM.column(CodeC[i],width=120,anchor='center')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
    for Stg in SelectStagiaireApartairNomModul(mod):
        for note in ListeNotes:
            if note.CIN_stgr==Stg.CIN and note.id_mod== retModByName(mod).getid():
                TM.insert('','end',values=(f'{Stg.CIN}',f'{Stg.Nom}',f'{Stg.Prenom}',f'{note.PrControl}',f'{note.DeControl}',f'{note.EFM}'))
########################################

def fenStgr(fen,frame=None):
    if frame:
        frame.destroy() 
    user=RetUserByCIN(UtlActuel,ListStgr)
    frameStger = Frame(fen, padx=5, pady=5)
    frameStger.pack(pady=10)
    username=user.Nom+" "+user.Prenom
    MsgLog=Label(frameStger, text=f"Bonjour {username}", font="Bahnschrift 16 bold", fg="#1199B7")
    MsgLog.grid(row=0,column=0)
    optionsS = [
        "Consulter les notes",
        "Déconnexion"
    ]

    consulte = Button(frameStger, text= optionsS[0].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=23,
                    command=lambda : OperationS(fen, frameStger,  optionsS[0], user))
    consulte.grid(row=1, column=0 , padx=5, pady=10)

    button = Button(frameStger, text= optionsS[1].upper(), font="times 12 bold ", fg="white", bg="#EA5A4F",width=23,
                    command=lambda : OperationS(fen, frameStger,  optionsS[1],user))
    button.grid(row=2, column=0 , padx=5, pady=10)
    
def OperationS(fen, frameStger, x,user):
    frameStger.destroy()
    framOpeStager = Frame(fen, padx=5, pady=5)
    framOpeStager.pack(pady=10)
    if x == "Consulter les notes":
        ConsulteNoteS(fen, framOpeStager,user)
    else:
        MenuPrincipale(fen,framOpeStager)
        
def ConsulteNoteS(fen,framOpeStager,user):
    Annuler = Button(framOpeStager, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenStgr(fen,framOpeStager))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(framOpeStager, text="Mes  Notes  ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("MODULES","CONTROLE 1","CONTROLE 2","EFM","MOYENNE GENERAL")
    CodeC=('MODULES','CONTROLE 1','CONTROLE 2','EFM','MOYENNE GENERAL')
    TM=ttk.Treeview(framOpeStager,columns=CodeC,show='headings')
    for i in range(5):
        TM.column(CodeC[i],width=150,anchor='w')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
        
    for note in ListeNotes:
        for mod in ToutsModules:
            if note.CIN_stgr==user.CIN and note.id_mod== mod.getid():
                TM.insert('','end',values=(f'{mod.Nom}',f'{note.PrControl}',f'{note.DeControl}',f'{note.EFM}',f'{round(note.MoyenModule(),2)}'))