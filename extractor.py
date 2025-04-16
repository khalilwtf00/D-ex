import pandas as pd
import tldextract
import sys
import os

def extract_root_domains(csv_file, column_name='identifier', output_file='domains.txt'):
    if not os.path.isfile(csv_file):
        print(f"❌ File '{csv_file}' not found.")
        return

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    if column_name not in df.columns:
        print(f"❌ Column '{column_name}' not found in the CSV.")
        return

    domains = df[column_name]
    root_domains = set()

    for entry in domains:
        extracted = tldextract.extract(str(entry))
        if extracted.domain and extracted.suffix:
            root = f"{extracted.domain}.{extracted.suffix}"
            root_domains.add(root)

    with open(output_file, 'w') as f:
        for domain in sorted(root_domains):
            f.write(domain + '\n')

    print(f"✅ Root domains written to '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_domains.py <local_csv_file>")
    else:
        csv_file = sys.argv[1]
        extract_root_domains(csv_file)
