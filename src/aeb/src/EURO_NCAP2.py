#!/usr/bin/env python3

# Copyright (c) 2018 Intel Labs.
# authors: German Ros (german.ros@intel.com)
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""
   EURO NCAP Test Scenario
"""

from __future__ import print_function

import collections
import datetime
import glob
import logging
import math
import rospy
import os
import re
import sys
import weakref

try:
    import pygame
    from pygame.locals import KMOD_CTRL
    from pygame.locals import K_ESCAPE
    from pygame.locals import K_q
except ImportError:
    raise RuntimeError('cannot import pygame, make sure pygame package is installed')

try:
    import numpy as np
except ImportError:
    raise RuntimeError(
        'cannot import numpy, make sure numpy package is installed')

# ==============================================================================
# -- find carla module ---------------------------------------------------------
# ==============================================================================

try:
    #    sys.path.append(glob.glob('/opt/carla-simulator/PythonAPI/carla/dist/carla-0.9.8-py2.7-linux-x86_64.egg')[0])

    #    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
    sys.path.append(glob.glob('/opt/carla-simulator/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

# ==============================================================================
# -- add PythonAPI for release mode --------------------------------------------
# ==============================================================================
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/carla')
except IndexError:
    pass

import carla
from carla import ColorConverter as cc


# ==============================================================================
# -- Global functions ----------------------------------------------------------
# ==============================================================================

def find_weather_presets():
    rgx = re.compile('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)')
    name = lambda x: ' '.join(m.group(0) for m in rgx.finditer(x))
    presets = [x for x in dir(carla.WeatherParameters) if re.match('[A-Z].+', x)]
    return [(getattr(carla.WeatherParameters, x), name(x)) for x in presets]


def get_actor_display_name(actor, truncate=250):
    name = ' '.join(actor.type_id.replace('_', '.').title().split('.')[1:])
    return (name[:truncate - 1] + u'\u2026') if len(name) > truncate else name


# ==============================================================================
# -- World ---------------------------------------------------------------
# ==============================================================================

class World(object):
    def __init__(self, carla_world, hud):
    #def __init__(self, carla_world, actor_filter):

        self.world = carla_world
        self.map = self.world.get_map()
        self.hud = hud

        self.blueprint_library = self.world.get_blueprint_library()
        self.player = None
        self.npc1 = None
        self.npc2 = None
        self.npc3 = None
        self.npc4 = None
        self.player_tranform = carla.Transform(carla.Location(x=29.4, y=7.2, z=1.843102), carla.Rotation(yaw=0))
        self.bp = self.blueprint_library.find('vehicle.chevrolet.impala')

        self.npc1_transform = carla.Transform(carla.Location(x=241.5, y=147, z=1.843102), carla.Rotation(yaw=270))
        self.npc1_bp = self.blueprint_library.find('vehicle.chevrolet.impala')

        self.npc2_transform = carla.Transform(carla.Location(x=134.5, y=-6.6, z=1.843102), carla.Rotation(yaw=180))
        self.npc2_bp =self.blueprint_library.find('vehicle.kawasaki.ninja')

        self.npc3_transform = carla.Transform(carla.Location(x=214.5, y=12.8, z=1.843102), carla.Rotation(yaw=0))
        self.npc3_bp= self.blueprint_library.find('vehicle.mustang.mustang')


        self.walker1 = None
        self.walker1_bp = self.blueprint_library.filter('"walker.pedestrian.*"')
        self.walker1_transform = carla.Transform(carla.Location(x=225.3, y=19, z=2), carla.Rotation(yaw=270))

        self.bicycle = None
        self.bicycle_transform = carla.Transform(carla.Location(x=35.7, y=10, z=1.843102), carla.Rotation(yaw=0))
        self.bicycle_transform =  self.blueprint_library.find('vehicle.gazelle.omafiets')


        self.walker1_control = carla.WalkerControl()
        self.walker1_control.speed = 1.39
        self.walker1_control.direction = carla.Vector3D(x=0.000000, y=-1.000000, z=0.000000)

        self.control2 = carla.VehicleControl()
        self.control2.throttle = 1

        self.control3 = carla.VehicleControl()

        self.control3.throttle = 0
        self.control3.brake = 1
        self.control3.hand_brake = True













        self.collision_sensor = None
        self.lane_invasion_sensor = None
        self.gnss_sensor = None
        self.camera_manager = None
        self._weather_presets = find_weather_presets()
        self._weather_index = 0
        self.restart()
        self.world.on_tick(hud.on_world_tick)
        self.recording_enabled = False
        self.recording_start = 0


    def restart(self):

        # Get a blueprint.

        blueprint = self.world.get_blueprint_library().filter("vehicle.*")

        #0 ActorBlueprint(id=vehicle.audi.a2, tags=[a2, audi, vehicle])
        #1 ActorBlueprint(id=vehicle.audi.tt, tags=[tt, audi, vehicle]),
        #2 ActorBlueprint(id=vehicle.carlamotors.carlacola, tags=[carlacola, carlamotors, vehicle]),
        #3 ActorBlueprint(id=vehicle.bmw.isetta, tags=[isetta, bmw, vehicle]),
        #4 ActorBlueprint(id=vehicle.nissan.micra, tags=[micra, nissan, vehicle]),
        #5 ActorBlueprint(id=vehicle.citroen.c3, tags=[c3, citroen, vehicle]),
        #6 ActorBlueprint(id=vehicle.gazelle.omafiets, tags=[omafiets, gazelle, vehicle]),
        #7 ActorBlueprint(id=vehicle.mercedes - benz.coupe, tags=[coupe, mercedes - benz, vehicle]),
        #8 ActorBlueprint(id=vehicle.mini.cooperst, tags=[mini, cooperst, vehicle]),
        #9 ActorBlueprint(id=vehicle.nissan.patrol, tags=[patrol, nissan, vehicle]),
        #10 ActorBlueprint(id=vehicle.mustang.mustang, tags=[mustang, vehicle]),
        #11 ActorBlueprint(id=vehicle.lincoln.mkz2017, tags=[mkz2017, lincoln, vehicle]),
        #12 ActorBlueprint(id=vehicle.tesla.cybertruck, tags=[cybertruck, tesla, vehicle]),
        #13 ActorBlueprint(id=vehicle.toyota.prius, tags=[prius, toyota, vehicle]),
        #14 ActorBlueprint(id=vehicle.volkswagen.t2, tags=[volkswagen, t2, vehicle]),
        #15 ActorBlueprint(id=vehicle.bmw.grandtourer, tags=[grandtourer, bmw, vehicle]),
        #16 ActorBlueprint(id=vehicle.tesla.model3, tags=[tesla, model3, vehicle]),
        #17 ActorBlueprint(id=vehicle.diamondback.century, tags=[century, diamondback, vehicle]),
        #18 ActorBlueprint(id=vehicle.dodge_charger.police, tags=[police, dodge_charger, vehicle]),
        #19 ActorBlueprint(id=vehicle.bh.crossbike, tags=[crossbike, bh, vehicle]),
        #20 ActorBlueprint(id=vehicle.kawasaki.ninja, tags=[ninja, kawasaki, vehicle]),
        #21 ActorBlueprint(id=vehicle.jeep.wrangler_rubicon, tags=[wrangler_rubicon, jeep, vehicle]),
        #22 ActorBlueprint(id=vehicle.yamaha.yzf, tags=[yzf, yamaha, vehicle]),
        #23 ActorBlueprint(id=vehicle.chevrolet.impala, tags=[impala, chevrolet, vehicle]),
        #24 ActorBlueprint(id=vehicle.harley - davidson.low_rider, tags=[low_rider, harley - davidson, vehicle]),
        #25 ActorBlueprint(id=vehicle.audi.etron, tags=[etron, audi, vehicle]),
        #26 ActorBlueprint(id=vehicle.seat.leon, tags=[leon, seat, vehicle])

        self.player = self.world.spawn_actor(self.bp, self.player_tranform)
        self.npc1 = self.world.spawn_actor(self.npc1_bp, self.npc1_tranform)
        self.npc2 = self.world.spawn_actor(self.npc2_bp, self.npc2_tranform)
        self.npc3 = self.world.spawn_actor(self.npc3_bp, self.npc3_tranform)
        self.npc4 = self.world.spawn_actor(self.npc4_bp, self.npc4_tranform)
        self.walker1 = self.world.spawn_actor(self.walker1_bp, self.walker1_tranform)
        self.bicycle = self.world.spawn_actor(self.bicycle_bp, self.bicycle_tranform)




        self.walker1.apply_control(self.walker1_control)

        self.npc1.apply_control(self.control2)
        self.bicycle.apply_control(self.control2)
        self.player.apply_control(self.control2)


        while (True):
            location = self.npc1.get_location()


            if location.y < 15:
                print(location.y)
                print('Braking')

                break

        self.npc1.apply_control(self.control3)
        self.bicycle.apply_control(self.control3)
        self.player.apply_control(self.control3)


        """

        if rospy.get_param("scenario") == 1:
            print ('''
            
            EURO NCAP CAR TO PEDESTRIAN NEAR SIDE CHILD - CPNC
            
            ''')
            blueprintPlayer = blueprint[0]
            blueprintNpc1 = blueprint[1]
            blueprintNpc2 = blueprint[25]


            blueprintPlayer.set_attribute('role_name', 'hero')
            blueprintNpc1.set_attribute('role_name', 'npc1')
            blueprintNpc2.set_attribute('role_name', 'npc2')

            blueprintPlayer.set_attribute('color','255,255,255')
            blueprintNpc1.set_attribute('color', '10,10,10')
            blueprintNpc2.set_attribute('color', '10,10,10')

            while self.player is None:
                spawn_point = carla.Transform(carla.Location(x=123.0845139, y=8.330196, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.player = self.world.spawn_actor(blueprintPlayer, spawn_point)
                self.player.set_target_velocity(carla.Vector3D(x=0.0000, y=0.000000, z=0.000000))

                # Spawn the npc cars
                spawn_point = carla.Transform(carla.Location(x=219.5872746, y=12.62206999, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.npc1 = self.world.try_spawn_actor(blueprintNpc1, spawn_point)
                spawn_point = carla.Transform(carla.Location(x=214.2239483, y=12.54190365, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.npc2 = self.world.spawn_actor(blueprintNpc2, spawn_point)

                # Spawn the walker
                blueprintsWalkers = self.world.get_blueprint_library().filter("walker.*")
                blueprintsWalkers = blueprintsWalkers[25]
                if blueprintsWalkers.has_attribute('is_invincible'):
                    blueprintsWalkers.set_attribute('is_invincible', 'false')
                spawn_point = carla.Transform(carla.Location(x=223.013613, y=13.82338109, z=2.063102),
                                              carla.Rotation(pitch=0.000000, yaw=270.855823, roll=0.000000))
                self.walker1 = self.world.spawn_actor(blueprintsWalkers, spawn_point)

                self.world.wait_for_tick()

                # Set up walker control by direct input
                self.control = carla.WalkerControl()
                self.control.speed = 5 / 3.6
                self.control.direction = carla.Vector3D(x=0.000000, y=-1.000000, z=0.000000)


        elif rospy.get_param("scenario") == 2:
            print ('''

                EURO NCAP CAR TO PEDESTRIAN LONGITUDINAL ADULT - CPLA 

                        ''')
            blueprintPlayer = blueprint[0]

            blueprintPlayer.set_attribute('role_name', 'hero')
            blueprintPlayer.set_attribute('color', '255,255,255')

            while self.player is None:
                spawn_point = carla.Transform(carla.Location(x=73.09, y=7.5833, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.player = self.world.spawn_actor(blueprintPlayer, spawn_point)
                self.player.set_target_velocity(carla.Vector3D(x=0.0000, y=0.000000, z=0.000000))

                #
                # Spawn the walker
                blueprintsWalkers = self.world.get_blueprint_library().filter("walker.*")
                blueprintsWalkers = blueprintsWalkers[14]
                if blueprintsWalkers.has_attribute('is_invincible'):
                    blueprintsWalkers.set_attribute('is_invincible', 'false')
                spawn_point = carla.Transform(carla.Location(x=213.0744, y=9.6744, z=2.063102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.walker1 = self.world.spawn_actor(blueprintsWalkers, spawn_point)
                self.world.wait_for_tick()

                # Set up walker control by direct input
                self.control = carla.WalkerControl()
                self.control.speed = 5 / 3.6
                self.control.direction = carla.Vector3D(x=1.000000, y=0.000000, z=0.000000)

        elif rospy.get_param("scenario") == 3:
            print ('''

            EURO NCAP CAR TO BICYCLIST LONGITUDINAL ADULT - CBLA 

              ''')
            blueprintPlayer = blueprint[0]
            blueprintNpc1 = blueprint[17]

            blueprintPlayer.set_attribute('role_name', 'hero')
            blueprintNpc1.set_attribute('role_name', 'npc1')
            self.vehicle_control = carla.VehicleControl()

            blueprintPlayer.set_attribute('color', '255,255,255')
            blueprintNpc1.set_attribute('color', '10,10,10')

            while self.player is None:
                spawn_point = carla.Transform(carla.Location(x=77.09, y=7.5833, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.player = self.world.spawn_actor(blueprintPlayer, spawn_point)
                self.player.set_target_velocity(carla.Vector3D(x=0.0000, y=0.000000, z=0.000000))

                # Spawn the npc cars
                spawn_point = carla.Transform(carla.Location(x=195.0764, y=9.4056, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.npc1 = self.world.try_spawn_actor(blueprintNpc1, spawn_point)

                    # set PI-Controller for Bycicle
                self.npc1.kp= 1.0  # Proportional value
                self.npc1.tn = 0.5  # Integral value
                self.npc1.vsoll = 15 * 1.16 / 3.6  # set 15km/h multiplicator
                self.npc1.stop = True



        elif rospy.get_param("scenario") == 4:
            print ('''

            EURO NCAP CAR TO CAR REAR STATIONARY - CCRS

                    ''')
            blueprintPlayer = blueprint[0]
            blueprintNpc1 = blueprint[15]

            blueprintPlayer.set_attribute('role_name', 'hero')
            blueprintNpc1.set_attribute('role_name', 'npc1')

            blueprintPlayer.set_attribute('color', '255,255,255')
            blueprintNpc1.set_attribute('color', '192,192,192')

            while self.player is None:

                spawn_point = carla.Transform(carla.Location(x=77.09, y=7.5833, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.player = self.world.spawn_actor(blueprintPlayer, spawn_point)
                self.player.set_target_velocity(carla.Vector3D(x=0.0000, y=0.000000, z=0.000000))

                # Spawn the npc cars
                spawn_point = carla.Transform(carla.Location(x=218.6299, y=9.7574, z=1.843102),
                                              carla.Rotation(pitch=0.000000, yaw=0.855823, roll=0.000000))
                self.npc1 = self.world.try_spawn_actor(blueprintNpc1, spawn_point)

        else:
            logging.info('''

            Unavailable Scenario selected
            
            1 - EURO NCAP CPNC
            2 - EURO NCAP CPLA
            3 - EURO NCAP CBLA
            4 - EURO NCAP CCRS

                ''')

        """


        # Keep same camera config if the camera manager exists.
        cam_index = self.camera_manager.index if self.camera_manager is not None else 0
        cam_pos_index = self.camera_manager.transform_index if self.camera_manager is not None else 0

        # Set up the sensors.
        self.camera_manager = CameraManager(self.player, self.hud)
        self.camera_manager.transform_index = cam_pos_index
        self.camera_manager.set_sensor(cam_index, notify=False)


    def next_weather(self, reverse=False):
        self._weather_index += -1 if reverse else 1
        self._weather_index %= len(self._weather_presets)
        preset = self._weather_presets[self._weather_index]
        self.hud.notification('Weather: %s' % preset[1])
        self.player.get_world().set_weather(preset[0])

    def tick(self, clock):
        self.hud.tick(self, clock)

    def render(self, display):
        self.camera_manager.render(display)
        self.hud.render(display)

    def destroy_sensors(self):
        self.camera_manager.sensor.destroy()
        self.camera_manager.sensor = None
        self.camera_manager.index = None


    def destroy(self):
        if rospy.get_param("scenario") == 1:
            actors = [
                self.camera_manager.sensor,
                #self.collision_sensor.sensor,
                #self.lane_invasion_sensor.sensor,
                #self.gnss_sensor.sensor,
                self.player,
                self.npc1,
                self.npc2,
                self.walker1]
        elif rospy.get_param("scenario") == 2:
            actors = [
                self.camera_manager.sensor,
                self.player,
                self.walker1]
        elif rospy.get_param("scenario") == 3 or rospy.get_param("scenario") == 4:
            actors = [
                self.camera_manager.sensor,
                self.player,
                self.npc1]

        for actor in actors:
            if actor is not None:
                actor.destroy()

# ==============================================================================
# -- KeyboardControl -----------------------------------------------------------
# ==============================================================================


class KeyboardControl(object):
    def __init__(self, world):
        world.hud.notification("Press 'H' or '?' for help.", seconds=4.0)

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                if self._is_quit_shortcut(event.key):
                    return True

    @staticmethod
    def _is_quit_shortcut(key):
        return (key == K_ESCAPE) or (key == K_q and pygame.key.get_mods() & KMOD_CTRL)

# ==============================================================================
# -- HUD -----------------------------------------------------------------------
# ==============================================================================


class HUD(object):
    def __init__(self, width, height):
        self.dim = (width, height)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        font_name = 'courier' if os.name == 'nt' else 'mono'
        fonts = [x for x in pygame.font.get_fonts() if font_name in x]
        default_font = 'ubuntumono'
        mono = default_font if default_font in fonts else fonts[0]
        mono = pygame.font.match_font(mono)
        self._font_mono = pygame.font.Font(mono, 12 if os.name == 'nt' else 14)
        self._notifications = FadingText(font, (width, 40), (0, height - 40))
        self.help = HelpText(pygame.font.Font(mono, 24), width, height)
        self.server_fps = 0
        self.frame = 0
        self.simulation_time = 0
        self._show_info = True
        self._info_text = []
        self._server_clock = pygame.time.Clock()
        if rospy.get_param("scenario") == 1:
            self.scenario= "EURO NCAP CPNC"
        elif rospy.get_param("scenario") == 2:
            self.scenario= "EURO NCAP CPLA"
        elif rospy.get_param("scenario") == 3:
            self.scenario = "EURO NCAP CBLA"
        elif rospy.get_param("scenario") == 4:
            self.scenario = "EURO NCAP CCRS"
        else:
            self.scenario = "Unknown"
        self.desvel = rospy.get_param("des_vel")

    def on_world_tick(self, timestamp):
        self._server_clock.tick()
        self.server_fps = self._server_clock.get_fps()
        self.frame = timestamp.frame
        self.simulation_time = timestamp.elapsed_seconds

    def tick(self, world, clock):
        self._notifications.tick(world, clock)
        if not self._show_info:
            return
        t = world.player.get_transform()
        v = world.player.get_velocity()
        c = world.player.get_control()
        heading = 'N' if abs(t.rotation.yaw) < 89.5 else ''
        heading += 'S' if abs(t.rotation.yaw) > 90.5 else ''
        heading += 'E' if 179.5 > t.rotation.yaw > 0.5 else ''
        heading += 'W' if -0.5 > t.rotation.yaw > -179.5 else ''
        #colhist = world.collision_sensor.get_collision_history()
        #collision = [colhist[x + self.frame - 200] for x in range(0, 200)]
        #max_col = max(1.0, max(collision))
        #collision = [x / max_col for x in collision]
        vehicles = world.world.get_actors().filter('vehicle.*')
        pedestrians = world.world.get_actors().filter('walker.*')
        self._info_text = [
            'Scenario: % 20s' % self.scenario,
            'Desired Speed: % 9.0f km/h' % self.desvel,
            '',
            'Vehicle: % 20s' % get_actor_display_name(world.player, truncate=20),
            'Simulation time: % 12s' % datetime.timedelta(seconds=int(self.simulation_time)),
            '',
            'Server:  % 16.0f FPS' % self.server_fps,
            #'Client:  % 16.0f FPS' % clock.get_fps(),
            #'',
            #'Map:     % 20s' % world.map.name,
            '',

            'Speed:   % 15.0f km/h' % (3.6 * math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2)),
            u'Heading:% 16.0f\N{DEGREE SIGN} % 2s' % (t.rotation.yaw, heading),
            'Location:% 20s' % ('(% 5.1f, % 5.1f)' % (t.location.x, t.location.y)),
            #'GNSS:% 24s' % ('(% 2.6f, % 3.6f)' % (world.gnss_sensor.lat, world.gnss_sensor.lon)),
            'Height:  % 18.0f m' % t.location.z,
            '']
        #if isinstance(c, carla.VehicleControl):
        #    self._info_text += [
        #        ('Throttle:', c.throttle, 0.0, 1.0),
        #        ('Steer:', c.steer, -1.0, 1.0),
        #        ('Brake:', c.brake, 0.0, 1.0),
        #        ('Reverse:', c.reverse),
        #        ('Hand brake:', c.hand_brake),
        #        ('Manual:', c.manual_gear_shift),
        #        'Gear:        %s' % {-1: 'R', 0: 'N'}.get(c.gear, c.gear)]
        #elif isinstance(c, carla.WalkerControl):
        #    self._info_text += [
        #        ('Speed:', c.speed, 0.0, 5.556),
        #        ('Jump:', c.jump)]
        self._info_text += [
            #'',
            #'Collision:',
            #collision,
            '',
            'Number of vehicles: % 8d' % len(vehicles)]

        if len(vehicles) > 1:
            self._info_text += ['Nearby vehicles:']
            def distance(l): return math.sqrt(
                (l.x - t.location.x) ** 2 + (l.y - t.location.y) ** 2 + (l.z - t.location.z) ** 2)
            vehicles = [(distance(x.get_location()), x) for x in vehicles if x.id != world.player.id]
            for d, vehicle in sorted(vehicles):
                if d > 200.0:
                    break
                vehicle_type = get_actor_display_name(vehicle, truncate=22)
                self._info_text.append('% 4dm %s' % (int(d), vehicle_type))

            self._info_text += ['','Number of pedestrians: % 5d' % len(pedestrians)]
        if len(pedestrians) > 0:
            self._info_text += ['Nearby pedestrians:']

            def distance(l):
                return math.sqrt(
                    (l.x - t.location.x) ** 2 + (l.y - t.location.y) ** 2 + (l.z - t.location.z) ** 2)
            pedestrians = [(distance(x.get_location()), x) for x in pedestrians if x.id != world.player.id]
            for d, pedestrian in sorted(pedestrians):
                if d > 200.0:
                    break
                pedestrian_type = get_actor_display_name(pedestrian, truncate=22)
                self._info_text.append('% 4dm %s' % (int(d), pedestrian_type))

    def toggle_info(self):
        self._show_info = not self._show_info

    def notification(self, text, seconds=2.0):
        self._notifications.set_text(text, seconds=seconds)

    def error(self, text):
        self._notifications.set_text('Error: %s' % text, (255, 0, 0))

    def render(self, display):
        if self._show_info:
            info_surface = pygame.Surface((220, self.dim[1]))
            info_surface.set_alpha(100)
            display.blit(info_surface, (0, 0))
            v_offset = 4
            bar_h_offset = 100
            bar_width = 106
            for item in self._info_text:
                if v_offset + 18 > self.dim[1]:
                    break
                if isinstance(item, list):
                    if len(item) > 1:
                        points = [(x + 8, v_offset + 8 + (1.0 - y) * 30) for x, y in enumerate(item)]
                        pygame.draw.lines(display, (255, 136, 0), False, points, 2)
                    item = None
                    v_offset += 18
                elif isinstance(item, tuple):
                    if isinstance(item[1], bool):
                        rect = pygame.Rect((bar_h_offset, v_offset + 8), (6, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect, 0 if item[1] else 1)
                    else:
                        rect_border = pygame.Rect((bar_h_offset, v_offset + 8), (bar_width, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect_border, 1)
                        f = (item[1] - item[2]) / (item[3] - item[2])
                        if item[2] < 0.0:
                            rect = pygame.Rect((bar_h_offset + f * (bar_width - 6), v_offset + 8), (6, 6))
                        else:
                            rect = pygame.Rect((bar_h_offset, v_offset + 8), (f * bar_width, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect)
                    item = item[0]
                if item:  # At this point has to be a str.
                    surface = self._font_mono.render(item, True, (255, 255, 255))
                    display.blit(surface, (8, v_offset))
                v_offset += 18
        self._notifications.render(display)
        self.help.render(display)

# ==============================================================================
# -- FadingText ----------------------------------------------------------------
# ==============================================================================


class FadingText(object):
    def __init__(self, font, dim, pos):
        self.font = font
        self.dim = dim
        self.pos = pos
        self.seconds_left = 0
        self.surface = pygame.Surface(self.dim)

    def set_text(self, text, color=(255, 255, 255), seconds=2.0):
        text_texture = self.font.render(text, True, color)
        self.surface = pygame.Surface(self.dim)
        self.seconds_left = seconds
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(text_texture, (10, 11))

    def tick(self, _, clock):
        delta_seconds = 1e-3 * clock.get_time()
        self.seconds_left = max(0.0, self.seconds_left - delta_seconds)
        self.surface.set_alpha(500.0 * self.seconds_left)

    def render(self, display):
        display.blit(self.surface, self.pos)

# ==============================================================================
# -- HelpText ------------------------------------------------------------------
# ==============================================================================


class HelpText(



object):
    def __init__(self, font, width, height):
        lines = __doc__.split('\n')
        self.font = font
        self.dim = (680, len(lines) * 22 + 12)
        self.pos = (0.5 * width - 0.5 * self.dim[0], 0.5 * height - 0.5 * self.dim[1])
        self.seconds_left = 0
        self.surface = pygame.Surface(self.dim)
        self.surface.fill((0, 0, 0, 0))
        for n, line in enumerate(lines):
            text_texture = self.font.render(line, True, (255, 255, 255))
            self.surface.blit(text_texture, (22, n * 22))
            self._render = False
        self.surface.set_alpha(220)

    def toggle(self):
        self._render = not self._render

    def render(self, display):
        if self._render:
            display.blit(self.surface, self.pos)

# ==============================================================================
# -- CollisionS



#ensor -----------------------------------------------------------
# ==============================================================================


class CollisionSensor(object):
    def __init__(self, parent_actor, hud):
        self.sensor = None
        self.history = []
        self._parent = parent_actor
        self.hud = hud
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.collision')
        self.sensor = world.spawn_actor(bp, carla.Transform(), attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: CollisionSensor._on_collision(weak_self, event))

    def get_collision_history(self):
        history = collections.defaultdict(int)
        for frame, intensity in self.history:
            history[frame] += intensity
        return history

    @staticmethod
    def _on_collision(weak_self, event):
        self = weak_self()
        if not self:
            return
        actor_type = get_actor_display_name(event.other_actor)
        self.hud.notification('Collision with %r' % actor_type)
        impulse = event.normal_impulse
        intensity = math.sqrt(impulse.x ** 2 + impulse.y ** 2 + impulse.z ** 2)
        self.history.append((event.frame, intensity))
        if len(self.history) > 4000:
            self.history.pop(0)

# ==============================================================================
# -- LaneInvasionSensor --------------------------------------------------------
# ==============================================================================


class LaneInvasionSensor(object):
    def __init__(self, parent_actor, hud):
        self.sensor = None
        self._parent = parent_actor
        self.hud = hud
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.lane_invasion')
        self.sensor = world.spawn_actor(bp, carla.Transform(), attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: LaneInvasionSensor._on_invasion(weak_self, event))

    @staticmethod
    def _on_invasion(weak_self, event):
        self = weak_self()
        if not self:
            return
        lane_types = set(x.type for x in event.crossed_lane_markings)
        text = ['%r' % str(x).split()[-1] for x in lane_types]
        self.hud.notification('Crossed line %s' % ' and '.join(text))

# ==============================================================================
# -- GnssSensor --------------------------------------------------------
# ==============================================================================


class GnssSensor(object):
    def __init__(self, parent_actor):
        self.sensor = None
        self._parent = parent_actor
        self.lat = 0.0
        self.lon = 0.0
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.gnss')
        self.sensor = world.spawn_actor(bp, carla.Transform(carla.Location(x=1.0, z=2.8)),
                                        attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: GnssSensor._on_gnss_event(weak_self, event))

    @staticmethod
    def _on_gnss_event(weak_self, event):
        self = weak_self()
        if not self:
            return
        self.lat = event.latitude
        self.lon = event.longitude

# ==============================================================================
# -- CameraManager -------------------------------------------------------------
# ==============================================================================


class CameraManager(object):
    def __init__(self, parent_actor, hud):
        self.sensor = None
        self.surface = None
        self._parent = parent_actor
        self.hud = hud
        self.recording = False
        #self._camera_transforms = [carla.Transform(carla.Location(x=-5.5, z=2.8), carla.Rotation(pitch=-15)),carla.Transform(carla.Location(x=1.6, z=1.7))]
        self._camera_transforms = [carla.Transform(carla.Location(x=0.44,y=0, z=1.45), carla.Rotation(pitch=-5,yaw=0)),carla.Transform(carla.Location(x=1.6, z=1.7))]
        #self._camera_transforms = [carla.Transform(carla.Location(x=0.44,y=1.0, z=0.8), carla.Rotation(pitch=-15,yaw=-15,roll=10)),carla.Transform(carla.Location(x=1.6, z=1.7))]

        self.transform_index = 1
        self.sensors = [
            ['sensor.camera.rgb', cc.Raw, 'Camera RGB'],
            ['sensor.camera.depth', cc.Raw, 'Camera Depth (Raw)'],
            ['sensor.camera.depth', cc.Depth, 'Camera Depth (Gray Scale)'],
            ['sensor.camera.depth', cc.LogarithmicDepth, 'Camera Depth (Logarithmic Gray Scale)'],
            ['sensor.camera.semantic_segmentation', cc.Raw, 'Camera Semantic Segmentation (Raw)'],
            ['sensor.camera.semantic_segmentation', cc.CityScapesPalette,
             'Camera Semantic Segmentation (CityScapes Palette)'],
            ['sensor.lidar.ray_cast', None, 'Lidar (Ray-Cast)']]
        world = self._parent.get_world()
        bp_library = world.get_blueprint_library()
        for item in self.sensors:
            bp = bp_library.find(item[0])
            if item[0].startswith('sensor.camera'):
                bp.set_attribute('image_size_x', str(hud.dim[0]))
                bp.set_attribute('image_size_y', str(hud.dim[1]))
            elif item[0].startswith('sensor.lidar'):
                bp.set_attribute('range', '50')
            item.append(bp)
        self.index = None

    def toggle_camera(self):
        self.transform_index = (self.transform_index + 1) % len(self._camera_transforms)
        self.sensor.set_transform(self._camera_transforms[self.transform_index])

    def set_sensor(self, index, notify=True):
        index = index % len(self.sensors)
        needs_respawn = True if self.index is None \
            else self.sensors[index][0] != self.sensors[self.index][0]
        if needs_respawn:
            if self.sensor is not None:
                self.sensor.destroy()
                self.surface = None
            self.sensor = self._parent.get_world().spawn_actor(
                self.sensors[index][-1],
                self._camera_transforms[self.transform_index],
                attach_to=self._parent)
            # We need to pass the lambda a weak reference to self to avoid
            # circular reference.
            weak_self = weakref.ref(self)
            self.sensor.listen(lambda image: CameraManager._parse_image(weak_self, image))
        if notify:
            self.hud.notification(self.sensors[index][2])
        self.index = index

    def next_sensor(self):
        self.set_sensor(self.index + 1)

    def toggle_recording(self):
        self.recording = not self.recording
        self.hud.notification('Recording %s' % ('On' if self.recording else 'Off'))

    def render(self, display):
        if self.surface is not None:
            display.blit(self.surface, (0, 0))

    @staticmethod
    def _parse_image(weak_self, image):
        self = weak_self()
        if not self:
            return
        if self.sensors[self.index][0].startswith('sensor.lidar'):
            points = np.frombuffer(image.raw_data, dtype=np.dtype('f4'))
            points = np.reshape(points, (int(points.shape[0] / 3), 3))
            lidar_data = np.array(points[:, :2])
            lidar_data *= min(self.hud.dim) / 100.0
            lidar_data += (0.5 * self.hud.dim[0], 0.5 * self.hud.dim[1])
            lidar_data = np.fabs(lidar_data)  # pylint: disable=E1111
            lidar_data = lidar_data.astype(np.int32)
            lidar_data = np.reshape(lidar_data, (-1, 2))
            lidar_img_size = (self.hud.dim[0], self.hud.dim[1], 3)
            lidar_img = np.zeros(lidar_img_size)
            lidar_img[tuple(lidar_data.T)] = (255, 255, 255)
            self.surface = pygame.surfarray.make_surface(lidar_img)
        else:
            image.convert(self.sensors[self.index][1])
            array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
            array = np.reshape(array, (image.height, image.width, 4))
            array = array[:, :, :3]
            array = array[:, :, ::-1]
            self.surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
        if self.recording:
            image.save_to_disk('_out/%08d' % image.frame)

def run_scenario(scenario,world):

    empiric_delay = 0.075  ## empiric parameter in a way that the pedestrian collide in the middle of the car 'system delay'
    player_pos = world.player.get_location()
    player_size = world.player.bounding_box.extent.x
    crash_point = 223.0733

    if scenario == 1:
        walker_pos = world.walker1.get_location()
        walker_size = world.walker1.bounding_box.extent.y

        if player_pos.x > ((walker_pos.x - player_size - walker_size - rospy.get_param("des_vel") * 4 / 5 - rospy.get_param("des_vel") * empiric_delay) * math.cos(0.014937)):
            world.walker1.apply_control(world.control)

    elif scenario == 2:
        walker_size = world.walker1.bounding_box.extent.x
        walker_pos = world.walker1.get_location()
        if player_pos.x > (crash_point-player_size-walker_size-rospy.get_param("des_vel")*10/5-rospy.get_param("des_vel")*empiric_delay)*math.cos(0.014937):
            if walker_pos.x > 225:
                    world.control.speed = 0
            world.walker1.apply_control(world.control)


    elif scenario == 3:
        npc1_size = world.npc1.bounding_box.extent.x
        npc1_pos = world.npc1.get_location()
        npc1_velocity = world.npc1.get_velocity()

        npc1_vel = math.sqrt(npc1_velocity.x ** 2 + npc1_velocity.y ** 2)

        if player_pos.x > (
                crash_point - player_size - npc1_size - rospy.get_param("des_vel") * 28 / 15 - rospy.get_param("des_vel") * empiric_delay) * math.cos(
                0.014937):

            if npc1_pos.x > 225:
                # start braking
                world.vehicle_control.manual_gear_shift = False
                world.vehicle_control.throttle = 0.0
                world.vehicle_control.brake = 1
                world.npc1.apply_control(world.vehicle_control)
            else:
                if world.npc1.stop:
                    world.npc1.set_target_velocity(carla.Vector3D(x=14.9983 / 3.6, y=0.2240 / 3.6, z=0.000000))
                    npc1_vel = 15 / 3.6
                    world.npc1.stop = False
                # accelerating to 15 Km/h and hold
                world.vehicle_control.manual_gear_shift = True
                world.vehicle_control.gear = 2
                E = world.npc1.vsoll - npc1_vel
                throttle = E * world.npc1.kp * (1 / world.npc1.tn)
                if throttle > 1:
                    throttle = 1
                elif throttle < 0.2:
                    throttle = 0.2
                world.vehicle_control.throttle = throttle
                world.npc1.apply_control(world.vehicle_control)




# ==============================================================================
# -- game_loop() ---------------------------------------------------------
# ==============================================================================

def game_loop():
    pygame.init()
    pygame.font.init()
    world = None

    try:
            ## Connect the client with the Server according to the arguments and wait 4 seconds for Server response
        client = carla.Client(rospy.get_param("carla_host"), int(rospy.get_param("carla_port")))
        client.set_timeout(4.0)
        print("Connected to client")
        ## Inicialize the display and Hud
        display = pygame.display.set_mode((rospy.get_param("cam_width"), rospy.get_param("cam_height")),pygame.HWSURFACE | pygame.DOUBLEBUF)
        hud = HUD(rospy.get_param("cam_width"), rospy.get_param("cam_height"))

        ## Initialise the world (Moving Object and Sensors)
        world = World(client.get_world(),hud)


        #world.restart()
        ## Initialise the clock
        clock = pygame.time.Clock()

        ## Initialize the Keyboard interaction
        controller = KeyboardControl(world)

        while True:
            if controller.parse_events():
                return




            # as soon as the server is ready continue!
            world.world.wait_for_tick(10.0)
            world.tick(clock)
            world.render(display)
            pygame.display.flip()
            world.restart()
           # run_scenario(rospy.get_param("scenario"),world)


    finally:
        world.destroy()
        pygame.quit()

# ==============================================================================
# -- main() --------------------------------------------------------------
# ==============================================================================

def main():

    game_loop()

    #log_level = logging.DEBUG if rospy.get_param("verbose") else logging.INFO
    #logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)
    #logging.info('listening to server %s:%s', rospy.get_param("carla_host"), rospy.get_param("carla_port"))
    #try:
    #    game_loop()
    #except KeyboardInterrupt:
    #    print('\nCancelled by user. Bye!')

# ==============================================================================
# ==============================================================================
if __name__ == '__main__':
     main()
