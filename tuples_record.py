from geolib import geohash as gh # type: ignore
from typing import NamedTuple

PRECISION = 9

def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)

class Coordinate(NamedTuple):
    lat: float
    lon: float

def geohash2(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PRECISION)

def display(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):0.1f}°{ns}, {abs(lon):0.1f}°{ew}'


if __name__=='__main__':
    shanghai = 31.2304, 121.4737
    print(geohash(shanghai))

    shanghai = Coordinate(31.2304, 121.4737)
    print(geohash2(shanghai))

    print(display(shanghai))