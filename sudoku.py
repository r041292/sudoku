# coding: cp437
class Casilla:
	i = -99
	j = -99
	restricciones = []
	numRestricciones = -99
	numPosibilidades = -99

	def __init__(self,i,j):
		self.i=i
		self.j=j


	def addRestriccion(self,value):
		self.restricciones.append(value)


fileName=""
fileName = raw_input('Digite la direccion o nombre del archivo:  ')
file = open(fileName,'r')
fileContent = file.read()
#print (fileContent)

sudokuTam=4
lineaTemporal = fileContent.split("\n")
sudoku = []
sudokuHistorico = []
casillas = []
#sudokuHistorico.append()
#sudokuHistorico.pop()

for i in range(0,sudokuTam):
	sudoku.append(lineaTemporal[i].split(","))

#print(sudoku[0][2])

for i in range(0,sudokuTam):
	for j in range(0,sudokuTam):
		if sudoku[i][j] == "0" :
			tempCasilla = Casilla(i,j)
			casillas.append(tempCasilla)


for i in range (0, len(casillas)):
	print (casillas[i])


