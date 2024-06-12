import sys
import os



def contains_keywords(file, keywords):
	with open(file) as f:
		contents = f.read().replace("\n", " ").lower() 
		for keyword in keywords:
			if keyword in contents: 
				return True
	return False





if __name__ == '__main__':
	dir = sys.argv[1]
	text_files = [dir + "/" + f for f in os.listdir(dir) if f.endswith(".txt")]
	text_files.sort()
	print(len(text_files))
	
	keywords = []
	for keyword in sys.argv[2:]:
		keywords.append(keyword)

	contains_list = []
	
	for f in text_files: 
		contains = contains_keywords(f, keywords)
		if contains:
			contains_list.append(f.split("/")[-1])
		print(f + ": " + str(contains))

	print(str(len(contains_list)) + " out of " + str(len(text_files)) + " contain the keywords " + str(keywords))

	print(str(contains_list))
