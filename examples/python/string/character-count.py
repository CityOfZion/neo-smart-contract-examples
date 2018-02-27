"""
Date Created:                   2018-02-27
Date Modified:                  2018-02-27
Version:                        1
Contract Hash:                  0a8b34b4097f0a472d5a31726d70ff807d37490d
Available on NEO TestNet:       False
Available on CoZ TestNet:       False
Available on MainNet:           False
Example Build Test Command:     build /path/to/character-count.py test 07 02 False False lorem
Example Import Command:         import contract /path/to/character-count.avm 07 02 False False
Example Invoke:                 testinvoke 0a8b34b4097f0a472d5a31726d70ff807d37490d 2 5
Estimate Operation Count:       37
Estimate GAS Consumption:       0.035
"""


def Main(text):
    """
    :param text: Input string of concern
    :type a: str
    :return: Character count of the input string
    :rtype: int
    """
    result = len(text)  # Obtain string length by using built in len() function
    return result
