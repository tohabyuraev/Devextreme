#include "../core/interp.hpp"
#include "graph.hpp"


float graph_3_4(
    const float argument_0,
    const float argument_1)
{
    map_t data_1 = {{-0.40000, 0.03484}, {-0.30395, 0.03482}, {-0.20347, 0.03503}, {-0.10362, 0.03515}, {-0.04973, 0.03577}, {-0.00002, 0.03657}, {0.05335, 0.03753}, {0.09913, 0.03773}, {0.15485, 0.03765}, {0.21660, 0.03705}, {0.27049, 0.03620}, {0.33929, 0.03473}, {0.39894, 0.03341}, {0.45179, 0.03241}, {0.49967, 0.03149}, {0.59908, 0.02987}, {0.69954, 0.02829}, {0.80288, 0.02677}, {0.90099, 0.02539}, {1.00000, 0.02410}};
    map_t data_2 = {{-0.40000, 0.03501}, {-0.30395, 0.03502}, {-0.20347, 0.03517}, {-0.10306, 0.03530}, {-0.04071, 0.03694}, {0.00006, 0.03848}, {0.03560, 0.04033}, {0.07157, 0.04239}, {0.09969, 0.04335}, {0.13218, 0.04388}, {0.16837, 0.04410}, {0.20478, 0.04408}, {0.25492, 0.04356}, {0.30397, 0.04284}, {0.35651, 0.04185}, {0.40884, 0.04078}, {0.46727, 0.03963}, {0.53245, 0.03840}, {0.59786, 0.03717}, {0.67416, 0.03578}, {0.75657, 0.03432}, {0.84465, 0.03270}, {0.92422, 0.03129}, {1.00000, 0.02994}};

    if (argument_1 < 0.0) {
        return interp1d(argument_0, data_1);
    }
    else if (argument_1 < 1.0) {
        map_t points = {
            {0.0, interp1d(argument_0, data_1)},
            {1.0, interp1d(argument_0, data_2)},
        };
        return interp1d(argument_1, points);
    }
    else {
        return interp1d(argument_0, data_2);
    };
}