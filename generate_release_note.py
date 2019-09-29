import re

regex = r"\[FIX\].*"

#test_str = "e75674b37bc - i350970, 5 days ago : [FIX] sap.m.Select: Fixed incorrect click behaviour in Quartz Light"

with open('git_log.txt','r') as f:
    test_str = f.read()
    matches = re.finditer(regex, test_str, re.MULTILINE)

#for i, line in enumerate(open('git_log.txt')):
#    for match in re.finditer(regex, line):
#        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

fixed_issue = ''
for matchNum, match in enumerate(matches, start=1):
    fixed_issue += match.group() + '\n'
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

with open('Release-Note', 'w') as f:
    f.write('Releas Notes:\n')
    f.write(f'Issues: {matchNum} issues fixed.\n\n')
    f.write('Bug\n')
    f.write(fixed_issue)
