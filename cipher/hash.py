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

    def SHA1(input: str) -> str:
        '''
        SHA1 hash function to take an input and produces a 160-bit hash value

        Args:
            input (str): bit string of any length

        Returns:
            str: return a 160-bit string
        '''

        # return a 160-bit string
        output = ''

        assert len(output) == 160
        return output
