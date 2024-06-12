# FTC Enforcement Actions Against Unfair and Deceptive Cyber Practices

Read the report [here](https://dfrlab.org/2024/06/12/forty-seven-cases-ftc-cyber/).

This repo provides the utils scripts and the data used for this analysis. The two folders complaints_txts and orders_txts contain the text file versions of the orders (fair warning, they are not perfectly cleaned -- we added a cleaning step in our analysis). You can experiment with regenerating these using the get_pdfs and scrape_pdf_text scripts. 

The search_keyword script allows you to search for keywords within the files (it is case-insensitive). The tfidf_similarity script and the embedding_similarity script both generate heatmaps visualizing the pairwise similarity of the complaints or consent decrees (specified by command-line argument) using two different similiarity comparisons. The clusters script does k-means clustering of the complaints or consent decrees and shows some of the words most strongly associated with each cluster.  

All of these scripts are offered for the purposes of research and experimentation -- they might be flawed or incomplete! 

If you have any questions, please reach out to the authors: mhamin@atlanticcouncil.org, nmessieh@atlanticcouncil.org, and iwright@atlanticcouncil.org. 


