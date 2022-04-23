#include "../core/interp.hpp"
#include "graph.hpp"


float graph_4_27(
    const float argument_0,
    const float argument_1)
{
    map_t data_1 = {{0.0, 1.0}, {0.025, 0.838057919453962}, {0.05, 0.713704016315244}, {0.075,0.634719841051644}, {0.1,0.573005445344625}, {0.125,0.517522647220079}, {0.15,0.471196662097383}, {0.2,0.39169997162581}, {0.25,0.326503516798165}, {0.3,0.269765838619792}, {0.35,0.220854875902463}, {0.4,0.175746760156458}, {0.45,0.136234706373233}, {0.5,0.101150572088625}, {0.55,0.0719224910397638}, {0.6,0.0522266123924579}, {0.65,0.0422790713544172} };
    map_t data_2 = {{0.0, 1.0}, {0.025, 0.866082218725098}, {0.05, 0.779842722466462}, {0.075,0.709805600872628}, {0.1,0.651744380258076}, {0.125,0.599018463794246}, {0.15,0.553822374566377}, {0.2,0.475937903465883}, {0.25,0.409351049614229}, {0.3,0.356089262416203}, {0.35,0.308924431705675}, {0.4,0.267791417128466}, {0.45,0.230585917472269}, {0.5,0.206132202809465}, {0.55,0.190055055455735}, {0.6,0.179992016806128}, {0.65,0.175005064226838} };
    map_t data_3 = {{0.0, 1.0}, {0.025, 0.881951720785904}, {0.05, 0.805049476034688}, {0.075,0.74301848069343}, {0.1,0.688752781172883}, {0.125,0.644285352428739}, {0.15,0.605432542571875}, {0.2,0.541410499479033}, {0.25,0.484628714278352}, {0.3,0.439327596284032}, {0.35,0.399666988117971}, {0.4,0.366494265922524}, {0.45,0.334201933556732}, {0.5,0.31392687483607}, {0.55,0.300862685879194}, {0.6,0.292205757666534}, {0.65,0.288010420977612} };
    map_t data_4 = {{0.0, 1.0}, {0.025, 0.892283311351229}, {0.05, 0.828377019288302}, {0.075,0.769630468276592}, {0.1,0.725500182853699}, {0.125,0.68735860257886}, {0.15,0.654422418857708}, {0.2,0.598860421693167}, {0.25,0.555966667659954}, {0.3,0.517631811786938}, {0.35,0.486523316614466}, {0.4,0.461450069910813}, {0.45,0.438980627408237}, {0.5,0.42392611631697}, {0.55,0.412421542961658}, {0.6,0.403705574301067}, {0.65,0.397526697429479} };
    map_t data_5 = {{0.0, 1.0}, {0.025, 0.908576251831605}, {0.05, 0.850123191783481}, {0.075,0.80380299087197}, {0.1,0.762612818146621}, {0.125,0.728886688038982}, {0.15,0.70027560870279}, {0.2,0.655163880471925}, {0.25,0.621791313431838}, {0.3,0.593426654361231}, {0.35,0.573071741793307}, {0.4,0.557353349137001}, {0.45,0.545624435871716}, {0.5,0.535698252015276}, {0.55,0.527819679775371}, {0.6,0.521200649202936}, {0.65,0.514571636137421} };

    if (argument_0 < 1.0) {
        return interp1d(argument_1, data_1);
    }
    else if (argument_0 < 1.5) {
        map_t points = {
            {1.0, interp1d(argument_1, data_1)},
            {1.5, interp1d(argument_1, data_2)},
        };
        return interp1d(argument_0, points);
    }
    else if (argument_0 < 2.0) {
        map_t points = {
            {1.5, interp1d(argument_1, data_2)},
            {2.0, interp1d(argument_1, data_3)},
        };
        return interp1d(argument_0, points);
    }
    else if (argument_0 < 2.5) {
        map_t points = {
            {2.0, interp1d(argument_1, data_3)},
            {2.5, interp1d(argument_1, data_4)},
        };
        return interp1d(argument_0, points);
    }
    else if (argument_0 < 3.0) {
        map_t points = {
            {2.5, interp1d(argument_1, data_4)},
            {3.0, interp1d(argument_1, data_5)},
        };
        return interp1d(argument_0, points);
    }
    else {
        return interp1d(argument_1, data_5);
    };
}