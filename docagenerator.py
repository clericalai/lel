#!/usr/bin/python3



elementcounter = 0

legalelements = [
 {
  'name': 'Eviction',
  'question': 'Are you being evicted?',
  'explainer': 'A landlord can only evict a tenant by filing an eviction action in court and meeting the legal requirements.',
  'elements': ['Grounds','OtherDefenses'],
  'backwardsbetter': False,
  'description':"Eviction",
  'questionlong':"",
  'answery':"",
  'answern':""
 },
 {
  'name': 'Grounds',
  'question': 'Does the landlord have a good reason to evict you?',
  'explainer': 'A landlord can only evict you if the lease is over or there is a good reason.',
  'elements': ['Nonpayment','ExpiredLease'],
  'backwardsbetter': False,
  'description':"Grounds",
  'questionlong':"",
  'answery':"",
  'answern':""
 }, 
 {
  'name': 'Nonpayment',
  'question': 'Is the landlord evicting you because you have not paid rent?',
  'explainer': 'A landlord can evict a tenant who has not paid full rent on time.',
  'elements': [],
  'backwardsbetter': False,
  'description':"Nonpayment",
  'questionlong':"Have you paid rent and any applicable late fees in full and on time as agreed in your lease (written or oral)?",
  'answery':"Collect payment receipts, your check register and/or bank/payment card records, and any other evidence of payment. Consider sending copies of these along with a letter explaining that you have paid your obligations as required. The landlord may have simply made an oversight, and your letter could save you both the trouble and expense of unnecessary litigation.",
  'answern':"I'm afraid it looks like you might not have a strong defense against eviction. Still, appear at the court hearing and bring any evidence which you think might support your reason for not paying rent as agreed."
 }, 
 {
  'name': 'ExpiredLease',
  'question': 'Is the landlord evicting you because the lease is expired?',
  'explainer': 'A landlord can evict a tenant after a lease is expired.',
  'elements': [],
  'backwardsbetter': False,
  'description':"Expired Lease",
  'questionlong':"Did your landlord give you notice to vacate of at least one lease 'period'? (one month if month-to-month, one week if week-to-week, etc.)",
  'answery':"A landlord may terminate this form of lease with at least one period of notice. This is not eviction and is legal.",
  'answern':"You cannot be evicted without proper written notice as long as you have paid rent as agreed and otherwise upheld your end of the lease agreement."
 }, 
 {
  'name': 'OtherDefenses',
  'question': 'Do you have other defenses?',
  'explainer': 'You may have defenses like discrimination or retaliation.',
  'elements': ['Discrimination','Retaliation'],
  'backwardsbetter': True,
  'description':"Other Defenses",
  'questionlong':"",
  'answery':"",
  'answern':""
 }, 
 {
  'name': 'Discrimination',
  'question': 'Is the landlord discriminating against you?',
  'explainer': 'You may have defenses like discrimination or retaliation.',
  'elements': [],
  'backwardsbetter': True,
  'description':"Discrimination",
  'questionlong':"Is the landlord discriminating against you based on race, ethnicity, national origin, religion, gender, disability, or the fact that I have children.",
  'answery':"You cannot be evicted for these reasons, and your landlord may be subject to separate legal consequences for violating these laws. You can find more information about housing discrimination in Kentucky and your rights at http://www.kyhousing.org/Resources/Planning-Documents/Pages/Fair-Housing-in-Kentucky.aspx. Bring evidence supporting your defense that the eviction is discriminatory, the agencies listed above and Legal Aid can help you determine the best evidence to bring to court.",
  'answern':""
 }, 
 {
  'name': 'Retaliation',
  'question': 'Is the landlord retaliating against you?',
  'explainer': 'You may have defenses like discrimination or retaliation.',
  'elements': [],
  'backwardsbetter': True,
  'description':"Retaliation",
  'questionlong':"Retaliatory eviction is illegal in most states. In URLTA jurisdictions in Kentucky, an eviction is presumed to be retaliatory if it takes place within 1 year of a tenant's exercise of their legal rights including reports of housing/building code violations, complaining to your landlord, or joining a tenant union or similar tenant organization. Retaliation in other forms including increased rent, decreased services, or threats to do so is also illegal. Is your landlord retaliating within 1 year of your report?",
  'answery':"The eviction is therefore presumed retaliatory. It is illegal unless your landlord can show a valid, non-retaliatory reason for eviction. Bring evidence of your report, including a copy of the report, any correspondence with the agency to which you reported, correspondence with your landlord, and evidence of the housing/building code violation you reported. Also bring evidence of any other retaliation by the landlord for this report.",
  'answern':"The eviction will not necessarily be PRESUMED retaliatory, but you may still be able to prove that it is and have it prevented at the eviction hearing at court. Bring evidence of your report, including a copy of the report, any correspondence with the agency to which you reported, correspondence with your landlord, and evidence of the housing/building code violation you reported. Also bring evidence of any other retaliation by the landlord for this report."
 }
]
f = open('test.txt', 'w')
for i in legalelements:
	if not i['elements']:
# BLOCK 2
		f.write("---\n")
		f.write("code: |\n")
		f.write("  if ")
		f.write(i['name'])
		f.write('isrelevant:\n')
		f.write('    if ')
		f.write(i['name'])
		f.write('trigger:\n')
		if i['backwardsbetter']:
			f.write('      relevantinformation.append("')
			f.write(i['answern'])
			f.write('")\n')
			f.write('      ')
			f.write(i['name'])
			f.write("ismet = False\n")
		else:
			f.write('      relevantinformation.append("')
			f.write(i['answery'])
			f.write('")\n')
			f.write('      ')
			f.write(i['name'])
			f.write("ismet = True\n")
		f.write('    else:\n')
		if i['backwardsbetter']:
			f.write('      relevantinformation.append("')
			f.write(i['answery'])
			f.write('")\n')
			f.write('      ')
			f.write(i['name'])
			f.write("ismet = True\n")
		else:
			f.write('      relevantinformation.append("')
			f.write(i['answern'])
			f.write('")\n')
			f.write('      ')
			f.write(i['name'])
			f.write("ismet = False\n")
		f.write('  else:\n')
		f.write('    ')
		f.write(i['name'])
		f.write("ismet = True\n")
# Block 3
		f.write("---\n")
		f.write("question: |\n")
		f.write('  ')
		f.write(i['description'])
		f.write('\n')
		f.write('subquestion: |\n')
		f.write('  ')
		f.write(i['questionlong'])
		f.write('\n')
		f.write('yesno: ')
		f.write(i['name'])
		f.write('trigger\n')
		f.write('---\n')
	else:
# BLOCK 1
		f.write('---\n')
		f.write('code: |\n')
		elementcounter = 0
		for j in i['elements']:
			elementcounter = elementcounter + 1
			if elementcounter == 1:
				f.write('  if ')
				f.write(j)
				f.write('ismet:\n')
				f.write('    ')
				f.write(i['name'])
				f.write('ismet = True\n')
			else:
				f.write('  elif ')
				f.write(j)
				f.write('ismet:\n')
				f.write('    ')
				f.write(i['name'])
				f.write('ismet = True\n')
		f.write('  else:\n')
		f.write('    ')
		f.write(i['name'])
		f.write('ismet = False\n')
		f.write('---\n')
		f.write('question: |\n')
		f.write('  ')
		f.write(i['question'])
		f.write('\n')
		f.write('subquestion: |\n')
		f.write('  ')
		f.write(i['explainer'])
		f.write('\n')
		f.write('fields:\n')
		f.write("  - note: Leave blank if no or you don't know\n")
		for j in i['elements']:
			for h in legalelements:
				if j == h['name']:
					f.write('  - ')
					f.write(h['question'])
					f.write(': ')
					f.write(j)
					f.write('isrelevant\n')
					if h['backwardsbetter']:
						f.write('    datatype: noyes\n')
					else:
						f.write('    datatype: yesno\n')
		f.write('---\n')
		


