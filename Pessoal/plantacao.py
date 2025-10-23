def imprime(matriz):
	for i in matriz:
	    print(i)


def Gera_Matriz_Plantio(sementes,area,area_plantio,matriz):
	i_p = 0
	j_p = 0
	for semente in sementes:
		print("i_p = ",i_p,"\nj_p = ",j_p)
		for i in range(i_p,area):
			cout = 0
			for j in range(j_p,area):
				if cout >= area_plantio:
					break
				matriz[i][j] = semente
				imprime(matriz)
				cout += 1
			if i == area_plantio-1:
				i_p += area_plantio
				break
			elif i == area-1:
				j_p += area_plantio
				i_p = 0
				break

def Calcula_Area_Plantio(area,sementes):
	if area%len(sementes) == 0:
		return 2
	else:
		return 1

def Gera_Matriz(area):
	matriz = []
	for i in range(area):
		lista = []
		for j in range(area):
			lista.append(0)
		matriz.append(lista)
	return matriz


sementes = ["Entities.Grass","Entities.Tree","Entities.Carrot","Entities.Pumpkin","Entities.Sunflower","Entities.Bust"]
area = 8
area_plantio = Calcula_Area_Plantio(area,sementes)
print(area_plantio)
area_plantio = int(area/area_plantio)
print(area_plantio)
matriz = Gera_Matriz(area)

imprime(matriz)
print()
Gera_Matriz_Plantio(sementes,area,area_plantio,matriz)
imprime(matriz)
