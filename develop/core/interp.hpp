#ifndef _INTERP_H_
#define _INTERP_H_

#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using vector_t = std::vector<float>;
using vector_i = std::pair<
    std::vector<float>::const_iterator,
    std::vector<float>::const_iterator
>;
using matrix_t = std::vector<
    std::vector<float>
>;
using pos_t = std::pair<
    int,
    int
>;
using map_t = std::map<
    float,
    float
>;

float interp1d(
    const float,
    const vector_t&,
    const vector_t&);
float interp1d(
    const float,
    const map_t&);

#ifdef  __cplusplus
extern "C" {
#endif

int testInterp1d();
int testInterp2d();
float interp(
    const float,
    const float*,
    const float*);
float interp2d(
    const float,
    const float,
    const vector_t&,
    const vector_t&,
    const matrix_t&);
pos_t findPosition_(
    const vector_t&,
    const vector_i&);

#ifdef  __cplusplus
}
#endif

#endif  /* _INTERP_H_ */