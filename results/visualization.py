# escargot/results/visualization.py
import matplotlib.pyplot as plt

def plot_enrichment_scores(enrichment_scores: pd.DataFrame):
    """
    Plot GSVA enrichment scores.
    """
    sorted_scores = enrichment_scores.mean().sort_values(ascending=False)
    terms, scores = sorted_scores.index, sorted_scores.values

    plt.figure(figsize=(10, 5))
    plt.barh(terms, scores)
    plt.xlabel('GSVA Enrichment Score')
    plt.ylabel('Gene Ontology Term')
    plt.title('GSVA Enrichment Scores')
    plt.show()
