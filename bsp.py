from jplephem.spk import SPK
from os import mkdir, remove, rmdir, listdir
from skyfield.api import load, wgs84
import csv
import math
import datetime
from pathlib import Path


def get_julian_datetime(date):
    julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int((275 * date.month) / 9.0) + date.day + 1721013.5 + (
        date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0 - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5) + 0.5
    return julian_datetime


def bspReader(startDate, endDate, epoch, path):
    kernel = SPK.open(path)
    positions = []
    time = startDate
    positions = []
    homeDir = str(Path.home()) + "/bsp"
    p = Path.resolve(Path(homeDir))
    mkdir(p)
    _p = Path(f"{str(p)}/HLS-NRHO.csv")
    with open(Path.resolve(_p), 'w', newline='') as c:
        writer = csv.writer(c, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        time = startDate
        while time < endDate:
            #date = get_julian_datetime(datetime.datetime(2025, 6, x, y, z))
            index = math.floor((time - epoch)/6.94)
            position = (kernel.segments[index].compute(time))
            writer.writerow([time, position[0], position[1], position[2]])
            time += 0.0006944444


bspReader((2460806.5 + 0), (2460806.5 + 9), 2458850.84, 'HLS-NRHO.bsp')
