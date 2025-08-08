import pandas as pd

class ExcelExtractor:
    def __init__(self):
        self.listtitel = []
        self.listinhalt = []
        self.listmasnahme = []
        self.listumsetzung = []
        self.listbaustein=[]

    def finde_startzeile(self, dateipfad, sheetname):
        df = pd.read_excel(dateipfad, sheet_name=sheetname, engine="openpyxl", header=None)
        for index, row in df.iterrows():
            if "Anforderung-Titel" in row.values:
                return index
        raise ValueError(" 'Anforderung-Titel' wurde nicht gefunden.")

    def daten_auslesen(self, dateipfad, sheetname, startzeile):
        df = pd.read_excel(dateipfad, sheet_name=sheetname, header=startzeile, engine="openpyxl")

        aktueller_titel = None
        temp_inhalt = []
        temp_massnahme = []

        for _, row in df.iterrows():
            titel = row["Anforderung-Titel"]
            inhalt = str(row["Anforderung-Inhalte"]).strip() if pd.notna(row["Anforderung-Inhalte"]) else ""
            massnahme = str(row["Maßnahmen"]).strip() if pd.notna(row["Maßnahmen"]) else ""
            umsetzung = row["Umsetzungsgrad"]
            baustein=row["Baustein"]


            if pd.notna(titel):
                aktueller_titel = titel

            temp_inhalt.append(inhalt)
            if massnahme and massnahme not in temp_massnahme:
                temp_massnahme.append(massnahme)


            if inhalt == "* Fazit *":
                self.listtitel.append(aktueller_titel)
                self.listinhalt.append(temp_inhalt.copy())
                self.listmasnahme.append(temp_massnahme.copy())
                self.listumsetzung.append(umsetzung)
                self.listbaustein.append(baustein)

                temp_inhalt = []
                temp_massnahme = []
                aktueller_titel = None

    def erstelle_dict(self):
        return {
            "index": list(range(1, len(self.listtitel) + 1)),
            "Baustein":self.listbaustein,
            "Anforderung-Titel": self.listtitel,
            "Anforderung-Inhalte": self.listinhalt,
            "Maßnahmen": self.listmasnahme,
            "Umsetzungsgrad": self.listumsetzung
        }

    def speichere_als_csv(self, daten_dict, pfad):
        df = pd.DataFrame(daten_dict)
        df["Anforderung-Inhalte"] = df["Anforderung-Inhalte"].apply(lambda x: "\n".join(x))
        df["Maßnahmen"] = df["Maßnahmen"].apply(lambda x: "\n".join(x))
        df.to_csv(pfad, sep=';', encoding="utf-8-sig", index=False)
        print(f" CSV gespeichert: {pfad}")
