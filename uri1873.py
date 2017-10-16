C = int(input())
for i in range(C):
	test,test2 = map(str,input().split())
	if test == test2:
		nome = "empate"
	else:
		if test == "tesoura" and test2 == "papel" or test == "tesoura" and test2 == "lagarto":
			nome = "rajesh"
		elif test == "papel" and test2 == "pedra" or  test == "papel" and test2 == "spock":
			nome = "rajesh"
		elif test == "pedra" and test2 == "lagarto" or  test == "pedra" and  test2 == "tesoura":
			nome = "rajesh"
		elif test == "lagarto" and test2 == "spock" or test == "lagarto" and test2 == "papel":
			nome = "rajesh"
		elif test == "spock" and test2 == "tesoura" or test == "spock" and test2 == "pedra":
			nome = "rajesh"
		else:
			nome = "sheldon"
	print(nome)
