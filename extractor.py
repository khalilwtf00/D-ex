import pandas as pd
import tldextract
import sys
import os

def extract_root_domains(csv_file, column_name='domain'):
    if not os.path.isfile(csv_file):
        print(f"Error: File '{csv_file}' does not exist.")
        return

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the CSV.")
        return

    domains = df[column_name]
    root_domains = set()

    for entry in domains:
        extracted = tldextract.extract(str(entry))
        if extracted.domain and extracted.suffix:
            root = f"{extracted.domain}.{extracted.suffix}"
            root_domains.add(root)

    print("\n".join(sorted(root_domains)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_domains.py <csv_file> [column_name]")
    else:
        csv_file = sys.argv[1]
        column_name = sys.argv[2] if len(sys.argv) > 2 else 'domain'
        extract_root_domains(csv_file, column_name)
