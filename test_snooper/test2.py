import pysnooper
from pathlib import Path


@pysnooper.snoop(Path.cwd()/'test_snooper/log/file.log')
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


number_to_bits(7)
