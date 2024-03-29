#include "interp.hpp"


int testInterp1d() {
    float x1[] = {1.0, 2.0, 3.0};
    float y1[] = {10, 50, 70};

    map_t source = {
        {1.0, 10},
        {2.0, 50},
        {3.0, 70},
    };

    float value; std::cin >> value;

    std::cout
        << "With vectors = "
        << interp(value, x1, y1) << std::endl;
    std::cout
        << "With map = "
        << interp1d(value, source) << std::endl;
    return EXIT_SUCCESS;
}

int testInterp2d() {
    vector_t x = {1.0, 2.0, 3.0};
    vector_t y = {15, 30, 70};
    matrix_t z = {
        {0, 1, 2},
        {0, 1, 3},
        {0, 1, 2},
    };

    float value_x; std::cin >> value_x;
    float value_y; std::cin >> value_y;

    std::cout
        << "interp2d = "
        << interp2d(value_x, value_y, x, y, z) << std::endl;
    return EXIT_SUCCESS;
}

float interp(
    const float x,
    const float* data_x,
    const float* data_y)
{
    vector_t data_x_ = vector_t(
        data_x, data_x + sizeof data_x / sizeof data_x[0] + 1);
    vector_t data_y_ = vector_t(
        data_y, data_y + sizeof data_y / sizeof data_y[0] + 1);
    return interp1d(x, data_x_, data_y_);
}

float interp1d(
    const float x,
    const vector_t& data_x,
    const vector_t& data_y)
{
    auto bound = std::equal_range(
        data_x.begin(), data_x.end(), x);

    if (data_x.begin() == bound.first) {
        return data_y.front();
    } else if (data_x.end() == bound.second) {
        return data_y.back();
    } else {
        const int i = bound.first - data_x.begin() - 1;
        const int j = bound.first - data_x.begin() - 0;

        return data_y[j] + (x - data_x[j]) *
            (data_y[i] - data_y[j]) /
            (data_x[i] - data_x[j]);
    };
}

float interp1d(
    const float x,
    const map_t& data_xy)
{
    auto bound = data_xy.equal_range(x);

    if (data_xy.begin() == bound.first) {
        return data_xy.begin()->second;
    } else if (data_xy.end() == bound.second) {
        return data_xy.rbegin()->second;
    } else {
        const float x_1 = std::prev(bound.first)->first;
        const float y_1 = std::prev(bound.first)->second;

        const float x_2 = bound.first->first;
        const float y_2 = bound.first->second;

        return y_2 + (x - x_2) *
            (y_1 - y_2) /
            (x_1 - x_2);
    };
}

float interp2d(
    const float x,
    const float y,
    const vector_t& data_x,
    const vector_t& data_y,
    const matrix_t& data_z)
{
    auto bound_x = std::equal_range(
        data_x.begin(), data_x.end(), x);
    auto bound_y = std::equal_range(
        data_y.begin(), data_y.end(), y);

    pos_t pos_x = findPosition_(data_x, bound_x);
    pos_t pos_y = findPosition_(data_y, bound_y);

    // Расположение точек
    //              x_1            x_2
    //      y_1      B    -z_1-     C
    //      y_2      A    -z_2-     D
    float z_a = data_z[pos_y.second][pos_x.first];
    float z_b = data_z[pos_y.first][pos_x.first];
    float z_c = data_z[pos_y.first][pos_x.second];
    float z_d = data_z[pos_y.second][pos_x.second];

    float z_1 = z_c + (x - data_x[pos_x.second]) *
            (z_b - z_c) /
            (data_x[pos_x.first] - data_x[pos_x.second]);
    float z_2 = z_d + (x - data_x[pos_x.second]) *
            (z_a - z_d) /
            (data_x[pos_x.first] - data_x[pos_x.second]);

    return z_1 + (y - data_y[pos_y.first]) *
            (z_2 - z_1) /
            (data_y[pos_y.second] - data_y[pos_y.first]);
}

pos_t findPosition_(
    const vector_t& data,
    const vector_i& bound)
{
    pos_t pos;

    if (data.begin() == bound.first) {
        pos = {
            0,
            0
        };
    } else if (data.end() == bound.second) {
        pos = {
            data.size() - 1,
            data.size() - 1,
        };
    } else {
        pos = {
            bound.first - data.begin() - 1,
            bound.first - data.begin() - 0,
        };
    }
    return pos;
}