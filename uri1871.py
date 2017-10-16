num,num2 = map(int,input().split())
while num != 0 and num2 != 0:
	num += num2
	num = str(num)
	for i in range(len(num)):
		if num[i] != "0":
			print(num[i],end='')
	print()
	num,num2 = map(int,input().split())
