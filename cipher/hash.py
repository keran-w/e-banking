from typing import *

class PKC:
    def __init__(self) -> None:
        pass
    

class HMAC:
    def __init__(self) -> None:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass


class Hash:
    def __init__(self) -> None:
        pass

    def SHA1(plaintext: str) -> str:
        '''
        SHA1 hash function to take an plaintext and produces a 160-bit hash value

        Args:
            plaintext (str): bit string of any length

        Returns:
            str: return a 160-bit string
        '''

        # return a 160-bit string
        ciphertext = ''

        assert len(ciphertext) == 160
        return ciphertext
