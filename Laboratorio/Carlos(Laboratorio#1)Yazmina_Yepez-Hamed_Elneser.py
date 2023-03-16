import pygame 
from pygame.locals import * 
import sys 

pygame.init() 

# Definimos unos colores 

negro = (0, 0, 0) 
blanco = (255, 255, 255) 
purple = (128, 0, 128) 

# Encendemos la pantalla
Tamaño_pantalla = (1300, 600) 
pantalla = pygame.display.set_mode(Tamaño_pantalla) 
pygame.display.set_caption("Carlos (Laboratorio #1 Estructura 2)") 

#Letra a usar
letra = pygame.font.Font(None, 20) 

# Tamaño (ancho,largo) del nodo
NodoAnc = 30 
NodoLar = 70 

# Arbol 
#Creacion de los nodos
class Nodo: 
    def __init__(self, valor, productos): 
        self.valor = valor 
        self.productos = productos 
        self.hijos = [] 
        self.padre = None 
    #Como conectamos a los hijos
    def AñadirHijo(self, hijo): 
        hijo.padre = self 
        self.hijos.append(hijo) 
    #Que tiene adentro cada nodo
    def contenido(self, valor): 
        if self.valor == valor: 
            return True 
        for hijo in self.hijos: 
            if hijo.contenido(valor): 
                return True 
        return False 

#Dibujo de cada nodo
def DibujarNodo(nodo, x, y): 
    posicionmouse = pygame.mouse.get_pos() 
    clickeado = pygame.mouse.get_pressed()[0] 
    conexion = pygame.Rect(x - NodoAnc, y - NodoAnc, NodoAnc*2, NodoAnc*2) 
    if conexion.collidepoint(posicionmouse) and clickeado: 
        pygame.display.set_caption("Introduce tu nueva ID y producto") 
        escribirpant = pygame.display.set_mode(Tamaño_pantalla) 
        valor_id = pygame.Rect(50, 30, 50, 30) 
        valor_producto = pygame.Rect(150, 30, 100, 30) 
        texto_id = letra.render("ID:", True, negro) 
        texto_producto = letra.render("Objeto:", True, negro) 
        valor = '' 
        productos = '' 
        TieneAlgo = True 
        while True: 
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit() 
                    sys.exit() 
                elif event.type == KEYDOWN: 
                    if event.key == K_RETURN: 
                        ValorNodo = int(valor) 
                        TextoNodoN = productos 
                        NuevoNodo = Nodo(ValorNodo, TextoNodoN) 
                        nodo.AñadirHijo(NuevoNodo) 
                        return 
                    elif event.key == K_ESCAPE: 
                        return 
                    elif TieneAlgo and event.unicode.isdigit(): 
                        valor += event.unicode 
                    elif not TieneAlgo and event.unicode.isalnum(): 
                        productos += event.unicode 
                elif event.type == MOUSEBUTTONDOWN: 
                    if valor_id.collidepoint(event.pos): 
                        TieneAlgo = True 
                    elif valor_producto.collidepoint(event.pos): 
                        TieneAlgo = False 
            escribirpant.fill(blanco) 
            escribirpant.blit(texto_id, (valor_id.x - 50, valor_id.y + 5)) 
            escribirpant.blit(texto_producto, (valor_producto.x - 50, valor_producto.y + 5)) 
            pygame.draw.rect(escribirpant, negro, valor_id, 2) 
            pygame.draw.rect(escribirpant, negro, valor_producto, 2) 
            RenderizarValor = letra.render(valor, True, negro) 
            textopantalla = letra.render(productos, True, negro) 
            escribirpant.blit(RenderizarValor, (valor_id.x + 5, valor_id.y + 5)) 
            escribirpant.blit(textopantalla, (valor_producto.x + 5, valor_producto.y + 5)) 
            pygame.display.update() 
    pygame.draw.circle(pantalla, purple, (x, y), NodoAnc) 
    RenderizarValor = letra.render("ID:"+str(nodo.valor), True, blanco) 
    textopantalla = letra.render(nodo.productos, True, blanco) 
    dibujovalor = RenderizarValor.get_rect(center=(x, y-10)) 
    dibujotexto = textopantalla.get_rect(center=(x, y+10)) 
    pantalla.blit(RenderizarValor, dibujovalor) 
    pantalla.blit(textopantalla, dibujotexto) 
 
 #Dibujo completo del arbol
def DibujarArbol(nodo, x, y, nivel): 
    DibujarNodo(nodo, x, y) 
    if nodo.hijos: 
        pos_ys = y + NodoLar 
        for hijo in nodo.hijos: 
            pos_xs = x + (NodoLar * (hijo.valor - 1 - nivel)) 
            pygame.draw.line(pantalla, negro, (x, y+NodoAnc), (pos_xs, pos_ys-NodoAnc)) 
            DibujarArbol(hijo, pos_xs, pos_ys, nivel+1) 

# Aqui va la marca de la empresa para iniciar el arbol
rama = Nodo(0, "Marca") 

#Estructura de como se dibuja y renderiza todo en pantalla (actualizacion)
while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == KEYDOWN: 
            if event.unicode.isnumeric(): 
                valor = int(event.unicode) 
                if not rama.contenido(valor): 
                    productos = input("Introduzca la ID del producto a introduccir: ") 
                    NuevoNodo = Nodo(valor, productos) 
                    rama.AñadirHijo(NuevoNodo) 
                else: 
                    print(f"El producto con id: {valor} ya existe.") 

    pantalla.fill(blanco) 
    DibujarArbol(rama, Tamaño_pantalla[0]/3, 50, 0) 
    pygame.display.update() 
