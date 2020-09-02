import re
import os 
import glob
import csv
import pandas as pd


path=os.getcwd()
target = 'Training-Set-2018/'

entries = os.listdir(target)

for entry in entries:



	print(entry)

	if entry == 'FilterSent':
		continue
	temPath = path+'/'+target+entry+'/Reference_XML/'
	print(temPath)
	temPath2 = glob.glob(temPath+entry+'.csv')[0]
	temPath3 = 'no name'
	# for name in temPath2:

	# 	if '_' not in name:
	# 		temPath3 = name
	# 		break

	print(temPath2)
	print(temPath3)
	filename = temPath2.split('/')[-1]
	print(filename)

	# print(inputFile)
	outTable = temPath+filename.rstrip(".csv")+"_table.csv"
	outFigure = temPath+filename.rstrip(".csv")+"_fig.csv"
	# outpath = temPath+filename.rstrip(".xml") + ".csv"
	print(outTable)
	print(outFigure)

	tab = re.compile('Table \d:')
	fig = re.compile('Figure \d:')

	file = temPath2
	print(file)
	df_table = pd.read_csv(file)

	print(df_table.head())
	lst = list(df_table.sentence)


	cnt_tbl=0
	cnt_fig =0
	with open(outTable,'w', newline = '')as f:
		thewriter = csv.writer(f)
		listRow = ['id', 'caption']
		thewriter.writerow(listRow)	

		for line in lst:
			if re.search(tab,line):
				out = line.split(':')[1].split('. ')[0]

				thewriter.writerow([cnt_tbl,out])
				cnt_tbl=cnt_tbl+1




	with open(outFigure,'w', newline = '')as f2:
		thewriter = csv.writer(f2)
		listRow = ['id', 'caption']
		thewriter.writerow(listRow)	

		for line in lst:
			if re.search(fig,line):
				out = line.split(':')[1].split('. ')[0]

				thewriter.writerow([cnt_fig,out])
				cnt_fig=cnt_fig+1


