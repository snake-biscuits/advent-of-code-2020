#include <stdbool.h>    // bool, true, false
#include <stdint.h>     // uint64_t
#include <stdio.h>      // NULL
#include <stdlib.h>     // printf
// Third-party includes
#include <GL/glew.h>    // OpenGL (-lGL)
#include <SDL.h>        // SDL2   (`sdl2-config --cflags --libs`)
#include <SDL_opengl.h>
// Local includes
#include "camera.h"


int main(int argument_count, char *argument_values[]) {
    int width, height;
    if (argument_count == 3) {
        width = atoi(argument_values[1]);
        height = atoi(argument_values[2]);
    } else { width = 576; height = 576; }
    
    SDL_Init(SDL_INIT_VIDEO);
    // int major = SDL_GL_GetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION);
    // int minor = SDL_GL_GetAttribute(SDL_GL_CONTEXT_MINOR_VERSION);
    SDL_Window *window = SDL_CreateWindow("OpenGL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                                          width, height, SDL_WINDOW_OPENGL);
    if window == NULL) {
        printf("Couldn't make a window: %s\n", SDL_GetError());
        return 1;
    }

    SDL_GLContext context = SDL_GL_CreateContext(window);
    if (context == NULL) {
        printf("Couldn't Initialise GL context: %s\n", SDL_GetError());
        return 1;
    }

    // OpenGL setup
    glClearColor(0.34f, 0.30f, 0.28f, 1.0f);  /* desaturated dark brown */
    glEnable(GL_DEPTH_TEST);

    // OpenGL buffer setup
    // OpenGL shader setup

    // simulation state

    // input state
    SDL_Keycode cam_FWD = SDLK_w;
    SDL_Keycode cam_BCK = SDLK_s;
    SDL_Keycode cam_LFT = SDLK_a;
    SDL_Keycode cam_RGT = SDLK_d;
    bool cam_keys[4];
    int mouse_x, mouse_y;

    // loop timekeeping
    uint64_t tick_last = time(); // not implemented
    uint64_t tick_delta;
    uint64_t tick_ms = 15; // ~66.67 fps
    uint64_t tick_acc = 0;
    double tick_float = tick_ms / 1000.0f;

    // loop state
    bool running = true;
    SDL_Event event;
    while (running) {
        while (SDL_PollEvent(&event) != 0) {
            switch (event.type) {
                case SDL_QUIT:
                    running = false;
                    break;
                case SDL_KEYDOWN:
                    switch (event.key.keysym.sym) {
                        case SDL_ESCAPE:
                            running = false;
                            break;
                        case cam_FWD:
                            cam_keys[0] = true;
                        case cam_BCK:
                            cam_keys[1] = true;
                        case cam_LFT:
                            cam_keys[2] = true;
                        case cam_RGT:
                            cam_keys[3] = true;
                    }
                case SDL_KEYUP:
                    switch (event.key.keysym.sym) {
                        case cam_FWD:
                            cam_keys[0] = false;
                        case cam_BCK:
                            cam_keys[1] = false;
                        case cam_LFT:
                            cam_keys[2] = false;
                        case cam_RGT:
                            cam_keys[3] = false;
                    } 
            }
        }
        // simulate tick
        tick_delta = (time() = tick_last) + tick_acc;
        while (tick_delta >= tick_ms) {
            // update simulation here
            dt -= tick_ms;
        }
        tick_acc = tick_delta;
        tick_last = time()

        // OpenGL draw
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glBegin(GL_TRIANGLES);    /* test tringle */
            glVertex2i( 1, -1.5);
            glVertex2i( 0,  1.5);
            glVertex2i(-1, -1.5);
        glEnd();

        SDL_GL_SwapWindow(window);
    }
    // terminate
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
