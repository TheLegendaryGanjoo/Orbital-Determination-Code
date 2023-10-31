from os import mkdir, remove, rmdir, listdir
from skyfield.api import load, wgs84
import csv
import math
import datetime
from pathlib import Path

ts = load.timescale()


def get_julian_datetime(date):
    julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int((275 * date.month) / 9.0) + date.day + 1721013.5 + (
        date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0 - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5) + 0.5
    return julian_datetime


homeDir = str(Path.home()) + "/moon"
p = Path.resolve(Path(homeDir))
mkdir(p)

planets = load('de421.bsp')
sun, mercury, venus, earth, moon, mars, jupiter, saturn, neptune, uranus = planets['sun'], planets[
   'mercury'], planets['venus'], planets['earth'], planets['moon'], planets['mars'], planets['jupiter barycenter'], planets['saturn barycenter'], planets['neptune barycenter'], planets['uranus barycenter']


toGen = ['sun', 'mercury', 'venus', 'earth',
         'moon', 'mars', 'jupiter', 'saturn', 'neptune', 'uranus']
toGenerate = [sun, mercury, venus, earth,
              moon, mars, jupiter, saturn, neptune, uranus]

for index in range(0, 12):
    positions = []
    _p = Path(f"{str(p)}/" + toGen[index] + ".csv")
    with open(Path.resolve(_p), 'w', newline='') as c:
        writer = csv.writer(c, delimiter=',', quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
        for x in range(11, 31):
            for i in range(24):
                t = ts.utc(2025, 5, x, i)
                date = datetime.datetime(2025, 5, x, i)
                jd = get_julian_datetime(date)
                position = sun.at(t).observe(toGenerate[index]).position.km
                writer.writerow([jd, position[0], position[1], position[2]])
        for x in range(1, 11):
            for i in range(24):
                t = ts.utc(2025, 6, x, i)
                date = datetime.datetime(2025, 6, x, i)
                jd = get_julian_datetime(date)
                position = sun.at(t).observe(toGenerate[index]).position.km
