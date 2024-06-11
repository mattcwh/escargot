# escargot/analysis/gsva.py
import pandas as pd
import numpy as np
from scipy.stats import rankdata
from sklearn.neighbors import KernelDensity

def estimate_cdf(expression_data):
    """
    Estimate the CDF for each gene expression profile using a non-parametric kernel method.
    """
    kde = KernelDensity(kernel='gaussian', bandwidth=0.5)
    cdf_estimates = []

    for gene in expression_data:
        kde.fit(expression_data[gene].values[:, None])
        cdf = kde.score_samples(expression_data[gene].values[:, None])
        cdf_estimates.append(np.exp(cdf))

    return np.array(cdf_estimates).T

def calculate_gsva_scores(expression_data, gene_to_go):
    """
    Calculate GSVA scores for each GO term.
    """
    # Step 1: Estimate CDF
    cdf_estimates = estimate_cdf(expression_data)

    # Step 2: Rank the expression-level statistics
    ranks = np.apply_along_axis(rankdata, 0, cdf_estimates)

    # Step 3: Calculate GSVA enrichment scores
    enrichment_scores = {}

    for gene_set_name, genes in gene_to_go.items():
        indices = [expression_data.columns.get_loc(gene) for gene in genes if gene in expression_data.columns]
        if not indices:
            continue
        
        # Rank-based statistic
        es = np.mean(ranks[:, indices], axis=1) - np.mean(ranks[:, np.setdiff1d(range(expression_data.shape[1]), indices)], axis=1)
        
        enrichment_scores[gene_set_name] = es

    return pd.DataFrame(enrichment_scores, index=expression_data.index)