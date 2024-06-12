import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import DBSCAN
from umap import UMAP
from sentence_transformers import SentenceTransformer
import os
import sys

def gen_embeddings(documents):
	embed_model = SentenceTransformer("BAAI/bge-small-en")
	text_embeddings = embed_model.encode(documents, show_progress_bar=True)
	print("text embeds: " + str(text_embeddings.shape))
	return text_embeddings


def gen_avg_embedding(embeddings):
	average_embeddings = np.mean(embeddings, axis=0)
	print("average embeds: " + str(average_embeddings.shape))
	return average_embeddings

def find_pairwise(average_embeddings):
	return cosine_similarity(average_embeddings)
		

def heatmap(x_labels, y_labels, values):
        fig, ax = plt.subplots(1, 1, figsize = (10, 10))
        im = ax.imshow(values)

        ax.set_xticks(np.arange(len(x_labels)))
        ax.set_yticks(np.arange(len(y_labels)))
        
        ax.set_xticklabels(x_labels)
        ax.set_yticklabels(y_labels)
        
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10,rotation_mode="anchor")
        
        for i in range(len(y_labels)):
                for j in range(len(x_labels)):
                        text = ax.text(j, i, "%.2f"%values[i, j], ha="center", va="center", color="w", fontsize=6)
        fig.tight_layout()
        plt.show()



def gen_clusters(text_embeddings):
	umap_model = UMAP(n_neighbors=10, n_components=5, min_dist=0.0, metric='cosine')
	reduced_text_embeddings = umap_model.fit_transform(text_embeddings)
	dbscan_model = DBSCAN(eps=2, min_samples=5)
	text_cluster = dbscan_model.fit(reduced_text_embeddings)
	labels = text_cluster.labels_
	return labels



if __name__ == '__main__':
	dir = sys.argv[1]
	text_files = [dir + "/" + f for f in os.listdir(dir) if f.endswith(".txt")]
	text_files.sort()
	documents = [open(f).read() for f in text_files]

	print("N docs = " + str(len(documents)))

	embeddings = gen_embeddings(documents)
	
	avg_embeds = gen_avg_embedding(embeddings)

	pairwise = find_pairwise(embeddings)
	textfilenames = [t.split("/")[-1].split("_")[0] for t in text_files]
	heatmap(textfilenames, textfilenames, pairwise)


