from tkinter import filedialog

# Ouvrir une boîte de dialogue pour sélectionner un fichier JSON ou CSV à ouvrir
chemin_fichier = filedialog.askopenfilename(title="Ouvrir un fichier",
    initialdir="C:/Utilisateurs/Documents",              # dossier initial (facultatif)
    filetypes=[("Fichiers CSV", "*.csv"), ("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")])
if chemin_fichier:
    print("Fichier sélectionné :", chemin_fichier)
else:
    print("Aucun fichier sélectionné.")

# ... (lecture du fichier peut suivre ici si un chemin a été retourné) ...

# Plus loin, ouvrir une boîte de dialogue pour enregistrer un fichier JSON
chemin_sauvegarde = filedialog.asksaveasfilename(
    title="Enregistrer sous",
    defaultextension=".json",
    filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
)
if chemin_sauvegarde:
    print("Enregistrer dans :", chemin_sauvegarde)
    # ... (écriture des données dans le fichier chemin_sauvegarde) ...
