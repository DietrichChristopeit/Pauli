from machine import Pin


class Meccabrain:

    def __init__(self, io_pin_nr: int):
        self._io_Pin: Pin = Pin(io_pin_nr, Pin.OUT)
        return

