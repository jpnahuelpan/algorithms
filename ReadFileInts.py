from typing import List


class ReadInts():
    def __init__(self, file: str) -> None:
        self._file = file

    def read(self) -> List:
        f = open(self._file, "r")
        list_ints: List[int] = []
        for line in f:
            list_ints.append(int(line))
        f.close()
        return list_ints
