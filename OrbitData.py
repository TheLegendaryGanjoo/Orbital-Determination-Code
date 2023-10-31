pip install jplephem
pip install skyfield
from skyfield.api import load
from skyfield.elementslib import osculating_elements_of

planets = load('de421.bsp')
ts = load.timescale()

def k0rbit_Elements():
    ts = load.timescale()
    t = ts.utc(2026, 10, 1)

    planets = load('de421.bsp')
    earth = planets['earth']
    moon = planets['moon']

    #moon barycenter --> earth
    position = (earth - moon).at(t)
    elements = osculating_elements_of(position)

    e = elements.eccentricity
    a = elements.semi_major_axis.km
    i = elements.inclination.radians
    longOfAscNode = elements.longitude_of_ascending_node.radians
    argOfPeriapsis = elements.argument_of_periapsis.radians
    T = elements.period_in_days*86400
    m = elements.mean_anomaly.radians
    v = elements.true_anomaly.radians

    print(e,a,i,longOfAscNode,argOfPeriapsis,T,m,v)

k0rbit_Elements()
