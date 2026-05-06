# 📊 Excel Data Extractor (.exe)

This program is designed for the **automated extraction of important information from Excel files**.

The user provides a folder path, and the program scans all Excel files inside it, extracts the required data, and saves the results as CSV files in the same directory.

The tool is developed in **Python** using **pandas** and compiled into a **standalone .exe file**, meaning it can run without requiring a Python installation.

---

## ⚙️ How It Works

1. When started, the program asks for the path to a folder containing Excel files.  
2. All Excel files in the folder are automatically loaded (e.g., `.xlsx`, `.xls`).  
3. Each file is analyzed, and the program searches for relevant information (e.g., specific columns, values, or patterns).  
4. If relevant data is found in a file:
   - The extracted data is written into a new CSV file.  
   - The CSV file keeps the same name as the original Excel file.  
   - The CSV file is saved in the same folder.  
5. Files without relevant data are automatically skipped.

---

## 🧩 Requirements

- No Python installation required  
- The provided `.exe` is fully standalone and ready to run

---

## 🚀 Installation / Usage

1. Download the `.exe` file  
2. Run the program  
3. Enter the path to the folder containing Excel files  
4. CSV files will be automatically generated in the same folder  

---

## 📝 Notes

- Supported file formats: `.xlsx`, `.xls`  
- Files without relevant data are ignored  
- Processing time may vary depending on the number and size of Excel files in the folder
