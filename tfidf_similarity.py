from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import os
from matplotlib import pyplot as plt
import numpy as np

def process(file): 
	with open(file, "r") as f: 
		tokens = word_tokenize(f.read())
		tokens = [w.lower() for w in tokens]
		words = [word for word in tokens if word.isalpha()]
		

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

if __name__ == '__main__':
	dir = sys.argv[1]
	text_files = [dir + "/" + f for f in os.listdir(dir) if f.endswith(".txt")]
	text_files.sort() 
	documents = [open(f).read() for f in text_files]
	print(len(text_files))
	tfidf = TfidfVectorizer().fit_transform(documents)
	pairwise_similarity = tfidf * tfidf.T
	print(pairwise_similarity)
	textfilenames = [t.split("/")[-1].split("_")[0] for t in text_files]
	heatmap(textfilenames, textfilenames, pairwise_similarity.toarray())
