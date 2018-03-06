using Neo.SmartContract.Framework;

// Date Created:                2018-03-03
// Date Modified:               2018-03-93
// Version:                     1
// Contract Hash:               0x4f088dab7a5167adeda956881c213ace55b64ebd
// Available on NEO TestNet:    False
// Available on CoZ TestNet:    False
// Available on MainNet:        False

// Example  
// Input Params     :           0202
// Output Params    :           02
// Expected Result  :           7
// Operation Count  :           Contract compiled in Debug: 60 / Contract compiled in Release: 34
// GAS Consumption  :           Contract compiled in Debug:     0.043 (NEO Debugger) / 0.054 (neo-gui-developer)  
// GAS Consumption  :           Contract compiled in Release:   0.024 (NEO Debugger) / 0.035 (neo-gui-developer)

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