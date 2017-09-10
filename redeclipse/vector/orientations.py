from redeclipse.vector import CoarseVector, FineVector


#: Reference to own position
SELF = CoarseVector(0, 0, 0)
#: One (coarse) position north of the current location
NORTH = CoarseVector(1, 0, 0)
#: One (coarse) position east of the current location
EAST = NORTH.rotate(90)
#: One (coarse) position south of the current location
SOUTH = NORTH.rotate(180)
#: One (coarse) position west of the current location
WEST = NORTH.rotate(270)

#: Northwest of current location
NORTHWEST = NORTH + WEST
#: Northeast of current location
NORTHEAST = NORTH + EAST
#: Southwest of current location
SOUTHWEST = SOUTH + WEST
#: Southeast of current location
SOUTHEAST = SOUTH + EAST

#: Above current location
ABOVE = CoarseVector(0, 0, 1)
#: Below current location
BELOW = CoarseVector(0, 0, -1)

#: x-y Center of the current 8x8x8 cube
TILE_CENTER = FineVector(4, 4, 0)
#: Vertical center of the current 8x8x8 cube. Combine with TILE_CENTER for the actual cube center.
HALF_HEIGHT = FineVector(0, 0, 4)

NORTH_FINE = FineVector(1, 0, 0)
EAST_FINE = NORTH_FINE.rotate(90)
SOUTH_FINE = NORTH_FINE.rotate(180)
WEST_FINE = NORTH_FINE.rotate(270)
ABOVE_FINE = FineVector(0, 0, 1)
BELOW_FINE = FineVector(0, 0, -1)

#: Map allowing conversion of old style ±xyz to new CoarseVector directions
VEC_ORIENT_MAP = {
    '+x': NORTH,
    '-x': SOUTH,
    '+y': EAST,
    '-y': WEST,
    '+z': ABOVE,
    '-z': BELOW,
}

def get_vector_rotation(vec):
    """
    Get the rotation from a cardinal direction vector.

    :param vec: A directional vector (must be one of the named constants, N/S/E/W)
    :type vec: redeclipse.vector.CoarseVector

    :returns: A (degree) direction
    :rtype: int
    """
    if vec == NORTH:
        return 0
    elif vec == EAST:
        return 90
    elif vec == SOUTH:
        return 180
    elif vec == WEST:
        return 270

#: Inverse of VEC_ORIENT_MAP allowing converting new to old style.
VEC_ORIENT_MAP_INV = {
    v: k
    for (k, v) in VEC_ORIENT_MAP.items()
}

__all__ = [NORTH, SOUTH, ABOVE, BELOW, EAST, WEST]
