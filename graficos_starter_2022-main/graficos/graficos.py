#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from OpenGL.GL import *
from glew_wish import *
import glfw
import math

color_triangulo = [0.6, 0.9, 0.6]
posicion_triangulo = [-0.4,0.2]
velocidad_triangulo = 0.01

color_cuadrado = [0.6, 0.4, 0.2]
posicion_cuadrado = [0.5,0.2]
velocidad_cuadrado = 0.01

def key_callback(window, key, scancode, action, mods):
    global color_triangulo
    global posicion_triangulo
    global velocidad_triangulo

    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    if key == glfw.KEY_R and action == glfw.PRESS:
        color_triangulo = [1.0,0.0,0.0]
    if key == glfw.KEY_G and action == glfw.PRESS:
        color_triangulo = [0.0,1.0,0.0]
    if key == glfw.KEY_B and action == glfw.PRESS:
        color_triangulo = [0.0,0.0,1.0]

    #Controles del triangulo
    if key == glfw.KEY_UP and (action == glfw.PRESS or glfw.REPEAT):
        posicion_triangulo[1] = posicion_triangulo [1] + velocidad_triangulo
        if posicion_triangulo[1] >= 1:
            posicion_triangulo[1] = -0.9999
    if key == glfw.KEY_DOWN and (action == glfw.PRESS or glfw.REPEAT):
        posicion_triangulo[1] = posicion_triangulo [1] - velocidad_triangulo
        if posicion_triangulo[1] <= -1:
            posicion_triangulo[1] = 0.9999
    if key == glfw.KEY_RIGHT and (action == glfw.PRESS or glfw.REPEAT):
        posicion_triangulo[0] = posicion_triangulo [0] + velocidad_triangulo
        if posicion_triangulo[0] >= 1:
            posicion_triangulo[0] = -0.9999
    if key == glfw.KEY_LEFT and (action == glfw.PRESS or glfw.REPEAT):
        posicion_triangulo[0] = posicion_triangulo [0] - velocidad_triangulo
        if posicion_triangulo[0] <= -1:
            posicion_triangulo[0] = 0.9999

    global color_cuadrado
    global posicion_cuadrado
    global velocidad_cuadrado

    #Controles del cuadrado
    if key == glfw.KEY_W and (action == glfw.PRESS or glfw.REPEAT):
        posicion_cuadrado[1] = posicion_cuadrado [1] + velocidad_cuadrado
        if posicion_cuadrado[1] >= 1:
            posicion_cuadrado[1] = -0.9999
    if key == glfw.KEY_S and (action == glfw.PRESS or glfw.REPEAT):
        posicion_cuadrado[1] = posicion_cuadrado [1] - velocidad_cuadrado
        if posicion_cuadrado[1] <= -1:
            posicion_cuadrado[1] = 0.9999
    if key == glfw.KEY_D and (action == glfw.PRESS or glfw.REPEAT):
        posicion_cuadrado[0] = posicion_cuadrado [0] + velocidad_cuadrado
        if posicion_cuadrado[0] >= 1:
            posicion_cuadrado[0] = -0.9999
    if key == glfw.KEY_A and (action == glfw.PRESS or glfw.REPEAT):
        posicion_cuadrado[0] = posicion_cuadrado [0] - velocidad_cuadrado
        if posicion_cuadrado[0] <= -1:
            posicion_cuadrado[0] = 0.9999

def draw():
    global color_triangulo
    #TRIANGULO
    glPushMatrix()
    glTranslatef(posicion_triangulo[0], posicion_triangulo[1], 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(color_triangulo[0],color_triangulo[1],color_triangulo[2])
    glVertex3f(-0.2,-0.1,0)
    glVertex3f(0,0.08,0)
    glVertex3f(0.08,-0.08,0)
    glEnd()
    glPopMatrix()
    #CUADRADO
    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(color_cuadrado[0],color_cuadrado[1],color_cuadrado[2])
    glVertex3f(0.1,0.1,0)
    glVertex3f(0,0.1,0)
    glVertex3f(0,0,0)
    glVertex3f(0.1,0,0)
    glEnd()
    glPopMatrix()

def main():
    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Establecer el key callback
    glfw.set_key_callback(window, key_callback)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
