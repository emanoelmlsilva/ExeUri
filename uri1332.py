totPalavra = int(input())
for i in range(totPalavra):
	palavra = input()
	if len(palavra) == 5:
		num = 3
	else:
		if palavra[0] == "o" or palavra[2] == "e":
			num = 1
		elif (palavra[0] == "t" or palavra[2] == "o"):
			num = 2
	print(num)

