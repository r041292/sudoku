# coding: cp437
import copy

class Casilla:
	i = -99
	j = -99
	val= 0
	restricciones = []
	posibilidades = []
	numRestricciones = -99
	numPosibilidades = -99

	def __init__(self,i,j):
		self.i=i
		self.j=j
		self.val=0
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

		if(sudokuTam == 9):
			if(self.j<3):
				if(self.i<3):
					self.verificarCuadrante(sudoku,0,0,3,3)
					#esta en el primer noveno
				else:
					if (self.i<6):
						self.verificarCuadrante(sudoku,3,0,6,2)
						#esta en el segundo noveno
					else:
						self.verificarCuadrante(sudoku,6,0,9,2)
						#esta en el tercer noveno
			else:
				if(self.j<6):
					if(self.i<3):
						self.verificarCuadrante(sudoku,0,3,3,6)
						#esta en el cuarto noveno
					else:
						if (self.i<6):
							self.verificarCuadrante(sudoku,3,3,6,6)
							#esta en el quinto noveno
						else:
							self.verificarCuadrante(sudoku,6,3,9,6)
							#esta en el sexto noveno
				else:
					if(self.i<3):
						self.verificarCuadrante(sudoku,0,6,3,9)
						#esta en el septimo noveno
					else:
						if (self.i<6):
							self.verificarCuadrante(sudoku,3,6,6,9)
							#esta en el octavo noveno
						else:
							self.verificarCuadrante(sudoku,6,6,9,9)
							#esta en el noveno noveno

		self.calPosibilidades(sudokuTam)
		self.numRestricciones = len(self.restricciones)
		self.numPosibilidades = sudokuTam - len(self.restricciones)
		#print("Las restricciones son:",self.restricciones)
		#print("las posibilidades son:", self.posibilidades)


def restRelativas(casillas):
	sumRestricciones=0
	for i in range(0,len(casillas)):
		sumRestricciones+=casillas[i].numRestricciones

	try:
		return (sumRestricciones*1.0)/len(casillas)
	except ZeroDivisionError:
		return 999




fileName=""
fileName = raw_input('Digite la direccion o nombre del archivo:  ')
file = open(fileName,'r')
fileContent = file.read()

lineaTemporal = fileContent.split("\n")
sudokuTam= len(lineaTemporal)
sudoku = []
sudokuHistorico = []
casillasHistorico = []
casillas = []
#sudokuHistorico.append()
#sudokuHistorico.pop()

###################


#regresa el indiciador del vector posibilidades que genera mas restricciones
def mejorPosibilidad(sudoku,casilla):
	max=-1
	indicador=-1
	#print(casilla.i,casilla.j)
	for x in range(0,casilla.numPosibilidades):
		sudokutemp=sudoku
		valorPosible =casilla.posibilidades[x]
		sudokutemp[casilla.i][casilla.j]=valorPosible
		casillasTemporal = []
		for i in range(0,sudokuTam):
			for j in range(0,sudokuTam):
				if sudokutemp[i][j] == "0" :
					casillasTemporal.append(Casilla(i,j))

		for i in range(0,len(casillasTemporal)):
			#print('casilla: ',casillas[i].i,casillas[i].j)
			casillasTemporal[i].calRestricciones(sudoku,sudokuTam)
		if(restRelativas(casillasTemporal)>max):
			indicador=x
			max=restRelativas(casillasTemporal)

	#print indicador
	return indicador


######################

for i in range(0,sudokuTam):
	sudoku.append(lineaTemporal[i].split(","))



for i in range(0,sudokuTam):
	for j in range(0,sudokuTam):
		if sudoku[i][j] == "0" :
			casillas.append(Casilla(i,j))

for i in range(0,len(casillas)):
	#print('casilla: ',casillas[i].i,casillas[i].j)
	casillas[i].calRestricciones(sudoku,sudokuTam)

iteracion = 0
while(restRelativas(casillas)!=999):
	iteracion+=1
	print("Iteracion Numero:",iteracion)
	print("sudoku")
	for i in range (0,sudokuTam):
		print sudoku[i]

	restRelativas1=restRelativas(casillas)
	#print(restRelativas1)
	min=999
	indicador=-1
	for i  in range(0,len(casillas)):
		if(casillas[i].numPosibilidades<min):
			min=casillas[i].numPosibilidades
			indicador=i
			#print("largo historico",len(sudokuHistorico))
	casillaTemporal = casillas[indicador]
	if(casillaTemporal.numPosibilidades>0):
		sudokuHistorico.append(copy.deepcopy(sudoku))
		mejorInidicador = mejorPosibilidad(sudoku,casillaTemporal)
		sudoku[casillaTemporal.i][casillaTemporal.j]=casillaTemporal.posibilidades[mejorInidicador]
		casillas[indicador].val=casillaTemporal.posibilidades[mejorInidicador]
		print("casilla modificada: ",casillaTemporal.i,casillaTemporal.j," valor agregado: ",casillas[indicador].val)
		print("restricciones de la casilla", casillaTemporal.restricciones)
		casillas[indicador].posibilidades.remove(casillas[indicador].val)
		casillas[indicador].numPosibilidades-=1
		casillasHistorico.append(copy.deepcopy(casillas))
		#print("largo historico",len(sudokuHistorico))

		casillas=[]
		for i in range(0,sudokuTam):
			for j in range(0,sudokuTam):
				if sudoku[i][j] == "0" :
					casillas.append(Casilla(i,j))

		for i in range(0,len(casillas)):
			#print('casilla: ',casillas[i].i,casillas[i].j)
			casillas[i].calRestricciones(sudoku,sudokuTam)
	
		#print(len(casillas))
		#print(restRelativas(casillas))
	else:
		#print("back tracking ----- ")
		sudoku= sudokuHistorico.pop()
		casillas=casillasHistorico.pop()


print("Resultado: ")
for i in range (0,sudokuTam):
        print sudoku[i]
