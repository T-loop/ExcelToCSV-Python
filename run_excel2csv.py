import os
import time
from excel_data_extractor import ExcelExtractor
import config 

def main():
    

    ordner = input("Bitte Pfad zum Ordner mit Excel-Dateien: ").strip()
    starttime = time.time()  

    for datei in os.listdir(ordner):
        if datei.endswith(".xlsx") or datei.endswith(".xls"):
            pfad_zur_datei = os.path.join(ordner, datei)
            print(f"\nVerarbeite: {datei}")

            try:
                extractor = ExcelExtractor()

                index = extractor.finde_startzeile(pfad_zur_datei, config.sheetname)
                extractor.daten_auslesen(pfad_zur_datei, config.sheetname, index)
                daten_dict = extractor.erstelle_dict()

                if daten_dict["Anforderung-Titel"]:
                    csv_name = os.path.splitext(datei)[0] + "_output.csv"
                    csv_pfad = os.path.join(ordner, csv_name)
                    extractor.speichere_als_csv(daten_dict, csv_pfad)
                else:
                    print("Keine relevanten Daten gefunden.")

            except Exception as e:
                print(f"Fehler bei Datei {datei}: {e}")

    endtime = time.time()  
    dauer = endtime - starttime
    print(f"\nLaufzeit: {dauer:.4f} Sekunden")

if __name__ == "__main__":
    main()



input("Drücke Enter zum Beenden...")
