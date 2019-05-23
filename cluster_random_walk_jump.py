import pandas as pd
from sklearn.cluster import SpectralClustering
from random_walk_jump import generate_rw_sample

PCT_SAMPLE = 0.01

def main():
	sampled_graph, adj_m = generate_rw_sample(PCT_SAMPLE)
	clusters = SpectralClustering(assign_labels="discretize").fit_predict(adj_m)
	df_clusters = pd.DataFrame(clusters, columns=['cluster'])
	df_clusters.to_csv('cluster_result.csv', index=False)

if __name__ == "__main__":
	main()