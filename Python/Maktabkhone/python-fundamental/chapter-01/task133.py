n = int(input())
rim = 0
r = 0
if (n>=0) and (n<=999):
		rim = n%10
		r = r*10 + rim
		n = n//10
		
		rim = n%10
		r = r*10 + rim
		n = n//10

		rim = n%10
		r = r*10 + rim
		n = n//10

		print(r*2)

	
	