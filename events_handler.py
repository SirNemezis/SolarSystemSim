import pygame

import math_base
import solar_system_stat
import window_init
from pygame.locals import *

satellite_counter = 0
orbit_in_way = False
orbit_needed = False


def set_on_click_listener():
    global orbit_in_way, satellite_counter, orbit_needed
    focus_object = window_init.focus_object
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                window_init.loop = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        window_init.loop = False
                    case pygame.K_1:
                        math_base.clear_orbits(focus_object)
                        window_init.SCALED = False
                        focus_object = solar_system_stat.Sun
                        math_base.orbit_scale = 5.681818181818182e-09
                        math_base.planet_scale = 250000
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_2:
                        focus_object = solar_system_stat.Mercury
                        window_init.SCALED = False
                        math_base.planet_scale = 30000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_3:
                        focus_object = solar_system_stat.Venus
                        window_init.SCALED = False
                        math_base.planet_scale = 30000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_4:
                        focus_object = solar_system_stat.Earth
                        window_init.SCALED = False
                        math_base.planet_scale = 30000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                        math_base.move_satellites_to_parent(focus_object)
                    case pygame.K_5:
                        focus_object = solar_system_stat.Mars
                        window_init.SCALED = False
                        math_base.planet_scale = 30000
                        math_base.orbit_scale = 10.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                        math_base.move_satellites_to_parent(focus_object)
                    case pygame.K_6:
                        focus_object = solar_system_stat.Jupiter
                        window_init.SCALED = False
                        math_base.planet_scale = 120000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_7:
                        focus_object = solar_system_stat.Saturn
                        window_init.SCALED = False
                        math_base.planet_scale = 120000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_8:
                        focus_object = solar_system_stat.Uranus
                        window_init.SCALED = False
                        math_base.planet_scale = 120000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_9:
                        focus_object = solar_system_stat.Neptune
                        window_init.SCALED = False
                        math_base.planet_scale = 120000
                        math_base.orbit_scale = 1000.681818181818182e-09
                        window_init.set_focus_in_center_of_vision(focus_object)
                    case pygame.K_UP:
                        window_init.SCALED = False
                        math_base.increase_scale()
                    case pygame.K_DOWN:
                        window_init.SCALED = False
                        math_base.decrease_scale()
                    case pygame.K_c:
                        math_base.clear_orbits(focus_object)
                    case pygame.K_y:
                        if not orbit_in_way:
                            orbit_in_way = True
                        else:
                            orbit_in_way = False
                    case pygame.K_q:
                        if satellite_counter + 1 < len(focus_object.satellite_array):
                            satellite_counter += 1
                        else:
                            satellite_counter = 0
                    case pygame.K_r:
                        if satellite_counter > 1:
                            satellite_counter -= 1
                        else:
                            satellite_counter = len(focus_object.satellite_array) - 1
                    case pygame.K_o:
                        if orbit_needed:
                            orbit_needed = False
                        else:
                            orbit_needed = True
    window_init.focus_object = focus_object
    if pygame.key.get_pressed()[K_w]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_y += 20
    if pygame.key.get_pressed()[K_s]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_y -= 20
    if pygame.key.get_pressed()[K_a]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_x += 20
    if pygame.key.get_pressed()[K_d]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_x -= 20
    if pygame.key.get_pressed()[K_LEFT]:
        math_base.clear_scaled_orbits(focus_object)
        math_base.clear_orbits(focus_object)
        math_base.decrease_timestep_tick()
    if pygame.key.get_pressed()[K_RIGHT]:
        math_base.clear_scaled_orbits(focus_object)
        math_base.clear_orbits(focus_object)
        math_base.increase_timestep_tick()
    if satellite_counter > len(focus_object.satellite_array):
        window_init.satellite_counter = 0
    if orbit_in_way and len(focus_object.satellite_array) > 0:
        window_init.SCALED = False
        window_init.track_object_in_screen(focus_object.satellite_array[satellite_counter])