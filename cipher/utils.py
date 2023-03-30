import random
from typing import *


class PRNG:
    """pseudo random number generator (PRNG)"""

    def __init__(self, SEED: int) -> None:
        """Set PRNG random seed

        Args:
            SEED (int): the random seed
        """
        random.seed(SEED)

    def __call__(self, low: int, high: int) -> int:
        """Get a random integer in range [low, high]

        Args:
            low (int): lower bound of the random integer
            high (int): upper bound of the random integer

        Returns:
            int: the random integer
        """
        return random.randint(low, high+1)
