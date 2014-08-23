# coding: cp437
class Casilla:
	i = -99
	j = -99
	restricciones = []
	posibilidades = []
	numRestricciones = -99
	numPosibilidades = -99

	def __init__(self,i,j):
		self.i=i
		self.j=j
		self.restricciones = []
		self.posibilidades = []
		self.numRestricciones = -99
		self.numPosibilidades = -99


	def verificarCuadrante(self,sudoku,inicioX,inicioY,limX,limY):
		for i  in range(inicioX,limX):
			for j  in range(inicioY,limY):
				try:
					yaAgregado = self.restricciones.index(sudoku[i][j])
				except ValueError:
					yaAgregado = -1

				if(yaAgregado ==-1 and sudoku[i][j]!="0"):
					#print ("Se agrego cuadrante: ",sudoku[i][j])
					self.restricciones.append(sudoku[i][j])


	def calPosibilidades(self,sudokuTam):
		for i in range(1,sudokuTam+1):
			try:
				esRestriccion = self.restricciones.index(str(i))
			except:
				esRestriccion= -1

			if(esRestriccion==-1):
				self.posibilidades.append(str(i))


	def calRestricciones(self,sudoku,sudokuTam):
		for i in range(0,sudokuTam):

			try:
				yaAgregadoI=self.restricciones.index(sudoku[self.i][i])
			except ValueError:
				yaAgregadoI = -1

			if(yaAgregadoI == -1 and sudoku[self.i][i] != "0"):
				#print ("Se agrego por fila: ",sudoku[self.i][i] )
				self.restricciones.append(sudoku[self.i][i])

			try:
				yaAgregadoJ=self.restricciones.index(sudoku[i][self.j])
			except ValueError:
				yaAgregadoJ = -1

			if(yaAgregadoJ ==-1 and sudoku[i][self.j] != "0"):
				#print ("Se agrego por columna: ",sudoku[i][self.j])
				self.restricciones.append(sudoku[i][self.j])

		if(sudokuTam==4):
			if(self.i<2 and self.j<2):
				self.verificarCuadrante(sudoku,0,0,2,2)
				#esta en el primer cuadrante
			else:
				if(self.i>=2 and self.j<2):
					self.verificarCuadrante(sudoku,2,0,4,0)
					#esta en el segudo cuadrante
				else:
					if(self.i<2 and self.j>=2):
						self.verificarCuadrante(sudoku,0,2,2,4)
						#esta en el tercer cuadrante
					else:
						self.verificarCuadrante(sudoku,2,2,4,4)
						#esta en el cuarto cuadrante

		self.calPosibilidades(sudokuTam)
		self.numRestricciones = len(self.restricciones)
		self.numPosibilidades = sudokuTam - len(self.restricciones)
		#print("Las restricciones son:",self.restricciones)
		#print("las posibilidades son:", self.posibilidades)



fileName=""
fileName = raw_input('Digite la direccion o nombre del archivo:  ')
file = open(fileName,'r')
fileContent = file.read()

sudokuTam=4
lineaTemporal = fileContent.split("\n")
sudoku = []
sudokuHistorico = []
casillas = []
#sudokuHistorico.append()
#sudokuHistorico.pop()

for i in range(0,sudokuTam):
	sudoku.append(lineaTemporal[i].split(","))



for i in range(0,sudokuTam):
	for j in range(0,sudokuTam):
		if sudoku[i][j] == "0" :
			casillas.append(Casilla(i,j))

for i in range(0,len(casillas)):
	#print('casilla: ',casillas[i].i,casillas[i].j)
	casillas[i].calRestricciones(sudoku,sudokuTam)





