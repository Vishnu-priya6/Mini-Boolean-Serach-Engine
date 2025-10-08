import os
import re
import json

# -----------------------------
# 1️⃣ Helper to get absolute path
# -----------------------------
def get_project_path():
    # Returns the folder where this script is located
    return os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# 2️⃣ Build Inverted Index
# -----------------------------
def build_index(folder_name="documents"):
    project_path = get_project_path()
    folder_path = os.path.join(project_path, folder_name)

    if not os.path.exists(folder_path):
        print(f"❌ Folder '{folder_name}' not found at {folder_path}")
        return

    index = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            doc_id = filename
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                text = f.read().lower()
                words = re.findall(r'\b\w+\b', text)
                for word in set(words):
                    index.setdefault(word, []).append(doc_id)

    # Save index to JSON
    index_file = os.path.join(project_path, "inverted_index.json")
    with open(index_file, "w", encoding='utf-8') as f:
        json.dump(index, f, indent=4)

    print(f"✅ Inverted index created successfully at {index_file}!")

# -----------------------------
# 3️⃣ Process Boolean Queries
# -----------------------------
def boolean_query(query):
    index_file = os.path.join(get_project_path(), "inverted_index.json")
    if not os.path.exists(index_file):
        print("❌ inverted_index.json not found! Build the index first.")
        return set()

    with open(index_file, "r", encoding='utf-8') as f:
        index = json.load(f)

    query = query.upper().split()
    if not query:
        return set()

    # Initialize result
    if query[0] == "NOT":  # Handle leading NOT
        next_term = query[1].lower()
        all_docs = set()
        for docs in index.values():
            all_docs.update(docs)
        result = all_docs - set(index.get(next_term, []))
        i = 2
    else:
        result = set(index.get(query[0].lower(), []))
        i = 1

    # Process remaining operators
    while i < len(query):
        operator = query[i]
        next_term = query[i + 1].lower()
        next_docs = set(index.get(next_term, []))

        if operator == "AND":
            result &= next_docs
        elif operator == "OR":
            result |= next_docs
        elif operator == "NOT":
            result -= next_docs
        else:
            print(f"⚠️ Unknown operator: {operator}")
        i += 2

    return result

# -----------------------------
# 4️⃣ Main Program
# -----------------------------
if __name__ == "__main__":
    build_index("documents")

    while True:
        print("\nEnter Boolean query (AND, OR, NOT) or 'exit' to quit:")
        query = input(">> ")
        if query.lower() == "exit":
            break
        result = boolean_query(query)
        if result:
            print("Documents found:", result)
        else:
            print("No documents matched your query.")
