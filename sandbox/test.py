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
up = 3
down = 4

try:

    while True:
        print('up')
        digitalWrite(up, HIGH)
        delay(500)
        digitalWrite(up, LOW)

        delay(6000)

        print('down')
        digitalWrite(down, HIGH)
        delay(500)
        digitalWrite(down, LOW)

        delay(6000)

except KeyboardInterrupt:
    digitalWrite(ALL, LOW)
