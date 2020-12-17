from ctypes import byref
import itertools
from time import time

from OpenGL.GL import *
from OpenGL.GLU import *
from sdl2 import *


def neighbours(point):
    x, y = point
    xm = x - 1
    ym = y - 1
    xp = x + 1
    yp = y + 1
    yield xm, ym
    yield xm, y
    yield xm, yp
    yield x, ym
    yield x, yp
    yield xp, ym
    yield xp, y
    yield xp, yp


def update(grid):
    next_tick = set()
    recalculate = grid | set(itertools.chain(*map(neighbours, grid)))
    for point in recalculate:
        i = sum((neighbour in grid) for neighbour in neighbours(point))
        if i == 3 or (i == 2 and point in grid):
            # if point[0] < -8:
            #     x = point[0] + 8
            # elif point[0] > 8:
            #     x = point[0] - 8
            # else:
            #     x = point[0]
            # if point[1] < -8:
            #     y = point[1] + 8
            # elif point[1] > 8:
            #     y = point[1] - 8
            # else:
            #     y = point[1]
            next_tick.add(point)
    return next_tick


def main(width, height):
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b'SDL2 OpenGL',
                              SDL_WINDOWPOS_CENTERED,  SDL_WINDOWPOS_CENTERED,
                              width, height,
                              SDL_WINDOW_OPENGL | SDL_WINDOW_BORDERLESS)
    glContext = SDL_GL_CreateContext(window)

    glClearColor(0.1, 0.1, 0.1, 0.0)

    zoom = 128
    glOrtho(-zoom, zoom, -zoom, zoom, .1, 256)
    glPointSize(3)
    glTranslate(0, 0, -1)

    grid = set([(1, 5), (2, 5), (1, 6), (2, 6),
                (14, 1), (15, 1), (13, 2), (17, 2),
                (12, 3), (12, 4), (12, 5), (13, 6),
                (14, 7), (15, 7), (17, 6), (16, 4),
                (18, 5), (18, 4), (19, 4), (18, 3),
                (22, 5), (23, 5), (22, 6), (23, 6),
                (22, 7), (23, 7), (24, 8), (24, 4),
                (26, 4), (26, 3), (26, 8), (26, 9),
                (36, 7), (36, 6), (37, 7), (37, 6)])
    # grid = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])

    event = SDL_Event()
    oldtime = time()
    tickrate = 15  # ms per tick
    while True:
        while SDL_PollEvent(byref(event)) != 0:
                if event.type == SDL_QUIT or event.key.keysym.sym == SDLK_ESCAPE and event.type == SDL_KEYDOWN:
                    SDL_GL_DeleteContext(glContext)
                    SDL_DestroyWindow(window)
                    SDL_Quit()
                    return False

        dt = time() - oldtime
        if dt >= 1 / tickrate:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glColor(1, 1, 1)
            glBegin(GL_POINTS)
            for point in grid:
                glVertex(point[0], point[1], 0)
            glEnd()
            SDL_GL_SwapWindow(window)

            grid = update(grid)
            oldtime = time()


if __name__ == "__main__":
    main(768, 768)
