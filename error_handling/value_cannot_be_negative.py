class ValueCannotBeNegative(Exception):
    """Value should be higher than zero"""


for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
