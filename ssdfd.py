import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# finditer finds all the detail of the matches as well as all the matches
# findall finds all the matches and it literally presents the string values
# search and match give the first match of the condition 
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'\d{3}-\d{3}-\d{4}',re.I)

with open('data.txt') as f:
	contents=f.read()
	matches =pattern.findall(contents)
	for match in matches:
		print(match)
		print(re.sub('\-','---',match))

