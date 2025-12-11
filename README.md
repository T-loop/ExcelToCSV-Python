Excel-Datenextraktor (.exe)
Beschreibung

Dieses Programm dient zur automatisierten Extraktion wichtiger Informationen aus Excel-Dateien.
Der Benutzer gibt einen Ordnerpfad an, das Programm durchsucht alle darin enthaltenen Excel-Dateien, extrahiert die benötigten Daten und speichert die Ergebnisse als CSV-Dateien im gleichen Ordner.

Das Programm wurde in Python mit pandas entwickelt und zu einer .exe-Datei kompiliert, sodass es ohne Python-Installation ausgeführt werden kann.


Funktionsweise


Beim Start fragt das Programm nach dem Pfad zu einem Ordner, der Excel-Dateien enthält.

Alle Excel-Dateien im Ordner werden automatisch eingelesen (z. B. .xlsx, .xls).

Jede Datei wird analysiert, und das Programm sucht nach den relevanten Informationen (z. B. bestimmte Spalten, Werte, Muster).

Wenn die gesuchte Information in einer Datei gefunden wird:

Die extrahierten Daten werden in eine neue CSV-Datei geschrieben.

Die CSV erhält den gleichen Namen wie die ursprüngliche Excel-Datei.

Die CSV wird im selben Ordner gespeichert.

Dateien ohne relevante Informationen werden übersprungen.



Voraussetzungen

Es wird keine Python-Installation benötigt.
Die mitgelieferte .exe reicht vollständig aus.
