# escargot/data/go_reader.py
import pandas as pd

def read_go_data(file_path: str) -> dict:
    """
    Reads GO annotations from a file and returns a dictionary mapping genes to GO terms.
    """
    go_data = pd.read_csv(file_path, sep='\t')
    gene_to_go = {}

    for _, row in go_data.iterrows():
        gene = row['HGNC symbol']
        go_term = row['GO term accession']
        if gene not in gene_to_go:
            gene_to_go[gene] = set()
        gene_to_go[gene].add(go_term)

    return gene_to_go