"""
Date Created:                   2018-02-27
Date Modified:                  2018-02-27
Version:                        1
Contract Hash:                  69d771147507c1c44a7842624b5c47c0d03c359c
Available on NEO TestNet:       False
Available on CoZ TestNet:       False
Available on MainNet:           False
Example Build Test Command:     build /path/to/current-height.py test ff 02 False False
Example Import Command:         import contract /path/to/current-height.avm ff 02 False False
Example Invoke:                 testinvoke 69d771147507c1c44a7842624b5c47c0d03c359c
Estimate Operation Count:       25
Estimate GAS Consumption:       0.026
"""


from boa.blockchain.vm.Neo.Blockchain import GetHeight


def Main():
    """
    :return: Current block height.
    :rtype: int
    """
    current_height = GetHeight()  # Obtain height value (in integer) via built-in GetHeight() function
    return current_height
