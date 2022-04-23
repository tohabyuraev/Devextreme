#include "../core/interp.hpp"
#include "graph.hpp"


float graph_4_42(
    const float argument_0,
    const float argument_1)
{
    map_t data_1 = {{-3.5, 0.664941306361023}, {-3.25, 0.627586064933643}, {-3.0, 0.591746112175901}, {-2.75,0.553687237760123}, {-2.5,0.515074956176316}, {-2.25,0.4759883222389}, {-2.0,0.434624797004157}, {-1.75,0.392312567062197}, {-1.5,0.349051632413017}, {-1.25,0.302391175487717}, {-1.0,0.256364047489956}, {-0.75,0.202068378227357}, {-0.5,0.143838240177612}, {-0.25,0.0751817598419332}, {0.0,0.0}, {1.0,-0.307089122658404}};
    map_t data_2 = {{-3.5, 0.669945101978095}, {-3.25, 0.633718164339943}, {-3.0, 0.596903318189314}, {-2.75,0.559480732920465}, {-2.5,0.521433433990318}, {-2.25,0.482747777945602}, {-2.0,0.443413872035613}, {-1.75,0.403425912305961}, {-1.5,0.362749621930762}, {-1.25,0.32093723329103}, {-1.0,0.277178718357939}, {-0.75,0.231193569869166}, {-0.5,0.182342978064343}, {-0.375,0.155047431208191}, {-0.25,0.126393209534366}, {-0.125,0.102460126599138}, {0.0,0.0843403024515715}, {0.125,0.0726130768436684}, {0.25,0.060760323035263}, {0.375,0.0395141931291114}, {0.5,0.0}, {1.5,-0.447944984797558}};
    map_t data_3 = {{-3.5, 0.674968608730459}, {-3.25, 0.639234066825375}, {-3.0, 0.601206821322086}, {-2.75,0.565616476516818}, {-2.5,0.52822170079321}, {-2.25,0.490826925069602}, {-2.0,0.453432149345994}, {-1.75,0.416116432344846}, {-1.5,0.379116950233539}, {-1.25,0.34006194133827}, {-1.0,0.3014022260553}, {-0.75,0.26171474738035}, {-0.5,0.219655507031599}, {-0.375,0.200121562988864}, {-0.25,0.178391873351358}, {-0.125,0.155888846915908}, {0.0,0.136501294188419}, {0.125,0.133596264952093}, {0.25,0.128928637607101}, {0.375,0.121409100436316}, {0.5,0.110696882470576}, {0.625,0.0951565450800999}, {0.75,0.0719322529245313}, {0.875,0.0406249963422711}, {1.0,0.0}, {2.0,-0.340889932796131}};
    map_t data_4 = {{-3.5, 0.687432313307140}, {-3.25, 0.650946581398625}, {-3.0, 0.614062594728929}, {-2.75,0.576884418497881}, {-2.5,0.539520094542662}, {-2.25,0.502080116951215}, {-2.0,0.464675818844177}, {-1.75,0.42741772582849}, {-1.5,0.390380754055557}, {-1.25,0.3532463992962}, {-1.0,0.315429582501425}, {-0.75,0.276324707296866}, {-0.5,0.23615863474614}, {-0.375,0.216052556753614}, {-0.25,0.196536553244837}, {-0.125,0.179298064782127}, {0.0,0.165695237050238}, {0.125,0.156122555194201}, {0.25,0.149202964228572}, {0.375,0.143480348984389}, {0.5,0.137771666812869}, {0.625,0.131021407987505}, {0.75,0.122870080858643}, {0.875,0.113182390346224}, {1.0,0.101737681661538}, {1.125,0.0875049884307223}, {1.25,0.0682589279035459}, {1.375,0.0407368089358053}, {1.5,0.0}, {2.5,-0.395175734733879}};
    map_t data_5 = {{-3.5, 0.698118763981290}, {-3.25, 0.661309023638049}, {-3.0, 0.624119799115070}, {-2.75,0.587310056474979}, {-2.5,0.550215702422722}, {-2.25,0.512646999428537}, {-2.0,0.477034507953928}, {-1.75,0.440476736926049}, {-1.5,0.402443540161618}, {-1.25,0.366869386291439}, {-1.0,0.332278849578962}, {-0.75,0.294573525200431}, {-0.5,0.260268365089144}, {-0.375,0.243001939417761}, {-0.25,0.22630473657071}, {-0.125,0.208709856616485}, {0.0,0.192768464829984}, {0.125,0.189243601797113}, {0.25,0.187301661097322}, {0.375,0.18374824222241}, {0.5,0.179165711688067}, {0.625,0.173800020041493}, {0.75,0.167489626639795}, {0.875,0.161084742684426}, {1.0,0.15268983261909}, {1.125,0.143691824434346}, {1.25,0.132880877545224}, {1.375,0.120435384501473}, {1.5,0.106355092877345}, {1.625,0.0880555634119868}, {1.75,0.0631588069976783}, {1.875,0.0349850182132887}, {2.0,0.0}, {3.0,-0.292159984743165}};
    map_t data_6 = {{-3.5, 0.713637094547349}, {-3.25, 0.676940844628718}, {-3.0, 0.641150553029576}, {-2.75,0.605944678308315}, {-2.5,0.570973238068554}, {-2.25,0.535878603071331}, {-2.0,0.500317289571148}, {-1.75,0.463986498203548}, {-1.5,0.426987754198891}, {-1.25,0.389940357217486}, {-1.0,0.353535990164586}, {-0.75,0.317906944565324}, {-0.5,0.281862297288008}, {-0.375,0.263756804228666}, {-0.25,0.247274600327247}, {-0.125,0.233781735756706}, {0.0,0.224067715091473}, {0.125,0.217599281378701}, {0.25,0.213188272424569}, {0.375,0.209930306912604}, {0.5,0.207072753385167}, {0.625,0.20390800860565}, {0.75,0.199917200629028}, {0.875,0.194993093087425}, {1.0,0.189080011712727}, {1.125,0.182125018831809}, {1.25,0.174079204823748}, {1.375,0.164895298051781}, {1.5,0.15449585906166}, {1.625,0.142766702381883}, {1.75,0.129557661431661}, {1.875,0.114669423819291}, {2.0,0.097832295726426}, {2.25,0.0566374007787316}, {2.5,0.0}, {3.5,-0.259415379839999}};
    map_t data_7 = {{-3.5, 0.733175398363890}, {-3.25, 0.696840012751407}, {-3.0, 0.662212290937919}, {-2.75,0.626446123475769}, {-2.5,0.591106876684916}, {-2.25,0.555329734685064}, {-2.0,0.519951981670181}, {-1.75,0.48475015774614}, {-1.5,0.44994236187375}, {-1.25,0.415531361999049}, {-1.0,0.381125662017186}, {-0.75,0.34668902562282}, {-0.5,0.312630526633663}, {-0.375,0.295269230491558}, {-0.25,0.278092859438301}, {-0.125,0.261337051944808}, {0.0,0.24601745000883}, {0.125,0.241601850989213}, {0.25,0.240824900527833}, {0.5,0.235904811111196}, {0.75,0.228077996249367}, {1.0,0.219653496508563}, {1.25,0.207585972153219}, {1.5,0.195973826075435}, {1.75,0.179261440444426}, {2.0,0.158906030628637}, {2.25,0.135545124061522}, {2.5,0.106173223991758}, {2.75,0.0623202941201557}, {3.0,0.0}, {4.0,-0.281117203828195}};
    map_t data_8 = {{-3.5, 0.803788327971296}, {-3.25, 0.769521113740980}, {-3.0, 0.734229297230067}, {-2.75,0.700645149260006}, {-2.5,0.665353332749095}, {-2.25,0.631313806501474}, {-2.0,0.596363523698732}, {-1.75,0.56175477460416}, {-1.5,0.528056782064709}, {-1.25,0.494472634094647}, {-1.0,0.461457708971536}, {-0.75,0.426924858307336}, {-0.5,0.393004639825887}, {-0.375,0.377284973049707}, {-0.25,0.360891353754694}, {-0.125,0.343684343323353}, {0.0,0.329415604708268}, {0.125,0.326126344931766}, {0.25,0.325196077212443}, {0.5,0.322008429269522}, {0.75,0.318365403049041}, {1.0,0.312900863718319}, {1.25,0.305842500416137}, {1.5,0.297645691420054}, {1.75,0.285988005169388}, {2.0,0.274239245141482}, {2.25,0.25839208045268}, {2.5,0.243227983207359}, {2.75,0.220276917106334}, {3.0,0.194047127276591}, {3.25,0.159620528125053}, {3.5,0.120412456869136}, {3.75,0.0644009265035386}, {4.0,0.0}, {5.0,-0.239033809297446}};
    map_t data_9 = {{-3.5, 0.887564861929586}, {-3.25, 0.852728421436910}, {-3.0, 0.819030428897459}, {-2.75,0.787267794037639}, {-2.5,0.754480558053307}, {-2.25,0.720441031805686}, {-2.0,0.688223018668305}, {-1.75,0.656118850100314}, {-1.5,0.624014681532323}, {-1.25,0.592024357533723}, {-1.0,0.561627857506582}, {-0.75,0.529295999799812}, {-0.5,0.499999999056127}, {-0.375,0.48453611232846}, {-0.25,0.469761711635591}, {-0.125,0.454540399344772}, {0.0,0.441494643370294}, {0.125,0.43726460752257}, {0.25,0.435738022715022}, {0.5,0.43283827944881}, {0.75,0.428534902120534}, {1.0,0.423525741067372}, {1.25,0.41658122233458}, {1.5,0.409522859032397}, {1.75,0.400187604342414}, {2.0,0.390510815944261}, {2.25,0.378670980727697}, {2.5,0.365920388956013}, {2.75,0.351689817782258}, {3.0,0.333702375818632}, {3.25,0.314234954452935}, {3.5,0.289986061172857}, {3.75,0.264143343921318}, {4.0,0.234885289588079}, {4.25,0.195381224009735}, {4.5,0.150526463670061}, {4.75,0.0900749973239503}, {5.0,0.0}, {6.0,-0.445834717838386}};
    map_t data_10 = {{-3.5, 0.962364376222621}, {-3.25,0.9323094082962250}, {-3.0,0.9028236648242040}, {-2.75,0.874248677907305}, {-2.5,0.844307556157725}, {-2.25,0.814594123546924}, {-2.0,0.784880690936125}, {-1.75,0.756988771435565}, {-1.5,0.728186095379886}, {-1.25,0.700294175879326}, {-1.0,0.672743790086937}, {-0.75,0.645193404294548}, {-0.5,0.618667619626669}, {-0.375,0.605552725911503}, {-0.25,0.592119066723479}, {-0.125,0.578457718396674}, {0.0,0.5655932820556}, {0.125,0.562723347841307}, {0.25,0.561547030204245}, {0.5,0.558416304670424}, {0.75,0.555279690241466}, {1.0,0.550634831625782}, {1.25,0.544213997657043}, {1.5,0.537907010266251}, {1.75,0.530393268686508}, {2.0,0.522497230818955}, {2.25,0.513845043545312}, {2.5,0.503257498592039}, {2.75,0.489823839404014}, {3.0,0.47604864650782}, {3.25,0.459996562223825}, {3.5,0.441326052843858}, {3.75,0.421403253200601}, {4.0,0.399203562169544}, {4.25,0.373569561383106}, {4.5,0.3447988490445}, {4.75,0.31417465987858}, {5.0,0.277516708534987}, {5.25,0.235394217860673}, {5.5,0.182570337663695}, {5.75,0.111872860072481}, {6.0,0.0}};

    if (argument_1 < 0.0) {
        return interp1d(argument_0, data_1);
    }
    else if (argument_1 < 0.5) {
        map_t points = {
            {0.0, interp1d(argument_0, data_1)},
            {0.5, interp1d(argument_0, data_2)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 1.0) {
        map_t points = {
            {0.5, interp1d(argument_0, data_2)},
            {1.0, interp1d(argument_0, data_3)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 1.5) {
        map_t points = {
            {1.0, interp1d(argument_0, data_3)},
            {1.5, interp1d(argument_0, data_4)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 2.0) {
        map_t points = {
            {1.5, interp1d(argument_0, data_4)},
            {2.0, interp1d(argument_0, data_5)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 2.5) {
        map_t points = {
            {2.0, interp1d(argument_0, data_5)},
            {2.5, interp1d(argument_0, data_6)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 3.0) {
        map_t points = {
            {2.5, interp1d(argument_0, data_6)},
            {3.0, interp1d(argument_0, data_7)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 4.0) {
        map_t points = {
            {3.0, interp1d(argument_0, data_7)},
            {4.0, interp1d(argument_0, data_8)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 5.0) {
        map_t points = {
            {4.0, interp1d(argument_0, data_8)},
            {5.0, interp1d(argument_0, data_9)},
        };
        return interp1d(argument_1, points);
    }
    else if (argument_1 < 6.0) {
        map_t points = {
            {5.0, interp1d(argument_0, data_9)},
            {6.0, interp1d(argument_0, data_10)},
        };
        return interp1d(argument_1, points);
    }
    else {
        return interp1d(argument_0, data_10);
    };
}