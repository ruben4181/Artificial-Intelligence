class Operation :
	def __init__(self, tarea, indexOp, duration):
		self.tarea=None
		self.indexOp=None
		self.duration=float('inf')
	def setNextOp(self, operation):
		self.nextOp=operation
	def setTarea(self, tarea):
		self.tarea=tarea

class Machine :
	def __init__(self, state, currentOp, supportedOps):
		self.state="free"
		self.currentOp=None
		self.supportedOps=list()
class Tasks :
	def __init__(self, state, ops):
		self.state="unstarted"
		self.ops=list() #Operations are a list with the ops in the right orden of ops

def fitness(solution):
	currentOp = [0 for _ in solution]
	currentOps=list()
	faul=0
	distance=0
	for i in range(solution):
		currentOps.append(solution[currentOp][i])
		if()


""" #### 3) Especificación del flujo de datos entre capas
* La primer capa recibira y enviara al ambiente cadenas codificadas, con el estado de las maquinas y ordenes, respectivamente. Lo que recibira del ambiente sera el estado de cada maquina, más detalladamente, recibirá un listado que contenga una estructura que le indicara la operación que se encuentra en ejecución o si esta sin operación en ese instante. La salida serán ordenes codificadas a las maquinas del tipo "liberar operación Op de la maquina M" y "asignar operación Op a la maquina M".
* La primer capa envía la información estructurada a la segunda capa
* La segunda capa es la que lleva en cuenta el progreso de la producción, dependiendo de la información que llega de la capa inferior y de lo que ella almacena internamente (El progreso)
* La segunda capa esta encargada de enviar a la tercera, la capa planeadora, en una primera instancia las maquinas y las operaciones a realizar, en el orden en que deben realizarse cada operación, pero además enviar el estado actual de las maquinas y esas operaciones por si, de ser el caso, se presentan inconvenientes, como la perdida de una maquina o el fracaso de una operación.
* La ultima capa es la encargada de recibir todas las dependencias de trabajos -y por ende operaciones consecutivas, además de la disponibilidad de las máquinas. Esta capa es la que envia las ordenes de asignación de maquinas a operacónes.   """