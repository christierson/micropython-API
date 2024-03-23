# arduino-controller

python 3.7.17

Requires a `boardconfig.py` (gitignored):

```
# boardconfig.py

import pyfirmata

BOARD = pyfirmata.Arduino(<Arduino port>)
FREQ = 12
```
