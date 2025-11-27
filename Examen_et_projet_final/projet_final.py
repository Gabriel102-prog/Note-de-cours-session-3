import math
import tkinter as tk
from gettext import install
from tkinter import ttk, messagebox
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import sqlite3
from tkinter import font as tkfont
import pygame
from fusee import Fusee
import json
import csv
from tkinter import filedialog



class SimulationFusee(tk.Tk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()  # Initialisation audio
        self.hover_sound = pygame.mixer.Sound("bouton.mp3")  # Son au survol
        pygame.mixer.music.load("Crystal Skies (Super Slowed).mp3")  # Musique fond
        pygame.mixer.music.play(-1)  # Lecture en boucle
        self.window_change_sound = pygame.mixer.Sound("changement_fenetre.mp3")  # Son changement fenêtre
        self.title("Menu fusée")
        self.id_en_modif = None  # ID utilisateur en modification
        self.current_user_id = None  # ID utilisateur connecté
        self.columnconfigure(0, weight=1)  # Grille responsive
        self.rowconfigure(0, weight=1)
        self._init_db()  # Initialisation BDD
        self.menuprincipal()
        self.update_selection()
        self.maj_etat_widgets(connecte=False)  # Widgets non-connecté

    def _init_db(self):
        self.conn = sqlite3.connect("rocket.db")  # Connexion à la BDD
        cur = self.conn.cursor()

        # Table fusée
        cur.execute(""" CREATE TABLE IF NOT EXISTS rocket(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    fuel INTEGER NOT NULL,
                    vitesse INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)  # Création table rocket si inexistante

        # Table utilisateur
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nom TEXT NOT NULL, 
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        sexe TEXT CHECK (sexe IN ('H', 'F', 'Autre')) NOT NULL
                    )
                """)  # Création table users si inexistante
        self.conn.commit()  # Sauvegarde des modifications

    # -- Gestion database --

    def insert_user(self, nom, email, password, sexe):
        cur = self.conn.cursor()  # Création d'un curseur
        cur.execute("INSERT INTO users (nom, email, password, sexe) VALUES (?, ?, ?, ?)",
                    (nom, email, password, sexe))  # Insertion d'un nouvel utilisateur
        self.conn.commit()  # Sauvegarde dans la BDD
        cur.close()  # Fermeture du curseur

    def fetch_user(self, nom):
        cur = self.conn.cursor()  # Création d'un curseur
        cur.execute("SELECT id, nom, email, password, sexe FROM users WHERE nom = ?", (nom,))  # Recherche utilisateur
        row = cur.fetchone()  # Récupère le premier résultat
        cur.close()  # Fermeture du curseur
        return row  # Retourne l'utilisateur ou None

    def insert_rocket(self, nom, fuel, vitesse, user_id):
        cur = self.conn.cursor()  # Création d'un curseur
        cur.execute("INSERT INTO rocket (nom, fuel, vitesse, user_id) VALUES (?, ?, ?, ?)",
                    (nom, fuel, vitesse, user_id))  # Insertion d'une fusée
        self.conn.commit()  # Sauvegarde dans la BDD

    def fetch_rocket(self, nom):
        cur = self.conn.cursor()  # Création d'un curseur
        cur.execute("SELECT id, nom, fuel, vitesse FROM rocket WHERE nom = ?", (nom,))  # Recherche fusée
        row = cur.fetchone()  # Récupère le premier résultat
        cur.close()  # Fermeture du curseur
        return row  # Retourne la fusée ou None

    def clear_page(self):
        for widget in self.winfo_children():  # Parcourt tous les widgets enfants
            widget.destroy()  # Les détruit pour nettoyer la page

    def play_window_change(self):
        try:
            self.window_change_sound.play()  # Joue le son de changement de fenêtre
        except:
            pass  # Ignore les erreurs si le son n'est pas chargé

    def play_hover_sound(self, event=None):
        try:
            self.hover_sound.play()  # Joue le son de survol
        except:
            pass  # Ignore les erreurs si le son n'est pas chargé

    def bind_hover_sound_to_all_buttons(self, widget=None):
        if widget is None:
            widget = self  # Par défaut, commence par la fenêtre principale

        if isinstance(widget, ttk.Button):  # Si le widget est un bouton ttk
            widget.bind("<Enter>", self.play_hover_sound)  # Lie le son au survol

        for child in widget.winfo_children():  # Parcourt tous les enfants
            self.bind_hover_sound_to_all_buttons(child)  # Applique la liaison aux boutons enfants

    def menuprincipal(self):
        self.play_window_change()
        self.clear_page()
        style = ttk.Style()
        style.theme_use("clam")
        self.title("Menu Principal")
        self.geometry("1350x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frm_principal = tk.LabelFrame(self)
        self.frm_principal.configure(bg="black")
        self.frm_principal.grid(column=0, row=0, sticky="nsew")
        self.frm_principal.columnconfigure(0, weight=1)
        self.frm_principal.rowconfigure((1, 2), weight=20)
        self.frm_principal.rowconfigure(0, weight=1)

        self.titre_principal = ttk.Label(self.frm_principal, text="MSG Rocket Simulator", style="labelperso.TLabel")
        self.titre_principal.grid(row=0, column=0, sticky="w")
        # -- sous-frame avec création de la rocket --
        self.frame_ajout_info = ttk.Frame(self.frm_principal, style="TFrame")
        self.frame_ajout_info.grid(row=1, column=0, pady=(10, 0), sticky="ew")
        self.frame_ajout_info.columnconfigure((0, 1), weight=1)
        self.frame_ajout_info.rowconfigure(0, weight=1)

        # -- sous-sous-frame boutons et entry pour infos --
        self.frame_info = ttk.Frame(self.frame_ajout_info)
        self.frame_info.grid(row=0, column=0, sticky="nsew")

        self.frame_info.columnconfigure(1, weight=3)
        self.frame_info.columnconfigure((3, 5), weight=1)
        self.frame_info.rowconfigure(0, weight=1)

        self.lbl_nom_rocket = ttk.Label(self.frame_info, text="Nom de la fusée :")
        self.lbl_nom_rocket.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entry_nom_rocket = ttk.Entry(self.frame_info)
        self.entry_nom_rocket.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.lbl_fuel_max = ttk.Label(self.frame_info, text="Grosseur du réservoir de carburant (L) :")
        self.lbl_fuel_max.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.entry_fuel_max = ttk.Entry(self.frame_info)
        self.entry_fuel_max.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.lbl_vitesse_max = ttk.Label(self.frame_info, text="Vitesse limite (m/s) :")
        self.lbl_vitesse_max.grid(row=0, column=4, padx=5, pady=5, sticky="e")

        self.entry_vitesse_max = ttk.Entry(self.frame_info)
        self.entry_vitesse_max.grid(row=0, column=5, padx=5, pady=5, sticky="ew")

        # -- sous-sous-frame connexion/inscription --
        self.frame_login = ttk.Frame(self.frame_ajout_info)
        self.frame_login.grid(row=0, column=1, padx=(100, 5))

        self.frame_login.columnconfigure((0, 1), weight=1)
        self.frame_login.rowconfigure((0, 1), weight=1)

        self.btn_login = ttk.Button(self.frame_login, text="Connexion", command=self.page_connexion)
        self.btn_login.grid(row=1, column=0, padx=5, pady=5)

        self.btn_signin = ttk.Button(self.frame_login, text="Inscription", command=self.page_insciption)
        self.btn_signin.grid(row=1, column=1, padx=5, pady=5)

        # option light mode
        self.valeur = tk.StringVar(value="Dark mode")
        self.mode = ["Dark mode", "Light mode"]
        self.combobox = ttk.Combobox(self.frame_login, values=self.mode, state="readonly", textvariable=self.valeur)
        self.combobox.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5)
        self.combobox.bind("<<ComboboxSelected>>", self.update_selection)

        # -- sous-frame modification --
        self.frm_modification = ttk.Frame(self.frm_principal)
        self.frm_modification.grid(row=2, column=0, padx=10, sticky="nsew")

        self.frm_modification.columnconfigure(1, weight=1)
        self.frm_modification.rowconfigure((0, 1, 2, 3), weight=1)

        # -- sous-sous-frame boutons modif
        self.frm_btn_outils = ttk.LabelFrame(self.frm_modification, text="Outils")
        self.frm_btn_outils.grid(row=0, column=0, sticky="")

        self.frm_btn_outils.columnconfigure(0, weight=1)
        self.frm_btn_outils.rowconfigure((0, 1, 2), weight=1)

        self.btn_creer = ttk.Button(self.frm_btn_outils, text="Créer", command=self.valider_info_rocket)
        self.btn_creer.grid(row=0, column=0, padx=5, pady=5)

        self.btn_modifier = ttk.Button(self.frm_btn_outils, text="Modifier", command=self.modifier_info_rocket)
        self.btn_modifier.grid(row=1, column=0, padx=5, pady=5)

        self.btn_appliquer = ttk.Button(self.frm_btn_outils, text="Appliquer",
                                        command=self.appliquer_modifications_rocket)
        self.btn_appliquer.grid(row=2, column=0, padx=5, pady=5)

        self.btn_supprimer = ttk.Button(self.frm_btn_outils, text="Supprimer", command=self.supprimer_info_rocket)
        self.btn_supprimer.grid(row=3, column=0, padx=5, pady=5)

        # -- sous-sous-frame boutons fichiers json
        self.frm_btn_fichierjson = ttk.LabelFrame(self.frm_modification, text="JSON")
        self.frm_btn_fichierjson.grid(row=1, column=0, sticky="")

        self.frm_btn_fichierjson.columnconfigure(0, weight=1)
        self.frm_btn_fichierjson.rowconfigure(0, weight=1)

        self.btn_exportjson = ttk.Button(self.frm_btn_fichierjson, text="Exporter", command=self.export_json)
        self.btn_exportjson.grid(row=0, column=0, padx=5, pady=5)

        # -- sous-sous-frame boutons fichiers csv
        self.frm_btn_fichiercsv = ttk.LabelFrame(self.frm_modification, text="CSV")
        self.frm_btn_fichiercsv.grid(row=2, column=0, sticky="")

        self.frm_btn_fichiercsv.columnconfigure(0, weight=1)
        self.frm_btn_fichiercsv.rowconfigure(0, weight=1)

        self.btn_exportcsv = ttk.Button(self.frm_btn_fichiercsv, text="Exporter", command=self.export_csv)
        self.btn_exportcsv.grid(row=0, column=0, padx=5, pady=5)

        # - bouton simuler -

        self.btn_simulation = ttk.Button(self.frm_modification, text="Simulation", command=self.menusimulation,
                                         state="disabled")
        self.btn_simulation.grid(row=3, column=0, padx=5, pady=5)

        # -- treeview --
        self.list = ttk.Treeview(self.frm_modification, columns=("ID", "Nom", "Réservoir (L)", "Vitesse limite (m/s)"),
                                 show="headings")
        # créer le nom des columns
        self.list.heading("ID", text="ID")
        self.list.heading("Nom", text="Nom")
        self.list.heading("Réservoir (L)", text="Réservoir (L)")
        self.list.heading("Vitesse limite (m/s)", text="Vitesse limite (m/s)")
        # width chaque column
        self.list.column("Nom", width=500, stretch=True)
        self.list.grid(row=0, column=1, padx=(10, 0), pady=10, rowspan=4, sticky="nsew")
        self.list.bind("<<TreeviewSelect>>", self.treeviewselected)
        self.bind_hover_sound_to_all_buttons()

    def treeviewselected(self, event=None):
        if self.list.selection():
            self.btn_simulation.configure(state="normal")
        else:
            self.btn_simulation.configure(state="disabled")

    def update_selection(self, envent=None):
        # Sert a la personiffication de couleur
        style = ttk.Style()
        style.theme_use("clam")

        # condition de sélection et style
        selection = self.valeur.get()
        if selection == "Light mode":
            # Police et couleurs
            label_font = ("Arial", 14)
            entry_font = ("Arial", 14)
            entry_bg = "#bfbfbd"
            btn_font = ("Arial", 12, "bold")
            self.frm_principal.configure(bg="white")

            # Titre
            style.configure("labelperso.TLabel", font=("Race Sport", 28), foreground="#4a346e", background="White")
            # Lable inscription
            style.configure("labelpersonnification.TLabel", font=label_font, foreground="#6d1b7d", background="white")
            # Entry
            style.configure("entry.TEntry", bordercolor="black", font=entry_font, foreground="#6d1b7d",
                            fieldbackground=entry_bg, background=entry_bg, insertcolor="#6d1b7d", padding=5)
            # Boutton coché
            style.configure("check.TCheckbutton", font=label_font, foreground="#6d1b7d", background="white")
            style.map("check.TCheckbutton", background=[("active", "white")], foreground=[("active", "#6d1b7d")])
            style.configure("radio.TRadiobutton", font=label_font, foreground="#6d1b7d", background="white")
            style.map("radio.TRadiobutton", background=[("active", "white")], foreground=[("active", "#6d1b7d")])
            # Bouton
            style.configure("Boutonpersonnifiquation.TButton", font=btn_font, background="#855ec4", foreground="white")
            # MENU
            style.configure("TLabel", background="white", foreground="#4a346e", font=("Arial", 12))
            style.configure("TEntry", fieldbackground="#bfbfbd", background="#bfbfbd", foreground="#6d1b7d")
            style.configure("TButton", background="#855ec4", foreground="white", font=btn_font)
            style.map("TButton", background=[("active", "#855ec4")], foreground=[("active", "white")])
            style.configure("TLabelframe", background="white", foreground="#6d1b7d")
            style.configure("TLabelframe.Label", background="white", foreground="#6d1b7d")
            # Treeview
            style.configure("Treeview", background="#bfbfbd", foreground="white", fieldbackground="#bfbfbd",
                            font=("Arial", 12))
            style.map("Treeview", background=[("selected", "#555555")], foreground=[("selected", "white")])
            style.configure("Treeview.Heading", background="#593b8a", foreground="white", font=btn_font)
            style.map("Treeview.Heading", background=[("active", "#593b8a")], foreground=[("active", "white")])
            style.configure("TFrame", background="white")

            # Combo box
            style.configure("TCombobox", fieldbackground="#bfbfbd", background="#593b8a", foreground="white",
                            bordercolor="#593b8a", lightcolor="#593b8a", darkcolor="#593b8a", arrowcolor="white",
                            padding=5, font=("Arial", 14))
            style.map("TCombobox", selectbackground=[("readonly", "#bfbfbd"), ("!readonly", "#bfbfbd")],
                      selectforeground=[("readonly", "white"), ("!readonly", "white")],
                      fieldbackground=[("readonly", "#bfbfbd"), ("!readonly", "#bfbfbd")],
                      background=[("active", "#593b8a")], foreground=[("disabled", "gray"), ("!disabled", "white")])
            style.configure("TComboboxPopdownFrame", background="#bfbfbd")

            # Couleur de la liste (Treeview interne)
            style.configure("TComboboxPopdownFrame.Treeview", background="#bfbfbd", fieldbackground="#bfbfbd",
                            foreground="#6d1b7d")
            style.map(
                "TComboboxPopdownFrame.Treeview",
                background=[("selected", "#593b8a")],
                foreground=[("selected", "white")]
            )

        else:
            # Police et couleurs
            label_font = ("Arial", 14)
            entry_font = ("Arial", 14)
            entry_bg = "#222222"
            entry_fg = "white"
            btn_font = ("Arial", 12, "bold")
            self.frm_principal.configure(bg="black")

            # Titre
            style.configure("labelperso.TLabel", font=("Race Sport", 28), foreground="#5176b0", background="black")
            # Lable inscription
            style.configure("labelpersonnification.TLabel", font=label_font, foreground="white", background="black")
            # Entry
            style.configure("entry.TEntry", font=entry_font, foreground=entry_fg, fieldbackground=entry_bg,
                            background=entry_bg, insertcolor="white", padding=5)
            # Boutton coché
            style.configure("check.TCheckbutton", font=label_font, foreground="white", background="black")
            style.map("check.TCheckbutton", background=[("active", "black")], foreground=[("active", "white")])
            style.configure("radio.TRadiobutton", font=label_font, foreground="white", background="black")
            style.map("radio.TRadiobutton", background=[("active", "black")], foreground=[("active", "white")])

            # Bouton
            style.configure("Boutonpersonnifiquation.TButton", font=btn_font, background="#3F5C8A", foreground="black")
            # MENU
            style.configure("TLabel", background="black", foreground="white", font=("Arial", 12))
            style.configure("TEntry", fieldbackground="#222222", background="#222222", foreground="white")
            style.configure("TButton", background="#3F5C8A", foreground="white", font=btn_font)
            style.map("TButton", background=[("active", "#3F5C8A")], foreground=[("active", "white")])
            style.configure("TLabelframe", background="black", foreground="white")
            style.configure("TLabelframe.Label", background="black", foreground="white")
            # Treeview
            style.configure("Treeview", background="#222222", foreground="white", fieldbackground="#222222",
                            font=("Arial", 12))
            style.map("Treeview", background=[("selected", "#555555")], foreground=[("selected", "white")])
            style.configure("Treeview.Heading", background="#3F5C8A", foreground="white", font=btn_font)
            style.map("Treeview.Heading", background=[("active", "#3F5C8A")], foreground=[("active", "white")])
            style.configure("TFrame", background="black")

            # Combo box
            style.configure("TCombobox", fieldbackground="#222222", background="#3F5C8A", foreground="white",
                            bordercolor="#3F5C8A", lightcolor="#3F5C8A", darkcolor="#3F5C8A", arrowcolor="white",
                            selectbackground="#3F5C8A", selectforeground="white", padding=5, font=("Arial", 14))
            style.map("TCombobox",
                      fieldbackground=[("readonly", "#222222"), ("focus", "#222222"), ("!disabled", "#222222")],
                      background=[("active", "#3F5C8A"), ("pressed", "#3F5C8A")],
                      foreground=[("disabled", "gray"), ("!disabled", "white")],
                      selectbackground=[("readonly", "#222222"), ("!readonly", "#222222")],
                      selectforeground=[("readonly", "white"), ("!readonly", "white")])

    def maj_etat_widgets(self, connecte):

        # Liste des widgets à activer/désactiver
        widgets = [
            self.entry_nom_rocket,
            self.entry_fuel_max,
            self.entry_vitesse_max,
            self.btn_creer,
            self.btn_modifier,
            self.btn_appliquer,
            self.btn_supprimer,
            self.btn_exportjson,
            self.btn_exportcsv,
            self.btn_simulation
        ]

        for w in widgets:
            if connecte:
                w.config(state="normal")
            else:
                w.config(state="disabled")

        # Treeview
        if connecte:
            self.list.config(selectmode="browse")
        else:
            self.list.config(selectmode="none")

    def valider_info_rocket(self):
        nom = str(self.entry_nom_rocket.get().strip())
        # Vérifier si la fusée existe déjà
        cur = self.conn.cursor()
        cur.execute("SELECT id FROM rocket WHERE nom = ?", (nom,))
        deja = cur.fetchone()
        cur.close()

        if deja and self.id_en_modif is None:  # seulement lors de la création
            messagebox.showerror("Erreur", "Une fusée avec ce nom existe déjà.")
            return

        fuel = str(self.entry_fuel_max.get().strip())
        vitesse = str(self.entry_vitesse_max.get().strip())
        fusee = Fusee(nom, fuel, vitesse)
        if fusee.verification_init():
            #  INSERT dans la BD
            self.insert_rocket(nom, fuel, vitesse, self.current_user_id)
            self.reload_rockets()
        self.clear_entries()

    def clear_entries(self):
        self.entry_nom_rocket.delete(0, tk.END)
        self.entry_fuel_max.delete(0, tk.END)
        self.entry_vitesse_max.delete(0, tk.END)

    def appliquer_modifications_rocket(self):
        if self.id_en_modif is None:
            messagebox.showerror("Erreur", "Aucune fusée en cours de modification.")
            return

        nom = self.entry_nom_rocket.get().strip()
        fuel = self.entry_fuel_max.get().strip()
        vitesse = self.entry_vitesse_max.get().strip()
        fusee = Fusee(nom, fuel, vitesse)

        if not fusee.verification_init():
            return

        # Update dans la BD
        cur = self.conn.cursor()
        cur.execute("""
                    UPDATE rocket
                    SET nom     = ?,
                        fuel    = ?,
                        vitesse = ?
                    WHERE id = ?
                      AND user_id = ?
                    """, (nom, fuel, vitesse, self.id_en_modif, self.current_user_id))
        self.conn.commit()

        self.reload_rockets()

        self.entry_nom_rocket.delete(0, tk.END)
        self.entry_fuel_max.delete(0, tk.END)
        self.entry_vitesse_max.delete(0, tk.END)

        self.id_en_modif = None
        messagebox.showinfo("Succès", "Fusée modifiée avec succès.")

    def modifier_info_rocket(self):
        selection = self.list.selection()

        if not selection:
            messagebox.showerror("Erreur", "Aucune fusée sélectionnée.")
            return

        item = selection[0]
        values = self.list.item(item, "values")

        # values = (ID, nom, fuel, vitesse)
        id_rocket = values[0]
        nom, fuel, vitesse = values[1], values[2], values[3]

        self.id_en_modif = id_rocket  # stocker l'ID pour le futur UPDATE

        # Remplir les champs
        self.entry_nom_rocket.delete(0, tk.END)
        self.entry_nom_rocket.insert(0, nom)

        self.entry_fuel_max.delete(0, tk.END)
        self.entry_fuel_max.insert(0, fuel)

        self.entry_vitesse_max.delete(0, tk.END)
        self.entry_vitesse_max.insert(0, vitesse)

    def supprimer_info_rocket(self):
        selection = self.list.selection()
        if not selection:
            messagebox.showerror("Erreur", "Aucune fusée sélectionnée.")
            return

        item = selection[0]
        values = self.list.item(item, "values")

        id_rocket = values[0]

        cur = self.conn.cursor()
        cur.execute("DELETE FROM rocket WHERE id = ?", (id_rocket,))
        self.conn.commit()
        cur.close()

        self.reload_rockets()

    def export_json(self):
        # sélection emplacement fichier
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Exporter les fusées en JSON"
        )

        if not file_path:
            return

        cur = self.conn.cursor()
        cur.execute("""
                    SELECT id, nom, fuel, vitesse
                    FROM rocket
                    WHERE user_id = ?
                    """, (self.current_user_id,))
        rockets = cur.fetchall()
        cur.close()

        # Format JSON
        data = []
        for r in rockets:
            data.append({
                "id": r[0],
                "nom": r[1],
                "fuel": r[2],
                "vitesse": r[3]
            })

        # Écriture fichier
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Succès", "Export JSON réussi.")

    def export_csv(self):
        # sélection emplacement fichier
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Exporter les fusées en CSV"
        )

        if not file_path:
            return

        cur = self.conn.cursor()
        cur.execute("""
                    SELECT id, nom, fuel, vitesse
                    FROM rocket
                    WHERE user_id = ?
                    """, (self.current_user_id,))
        rockets = cur.fetchall()
        cur.close()

        # Écriture CSV
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nom", "Fuel", "Vitesse"])  # entêtes
            writer.writerows(rockets)

        messagebox.showinfo("Succès", "Export CSV réussi.")

    def reload_rockets(self):
        if self.current_user_id is None:
            return

        # vider le treeview
        for row in self.list.get_children():
            self.list.delete(row)

        # charger depuis la BD
        cur = self.conn.cursor()
        cur.execute("""
                    SELECT id, nom, fuel, vitesse
                    FROM rocket
                    WHERE user_id = ?
                    """, (self.current_user_id,))
        rows = cur.fetchall()
        cur.close()

        for r in rows:
            self.list.insert("", "end", values=r)
        self.treeviewselected()

    def menusimulation(self):
        self.play_window_change()
        selection = self.list.selection()
        if selection:
            item_id = selection[0]  # le premier élément sélectionné
            values = self.list.item(item_id, "values")  # tuple avec (ID, Nom, Fuel, Vitesse)
            self.selected_nomf = values[1]
            self.selected_fuel = values[2]
            self.selected_vitesse = values[3]

        self.list.selection_remove(self.list.selection())
        self.withdraw()
        self.simu = tk.Toplevel(self)
        self.simu.title("Simulation Fusées")
        self.simu.geometry("1200x900")
        self.simu.columnconfigure(0, weight=1)
        self.simu.rowconfigure(0, weight=1)

        self.framesim = ttk.LabelFrame(self.simu, text="MSG Rocket Simulator")
        self.framesim.columnconfigure(0, weight=1)
        self.framesim.columnconfigure(1, weight=1)
        self.framesim.columnconfigure(2, weight=5)
        self.framesim.rowconfigure(0, weight=1)
        self.framesim.rowconfigure((1, 2, 3, 4, 5, 6), weight=1000000)
        self.framesim.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.textfusee = ttk.Label(self.framesim,
                                   text=f" User : {self.user_nom}, fusée : {self.selected_nomf}",
                                   font=("Arial", 14, "bold"))
        self.textfusee.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        self.fuel = ttk.Label(self.framesim, text=f"Fuel (max : {self.selected_fuel}L)")
        self.fuel.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.fuelent = ttk.Entry(self.framesim)
        self.fuelent.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        self.angle = ttk.Label(self.framesim, text="Angle (°)")
        self.angle.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.anglent = ttk.Entry(self.framesim)
        self.anglent.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        self.frameinfossim = ttk.Frame(self.framesim)
        self.frameinfossim.columnconfigure((0, 1), weight=1)
        self.frameinfossim.rowconfigure(0, weight=1)
        self.frameinfossim.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.angleframe = ttk.LabelFrame(self.frameinfossim, text="Angle (°)")
        self.angleframe.columnconfigure(0, weight=1)
        self.angleframe.rowconfigure(0, weight=1)
        self.angleframe.grid(row=0, column=1, padx=5, pady=5, sticky="ensw")

        self.vitesseframe = ttk.LabelFrame(self.frameinfossim, text="Vitesse (m/s)")
        self.vitesseframe.columnconfigure(0, weight=1)
        self.vitesseframe.rowconfigure(0, weight=1)
        self.vitesseframe.grid(row=0, column=0, padx=5, pady=5, sticky="ensw")

        self.vitesse = ttk.Entry(self.vitesseframe, state="readonly", font=("Arial", 9, "bold"), justify="center")
        self.vitesse.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.vitesse.config(state="normal")
        self.vitesse.insert(0, "0.0")
        self.vitesse.config(state="readonly")

        self.angleentsim = ttk.Entry(self.angleframe, state="readonly", font=("Arial", 9, "bold"), justify="center")
        self.angleentsim.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.angleentsim.config(state="normal")
        self.angleentsim.insert(0, "0.0")
        self.angleentsim.config(state="readonly")

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.framesim)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, rowspan=7, column=2, padx=5, pady=5, sticky="nsew")
        self.ax.grid(True, color="gray")
        self.lancement = ttk.Button(self.framesim, text="Lancement", command=self.lancementaction)
        self.lancement.grid(row=4, column=0, padx=5, sticky="ew")

        self.retourmenu = ttk.Button(self.framesim, text="Retour au Menu", command=self.simuretourmenu)
        self.retourmenu.grid(row=4, column=1, padx=5, sticky="ew")

        self.bind_hover_sound_to_all_buttons(self.simu)

    def lancementaction(self):  # todo logique vitesse et affichage en directe lineaire
        f = Fusee(self.selected_nomf, self.selected_fuel, self.selected_vitesse)
        f.angle = self.anglent.get().strip()
        f.carburant = self.fuelent.get().strip()
        s = f.verification_init()
        d = f.verif_angle_carburant()
        if not s or not d:
            self.fuelent.delete(0, "end")
            self.vitesse.delete(0, "end")
            return

        self.ax.clear()
        # Ligne initiale
        p_linear = np.linspace(0, 3500 * float(self.fuelent.get().strip()) * np.cos(
            np.radians(float(self.anglent.get().strip()))), 4000)
        m = np.tan(np.radians(float(self.anglent.get().strip())))
        b = 0
        y_linear = m * p_linear + b

        # Parabole
        x0, y0 = p_linear[-1], y_linear[-1]  # départ à la fin de la ligne
        t = np.linspace(0, 100, 4000)  # points de temps

        v_initial = math.sqrt(2 * 34 * 3500 * float(self.fuelent.get().strip()))
        v_limit = float(self.selected_vitesse)

        # Limitation de la vitesse
        v_init = min(v_initial, v_limit)

        vx = v_init * math.cos(math.radians(float(self.anglent.get().strip())))
        vy = v_init * math.sin(math.radians(float(self.anglent.get().strip())))
        g = 9.8

        qx = x0 + vx * t
        qy = y0 + vy * t - 0.5 * g * t ** 2

        # On ne garde que qy >= 0 (fusée pas sous le sol)
        mask = (qy >= 0) & (qx >= 0)
        qx = qx[mask]
        qy = qy[mask]

        # On prépare le graphique
        self.ax.set_xlim(0, max(max(p_linear), max(qx)))
        self.ax.set_ylim(0, max(max(y_linear), max(qy)))
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.grid(True)
        self.ax.plot(p_linear, y_linear, color="green")  # ligne fixe
        self.canvas.draw()

        # Variables pour animation
        step = 5  # nombre de points ajoutés par "frame"
        delay_ms = 5  # temps entre chaque mise à jour en ms
        index = 0
        line, = self.ax.plot([], [], color="blue")  # ligne animée

        def update():
            nonlocal index
            if index < len(qx):
                end = min(index + step, len(qx))
                line.set_data(qx[:end], qy[:end])

                # Calculer vitesse instantanée pour le dernier point ajouté
                vx_inst = np.gradient(qx[:end], t[:end])
                vy_inst = np.gradient(qy[:end], t[:end])
                v_inst = np.sqrt(vx_inst[-1] ** 2 + vy_inst[-1] ** 2)

                # Mettre à jour l'affichage
                self.vitesse.config(state="normal")
                self.vitesse.delete(0, "end")
                self.vitesse.insert(0, f"{v_inst:.2f}")
                self.vitesse.config(state="readonly")

                self.canvas.draw()
                index += step
                self.simu.after(delay_ms, update)

        update()

    def simuretourmenu(self):
        self.play_window_change()
        self.simu.destroy()
        self.deiconify()

        # Page d'inscription

    def page_insciption(self):
        self.play_window_change()
        self.withdraw()
        self.inscription = tk.Toplevel(self)
        self.inscription.geometry("700x300")
        if self.valeur.get() == "Dark mode":
            self.inscription.configure(bg="black")
            couleur = "black"
        else:
            self.inscription.configure(bg="white")
            couleur= "white"
        self.inscription.title("Inscription")

        # Reviens a page d'acueuille lors de supression de la page
        self.inscription.protocol("WM_DELETE_WINDOW", self.retour_menu_inscription)

        # Sert a la personiffication de couleur
        style = ttk.Style()
        style.theme_use("clam")

        # Configuration de la grille principale
        self.inscription.columnconfigure(0, weight=1)
        self.inscription.rowconfigure(0, weight=1)

        # Frame principale avec fond noir
        self.frame_inscription = tk.Frame(self.inscription, bg=couleur)
        self.frame_inscription.grid(row=0, column=0, sticky="nsew")
        self.frame_inscription.columnconfigure(0, weight=1)
        self.frame_inscription.columnconfigure(1, weight=1)
        self.frame_inscription.columnconfigure(2, weight=1)
        for i in range(7):
            self.frame_inscription.rowconfigure(i, weight=1)

        # Titre
        self.title_inscription = ttk.Label(self.frame_inscription, text="Inscription", style="labelperso.TLabel")
        self.title_inscription.grid(column=0, row=0, columnspan=3, pady=10)

        # Username
        self.title_username = ttk.Label(self.frame_inscription, text="Nom d'utilisateur:",
                                        style="labelpersonnification.TLabel")
        self.title_username.grid(column=0, row=1, sticky="e", padx=5)
        self.ent_username = ttk.Entry(self.frame_inscription, style="entry.TEntry")
        self.ent_username.grid(column=1, row=1, padx=10, pady=2, sticky="ew")

        # Email
        self.title_email = ttk.Label(self.frame_inscription, text="Email:", style="labelpersonnification.TLabel")
        self.title_email.grid(column=0, row=2, sticky="e", padx=5)
        self.ent_email = ttk.Entry(self.frame_inscription, style="entry.TEntry")
        self.ent_email.grid(column=1, row=2, padx=10, pady=2, sticky="ew")

        # Password
        self.title_mot_passe = ttk.Label(self.frame_inscription, text="Mot de passe:",
                                         style="labelpersonnification.TLabel")
        self.title_mot_passe.grid(column=0, row=3, sticky="e", padx=5)
        self.ent_mot_passe = ttk.Entry(self.frame_inscription, style="entry.TEntry", show="*")
        self.ent_mot_passe.grid(column=1, row=3, padx=10, pady=2, sticky="ew")

        # Condition d'utilisation
        self.valeur_check = tk.IntVar(value=0)
        self.bouton_condition = ttk.Checkbutton(self.frame_inscription, text="J'ai lu et accepte les conditions",
                                                variable=self.valeur_check, style="check.TCheckbutton")
        self.bouton_condition.grid(column=0, row=4, rowspan=2, pady=10)

        self.gender = tk.StringVar(value="")
        self.male = ttk.Radiobutton(self.frame_inscription, text="Homme", variable=self.gender, value="H",
                                    style="radio.TRadiobutton")
        self.male.grid(column=1, row=4, sticky="ew")
        self.female = ttk.Radiobutton(self.frame_inscription, text="Femme", variable=self.gender, value="F",
                                      style="radio.TRadiobutton")
        self.female.grid(column=1, row=5, sticky="ew")

        # Buttons
        self.bouton_inscription = ttk.Button(self.frame_inscription, text="Inscription",
                                             style="Boutonpersonnifiquation.TButton", command=self.verifier_inscription)
        self.bouton_inscription.grid(column=1, row=6, pady=10, sticky="ew")
        self.bouton_sortir = ttk.Button(self.frame_inscription, text="Page principale",
                                        style="Boutonpersonnifiquation.TButton", command=self.retour_menu_inscription)
        self.bouton_sortir.grid(column=0, row=6, pady=10, sticky="e", padx=10)

        self.bind_hover_sound_to_all_buttons(self.inscription)

    # Vérification d'information d'inscription
    def verifier_inscription(self):

        # Vérifie username
        valeur = self.ent_username.get().strip()
        if not valeur.isalpha():
            self.ent_username.delete(0, "end")
            self.ent_username.insert("end", "Veuillez entrez des lettres seulement")
            self.ent_username.config(foreground="red")
            self.after(3000, lambda e=self.ent_username: (e.delete(0, "end"), e.config(foreground="white")))
            return

        # Vérifie l'email
        if "@" not in self.ent_email.get():
            self.ent_email.delete(0, "end")
            self.ent_email.insert("end", "Veuillez entrez des lettres et @")
            self.ent_email.config(foreground="red")
            self.after(3000, lambda e=self.ent_email: (e.delete(0, "end"), e.config(foreground="white")))
            return

        # Vérifie le mot de passe
        mdp = self.ent_mot_passe.get()
        if len(mdp) <= 5 or not any(c.isalpha() for c in mdp) or not any(c.isdigit() for c in mdp):
            self.ent_mot_passe.delete(0, "end")
            self.ent_mot_passe.configure(show="")
            self.ent_mot_passe.insert("end", "Le mot de passe doit contenir des lettres et >5 ")
            self.ent_mot_passe.config(foreground="red")

            def reset_star():
                self.ent_mot_passe.delete(0, "end")
                self.ent_mot_passe.config(foreground="white")
                self.ent_mot_passe.configure(show="*")

            self.after(3000, reset_star)
            return
        if self.gender.get() == "":
            messagebox.showerror("Error", "Veuillez sélectionné male ou femelle")
            return
        if self.valeur_check.get() != 1:
            messagebox.showerror("Error", "Veuillez cocher l'acceptation des condition")
            return

        # Vérifier si le nom existe déjà
        cur = self.conn.cursor()
        cur.execute("SELECT id FROM users WHERE nom = ?", (self.ent_username.get().strip(),))
        if cur.fetchone():
            messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà.")
            cur.close()
            return

        # Vérifier si l'email existe déjà
        cur.execute("SELECT id FROM users WHERE email = ?", (self.ent_email.get().strip(),))
        if cur.fetchone():
            messagebox.showerror("Erreur", "Cet email est déjà utilisé.")
            cur.close()
            return
        cur.close()
        # --- Sauvegarder les valeurs avant de détruire la fenêtre ---
        username = self.ent_username.get().strip()
        self.user_nom = username
        email = self.ent_email.get().strip()
        password = self.ent_mot_passe.get()
        sexe = self.gender.get()

        # --- Insertion BD ---
        self.insert_user(username, email, password, sexe)

        # Récupérer l'id
        user = self.fetch_user(username)
        self.current_user_id = user[0]

        # Fermer la fenêtre inscription
        self.retour_menu_inscription()

        # Recharger les fusées
        self.reload_rockets()

        # Modifier les boutons de login/inscription
        self.btn_login.config(text=username, state="disabled")
        self.btn_signin.config(text="Déconnexion", command=self.deconnexion)

        # Activer les widgets
        self.maj_etat_widgets(connecte=True)

        # Remplacer inscription par déconnexion
        self.btn_signin.config(text="Déconnexion", command=self.deconnexion)

        self.maj_etat_widgets(connecte=True)

    def page_connexion(self):
        self.play_window_change()
        self.withdraw()
        self.connexions = tk.Toplevel(self)
        self.connexions.geometry("500x200")
        if self.valeur.get() == "Dark mode":
            self.connexions.configure(bg="black")
            couleur = "black"
        else:
            self.connexions.configure(bg="white")
            couleur= "white"
        self.connexions.title("Connexion")
        self.connexions.columnconfigure(0, weight=1)
        self.connexions.rowconfigure(0, weight=1)
        self.connexions.rowconfigure(1, weight=1)

        # Reviens a page d'acueuille lors de supression de la page
        self.connexions.protocol("WM_DELETE_WINDOW", self.retour_menu_connexion)

        style = ttk.Style()
        style.theme_use("clam")

        self.labelframeconnexion = tk.Frame(self.connexions, bg=couleur)
        self.labelframeconnexion.columnconfigure(0, weight=1)
        self.labelframeconnexion.rowconfigure(0, weight=1)
        self.labelframeconnexion.grid(row=0, column=0)
        self.label_login = ttk.Label(self.labelframeconnexion, text="Connexion", style="labelperso.TLabel")
        self.label_login.grid(row=0, column=0)

        self.frame_connexion = tk.Frame(self.connexions, bg=couleur)
        self.frame_connexion.columnconfigure((0, 1), weight=1)
        self.frame_connexion.rowconfigure((0, 1), weight=1)
        self.frame_connexion.grid(row=1, column=0, sticky="nsew")

        self.lbl_user = ttk.Label(self.frame_connexion, text="Utilisateur :", style="labelpersonnification.TLabel")
        self.lbl_user.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.lbl_password = ttk.Label(self.frame_connexion, text="Mot de passe :", style="labelpersonnification.TLabel")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_user = ttk.Entry(self.frame_connexion, style="entry.TEntry")
        self.entry_user.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.entry_password = ttk.Entry(self.frame_connexion, show="*", style="entry.TEntry")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.btn_connexion = ttk.Button(self.frame_connexion, text="Connexion", style="Boutonpersonnifiquation.TButton",
                                        command=self.connexion)
        self.btn_connexion.grid(row=0, column=2, padx=10, pady=10)

        self.btn_retour_menu = ttk.Button(self.frame_connexion, text="Retour",
                                          style="Boutonpersonnifiquation.TButton", command=self.retour_menu_connexion)
        self.btn_retour_menu.grid(row=1, column=2, padx=10, pady=10)

        self.bind_hover_sound_to_all_buttons(self.connexions)

    def connexion(self):

        utilisateur = self.entry_user.get().strip()
        password1 = self.entry_password.get().strip()

        if utilisateur == "" or password1 == "":
            messagebox.showerror("Error", "Utilisateur ou mot de passe est vide")

        user = self.fetch_user(utilisateur)
        if not user:
            messagebox.showerror("Error", "Utilisateur introuvable.")
            return

        user_id, nom, email, password_db, sexe = user
        self.user_nom = nom
        if password_db != password1:
            messagebox.showerror("Error", "Mot de passe incorrect")
            return

        self.current_user_id = user_id

        # Mettre le nom sur le bouton connexion
        self.btn_login.config(text=nom, state="disabled")

        # Remplacer inscription par déconnexion
        self.btn_signin.config(text="Déconnexion", command=self.deconnexion)

        self.retour_menu_connexion()
        self.reload_rockets()

        self.maj_etat_widgets(connecte=True)

    def deconnexion(self):
        self.clear_entries()
        self.current_user_id = None

        # Remettre les boutons comme au début
        self.btn_login.config(text="Connexion", state="normal", command=self.page_connexion)
        self.btn_signin.config(text="Inscription", command=self.page_insciption)

        # Désactiver les widgets
        self.maj_etat_widgets(connecte=False)

        # Effacer le treeview
        for row in self.list.get_children():
            self.list.delete(row)

        # Vider les champs
        self.entry_nom_rocket.delete(0, tk.END)
        self.entry_fuel_max.delete(0, tk.END)
        self.entry_vitesse_max.delete(0, tk.END)

    def retour_menu_connexion(self):
        self.play_window_change()
        self.connexions.destroy()  # fermer la fenêtre connexion
        self.deiconify()
        self.reload_rockets()

    def retour_menu_inscription(self):
        self.play_window_change()
        self.inscription.destroy()  # fermer la fenêtre inscription
        self.deiconify()


if __name__ == '__main__':
    i = SimulationFusee()
    i.mainloop()
