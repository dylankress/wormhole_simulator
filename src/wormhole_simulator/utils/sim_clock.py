#sim_clock.py
class SimClock:
    def __init__(self):
        self.tick = 0

    def advance(self) -> None:
        self.tick += 1

    def current(self) -> int:
        return self.tick

    def reset(self) -> None:
        self.tick = 0

    def __repr__(self):
        return f"<SimClock Tick={self.tick}>"

