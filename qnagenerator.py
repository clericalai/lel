#!/usr/bin/python


counter = 0
minuscounter = 0

legalelements = [
 {
  'name': 'Eviction',
  'question': 'Are you being evicted?',
  'plainEnglish': 'A landlord can only evict a tenant by filing an eviction action in court and meeting the legal requirements.',
  'elements': ['Grounds','OtherDefenses']
 },
 {
  'name': 'Grounds',
  'question': 'Does the landlord have a good reason to evict you?',
  'plainEnglish': 'A landlord can only evict you if the lease is over or there is a good reason.',
  'elements': ['Nonpayment','ExpiredLease']
 }, 
 {
  'name': 'Nonpayment',
  'question': 'Is the landlord evicting you because you have not paid rent?',
  'plainEnglish': 'A landlord can evict a tenant who has not paid full rent on time.',
  'elements': []
 }, 
 {
  'name': 'ExpiredLease',
  'question': 'Is the landlord evicting you because the lease is expired?',
  'plainEnglish': 'A landlord can evict a tenant after a lease is expired.',
  'elements': []
 }, 
 {
  'name': 'OtherDefenses',
  'question': 'Do you have other defenses?',
  'plainEnglish': 'You may have defenses like discrimination or retaliation.',
  'elements': []
 }
]
f = open('test.txt', 'w')
for i in range(0,counter):
  f.write("\t")
f.write("Q(")
f.write(legalelements[0]['name'])
f.write("): ")
f.write(legalelements[0]['question'])
f.write("\n")
for i in range(0,counter):
  f.write("\t")
f.write("A: Yes\n")
counter = counter + 1
for i in range(0,counter):
    f.write("\t")
f.write("Q(")
f.write(legalelements[0]['name'])
f.write("Explainer): ")
f.write(legalelements[0]['plainEnglish'])
f.write("\n")
for i in range(0,counter):
    f.write("\t")
f.write("A: Continue\n")
e = 0
for x in legalelements[0]['elements']:
	for y in legalelements:
		if y['name'] == x:
			counter = counter + 1
			for i in range(0,counter):
				f.write("\t")
			f.write("Q(")
			f.write(y['name'])
			f.write("): ")
			f.write(y['question'])
			f.write("y\n")
			for i in range(0,counter):
				f.write("\t")
			f.write("A: Yes\n")
			for u in y['elements']:
				for v in legalelements:
					if v['name'] == u:
						counter = counter + 1
						minuscounter = minuscounter + 1
						for i in range(0,counter):
							f.write("\t")
						f.write("Q(")
						f.write(v['name'])
						f.write("): ")
						f.write(v['question'])
						f.write("\n")
						for i in range(0,counter):
							f.write("\t")
						f.write("A: Yes\n")
			counter = counter - minuscounter
			minuscounter = 0

