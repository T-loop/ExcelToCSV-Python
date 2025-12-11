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




README – Excel Data Extractor (.exe)
Description

This program is designed to automatically extract important information from Excel files.
The user provides a folder path, and the program scans all Excel files in that folder, extracts the required data, and saves the results as CSV files in the same directory.

The program was developed in Python using pandas, and compiled into an .exe so it can run without a Python installation.

How It Works

When the program starts, it asks the user to enter the path of a folder containing Excel files.

The program automatically reads all Excel files inside the folder (e.g., .xlsx, .xls).

Each file is analyzed, and the program searches for the relevant information (e.g., specific columns, values, or patterns).

If the required information is found in a file:

The extracted data is saved to a new CSV file.

The CSV file uses the same name as the original Excel file.

The CSV file is stored in the same folder.

Files that do not contain the required information are skipped.

Requirements

No Python installation is required.
The provided .exe file is fully self-contained.
