# escargot/main.py
from data.reader import read_gene_count_data
from data.go_reader import read_go_data
from analysis.gsva import calculate_gsva_scores
from results.visualization import plot_enrichment_scores

def main(gene_count_file, go_data_file):
    gene_count_data = read_gene_count_data(gene_count_file)
    gene_to_go = read_go_data(go_data_file)
    enrichment_scores = calculate_gsva_scores(gene_count_data, gene_to_go)
    plot_enrichment_scores(enrichment_scores)

if __name__ == "__main__":
    main("path/to/gene_count_file.csv", "data/GO_all_human_coding_genes.txt")
