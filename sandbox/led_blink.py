from shiftpi import (
    HIGH, 
    LOW, 
    ALL,
    digitalWrite, 
    startupMode,
    delay,
    shiftRegisters
)

shiftRegisters(1)
startupMode(LOW)
pins = [1, 2, 3, 4]

try:
    cpt = 0
    while True:
        cpt += 1
        digitalWrite(pins[cpt % len(pins)], HIGH)
        delay(100)
        digitalWrite(pins[cpt % len(pins)], LOW)
        delay(100)
except KeyboardInterrupt:
    digitalWrite(ALL, LOW)
