import sys 
import getopt 


start_date=None
end_date=None
	
argv=sys.argv[1:]

try:
	opts, args = getopt.getopt(argv,"s:e")
except getopt.GetoptError as err:
	print(err)
	opts=[]

for opt,arg in opts:
	if opt in ['-s']:
		start_date = arg
	elif opt in ['-e']:
		end_date = arg

print('start_date: {}'.format(start_date))
print('end_date: {}'.format(end_date))


