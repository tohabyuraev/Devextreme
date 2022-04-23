#include "../core/interp.hpp"
#include "graph.hpp"


float graph_3_21(
    const float M,
    const float lambda_n)
{
    map_t data_1 = {{0.70000, 0.93429}, {0.79355, 0.94892}, {0.89260, 0.96158}, {0.99164, 0.96999}, {1.09242, 0.97623}, {1.19320, 0.98132}, {1.29242, 0.98482}, {1.39164, 0.98773}, {1.48871, 0.98957}, {1.58578, 0.99124}, {1.68468, 0.99254}, {1.78359, 0.99356}, {1.97906, 0.99501}, {2.18058, 0.99535}, {2.37700, 0.99568}, {2.57329, 0.99601}, {2.76828, 0.99634}, {2.96705, 0.99668}, {3.21390, 0.99709}, {3.46076, 0.99751}, {3.70761, 0.99793}, {3.95446, 0.99834}, {4.20132, 0.99876}, {4.44817, 0.99918}, {4.69502, 0.99959}, {4.94188, 1.00001}};
    map_t data_2 = {{0.70000, 0.82205}, {0.79355, 0.86140}, {0.89260, 0.89666}, {0.99164, 0.92046}, {1.09242, 0.93928}, {1.19320, 0.95130}, {1.29242, 0.96142}, {1.39164, 0.96885}, {1.48871, 0.97392}, {1.58578, 0.97745}, {1.68468, 0.98146}, {1.78359, 0.98426}, {1.97906, 0.98882}, {2.18058, 0.99205}, {2.37700, 0.99379}, {2.57329, 0.99470}, {2.76828, 0.99529}, {2.96705, 0.99576}, {3.21390, 0.99633}, {3.46076, 0.99690}, {3.70761, 0.99741}, {3.95446, 0.99796}, {4.20132, 0.99847}, {4.44817, 0.99901}, {4.69502, 0.99952}, {4.94188, 1.00001}};
    map_t data_3 = {{0.70000, 0.71277}, {0.79355, 0.76119}, {0.89260, 0.80493}, {0.99164, 0.83990}, {1.09242, 0.87016}, {1.19320, 0.89545}, {1.29242, 0.91403}, {1.39164, 0.92790}, {1.48871, 0.93999}, {1.58578, 0.94974}, {1.68468, 0.95862}, {1.78359, 0.96635}, {1.97906, 0.97730}, {2.18058, 0.98473}, {2.37700, 0.98961}, {2.57329, 0.99287}, {2.76828, 0.99413}, {2.96705, 0.99485}, {3.21390, 0.99566}, {3.46076, 0.99635}, {3.70761, 0.99702}, {3.95446, 0.99767}, {4.20132, 0.99828}, {4.44817, 0.99889}, {4.69502, 0.99946}, {4.94188, 1.00001}};
    map_t data_4 = {{0.70000, 0.60000}, {0.79355, 0.64967}, {0.89260, 0.70394}, {0.99164, 0.75040}, {1.09242, 0.79151}, {1.19320, 0.82670}, {1.29242, 0.85510}, {1.39164, 0.87993}, {1.48871, 0.89980}, {1.58578, 0.91462}, {1.68468, 0.92736}, {1.78359, 0.93776}, {1.97906, 0.95490}, {2.18058, 0.96680}, {2.37700, 0.97655}, {2.57329, 0.98403}, {2.76828, 0.99005}, {2.96705, 0.99402}, {3.21390, 0.99527}, {3.46076, 0.99608}, {3.70761, 0.99677}, {3.95446, 0.99744}, {4.20132, 0.99809}, {4.44817, 0.99876}, {4.69502, 0.99940}, {4.94188, 1.00001}};

    if (M < 1.0) {
        return 1.0;
    }
    else if (M < 2.0) {
        map_t points = {
            {1.0, 1.0},
            {2.0, interp1d(lambda_n, data_1)},
        };
        return interp1d(M, points);
    }
    else if (M < 3.0) {
        map_t points = {
            {2.0, interp1d(lambda_n, data_1)},
            {3.0, interp1d(lambda_n, data_2)},
        };
        return interp1d(M, points);
    }
    else if (M < 4.0) {
        map_t points = {
            {3.0, interp1d(lambda_n, data_2)},
            {4.0, interp1d(lambda_n, data_3)},
        };
        return interp1d(M, points);
    }
    else if (M < 5.0) {
        map_t points = {
            {4.0, interp1d(lambda_n, data_3)},
            {5.0, interp1d(lambda_n, data_4)},
        };
        return interp1d(M, points);
    }
    else {
        return interp1d(lambda_n, data_4);
    };
}