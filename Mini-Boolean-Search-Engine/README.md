"# Mini-Boolean-Search-Engine" 

## 🔍 Overview
This is a **Mini Boolean Search Engine** built in **Python**.  
It supports **Boolean queries** using `AND`, `OR`, and `NOT` operators over a set of text documents.  
The project demonstrates **inverted index creation** and basic **information retrieval** concepts.

## ⚙️ Features
- Supports Boolean operators: `AND`, `OR`, `NOT`
- Builds an **inverted index** for fast searching
- Works on multiple `.txt` documents in the `documents/` folder
- Easy to extend for web interface or ranking algorithms

## 🗂️ Project Structure
mini-boolean-search-engine/
│
├── documents/ ← Folder containing .txt files
├── search_engine.py ← Main Python script
├── inverted_index.json ← Generated index file
└── README.md ← Project description

---

## 🚀 How to Run
1. Navigate to the project folder in terminal:
```bash
cd "C:\Mini-Search Engine"
python search_engine.py
Enter Boolean queries:
AI AND Machine
Python OR Data
NOT Web
Type exit to quit the program.

📄 Example Output
Query: AI AND Machine
Documents found: {'doc1.txt', 'doc5.txt'}

Query: Python OR Data
Documents found: {'doc2.txt', 'doc3.txt'}

Query: NOT Web
Documents found: {'doc1.txt', 'doc2.txt', 'doc3.txt', 'doc5.txt', 'doc6.txt', 'doc7.txt'}


💡 Future Enhancements

Add a Flask web interface

Implement TF-IDF ranking

Support phrase and proximity search

Integrate real-world datasets
