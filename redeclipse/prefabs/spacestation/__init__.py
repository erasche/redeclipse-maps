import os
from redeclipse.prefabs.magica import MagicaRoom
from redeclipse.entities import Pusher
from redeclipse.vector import FineVector
from redeclipse.vector.orientations import EAST, SOUTH, ABOVE, WEST, NORTH
from redeclipse.vector.orientations import rotate_yaw
from redeclipse.prefabs import LIGHTMAN


class station_tube1(MagicaRoom):
    name = 'station_tube1'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_tube1.vox')
    room_type = 'hallway_setpiece'

    doors = [
        {'orientation': WEST, 'offset': WEST},
        {'orientation': EAST, 'offset': EAST},
    ]


class station_tube3(MagicaRoom):
    name = 'station_tube3'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_tube3.vox')
    room_type = 'hallway_setpiece'

    doors = [
        {'orientation': WEST, 'offset': WEST},
        {'orientation': EAST, 'offset': EAST + EAST + EAST},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + (ABOVE + EAST).rotate(self.orientation), size_factor=2)


class station_tube_jumpx(MagicaRoom):
    name = 'station_tube_jumpx'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_tube_jumpx.vox')
    room_type = 'hallway_setpiece'

    doors = [
        {'orientation': WEST, 'offset': WEST + NORTH},
        {'orientation': EAST, 'offset': EAST + EAST + EAST + NORTH},
        {'orientation': NORTH, 'offset': EAST + NORTH + NORTH + NORTH},
        {'orientation': SOUTH, 'offset': EAST + SOUTH},

        {'orientation': WEST, 'offset': WEST + ABOVE + ABOVE + NORTH},
        {'orientation': EAST, 'offset': EAST + EAST + EAST + ABOVE + ABOVE + NORTH},
        {'orientation': NORTH, 'offset': EAST + NORTH + NORTH + ABOVE + ABOVE + NORTH},
        {'orientation': SOUTH, 'offset': EAST + SOUTH + ABOVE + ABOVE},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + (EAST + NORTH + ABOVE).rotate(self.orientation), size_factor=2)

        pusher_a = Pusher(
            xyz=self.pos + (EAST + NORTH + FineVector(4, 5, 12)).rotate(self.orientation),
            pitch=90,
            maxrad=1,
            yaw=rotate_yaw(0, self.orientation),
            force=230,
        )
        xmap.ents.append(pusher_a)


class station_tubeX(MagicaRoom):
    name = 'station_tubeX'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_tubeX.vox')
    room_type = 'hallway_setpiece'

    doors = [
        {'orientation': WEST, 'offset': WEST + NORTH},
        {'orientation': EAST, 'offset': EAST + EAST + EAST + NORTH},
        {'orientation': NORTH, 'offset': EAST + NORTH + NORTH + NORTH},
        {'orientation': SOUTH, 'offset': EAST + SOUTH},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + (EAST + NORTH).rotate(self.orientation))


class station_endcap(MagicaRoom):
    name = 'station_endcap'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_endcap.vox')
    room_type = 'endcap'

    doors = [
        {'orientation': WEST, 'offset': WEST},
    ]


class station_right(MagicaRoom):
    name = 'station_right'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_right.vox')
    room_type = 'hallway'

    doors = [
        {'orientation': WEST, 'offset': WEST},
        {'orientation': SOUTH, 'offset': SOUTH},
    ]


class station_ring(MagicaRoom):
    name = 'station_ring'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_ring.vox')
    room_type = 'setpiece_large'

    doors = [
        {'orientation': WEST, 'offset': WEST + NORTH + NORTH},
        {'orientation': EAST, 'offset': (EAST * 5) + NORTH + NORTH},
        {'orientation': SOUTH, 'offset': (EAST * 2) + SOUTH},
        {'orientation': NORTH, 'offset': (EAST * 2) + (NORTH * 5)},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + (EAST * 2).rotate(self.orientation))
        LIGHTMAN.light(xmap, self.pos + (NORTH * 2).rotate(self.orientation))
        LIGHTMAN.light(xmap, self.pos + ((EAST * 2) + (NORTH * 4)).rotate(self.orientation))
        LIGHTMAN.light(xmap, self.pos + ((EAST * 4) + (NORTH * 2)).rotate(self.orientation))


class station_ring_vertical(MagicaRoom):
    name = 'station_ring_vertical'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_ring_vertical.vox')
    room_type = 'setpiece_large'

    doors = [
        {'orientation': WEST, 'offset': WEST + ABOVE + ABOVE},
        {'orientation': EAST, 'offset': (EAST * 5) + ABOVE + ABOVE},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + ((EAST * 0.5) + (ABOVE * 3)).rotate(self.orientation))
        LIGHTMAN.light(xmap, self.pos + ((EAST * 3.5) + (ABOVE * 3)).rotate(self.orientation))
        LIGHTMAN.light(xmap, self.pos + ((EAST * 2) + (ABOVE * 4)).rotate(self.orientation))


class station_sphere(MagicaRoom):
    name = 'station_sphere'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_sphere.vox')
    room_type = 'setpiece_medium'

    doors = [
        {'orientation': WEST, 'offset': WEST + NORTH + ABOVE},
        {'orientation': EAST, 'offset': (EAST * 3) + NORTH + ABOVE},
        {'orientation': NORTH, 'offset': EAST + NORTH + NORTH + NORTH + ABOVE},
        {'orientation': SOUTH, 'offset': EAST + SOUTH + ABOVE},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + (EAST + NORTH).rotate(self.orientation), size_factor=3)


class station_sphere_slice(MagicaRoom):
    name = 'station_sphere_slice'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_sphere_slice.vox')
    room_type = 'setpiece_medium'

    doors = [
        {'orientation': WEST, 'offset': WEST + NORTH},
        {'orientation': EAST, 'offset': EAST * 3 + NORTH},
        {'orientation': NORTH, 'offset': EAST + NORTH + NORTH + NORTH},
        {'orientation': SOUTH, 'offset': EAST + SOUTH},
    ]

    def render_extra(self, world, xmap):
        LIGHTMAN.light(xmap, self.pos + (EAST + NORTH).rotate(self.orientation), size_factor=2)


class station_stair2(MagicaRoom):
    name = 'station_stair2'
    vox_file = os.path.abspath(__file__).replace('__init__.py', 'station_stair2.vox')
    room_type = 'stair'

    doors = [
        {'orientation': WEST, 'offset': WEST},
        {'orientation': EAST, 'offset': EAST * 2 + ABOVE},
    ]
