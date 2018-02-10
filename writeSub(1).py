import sys

helpText = '''
  =================HELP=================
  Usage: python writeSub.py --input * --num * --output * --h
  Default: python writeSub.py --input input.txt --num 10000 --output output
  ======================================'''

arg={'--input': "input.txt", '--num': 10000, '--output': "output", '--h': None}

if len(sys.argv)%2==1:
  for i in range(len(sys.argv)/2):
    arg[sys.argv[2*i+1]]=sys.argv[2*i+2]
else:
  if sys.argv[1]!='--h': print 'The number of arguments is wrong!'
  print helpText
  sys.exit(1)

filename = arg['--input']
numPerFile = int(arg['--num'])
outname = arg['--output']

with open(filename, mode='r') as f:
	lines = f.readlines()
	lastInt = int(len(lines)/numPerFile)
	m = 0
	for i in range(lastInt):
		with open(outname+"_"+str(i)+".txt", mode='w') as fout:
			for k in range(numPerFile):
				fout.write(lines[m+k])
		m += numPerFile
	if m < len(lines):
		with open(outname+"_"+str(lastInt)+".txt", mode='w') as fout:
			for line in lines[m:]:
				fout.write(line)

