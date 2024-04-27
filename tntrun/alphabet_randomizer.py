import random
from typing import Callable

class AlphabetRandomizer:
    """Handles randomly picking letters from a subset of the English alphabet a
       according to either a Gaussian or a uniform distribution."""

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, mode: str, dist: Callable[[], float] = lambda: random.randrange(10, 26)):
        self.current_alphabet = self.get_sized_set(dist) if mode == "size" else self.get_bounded_set(dist)
        mu, sig = random.random() * len(self.current_alphabet), random.random() * (len(self.current_alphabet) / 3)
        self.gaussian_dist = lambda: random.gauss(mu, sig)

    def clamp(self, i: float, low: int, high: int) -> int:
        """Clamps i to be in [low, high]."""
        return min(max(int(i), low), high)
    
    def get_sized_set(self, dist: Callable[[], float]) -> str:
        """Gets a subset of the alphabet by randomly picking a random number of letters."""
        lst = random.sample(self.alphabet, self.clamp(dist(), 1, 26))
        return ''.join(lst)

    def get_bounded_set(self, dist: Callable[[], float]) -> str:
        """Gets a subset of the alphabet by randomly picking the bounds of the region."""
        a, b = self.clamp(dist(), 0, 25), self.clamp(dist(), 0, 25)
        return self.alphabet[min(a, b): max(a, b) + 1]

    def uniform_pick(self) -> str:
        """Picks a random letter from the current alphabet uniformly."""
        return random.choice(self.current_alphabet)

    def gaussian_pick(self) -> str:
        """Picks a random letter from the current alphabet according to a gaussian distribution."""
        return self.current_alphabet[self.clamp(self.gaussian_dist(), 0, len(self.current_alphabet)-1)]

    def pick(self) -> str:
        """Picks a random letter according to a random distribution."""
        return random.choice([self.uniform_pick, self.gaussian_pick])()
