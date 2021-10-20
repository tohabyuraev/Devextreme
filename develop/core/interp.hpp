#ifndef _INTERP_H_
#define _INTERP_H_

#include <iostream>
#include <vector>
#include <algorithm>

using vector_t = std::vector<float>;
using matrix_t = std::vector<
    std::vector<float>
>;
using pospair_t = std::pair<int, int>;
using boundpair_t = std::pair<
    std::vector<float>::const_iterator,
    std::vector<float>::const_iterator
>;

#ifdef  __cplusplus
extern "C" {
#endif

float testInterp1d();
float testInterp2d();
float interp(
    const float,
    const float*,
    const float*);
float interp1d(
    const float&,
    const vector_t&,
    const vector_t&);
float interp2d(
    const float,
    const float,
    const vector_t&,
    const vector_t&,
    const matrix_t&);
pospair_t findPosition_(
    const vector_t&,
    const boundpair_t&);

#ifdef  __cplusplus
}
#endif

#endif  /* _INTERP_H_ */