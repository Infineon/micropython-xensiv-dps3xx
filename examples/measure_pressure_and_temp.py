from machine import I2C
import DPS
from time import sleep

i2c = I2C(scl='P0_2', sda='P0_3', freq=400000)
dps = DPS.DPS(i2c)

for i in range(8):
    t = dps.measureTemperatureOnce()
    p = dps.measurePressureOnce()
    print(f'Pressure: {p},\t Temperature: {t}')
    sleep(1)