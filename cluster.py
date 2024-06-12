from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
import pandas as pd
from nltk.corpus import stopwords


def process(file):
	with open(file, "r") as f:
		tokens = word_tokenize(f.read())
		tokens = [w.lower() for w in tokens]
		words = [word for word in tokens if word.isalpha()]

def find_optimal_clusters(data, max_k):
	iters = range(2, max_k+1, 2)
	sse = []
	for k in iters:
		sse.append(MiniBatchKMeans(n_clusters=k, init_size=1024, batch_size=2048, random_state=20).fit(data).inertia_)
		print('Fit {} clusters'.format(k))
	f, ax = plt.subplots(1, 1)
	ax.plot(iters, sse, marker='o')
	ax.set_xlabel('Cluster Centers')
	ax.set_xticks(iters)
	ax.set_xticklabels(iters)
	ax.set_ylabel('SSE')
	ax.set_title('SSE by Cluster Center Plot')
	plt.show()	

def plot_tsne_pca(data, labels, names):

	svd = TruncatedSVD(n_components=2).fit_transform(data)
	# tsne = TSNE().fit_transform(TruncatedSVD(n_components=50).fit_transform(data))
	
	f, ax = plt.subplots(1, 2, figsize=(14, 6))
    
	ax[0].scatter(svd[:, 0], svd[:, 1], c=labels)
	ax[0].set_title('SVD Cluster Plot')    
	for i in range(len(names)): 
		ax[0].annotate(names[i], (svd[i, 0], svd[i, 1]))
	#ax[1].scatter(svd[:, 0], svd[:, 1], c=labels)
	#ax[1].set_title('TSNE Cluster Plot')
	plt.show() 


def get_top_keywords_2(data,vocab): 
	lsa_model = TruncatedSVD(n_components=5, algorithm='randomized', n_iter=10, random_state=42)
	lsa_top=lsa_model.fit_transform(data)
	for i, comp in enumerate(lsa_model.components_):
		vocab_comp = zip(vocab, comp)
		sorted_words = sorted(vocab_comp, key= lambda x:x[1], reverse=True)[:10]
		print("Topic "+str(i)+": ")
		for t in sorted_words:
			print(t[0],end=" ")
		print("\n")

def clean_docs(documents): 
	s=set(stopwords.words('english'))
	# documents = [" ".join(filter(lambda w: ((not w in s,txt.split()) and w.isalnum()),txt)).lower() for txt in documents]
	documents = [' '.join([word for word in text.split() if word not in s]) for text in documents]
	return documents
	

if __name__ == '__main__':
	dir = sys.argv[1]
	text_files = [dir + "/" + f for f in os.listdir(dir) if f.endswith(".txt")]
	text_files.sort()
	documents = [open(f).read() for f in text_files]
	print(len(text_files))
	
	documents = clean_docs(documents)

	tfidfer = TfidfVectorizer()
	tfidf = tfidfer.fit_transform(documents)
	textfilenames = [t.split("/")[-1].split("_")[0] for t in text_files]
		
	clusters = MiniBatchKMeans(n_clusters=8, init_size=1024, batch_size=2048, random_state=20).fit_predict(tfidf)
	plot_tsne_pca(tfidf, clusters, textfilenames)
	get_top_keywords_2(tfidf, tfidfer.get_feature_names_out())

