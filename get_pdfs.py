import csv
import urllib.request

filename = "cases2.csv"
complaint_pdfs = "complaints_pdfs/"
orders_pdfs = "orders_pdfs/"

file = open(filename, "r")
reader = csv.reader(file)

for line in reader: 
	casename = line[0]
	complaintfile = line[1]
	cdfile = line[2]
	date = line[3]
	print(date)
	
	casename_clean = date + "".join(e for e in casename if e.isalnum())
	complaintfilename = complaint_pdfs + casename_clean + "_complaint.pdf"
	cdfilename = orders_pdfs + casename_clean + "_order.pdf"

	if complaintfile !=  "Complaint URL" and complaintfile != "": 
		urllib.request.urlretrieve(complaintfile, complaintfilename)
	if cdfile != "Agreement URL" and cdfile != "":
		urllib.request.urlretrieve(cdfile, cdfilename)
