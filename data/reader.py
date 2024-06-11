# escargot/data/reader.py
import pandas as pd

def read_gene_count_data(file_path: str) -> pd.DataFrame:
    """
    Reads single-cell gene count data from a file.
    """
    return pd.read_csv(file_path, sep='\t', index_col=0)