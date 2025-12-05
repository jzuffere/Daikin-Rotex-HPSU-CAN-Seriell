#include <gtest/gtest.h>
#include "esphome/components/daikin_rotex_can/pid.h"
#include "esphome/core/hal.h"

using namespace esphome::daikin_rotex_can;

TEST(PIDTest, Simple) {
    auto delta = 0.00001f;

    PID pid(0.2, 0.05f, 0.05f, 0.2, 0.2, 0.1f);
    EXPECT_EQ(0, pid.get_last_update());

    std::string logstr;

    float dt = 10.f;
    float state = 5.f;
    float smooth_state = 4.f;

    EXPECT_NEAR(0.0505000055, pid.compute(state, smooth_state, dt, logstr), delta);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.040000, i: 0.010000, d: 0.000500, map: 0.200000, fp: 0.200000, mfp: 0.200000, mp: 0.200000, o: 0.050500", logstr);

    EXPECT_NEAR(0.08245, pid.compute(state, smooth_state, dt, logstr), delta);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.072000, i: 0.010000, d: 0.000450, map: 0.200000, fp: 0.360000, mfp: 0.360000, mp: 0.200000, o: 0.082450", logstr);

    EXPECT_NEAR(0.108005, pid.compute(state, smooth_state, dt, logstr), delta);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.097600, i: 0.010000, d: 0.000405, map: 0.200000, fp: 0.488000, mfp: 0.488000, mp: 0.200000, o: 0.108005", logstr);

    EXPECT_GE(pid.get_last_update(), esphome::millis());
}
