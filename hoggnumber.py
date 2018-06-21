import numpy as np 
import os
import ads
import sys
from astropy.table import Table 

token = os.environ.get('ADS_DEV_KEY', None)
if token:
	ads.config.token = token

#list of people at hack day 

people = Table.read('hoggnumber/participants.csv')

participants=[]
for n in range(len(people)):
	participants.append(str(people['surname'][n])+','+str(people['name'][n]))

participants.append('Foreman-Mackey,Daniel')
participants.remove('Hogg,David')

#Get list of Hogg coauthors 
hogg_coauthors = []
hogg_papers = list(ads.SearchQuery(author="Hogg, David", max_pages=10))
for paper in hogg_papers:
	for author in paper.author:
		if any(author in s for s in hogg_coauthors):
			pass
		else:
			hogg_coauthors.append(author)

#Get list of participant coauthors
for participant in participants:
	globals()[participant.split(',')[0]+'_coauthors'] = []
	globals()[participant.split(',')[0]+'_papers'] = list(ads.SearchQuery(author=participant, max_pages=10))
	for paper in globals()[participant.split(',')[0]+'_papers']:
		for author in paper.author:
			if any(author in s for s in globals()[participant.split(',')[0]+'_coauthors']):
				pass
			else:
				globals()[participant.split(',')[0]+'_coauthors'].append(author)


hogg_0= "Hogg, David"
hogg_1 = []
for participant in participants.copy():
	if any(participant.split(',')[0]+', '+participant.split(',')[1][:1] in s for s in hogg_coauthors):
		hogg_1.append(participant)
		participants.remove(participant)
	else:
		pass

print('updated list of',participants)


hogg_2 = []
for participant in participants.copy():
	print('participant is ', participant)
	n=0
	for hoggs in hogg_1:
		print('hogg ', hoggs.split(', ')[0]+','+hoggs.split(',')[1][:1])
		if any(hoggs.split(',')[0]+', '+hoggs.split(',')[1][:1] in s for s in globals()[participant.split(',')[0]+'_coauthors']):
			n+=1
			print('added one to n for', participant.split(',')[0], ' , ', hoggs.split(',')[0])
		else:
			pass
	if n > 0:
		hogg_2.append(participant)
		participants.remove(participant)

if len(hogg_2) > 0:

	hogg_3 = []
	for participant in participants.copy():
		n=0
		for hoggs in hogg_2:
			if any(hoggs.split(',')[0]+', '+hoggs.split(',')[1][:1] in s for s in globals()[participant.split(',')[0]+'_coauthors']):
				n+=1
			else:
				pass
		if n > 0:	
			hogg_3.append(participant)
			participants.remove(participant)
else:
	sys.exit('Nobody with Hogg Number of 2')

if len(hogg_3) > 0:

	hogg_4 = []
	for participant in participants.copy():
		n=1
		for hoggs in hogg_3:
			if any(hoggs.split(',')[0]+', '+hoggs.split(',')[1][:1] in s for s in globals()[participant.split(',')[0]+'_coauthors']):
				n+=1
			else:
				pass
		if n > 0:
			hogg_4.append(participant)
			participants.remove(participant)
else:
	sys.exit('Nobody with Hogg Number of 3')


if len(hogg_4) > 0:

	hogg_5 = []
	for participant in participants.copy():
		n=0
		for hoggs in hogg_4:
			if any(hoggs.split(',')[0]+', '+hoggs.split(',')[1][:1] in s for s in globals()[participant.split(',')[0]+'_coauthors']):
				n+=1
			else:
				pass
		if n >0:
			hogg_5.append(participant)
			participants.remove(participant)
else:
	sys.exit('Nobody with Hogg Number of 4')


print('Number of people with Hogg number of 5 is ', len(hogg_5))