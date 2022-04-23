#include "../core/interp.hpp"
#include "graph.hpp"


float graph_4_5(
    const float M,
    const float RheL)
{
    map_t data_1 = {{10.0, 2948431.83405761}, {11.8540488374834, 2624495.86413504}, {14.0518473841441, 2325687.15670159}, {16.6571285148507, 2053300.65509550}, {19.7454414907277,1812349.36365008}, {23.3910154232062,1587106.25002598}, {27.7096666987974,1389856.88929117}, {32.8256646693791,1208423.2356284}, {38.8862223677807,1040561.93101611}, {47.6816836662941,865232.853488997}, {58.466542101973,709337.189140976}, {67.8553557749417,603251.925919516}, {78.7518663120756,512258.622337134}, {88.7422479040242,439532.13584902}, {99.9999991346456,376082.796787695}, {118.25431067843,290489.467142136}, {128.595411698276,243162.863276073}, {139.840821150425,190097.788558191}, {152.069618983826,125542.473874264}, {173.449056114054,12681.3152788257}, {196.798921273205,-110581.650853386}, {220.148786432355,-233844.616985599}, {243.498651591506,-357107.583117811}, {266.848516750656,-480370.549250023}, {290.198381909807,-603633.515382235}, {313.548247068957,-726896.481514447}, {336.898112228108,-850159.447646659}, {360.247977387259,-973422.413778872}, {383.597842546409,-1096685.37991108}, {406.94770770556,-1219948.3460433}, {430.29757286471,-1343211.31217551}, {453.647438023861,-1466474.27830772}, {476.997303183011,-1589737.24443993}, {500.347168342162,-1713000.21057214}, {523.697033501312,-1836263.17670436}, {547.046898660463,-1959526.14283657}, {570.396763819614,-2082789.10896878}, {593.746628978764,-2206052.07510099}, {617.096494137915,-2329315.04123321}, {640.446359297065,-2452578.00736542}, {663.796224456216,-2575840.97349763}, {687.146089615366,-2699103.93962984}, {710.495954774517,-2822366.90576205}, {733.845819933668,-2945629.87189427}, {757.195685092818,-3068892.83802648}, {780.545550251969,-3192155.80415869}, {803.895415411119,-3315418.7702909}, {827.24528057027,-3438681.73642311}, {850.59514572942,-3561944.70255533}, {873.945010888571,-3685207.66868754}, {897.294876047722,-3808470.63481975}, {920.644741206872,-3931733.60095196}, {943.994606366023,-4054996.56708418}, {967.344471525173,-4178259.53321639}, {990.694336684324,-4301522.4993486}, {1014.04420184347,-4424785.46548081}, {1037.39406700262,-4548048.43161303}, {1060.74393216178,-4671311.39774524}, {1084.09379732093,-4794574.36387745}, {1107.44366248008,-4917837.33000966}, {1130.79352763923,-5041100.29614187}, {1154.14339279838,-5164363.26227409} };
    map_t data_2 = {{10.0, 3679260.57771473}, {14.0518473841441, 3283638.15659487}, {19.7454414907277, 2858767.49287279}, {27.7096666987974, 2423407.41333743}, {38.8862223677807,2011192.92907763}, {58.466542101973,1543711.13117586}, {78.7518663120756,1214938.57591053}, {99.9999991346456,946276.60393283}, {118.25431067843,736423.186494455}, {128.595411698276,647087.324525356}, {139.840821150425,548392.820404942}, {152.069618983826,451731.039759632}, {165.367800529509,358386.256120919}, {179.828881236796,267058.723174628}, {195.554554292491,180482.905636948}, {206.105812808632,100000.0}, {229.692904393422,-79917.6527960905}, {254.103227103802,-266114.749214654}, {278.513549814183,-452311.845633217}, {302.923872524563,-638508.942051781}, {327.334195234943,-824706.038470344}, {351.744517945323,-1010903.13488891}, {376.154840655704,-1197100.23130747}, {400.565163366084,-1383297.32772603}, {424.975486076464,-1569494.4241446}, {449.385808786844,-1755691.52056316}, {473.796131497224,-1941888.61698172}, {498.206454207605,-2128085.71340029}, {522.616776917985,-2314282.80981885}, {547.027099628365,-2500479.90623741}, {571.437422338745,-2686677.00265598}, {595.847745049126,-2872874.09907454}, {620.258067759506,-3059071.1954931}, {644.668390469886,-3245268.29191167}, {669.078713180266,-3431465.38833023}, {693.489035890647,-3617662.48474879}, {717.899358601027,-3803859.58116736}, {742.309681311407,-3990056.67758592}, {766.720004021787,-4176253.77400448}, {791.130326732168,-4362450.87042305}, {815.540649442548,-4548647.96684161}, {839.950972152928,-4734845.06326017}, {864.361294863308,-4921042.15967874}, {888.771617573688,-5107239.2560973}, {913.181940284069,-5293436.35251586}, {937.592262994449,-5479633.44893442}, {962.002585704829,-5665830.54535299}, {986.412908415209,-5852027.64177155}, {1010.82323112559,-6038224.73819012}, {1035.23355383597,-6224421.83460868}, {1059.64387654635,-6410618.93102724}, {1084.05419925673,-6596816.0274458}, {1108.46452196711,-6783013.12386437}, {1132.87484467749,-6969210.22028293}, {1157.28516738787,-7155407.31670149}, {1181.69549009825,-7341604.41312006}, {1206.10581280863,-7527801.50953862} };
    map_t data_3 = {{10.0, 4000000.00000000}, {14.0518473841441, 3804495.52235223}, {19.7454414907277, 3576346.17309578}, {27.7096666987974, 3340209.58298707}, {38.8862223677807,3080504.03806261}, {58.4665421019731,2720866.42238453}, {78.7518663120756,2457166.45182617}, {99.9999991346456,2215465.84819352}, {118.25431067843,2012173.71934758}, {128.595411698276,1916391.87464238}, {139.840821150425,1797892.40131988}, {152.069618983827,1673631.16566808}, {165.367800529509,1544607.43826341}, {179.828881236796,1423018.47969851}, {195.554554292491,1292562.06992669}, {232.460657470781,1032971.4648959}, {276.331878166963,778930.799647571}, {301.281005684365,608451.988496094}, {328.482710674943,440137.026295966}, {342.991136817049,358336.215128032}, {358.140371203487,276486.55355934}, {373.958717056259,198175.736029746}, {382.127991869404,160642.793533891}, {400.0,100000.0}, {407.142857142857,75763.058756961}, {435.510204081633,-20492.222179679}, {463.877551020408,-116747.503116319}, {492.244897959184,-213002.78405296}, {520.612244897959,-309258.0649896}, {548.979591836735,-405513.34592624}, {577.34693877551,-501768.62686288}, {605.714285714286,-598023.90779952}, {634.081632653061,-694279.18873616}, {662.448979591837,-790534.4696728}, {690.816326530612,-886789.750609441}, {719.183673469388,-983045.031546081}, {747.551020408163,-1079300.31248272}, {775.918367346939,-1175555.59341936}, {804.285714285714,-1271810.874356}, {832.65306122449,-1368066.15529264}, {861.020408163265,-1464321.43622928}, {889.387755102041,-1560576.71716592}, {917.755102040816,-1656831.99810256}, {946.122448979592,-1753087.2790392}, {974.489795918367,-1849342.55997584}, {1002.85714285714,-1945597.84091248}, {1031.22448979592,-2041853.12184912}, {1059.59183673469,-2138108.40278576}, {1087.95918367347,-2234363.6837224}, {1116.32653061225,-2330618.96465904}, {1144.69387755102,-2426874.24559568}, {1173.0612244898,-2523129.52653232}, {1201.42857142857,-2619384.80746896}, {1229.79591836735,-2715640.0884056}, {1258.16326530612,-2811895.36934224}, {1286.5306122449,-2908150.65027888}, {1314.89795918367,-3004405.93121552}, {1343.26530612245,-3100661.21215216}, {1371.63265306122,-3196916.4930888}, {1400.0,-3293171.77402544} };
    map_t data_4 = {{10.0, 3327972.76921780}, {14.0518473841441, 3283638.15659487}, {19.7454414907277, 3158365.94148842}, {27.7096666987974, 3040272.02181630}, {38.8862223677807,2905506.56533469}, {58.4665421019731,2720866.42238453}, {78.7518663120756,2550714.29363647}, {99.9999991346457,2426110.28255497}, {118.25431067843,2342111.95124411}, {128.595411698276,2289810.95438913}, {139.840821150425,2238003.64265902}, {152.069618983827,2187537.60035932}, {165.367800529509,2142512.03591385}, {179.828881236796,2094361.20699365}, {195.554554292491,2034213.27833838}, {232.460657470781,1905987.16435848}, {276.331878166963,1753566.67931005}, {301.281005684365,1671813.67188051}, {328.482710674943,1589330.1195733}, {342.991136817049,1551631.23351175}, {358.140371203487,1507696.49539598}, {373.95871705626,1464190.49061565}, {390.47572769423,1418840.43167565}, {485.453217820756,1193285.52704827}, {603.532588527675,955182.982034007}, {650.083650412549,856449.102127347}, {700.225241464864,741717.20904093}, {754.234302729145,608742.522861671}, {812.409135984945,478722.326964823}, {853.67011020874,354571.233553138}, {897.026664009973,246548.135428711}, {919.523834992393,181229.345777272}, {949.067957693876,100000.0}, {955.761044820074,81597.8597846768}, {1005.53794191587,-55259.9791421512}, {1055.31483901166,-192117.818068979}, {1105.09173610745,-328975.656995807}, {1154.86863320325,-465833.495922635}, {1204.64553029904,-602691.334849463}, {1254.42242739483,-739549.173776291}, {1304.19932449063,-876407.012703119}, {1353.97622158642,-1013264.85162995}, {1403.75311868221,-1150122.69055677}, {1453.53001577801,-1286980.5294836}, {1503.3069128738,-1423838.36841043}, {1553.08380996959,-1560696.20733726}, {1602.86070706539,-1697554.04626409}, {1652.63760416118,-1834411.88519091}, {1702.41450125697,-1971269.72411774}, {1752.19139835277,-2108127.56304457}, {1801.96829544856,-2244985.4019714}, {1851.74519254436,-2381843.24089823}, {1901.52208964015,-2518701.07982505}, {1951.29898673594,-2655558.91875188}, {2001.07588383174,-2792416.75767871}, {2050.85278092753,-2929274.59660554}, {2100.62967802332,-3066132.43553237}, {2150.40657511912,-3202990.27445919}, {2200.18347221491,-3339848.11338602}, {2249.9603693107,-3476705.95231285}, {2299.7372664065,-3613563.79123968}, {2349.51416350229,-3750421.6301665}, {2399.29106059808,-3887279.46909333}, {2449.06795769388,-4024137.30802016} };
    map_t data_5 = {{10.0, 2948431.83405761}, {38.8862223677807, 2929404.71850323}, {47.6816836662941, 2923672.06248654}, {58.4665421019731, 2908214.81666961}, {78.7518663120756,2879670.70837814}, {99.9999991346457,2841194.80403625}, {118.25431067843,2811921.45162463}, {139.840821150425,2779576.12153377}, {165.367800529509,2721048.72224561}, {195.554554292491,2663753.68944704}, {232.460657470781,2586568.93079422}, {276.331878166963,2510128.60260794}, {328.482710674943,2414225.87461647}, {358.140371203487,2367657.42105187}, {390.47572769423,2321987.23508112}, {485.453217820756,2162223.52157702}, {603.532588527675,1959860.36803529}, {650.08365041255,1864629.37100066}, {700.225241464864,1774025.71525224}, {754.234302729146,1686494.97082906}, {812.409135984947,1603283.00890908}, {853.67011020874,1533640.1568522}, {897.026664009975,1464258.62085567}, {942.585228558732,1393473.61598961}, {1000.0,1326110.490867}, {1078.60605201939,1203280.70738263}, {1174.59946582926,1051991.46219483}, {1279.13606876515,884084.550880412}, {1392.97618466124,693208.5317824}, {1516.94780439315,471689.48314737}, {1651.95260808627,278349.845099651}, {1723.89598053903,179425.265372828}, {1792.34784498045,100000.0}, {1818.64064927494,69492.2413651262}, {1885.62733998883,-8232.97079401507}, {1952.61403070271,-85958.1829531564}, {2019.6007214166,-163683.395112298}, {2086.58741213049,-241408.607271439}, {2153.57410284437,-319133.819430581}, {2220.56079355826,-396859.031589722}, {2287.54748427215,-474584.243748863}, {2354.53417498603,-552309.455908005}, {2421.52086569992,-630034.668067146}, {2488.50755641381,-707759.880226287}, {2555.4942471277,-785485.092385429}, {2622.48093784158,-863210.30454457}, {2689.46762855547,-940935.516703712}, {2756.45431926936,-1018660.72886285}, {2823.44100998324,-1096385.94102199}, {2890.42770069713,-1174111.15318114}, {2957.41439141102,-1251836.36534028}, {3024.4010821249,-1329561.57749942}, {3091.38777283879,-1407286.78965856}, {3158.37446355268,-1485012.0018177}, {3225.36115426656,-1562737.21397684}, {3292.34784498045,-1640462.42613598} };
    map_t data_6 = {{10.0, 3679266.88459059}, {78.7518663120756, 3679266.88459059}, {99.9999991346457, 3654526.37982186}, {139.840821150425, 3635652.58991639}, {195.554554292491,3566418.45309606}, {276.331878166963,3430459.39020263}, {390.47572769423,3240162.75217165}, {485.453217820756,3075013.93092682}, {603.532588527675,2894785.16254159}, {700.225241464864,2755151.61693073}, {812.409135984947,2608106.91881005}, {897.026664009975,2498699.83437865}, {1000.0,2369257.79217514}, {1078.60605201939,2249948.87404659}, {1174.59946582926,2115015.33056303}, {1279.13606876515,1972631.07650651}, {1392.97618466124,1815162.74293112}, {1516.94780439315,1662939.68054479}, {1651.95260808627,1506361.323989}, {1798.97252328648,1348767.86011174}, {1959.07686679272,1172107.66768136}, {2131.77493123062,961896.894985065}, {2319.69680947906,731220.628025095}, {2524.18452298855,472131.631062572}, {2633.09201905649,343271.054537036}, {2746.69839612609,216860.231404202}, {2805.32668273086,159686.635244492}, {2846.05628756034,100000.0} };

    if (M < 0.0) {
        return interp1d(RheL, data_1);
    }
    else if (M < 1.0) {
        map_t points = {
            {0.0, interp1d(RheL, data_1)},
            {1.0, interp1d(RheL, data_2)},
        };
        return interp1d(M, points);
    }
    else if (M < 2.0) {
        map_t points = {
            {1.0, interp1d(RheL, data_2)},
            {2.0, interp1d(RheL, data_3)},
        };
        return interp1d(M, points);
    }
    else if (M < 3.0) {
        map_t points = {
            {2.0, interp1d(RheL, data_3)},
            {3.0, interp1d(RheL, data_4)},
        };
        return interp1d(M, points);
    }
    else if (M < 4.0) {
        map_t points = {
            {3.0, interp1d(RheL, data_4)},
            {4.0, interp1d(RheL, data_5)},
        };
        return interp1d(M, points);
    }
    else if (M < 5.0) {
        map_t points = {
            {4.0, interp1d(RheL, data_5)},
            {5.0, interp1d(RheL, data_6)},
        };
        return interp1d(M, points);
    }
    else {
        return interp1d(RheL, data_6);
    };
}