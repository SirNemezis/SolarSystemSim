import pygame
import custom_themes
import solar_system_stat
import window_init
import pygame_menu


def init_and_draw(focus_object):
    menu = pygame_menu.Menu(focus_object.name, window_init.WIDTH, window_init.HEIGHT,
                            theme=custom_themes.planet_info_theme)
    menu.add.image(focus_object.real_image)
    menu.add.button(("Статус: "+focus_object.type))
    menu.add.button(("Год открытия: "+focus_object.info[0:4]))
    menu.add.button(("Радиус объекта (м) : " + str(focus_object.radius)))
    menu.add.button(("Масса объекта (кг) : " + str(focus_object.mass)))
    menu.add.button("Назад", window_init.start_program)
    menu.mainloop(window_init.WIN)