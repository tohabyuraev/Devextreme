#include "../core/interp.hpp"
#include "graph.hpp"


float graph_4_36(
    const float M_kr,
    const float chi_c)
{
    map_t data_1 = {{0.70000, 0.01272}, {0.75239, 0.01260}, {0.80215, 0.01260}, {0.85080, 0.01183}, {0.90122, 0.01012}, {0.94854, 0.00654}, {1.00000, 0.00000}};
    map_t data_2 = {{0.70000, 0.04512}, {0.75121, 0.04365}, {0.80086, 0.04064}, {0.85492, 0.03575}, {0.89106, 0.03023}, {0.91868, 0.02563}, {0.94564, 0.01929}, {0.96539, 0.01349}, {0.97998, 0.00873}, {1.00000, 0.00000}};
    map_t data_3 = {{0.70000, 0.09231}, {0.72417, 0.08981}, {0.75156, 0.08638}, {0.78190, 0.08183}, {0.80781, 0.07699}, {0.83557, 0.07157}, {0.85832, 0.06603}, {0.87664, 0.06102}, {0.89696, 0.05507}, {0.91542, 0.04813}, {0.93131, 0.04206}, {0.94862, 0.03361}, {0.96050, 0.02702}, {0.97267, 0.01929}, {0.98342, 0.01180}, {1.00000, 0.00000}};
    map_t data_4 = {{0.70000, 0.15696}, {0.73632, 0.14430}, {0.76533, 0.13398}, {0.78932, 0.12511}, {0.81034, 0.11746}, {0.83359, 0.10839}, {0.85691, 0.09825}, {0.87983, 0.08834}, {0.89517, 0.08127}, {0.91075, 0.07286}, {0.92037, 0.06741}, {0.92816, 0.06258}, {0.93746, 0.05669}, {0.95005, 0.04813}, {0.96015, 0.04131}, {0.96974, 0.03361}, {0.97878, 0.02465}, {0.98711, 0.01605}, {1.00000, 0.00000}};

    if (chi_c < 15.0) {
        return interp1d(M_kr, data_1);
    }
    else if (chi_c < 30.0) {
        map_t points = {
            {15.0, interp1d(M_kr, data_1)},
            {30.0, interp1d(M_kr, data_2)},
        };
        return interp1d(chi_c, points);
    }
    else if (chi_c < 45.0) {
        map_t points = {
            {30.0, interp1d(M_kr, data_2)},
            {45.0, interp1d(M_kr, data_3)},
        };
        return interp1d(chi_c, points);
    }
    else if (chi_c < 60.0) {
        map_t points = {
            {45.0, interp1d(M_kr, data_3)},
            {60.0, interp1d(M_kr, data_4)},
        };
        return interp1d(chi_c, points);
    }
    else {
        return interp1d(M_kr, data_4);
    };
}