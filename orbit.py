import matplotlib.pyplot as plt
import datetime as dt
import time as ti

from astropy import time
from astropy import units as u
from poliastro.neos import neows

from poliastro.examples import molniya
from poliastro.plotting import plot, OrbitPlotter, BODY_COLORS
from poliastro.bodies import Sun, Earth, Mars
from poliastro.twobody import Orbit

date = time.Time("2018-02-07 12:00", scale='utc')

start=dt.datetime(2018, 2, 1, 12, 0)
length=1
days_dt=[dt.datetime(2018, 2, 1, 12, 0)+dt.timedelta(days=1*n) for n in range(length)]
days_as=[time.Time(day, scale='tdb') for day in days_dt]

op = OrbitPlotter(num_points=1000)

r_p = Sun.R + 165 * u.km
r_a = Sun.R + 215 * u.km

a = (r_p + r_a) / 2

roadster=Orbit.from_classical(attractor=Sun,
                              a=0.9860407221838553 * u.AU,
                              ecc=0.2799145376150214*u.one,
                              inc=1.194199764898942*u.deg,
                              raan=49*u.deg,
                              argp=286*u.deg,
                              nu=23*u.deg,
                              epoch=date)
for date in days_as:
    
    apophis_orbit = neows.orbit_from_name('99942')
    spacex = neows.orbit_from_name('-143205')
    op.orbits.clear()
    earth = Orbit.from_body_ephem(Earth, date)
    mars = Orbit.from_body_ephem(Mars, date)
    
    op.plot(earth, label=Earth)
    op.plot(mars, label=Mars)
    op.plot(roadster, label='Roadster')
    op.plot(apophis_orbit, label='Apophis')
    op._redraw()
    plt.pause(0.01)

    
input('type to exit')

op.plot(Orbit.from_body_ephem(Mars, time.Time("2018-07-28 12:00", scale='utc')), label=Mars)
