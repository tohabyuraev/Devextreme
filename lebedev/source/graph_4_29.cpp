#include "../core/interp.hpp"
#include "graph.hpp"


float graph_4_29(
    const float chi)
{
    map_t data = {
        {0.00000, 1.00000},
        {5.00000, 0.98120},
        {10.00000, 0.94577},
        {15.00000, 0.89539},
        {20.00000, 0.82578},
        {25.00000, 0.73201},
        {30.00000, 0.62439},
        {35.00000, 0.51699},
        {40.00000, 0.42221},
        {45.00000, 0.34407},
        {50.00000, 0.27732},
        {55.00000, 0.21878},
        {60.00000, 0.16811},
        {65.00000, 0.12684},
        {70.00000, 0.09803},
        {75.00000, 0.07685},
        {80.00000, 0.06335},
    };
    return interp1d(chi, data);
}