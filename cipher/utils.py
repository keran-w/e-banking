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

    def isPrime(self, n: int) -> bool:
        """Check whether n is a prime number or not

        Args:
            n (int): the number to be checked

        Returns:
            bool: return true if n is prime; otherwise, false
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def __call__(self, low: int, high: int, prime=False) -> int:
        """Get a random integer in range [low, high]

        Args:
            low (int): lower bound of the random integer
            high (int): upper bound of the random integer
            prime (bool, optional): 
                whether the number generated should be prime. 
                Defaults to False.

        Returns:
            int: the random integer
        """
        assert low <= high
        if prime:
            all_primes = [n for n in range(low, high+1) if self.isPrime(n)]
            assert len(all_primes) > 0
            random_index = self(0, len(all_primes)-1)
            random_prime = all_primes[random_index]
            return random_prime
        else:
            random_number = random.randint(low, high)
            return random_number
