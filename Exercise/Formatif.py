import tkinter as tk
from tkinter import ttk as ttk, messagebox
from tkinter import filedialog
import json,csv
class Produit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ajouter un produit")
        self.geometry("800x600")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=8)
        self.produits = []


        # Frame 1 avec enter
        self.frame1 = ttk.LabelFrame(self, text="Ajouter un produit")
        self.frame1.grid(row=0, column=0, padx=10, pady=10,sticky="snew")
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=20)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.rowconfigure(2, weight=1)
            # widget de frame 1 column 1
        self.label1 = ttk.Label(self.frame1, text="Produit:")
        self.label1.grid(row=0, column=0, padx=10, sticky="e")
        self.label2 = ttk.Label(self.frame1, text="Quantité:")
        self.label2.grid(row=1, column=0, padx=10, sticky="e")
        self.label3 = ttk.Label(self.frame1, text="Prix:")
        self.label3.grid(row=2, column=0, padx=10, sticky="e")
            # widget de frame 1 column 2
        self.entry1 = ttk.Entry(self.frame1)
        self.entry1.grid(row=0, column=1, padx=10, sticky="ew")
        self.entry2 = ttk.Entry(self.frame1)
        self.entry2.grid(row=1, column=1, padx=10, sticky="ew")
        self.entry3 = ttk.Entry(self.frame1)
        self.entry3.grid(row=2, column=1, padx=10, sticky="ew")
            # widget de frame 1 column 3
        self.bt1 = ttk.Button(self.frame1, text= "Ajouter produit", command=self.ajouter)
        self.bt1.grid(row=0, column=2,rowspan=3, padx=10, pady=10, sticky="ew")


        #Frame 2
        self.frame2 = ttk.LabelFrame(self, text="Gestion deproduit")
        self.frame2.grid(row=1, column=0, padx=10, pady=10,sticky="snew")
        self.frame2.columnconfigure((0,1,2,3), weight=1)
        self.frame2.rowconfigure((0,1), weight=1)
       

            # widget de frame 2
        self.bt2 = ttk.Button(self.frame2, text="Supprimer Produit",command=self.supprimer)
        self.bt2.grid(row=0, column=0,columnspan=2, padx=10, pady=10)
        self.bt3 = ttk.Button(self.frame2, text="Modifier Produit", command=self.modifier)
        self.bt3.grid(row=0, column=2,columnspan=2, padx=10, pady=10)
        self.bt4 = ttk.Button(self.frame2, text="Sauvegarder CSV", command= self.sauvegarder_csv)
        self.bt4.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.bt5 = ttk.Button(self.frame2, text="Sauvegarder JSON", command=self.sauvegarder_json)
        self.bt5.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.bt6 = ttk.Button(self.frame2, text="Importer CSV")
        self.bt6.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        self.bt7 = ttk.Button(self.frame2, text="Importer JSON")
        self.bt7.grid(row=1, column=3, padx=10, pady=10, sticky="ew")


        #Frame3
        self.frame3 = ttk.Frame(self)
        self.frame3.grid(row=2, column=0, padx=10, pady=10,sticky="snew")
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.list = ttk.Treeview(self.frame3, columns=("Produit", "Quantité", "Prix"), show="headings", selectmode="extended")
        self.list.heading("Produit", text="Produit")
        self.list.heading("Quantité", text="Quantité")
        self.list.heading("Prix", text="Prix")
        self.list.grid(row=0, column=0, sticky="snew")

    def ajouter(self):
        produit= self.entry1.get()
        quantite= self.entry2.get()
        prix= self.entry3.get()
        self.list.insert("","end", values=(produit, quantite, prix))
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")
        self.produits.append([{"Produit": produit, "Quantite": quantite, "Prix": prix}])
        quit()
    def supprimer(self):
        selection = self.list.selection()
        for item in selection:
            if item == selection[0]:
                self.list.delete(item)


    def modifier(self):
        selection = self.list.selection()
        if not selection:
            return
        item_id = selection[0]
        values = self.list.item(item_id, 'values')
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry1.insert("end", values[0])
        self.entry2.insert("end", values[1])
        self.entry3.insert("end", values[2])
        self.list.delete(item_id)

    def sauvegarder_csv(self):
        if not self.produits:
            messagebox.showerror("Export CSV", "Aucun contenue a exporter")
            return
        path = filedialog.asksaveasfilename(title="exportercsv", defaultextension=".csv",
                                            filetypes=(("Fichier CSV", "*.csv"),))
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(["Produit", "Quantité", "Prix"])
                for produit in self.produits:
                    writer.writerow([
                        produit.produit,
                        produit.quantite,
                        produit.prix])
            messagebox.showinfo("Exporter csv", "Exporter csv exported successfully")
        except Exception as e:
            messagebox.showerror("Exporter csv", str(e))


    def sauvegarder_json(self):
        if not self.produits:
            messagebox.showerror("Export json", "Aucun contenue a exporter")
            return
        path = filedialog.asksaveasfilename(title="exporterjson", defaultextension=".json",filetypes=(("JSON Files", "*.json"),))
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.produits, f, indent=4)
            messagebox.showinfo("Exporter json", "Exporter json exported successfully")
        except Exception as e:
            messagebox.showerror("Exporter json", str(e))



if __name__ == '__main__':
    Produit().mainloop()

