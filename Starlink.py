from os import mkdir, remove, rmdir, listdir
from skyfield.api import load, wgs84
import csv
import math
import numpy as np
import datetime
from pathlib import Path

ts = load.timescale()
t = ts.utc(2021, 6, 30)


def get_julian_datetime(date):
    julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int((275 * date.month) / 9.0) + date.day + 1721013.5 + (
        date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0 - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5) + 0.5
    return julian_datetime


active_url = 'https://celestrak.com/NORAD/elements/starlink.txt'
#active_url = 'http://web.archive.org/web/20210630064438/https://celestrak.com/NORAD/elements/goes.txt'
satellites = load.tle_file(active_url)
#by_number = {sat.model.satnum: sat for sat in satellites}
#homeDir = str(Path.home()) + "/Starlink"

#p = Path.resolve(Path(homeDir))
#mkdir(p)

for sat in satellites:
    positions = []
    print(sat.name + ",")
    #_p = Path(f"{str(p)}/{sat}.npy")
    #_p = Path(f"{str(p)}/{sat.name}")

    #t = ts.utc(2025, 5, 11, 0, 0)
    #date = datetime.datetime(2025, 5, 5, 11, 0)
    #jdd = get_julian_datetime(date)
    #geocentric = sat.at(t)
    #positiond = geocentric.position.km
    #a=[[jdd, positiond[0], positiond[1], positiond[2]]]
    with open(Path.resolve(_p), 'w', newline='') as c:
        writer = csv.writer(c, delimiter=',', quotechar='|',
                       quoting=csv.QUOTE_MINIMAL)
        for x in range(11, 31):
            for i in range(24):
                for y in range(1, 60, 1):
                    t = ts.utc(2025, 5, x, i, y)
                    date = datetime.datetime(2025, 5, x, i, y)
                    jd = get_julian_datetime(date)
                    geocentric = sat.at(t)
                    position = geocentric.position.km
                    #a = np.append(a, [[jd, position[0], position[1], position[2]]], axis=0)
                    writer.writerow([jd, position[0], position[1], position[2]])

        for x in range(1, 11):
            for i in range(24):
                for y in range(0, 60, 1):
                    t = ts.utc(2025, 6, x, i, y)
                    date = datetime.datetime(2025, 6, x, i, y)
                    jd = get_julian_datetime(date)
                    geocentric = sat.at(t)
                    position = geocentric.position.km
                    #a = np.append(a, [[jd, position[0], position[1], position[2]]], axis=0)
                    writer.writerow([jd, position[0], position[1], position[2]])


    #with open(_p, 'wb') as f:
    #    np.save(f, a)
    #    print("saved")
