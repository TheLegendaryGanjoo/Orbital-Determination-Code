from os import mkdir, remove, rmdir, listdir
from skyfield.api import load, wgs84
import csv
import math
import datetime
from pathlib import Path

ts = load.timescale()
t = ts.utc(2021, 6, 30)

def get_julian_datetime(date):
    julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int((275 * date.month) / 9.0) + date.day + 1721013.5 + (date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0 - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5) + 0.5
    return julian_datetime

toGenerate = {
    "AIM"       :31304,
    "AQUA"        :27424,
    "AURA"        :28376,
    "FGST"        :33053,
    "GPM_CORE"    :39574,
    "GRACE FO1"    :43476,
    "GRACE FO2"    :43477,
    "HST"        :20580,
    "ICESAT 2"    :43613,
    "ICON"      :44628,
    "IRIS"        :39197,
    "ISS"       :25544,
    "LANDSAT 7"    :25682,
    "LANDSAT 8"    :39084,
    "METOP A"    :29499,
    "METOP B"    :38771,
    "METOP C"   :43689,
    "NUSTAR"     :38358,
    "OCO-2"     :40059,
    "SCISAT 1"    :27858,
    "SEAHAWK 1"    :43820,
    "SMAP"      :40376,
    "SOLAR B"    :29479,
    "SOYUZ"        :48159,
    "STPSat 3"    :39380,
    "STPSat 4"    :45043,
    "STPSat 5"    :43762,
    "SWIFT"        :28485,
    "TERRA"        :25994,
    "TDRS 3"    :19548,
    "TDRS 5"    :22314,
    "TDRS 6"    :21639,
    "TDRS 7"    :23613,
    "TDRS 8"    :26388,
    "TDRS 9"    :27389,
    "TDRS 10"    :27566,
    "TDRS 11"    :39070,
    "TDRS 12"    :39504,
    "TDRS 13"    :42915,
    "Geotail"    :22049,
    "SDO"       :36395,
    "THEMIS_A"    :30580,
    "THEMIS_E"    :30798,
    "THEMIS_D"    :30797,
    "MMS 1"     :40482,
    "MMS 2"     :40483,
    "MMS 3"     :40484,
    "MMS 4"     :40485,
}

#active_url = 'http://web.archive.org/web/20210630064435/http://celestrak.com/NORAD/elements/active.txt'
active_url = 'http://celestrak.com/NORAD/elements/active.txt'
satellites = load.tle_file(active_url)
by_number = {sat.model.satnum: sat for sat in satellites}
homeDir = str(Path.home()) + "/satellit"
p = Path.resolve(Path(homeDir))
mkdir(p)

for kvp in toGenerate.items():
    #try:
    satellite = by_number[kvp[1]]
    positions = []
    _p = Path(f"{str(p)}/{kvp[0]}.csv")
    with open(Path.resolve(_p), 'w', newline='') as c:
        writer = csv.writer(c, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for x in range(8,16):
            for i in range(24):
                for y in range(0,60,1):
                    t = ts.utc(2021, 8, x, i, y)
                    date = datetime.datetime(2021, 8, x, i, y)
                    jd = get_julian_datetime(date)
                    geocentric = satellite.at(t)
                    position = geocentric.position.km
                    writer.writerow([jd, position[0], position[2], position[1]])
