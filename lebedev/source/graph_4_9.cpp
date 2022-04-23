#include "../core/interp.hpp"
#include "graph.hpp"


float graph_4_9(
    const float argument_0,
    const float argument_1)
{
    map_t data_1 = {{0.5, 4.98735360294118}, {0.5125, 4.96806979476823}, {0.525, 4.94480763282122}, {0.5375,4.91913111576297}, {0.55,4.88918414705038}, {0.5625,4.85625062763478}, {0.575,4.81990693217952}, {0.5875,4.78034029844058}, {0.6,4.73252532965098}, {0.6125,4.68106654248995}, {0.625,4.62709184142914}, {0.6375,4.57077604707262}, {0.649999999999999,4.50590120346714}, {0.662499999999999,4.43470059794527}, {0.674999999999999,4.35229926367572}, {0.687499999999999,4.26841794726066}, {0.699999999999999,4.18193416225173}, {0.712499999999999,4.08792978674603}, {0.724999999999999,3.98724881969083}, {0.737499999999999,3.87471527350578}, {0.749999999999999,3.75698284135789}, {0.762499999999999,3.63163971805932}, {0.774999999999999,3.50096912100239}, {0.787499999999999,3.36136632861099}, {0.799999999999999,3.20688873911258}, {0.812499999999999,3.03727698315524}, {0.824999999999999,2.84703437315165}, {0.837499999999999,2.63554418145136}, {0.849999999999999,2.39951239548777}, {0.862499999999999,2.14573337006619}, {0.874999999999999,1.92502093357869}, {0.887499999999999,1.75221634906722}, {0.899999999999999,1.59715208541886}, {0.912499999999999,1.46427641675724}, {0.924999999999998,1.36599723684628}, {0.937499999999998,1.28786913076079}, {0.949999999999998,1.21749775836936}, {0.962499999999998,1.15587216975217}, {0.974999999999998,1.10392457123314}, {0.987499999999998,1.06691018058096}, {0.999999999999998,1.04192094899868}};
    map_t data_2 = {{0.5, 4.98735360294118}, {0.5125, 4.84654184073013}, {0.525, 4.71431035336218}, {0.5375,4.58699623999887}, {0.55,4.46000109911405}, {0.5625,4.3336437013241}, {0.575,4.21133452947012}, {0.5875,4.08535821342282}, {0.6,3.95449581903978}, {0.6125,3.83538370859705}, {0.625,3.70466180071209}, {0.6375,3.5600739499038}, {0.649999999999999,3.40579493766587}, {0.662499999999999,3.24479079066409}, {0.674999999999999,3.0603578395866}, {0.687499999999999,2.83717470621845}, {0.699999999999999,2.59960637354118}, {0.712499999999999,2.39071123250936}, {0.724999999999999,2.21823981866239}, {0.737499999999999,2.07711709019414}, {0.749999999999999,1.94778088433508}, {0.762499999999999,1.83277264178337}, {0.774999999999999,1.7415316250639}, {0.787499999999999,1.66837501504761}, {0.799999999999999,1.60435641017127}, {0.812499999999999,1.54920549233225}, {0.824999999999999,1.49928603280671}, {0.837499999999999,1.45302536573128}, {0.849999999999999,1.40724153444748}, {0.862499999999999,1.36716700881431}, {0.874999999999999,1.32949256208}, {0.887499999999999,1.29168689812431}, {0.899999999999999,1.2599050620255}, {0.912499999999999,1.22694125192463}, {0.924999999999998,1.19572241634417}, {0.937499999999998,1.16501063382059}, {0.949999999999998,1.13490885990746}, {0.962499999999998,1.10801510725181}, {0.974999999999998,1.08454113886967}, {0.987499999999998,1.06181120265872}, {0.999999999999998,1.04192094899868}};
    map_t data_3 = {{0.5, 4.98735360294118}, {0.5125, 4.62922452890558}, {0.525, 4.15981290794350}, {0.5375,3.76255609573033}, {0.55,3.4034035083621}, {0.5625,3.11316281699004}, {0.575,2.86751217596842}, {0.5875,2.67334534902058}, {0.6,2.53066690222961}, {0.6125,2.41379971734102}, {0.625,2.3056368650142}, {0.6375,2.20531505638628}, {0.649999999999999,2.10660187776256}, {0.662499999999999,2.02753352316775}, {0.674999999999999,1.9559848952467}, {0.687499999999999,1.89030091296681}, {0.699999999999999,1.82558713568977}, {0.712499999999999,1.77073319730676}, {0.724999999999999,1.72036390742786}, {0.737499999999999,1.6726633605651}, {0.749999999999999,1.62588198354105}, {0.762499999999999,1.58036609815324}, {0.774999999999999,1.53385245053386}, {0.787499999999999,1.49222870460134}, {0.799999999999999,1.45218080933612}, {0.812499999999999,1.41596292289575}, {0.824999999999999,1.38165222948719}, {0.837499999999999,1.3493967017881}, {0.849999999999999,1.31746698750012}, {0.862499999999999,1.28490245498064}, {0.874999999999999,1.2548193421409}, {0.887499999999999,1.22928643122963}, {0.899999999999999,1.20023473656079}, {0.912499999999999,1.17531000442947}, {0.924999999999998,1.15239619158079}, {0.937499999999998,1.13114230006282}, {0.949999999999998,1.11021241163646}, {0.962499999999998,1.08974009667361}, {0.974999999999998,1.07103701050013}, {0.987499999999998,1.05538636531696}, {0.999999999999998,1.04192094899868}};
    map_t data_4 = {{0.5, 4.98735357266035}, {0.5125, 4.15689049560639}, {0.525, 3.50488244541065}, {0.5375,2.95352709174255}, {0.55,2.63072380376052}, {0.5625,2.41722077150418}, {0.575,2.24102529129034}, {0.5875,2.09308618232532}, {0.6,1.97096484765083}, {0.6125,1.87681500234627}, {0.625,1.80339725180563}, {0.6375,1.74146009547897}, {0.649999999999999,1.68403728889067}, {0.662499999999999,1.63347109652095}, {0.674999999999999,1.58853754951233}, {0.687499999999999,1.54628643391892}, {0.699999999999999,1.51176866378754}, {0.712499999999999,1.4811068033572}, {0.724999999999999,1.44985472609597}, {0.737499999999999,1.4174044759631}, {0.749999999999999,1.38871479895025}, {0.762499999999999,1.35994215410876}, {0.774999999999999,1.33341552347077}, {0.787499999999999,1.31053014075139}, {0.799999999999999,1.28885091782759}, {0.812499999999999,1.26572477574498}, {0.824999999999999,1.24397806953152}, {0.837499999999999,1.22363761643086}, {0.849999999999999,1.20491842933664}, {0.862499999999999,1.18768983014971}, {0.874999999999999,1.17072037639524}, {0.887499999999999,1.15319584083782}, {0.899999999999999,1.13777267687861}, {0.912499999999999,1.12300549028281}, {0.924999999999998,1.10868130291957}, {0.937499999999998,1.09476832910936}, {0.949999999999998,1.08092125968776}, {0.962499999999998,1.06906717739238}, {0.974999999999998,1.05944999918139}, {0.987499999999998,1.05036821375106}, {0.999999999999998,1.04192095588235}};

    if (argument_0 < 1.9) {
        return interp1d(argument_1, data_1);
    }
    else if (argument_0 < 2.7) {
        map_t points = {
            {1.9, interp1d(argument_1, data_1)},
            {2.7, interp1d(argument_1, data_2)},
        };
        return interp1d(argument_0, points);
    }
    else if (argument_0 < 3.12) {
        map_t points = {
            {2.70, interp1d(argument_1, data_2)},
            {3.12, interp1d(argument_1, data_3)},
        };
        return interp1d(argument_0, points);
    }
    else if (argument_0 < 3.65) {
        map_t points = {
            {3.12, interp1d(argument_1, data_3)},
            {3.65, interp1d(argument_1, data_4)},
        };
        return interp1d(argument_0, points);
    }
    else {
        return interp1d(argument_1, data_4);
    };
}