import cv2
import numpy as np
from entities import entity


# X+ = DIREITA
# X- = ESQUERDA
# Y+ = BAIXO
# Y- = CIMA
def colide(entity):
    global tela
    resultados = {"E": False, "D": False, "C": False, "B": False}  # Esquerda, Direita, Cima, Baixo
    if np.all(tela[entity.y+1][entity.x] == 255):
        resultados["B"] = True
    if np.all(tela[entity.y-1][entity.x] == 255):
        resultados["C"] = True
    if np.all(tela[entity.y][entity.x+1] == 255):
        resultados["D"] = True
    if np.all(tela[entity.y][entity.x-1] == 255):
        resultados["E"] = True
    return resultados


def gravity(entity):
    global resolution
    if 0 < entity.x < resolution[1]-1 and 0 < entity.y < resolution[0]-1 and not colide(entity)['B'] and entity.y_speed == 0:
        entity.y_speed = 1
    else:
        entity.y_speed = 0
    return entity


def gameTick():
    global tela
    global entityList
    tela = np.zeros([resolution[0], resolution[1], 3])
    for entity in entityList:
        entity = gravity(entity)
        entity.y += entity.y_speed
        entity.x += entity.x_speed
        tela[entity.y][entity.x] = [255, 255, 255]


def mainLoop():
    global tela
    cv2.setMouseCallback(TITULO, add_entity)
    while True:
        gameTick()
        cv2.imshow(TITULO, tela)
        if cv2.waitKey(1) == 113:  # pressione Q para fechar
            cv2.destroyAllWindows()
            break


def add_entity(event, x, y, flags, param):
    global arrastando
    global resolution
    global tela
    if 0 < x < resolution[1] and 0 < y < resolution[0]:
        if event == cv2.EVENT_LBUTTONDOWN:
            arrastando = True
            e = entity(x, y)
            entityList.append(e)
        elif event == cv2.EVENT_MOUSEMOVE:
            if arrastando:
                e = entity(x, y)
                entityList.append(e)
        elif event == cv2.EVENT_LBUTTONUP:
            arrastando = False


if __name__ == "__main__":
    TITULO = "PY 2D ENGINE"
    arrastando = False
    resolution = [400, 400]
    entityList = []
    cv2.namedWindow(TITULO, cv2.WINDOW_AUTOSIZE)
    tela = np.zeros([resolution[0], resolution[1], 3])
    cv2.imshow(TITULO, tela)
    mainLoop()
