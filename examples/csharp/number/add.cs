using Neo.SmartContract.Framework;

// Date Created:                2018-03-03
// Date Modified:               2018-03-93
// Version:                     1
// Contract Hash:               0x4f088dab7a5167adeda956881c213ace55b64ebd
// Available on NEO TestNet:    False
// Available on CoZ TestNet:    False
// Available on MainNet:        False

// Example:
// Test Invoke:            
// Expected Result:             7
// Operation Count:             59
// GAS Consumption:             0.043 (Debugger) / 0.054 (neo-gui-developer)  <-- Trying to get information about this difference of values

namespace SumSmartContract
{
    public class Contract : SmartContract
    {
        public static int Main(int a, int b)
        {
            var c = a + b;
            return c;
        }
    }
}