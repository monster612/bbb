a=int(input('what year were you born?'))
b=int(input('what month were you born?'))
c=int(input('what day were you born?'))
print('It looks like you were on ',a,'/',b,'/',c)
if b==12:
	c=54+c
	print('Looks like your birthday is in',c,'days.')
elif b>=11:
    c=24+c
    print('Looks like your birthday is in',c,'days.')
elif b>=10 and c>7:
    c=c-7
    print('Looks like your birthday is in',c,'days.')
elif b>=10 and c==7:
    print('HAPPY BIRTHDAY')	
else:
	print('Looking forward to your next birthday')