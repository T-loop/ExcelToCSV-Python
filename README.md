# Excel Data Extractor (.exe)

Dieses Programm dient zur **automatisierten Extraktion wichtiger Informationen aus Excel-Dateien**.  

Der Benutzer gibt einen Ordnerpfad an, das Programm durchsucht alle darin enthaltenen Excel-Dateien, extrahiert die benötigten Daten und speichert die Ergebnisse als CSV-Dateien im gleichen Ordner.

Das Programm wurde in **Python** unter Verwendung von **pandas** entwickelt und zu einer **.exe-Datei kompiliert**, sodass es ohne Python-Installation ausgeführt werden kann.

---

## Funktionsweise

1. Beim Start fragt das Programm nach dem Pfad zu einem Ordner, der Excel-Dateien enthält.  
2. Alle Excel-Dateien im Ordner werden automatisch eingelesen (z. B. `.xlsx`, `.xls`).  
3. Jede Datei wird analysiert, und das Programm sucht nach den relevanten Informationen (z. B. bestimmte Spalten, Werte oder Muster).  
4. Wenn die gesuchte Information in einer Datei gefunden wird:
   - Die extrahierten Daten werden in eine neue CSV-Datei geschrieben.  
   - Die CSV-Datei erhält den gleichen Namen wie die ursprüngliche Excel-Datei.  
   - Die CSV-Datei wird im selben Ordner gespeichert.  
5. Dateien ohne relevante Informationen werden automatisch übersprungen.

---

## Voraussetzungen

- Keine Python-Installation erforderlich.  
- Die mitgelieferte `.exe` ist vollständig eigenständig und lauffähig.

---

## Installation / Nutzung

1. `.exe`-Datei herunterladen.  
2. Programm starten.  
3. Pfad zum Ordner mit Excel-Dateien eingeben.  
4. Die CSV-Dateien werden automatisch im gleichen Ordner erstellt.  

---

## Hinweise

- Unterstützte Dateiformate: `.xlsx`, `.xls`  
- Dateien ohne relevante Daten werden ignoriert.  
- Für große Ordner kann die Verarbeitung einige Minuten dauern, abhängig von der Anzahl der Excel-Dateien und deren Größe.
