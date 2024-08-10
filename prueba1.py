#Nombre de los participantes Prueba1
#Juan José Naranjo Velásquez CC : 1039474689
#Alejandro Mora Suarez CC: 1128437044
#Kenneth David Leonel Triana CC: 1192817456
#Creación de la clase Pedido 
class Pedido:
    """
    Documentación Clase Pedido 
    Esta clase servira para la toma de uestros productos de mercado, en donde el usuario podrá hacer el pedido, retirarlo y calcular el costo de este
    
    args: 
    id_pedido: int
    fecha:str
    costo_pedido:float
    descuento_pedido:float
    """
    def __init__(self, id_pedido: int, fecha: str, productos:list, cantidades:list, precios:list):
        """
        Se iniciailiza un Pedido con sus atributos
            id_pedido: int -> Identificador del pedido
            fecha: str -> Fecha en la que se realizó el pedido
            costo_pedido: float -> Costo total del pedido
            productos: list -> Lista de productos del pedido
            cantidades: list -> Lista de cantidades de cada producto
            precios: list -> Lista de precios de cada producto
        """
        self.id_pedido = id_pedido
        self.fecha = fecha
        self.productos = []
        self.cantidades = []
        self.precios = []

    def calcularCostoPedido(self,cantidades,precios):
        """
        función que calcula el costo del pedido realizado.
        argumentos: 
        In[0]:
        Out[0]:
        """
        total = sum(cantidad * precio for cantidad, precio in zip(cantidades, precios))
        return total
    def hacerPedido(self, productos:list, cantidades:list, precios:list):
        """"
        Se realiza un pedido, para ello la función va recibir los siguientes parametros
        productos: str -> Lista de productos del pedido
        cantidades: int -> Lista de cantidades de cada producto
        precios: int -> Lista de precios de cada producto
        """
        if len(productos) == len(cantidades) == len(precios):
            self.productos.append(productos)
            self.precios.append(precios)
            self.cantidades.append(cantidades)
            valorPedido = self.calcularCostoPedido(cantidades,precios)
            return f"El pedido se realizo con exito con el valor total de :{valorPedido} pesos colombianos"
            
        else:
            raise ValueError("Las listas deben ser del mismo tamaño")
        

        


#se crea la clase hija que hereda 
class Usuario (Pedido): 
     """"
     Documentación Clase Usuario

     Esta clase hereda los atributos de la Clase Pedido para establecer los detalles de la persona que realiza el pedido

     args:

    nombre:str
    apellido:str
    cedula:int
    direccion:str
    telefono:int
    email:str

     """
     def __init__(self,id_pedido: int, fecha: str, productos:list, cantidades:list, precios:list, nombre:str, apellido:str, cedula:int):
        Pedido.__init__(self, id_pedido, fecha, productos, cantidades, precios)
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
     def retirarPedido(self,id_pedido:int, nombre:str, apellido:str,cedula:int):
        """"
        Se retira un pedido, para ello la función va recibir el id del pedido que se quiere retirar
        """
        if id_pedido == self.id_pedido:
            self.id_pedido = None
            self.fecha = None
            self.productos = None
            self.cantidades = None
            self.precios = None
            mensaje = "Pedido eliminado del sistema"
            print(f"Pedido retirado por el Usuario {nombre}  {apellido} con cedula ciudadana : {cedula}")
            return mensaje
        else:
           return print("Pedido no encontrado")
   
productos_mercado = ['papa', 'huevos', 'pan']
cantidades_mercado = [2, 3, 4]
precios_mercado = [100, 200, 300]
#Se va a realizar un pedido 
pedido1 = Pedido(
    1,
    "2022-01-15",
    productos_mercado,
    cantidades_mercado,
    precios_mercado
)

print (pedido1.hacerPedido(productos_mercado,
    cantidades_mercado,
    precios_mercado))

usuario1 = Usuario(1,
    "2022-01-15",
    productos_mercado,
    cantidades_mercado,
    precios_mercado,
    "Carolina",
    "Molina",
    1127432)
print(usuario1.retirarPedido(1,"Carolina","Molina", 1127432))