import pygame  
import sys   

# Ponemos algunos colores para usarlos en la creacion de los nodos    
Amarillo = (255, 255, 0)     
Purpura = (255,0,255)     
Negro = (0, 0, 0)          

# Damos el tamaño de la pantalla     
ANCHO = 800     
LARGO = 600     

# iniciamos pygame     
pygame.init()     

# Ponemos un titulo y le damos el tamaño a la pantalla     
pantalla = pygame.display.set_mode((ANCHO, LARGO))     
pygame.display.set_caption("Laboratorio 1 Estructura de datos II (avance)")     

# Creamos la letra de nuestros nodos    
fuente = pygame.font.SysFont('Arial', 15)     

# Definimos el tamaño visual que tendra el nodo     
NODO_TAMAÑO = 15     

#Creacion minijuego
class MiniJuego:
    ...
# Creamos la clase nodo
class Nodo:     
    def __init__(self, valor, x, y):     
        self.valor = valor     
        self.izquierda = None     
        self.derecha = None     
        self.x = x     
        self.y = y     

# Creamos la clase del arbol (en este caso binario) para agregarle los 
class ArbolBinario1:     
    def __init__(self):     
        self.padre = None     

        # Funcion que añade los valores a los nodos y creacion del arbol
    def Añadirnodo(self, valor):     
        if self.padre is None:     
            self.padre = Nodo(valor, ANCHO/3.5, 50)     
        else:     
            self.AgregarNodo(valor, self.padre, ANCHO/3.5, 100, 1)     
    def AgregarNodo(self, valor, nodo, x, y, nivel):     
        if nodo.izquierda is None:     
            nodo.izquierda = Nodo(valor, x-4*(6-nivel), y+NODO_TAMAÑO*2)     
        elif nodo.derecha is None:     
            nodo.derecha = Nodo(valor, x+4*(6-nivel), y+NODO_TAMAÑO*2)     
        else:     
            if valor < nodo.valor:     
                self.AgregarNodo(valor, nodo.izquierda, x-2**(6-nivel), y+NODO_TAMAÑO*4, nivel+1)     
            else:     
                self.AgregarNodo(valor, nodo.derecha, x+2**(6-nivel), y+NODO_TAMAÑO*4, nivel+1)     
    def draw(self, pantalla, fuente):     
        self.DibujarNodo(pantalla, fuente, self.padre)     
    def DibujarNodo(self, pantalla, fuente, nodo):     
        if nodo is not None:     
            pygame.draw.circle(pantalla, Amarillo, (nodo.x, nodo.y), NODO_TAMAÑO, 2)     
            text_surface = fuente.render(str(nodo.valor), True, Amarillo)     
            text_rect = text_surface.get_rect(center=(nodo.x, nodo.y))     
            pantalla.blit(text_surface, text_rect)     
            if nodo.izquierda is not None:     
                pygame.draw.line(pantalla, Negro, (nodo.x, nodo.y+NODO_TAMAÑO), (nodo.izquierda.x, nodo.izquierda.y-NODO_TAMAÑO), 3)     
                self.DibujarNodo(pantalla, fuente, nodo.izquierda)     
            if nodo.derecha is not None:    
                pygame.draw.line(pantalla, Negro, (nodo.x, nodo.y+NODO_TAMAÑO), (nodo.derecha.x, nodo.derecha.y-NODO_TAMAÑO), 3)     
                self.DibujarNodo(pantalla, fuente, nodo.derecha)     

class ArbolBinario2:     
    def __init__(self):     
        self.padre = None     

        # Funcion que añade los valores a los nodos y creacion del arbol
    def Añadirnodo(self, valor):     
        if self.padre is None:     
            self.padre = Nodo(valor, ANCHO/1.5, 50)     
        else:     
            self.AgregarNodo(valor, self.padre, ANCHO/1.5, 100, 1)     
    def AgregarNodo(self, valor, nodo, x, y, nivel):     
        if nodo.izquierda is None:     
            nodo.izquierda = Nodo(valor, x-4*(6-nivel), y+NODO_TAMAÑO*2)     
        elif nodo.derecha is None:     
            nodo.derecha = Nodo(valor, x+4*(6-nivel), y+NODO_TAMAÑO*2)     
        else:     
            if valor < nodo.valor:     
                self.AgregarNodo(valor, nodo.izquierda, x-2**(6-nivel), y+NODO_TAMAÑO*4, nivel+1)     
            else:     
                self.AgregarNodo(valor, nodo.derecha, x+2**(6-nivel), y+NODO_TAMAÑO*4, nivel+1)     
    def draw(self, pantalla, fuente):     
        self.DibujarNodo(pantalla, fuente, self.padre)     
    def DibujarNodo(self, pantalla, fuente, nodo):     
        if nodo is not None:     
            pygame.draw.circle(pantalla, Amarillo, (nodo.x, nodo.y), NODO_TAMAÑO, 2)     
            text_surface = fuente.render(str(nodo.valor), True, Amarillo)     
            text_rect = text_surface.get_rect(center=(nodo.x, nodo.y))     
            pantalla.blit(text_surface, text_rect)     
            if nodo.izquierda is not None:     
                pygame.draw.line(pantalla, Negro, (nodo.x, nodo.y+NODO_TAMAÑO), (nodo.izquierda.x, nodo.izquierda.y-NODO_TAMAÑO), 3)     
                self.DibujarNodo(pantalla, fuente, nodo.izquierda)     
            if nodo.derecha is not None:    
                pygame.draw.line(pantalla, Negro, (nodo.x, nodo.y+NODO_TAMAÑO), (nodo.derecha.x, nodo.derecha.y-NODO_TAMAÑO), 3)     
                self.DibujarNodo(pantalla, fuente, nodo.derecha) 
                

# Creamos el objeto arbol y le ajuntamos los nodos a el     
arbol = ArbolBinario1()     
arbol.Añadirnodo(50)     
arbol.Añadirnodo(30)     
arbol.Añadirnodo(70)     
arbol.Añadirnodo(20)     
arbol.Añadirnodo(40)     
arbol.Añadirnodo(60)     
arbol.Añadirnodo(80)     
arbol.Añadirnodo(71)     
arbol.Añadirnodo(29)
#arbol.Añadirnodo(30) 
#arbol.Añadirnodo(30)  
#arbol.Añadirnodo(91)

tree = ArbolBinario2()
tree.Añadirnodo(5)
tree.Añadirnodo(8)
tree.Añadirnodo(19)
tree.Añadirnodo(20)
tree.Añadirnodo(23)
tree.Añadirnodo(28)
tree.Añadirnodo(10)
tree.Añadirnodo(3)

     

# Hacemos el loop de la pantalla para que corra hasta que le demos a la X   
Terminado = False     
while not Terminado:          
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:     
            Terminado = True     

    # Le ponemos purpura en el fondo de la pantalla    
    pantalla.fill(Purpura)     

   # Pintamos el arbol binario     
    arbol.draw(pantalla, fuente)   
    tree.draw(pantalla,fuente)  

   # Actualizamos la imagen (En este caso no es una funcion necesaria ya que no hay movimiento en la imagen)     
    pygame.display.flip()     

# Cuando se le da "X" se hace el cierre correctamente     
pygame.quit()     

 