class Operation :
	def __init__(self, tarea, indexOp, duration):
		self.tarea=tarea
		self.indexOp=indexOp
		self.duration=duration
	def setNextOp(self, operation):
		self.nextOp=operation
	def setTarea(self, tarea):
		self.tarea=tarea

class Machine :
	def __init__(self, state, currentOp, supportedOps):
		self.state="free"
		self.currentOp=None
		self.supportedOps=list()
class Task :
	def __init__(self, state, ops):
		self.state="unstarted"
		self.ops=list() #Operations are a list with the ops in the right orden of ops

def fitness(solution):
	executionOps=[c[0] for c in solution]
	executionTimes=[c.duration for c in executionOps]
	maqTopIndex=[len(c) for c in solution]
	maqIndex=[1 for _ in solution]
	maqTime=[0 for _ in solution]
	maqFinishTime=[0 for _ in solution]
	oldOps=list()
	flag=True
	M=len(solution)
	x=0
	sF=0
	k=0
	while x<M+1:
		t=min(executionTimes)
		#print(t, maqTime, maqIndex, executionTimes, maqFinishTime,"\n")
		printOps(executionOps)
		for i in range(M):
			if t>=maqTime[i]+executionOps[i].duration:
				if maqIndex[i]<maqTopIndex[i]:
					maqTime[i]=maqTime[i]+executionOps[i].duration
					executionOps[i]=solution[i][maqIndex[i]]
					maqIndex[i]+=1
				else:
					if maqFinishTime[i]==0:
						maqFinishTime[i]=maqTime[i]+executionOps[i].duration
						oldOps.append(executionOps[i])
						executionOps[i].duration=10000000000
					x+=1
			executionTimes[i]=maqTime[i]+executionOps[i].duration
		#aqui ya estan en executionOps las operaciones en ese instante t
		sF+=sortBalance(executionOps, oldOps)
		k+=max(maqFinishTime)
		t=min(executionTimes)
	print(str(500-(k+sF))+"\n")


def sortBalance(actualOps, oldOps):
	balance = 0
	for actOp in actualOps:
		if actOp.duration!=10000000000:
			for oldOp in oldOps:
				if actOp.indexOp<oldOp.indexOp and actOp.tarea==oldOp.tarea:
					balance+=5*(oldOp.indexOp-actOp.indexOp)
				if actOp.indexOp==oldOp.indexOp and actOp.tarea==oldOp.tarea:
					balance+=10
				if actOp.indexOp>oldOp.indexOp and actOp.tarea==oldOp.tarea:
					balance-=2*(1/(actOp.indexOp-oldOp.indexOp))
	return balance
def printOps(ops):
	string = "["
	for op in ops:
		string+="("+str(op.tarea)+", "+str(op.indexOp)+", "+str(op.duration)+"), "
	print(string[:-1]+"]\n")

def main():
	ops=list()
	tarea=Task("unfinished", ops)
	sol=[[Operation(0, 0, 7), Operation(0, 0, 3)],
	[Operation(1, 1, 2), Operation(1, 0, 15), Operation(2, 0, 12), Operation(1, 0, 5)],
	[Operation(1, 0, 9), Operation(0, 0, 1)]]

	fitness(sol)
main()

""" #### 3) Especificación del flujo de datos entre capas
* La primer capa recibira y enviara al ambiente cadenas codificadas, con el estado de las maquinas y ordenes, respectivamente. Lo que recibira del ambiente sera el estado de cada maquina, más detalladamente, recibirá un listado que contenga una estructura que le indicara la operación que se encuentra en ejecución o si esta sin operación en ese instante. La salida serán ordenes codificadas a las maquinas del tipo "liberar operación Op de la maquina M" y "asignar operación Op a la maquina M".
* La primer capa envía la información estructurada a la segunda capa
* La segunda capa es la que lleva en cuenta el progreso de la producción, dependiendo de la información que llega de la capa inferior y de lo que ella almacena internamente (El progreso)
* La segunda capa esta encargada de enviar a la tercera, la capa planeadora, en una primera instancia las maquinas y las operaciones a realizar, en el orden en que deben realizarse cada operación, pero además enviar el estado actual de las maquinas y esas operaciones por si, de ser el caso, se presentan inconvenientes, como la perdida de una maquina o el fracaso de una operación.
* La ultima capa es la encargada de recibir todas las dependencias de trabajos -y por ende operaciones consecutivas, además de la disponibilidad de las máquinas. Esta capa es la que envia las ordenes de asignación de maquinas a operacónes.   """