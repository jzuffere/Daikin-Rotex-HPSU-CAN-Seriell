#include "esphome/components/daikin_rotex_can/pid.h"
#include "esphome/core/hal.h"

#include <gtest/gtest.h>
#include <iostream>
#include <math.h>
#include <string>
#include <regex>

using namespace esphome::daikin_rotex_can;

std::string unify(const std::string& str) {
    const std::regex negative_zero_pattern("-0\\.000000");
    const std::string replacement("0.000000");
    return std::regex_replace(str, negative_zero_pattern, replacement);
}

TEST(PIDTest, compute) {
    auto delta = 0.00001f;

    PID pid(0.2, 0.05f, 0.05f, 0.2, 0.2, 0.1f);
    EXPECT_EQ(0, pid.get_last_update());

    std::string logstr;

    float dt = 10.f;
    float setpoint = 5.f;
    float current = 0.f;

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 0.000000, e: 5.000000, p: 0.200000, i: 0.010000, d: 0.002500, map: 0.200000, fp: 1.000000, mfp: 1.000000, mp: 0.200000, o: 0.212500", logstr);

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 0.212500, e: 4.787500, p: 0.351500, i: 0.010000, d: 0.002144, map: 0.200000, fp: 1.757500, mfp: 1.757500, mp: 0.200000, o: 0.363644", logstr);

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 0.576144, e: 4.423856, p: 0.458154, i: 0.010000, d: 0.001748, map: 0.200000, fp: 2.290771, mfp: 2.290771, mp: 0.200000, o: 0.469902", logstr);

    EXPECT_GE(esphome::millis(), pid.get_last_update());
}

TEST(PIDTest, zero_dt) {
    auto delta = 0.00001f;

    PID pid(0.2, 0.05f, 0.05f, 0.2, 0.2, 0.1f);

    std::string logstr;

    float dt = 10.f;
    float setpoint = 5.f;
    float current = 4.f;

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.040000, i: 0.010000, d: 0.000500, map: 0.200000, fp: 0.200000, mfp: 0.200000, mp: 0.200000, o: 0.050500", logstr);

    current += pid.compute(setpoint, current, 0, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.040000, i: 0.010000, d: 0.000500, map: 0.200000, fp: 0.200000, mfp: 0.200000, mp: 0.200000, o: 0.050500", logstr);

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.050500, e: 0.949500, p: 0.069980, i: 0.010000, d: 0.000425, map: 0.200000, fp: 0.349900, mfp: 0.349900, mp: 0.200000, o: 0.080405", logstr);

    current += pid.compute(setpoint, current, std::numeric_limits<float>::quiet_NaN(), logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.050500, e: 0.949500, p: 0.069980, i: 0.010000, d: 0.000425, map: 0.200000, fp: 0.349900, mfp: 0.349900, mp: 0.200000, o: 0.080405", logstr);

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.130905, e: 0.869095, p: 0.090748, i: 0.010000, d: 0.000342, map: 0.200000, fp: 0.453739, mfp: 0.453739, mp: 0.200000, o: 0.101090", logstr);

    current += pid.compute(setpoint, current, std::numeric_limits<float>::infinity(), logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.130905, e: 0.869095, p: 0.090748, i: 0.010000, d: 0.000342, map: 0.200000, fp: 0.453739, mfp: 0.453739, mp: 0.200000, o: 0.101090", logstr);

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.231995, e: 0.768005, p: 0.103318, i: 0.010000, d: 0.000257, map: 0.200000, fp: 0.516592, mfp: 0.516592, mp: 0.200000, o: 0.113576", logstr);
}

TEST(PIDTest, invalid_setpoint) {
    auto delta = 0.00001f;

    PID pid(0.2, 0.05f, 0.05f, 0.2, 0.2, 0.1f);

    std::string logstr;

    float dt = 10.f;
    float setpoint = 5.f;
    float current = 4.f;

    current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.040000, i: 0.010000, d: 0.000500, map: 0.200000, fp: 0.200000, mfp: 0.200000, mp: 0.200000, o: 0.050500", logstr);

    current += pid.compute(std::numeric_limits<float>::quiet_NaN(), current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.040000, i: 0.010000, d: 0.000500, map: 0.200000, fp: 0.200000, mfp: 0.200000, mp: 0.200000, o: 0.050500", logstr);

    current += pid.compute(std::numeric_limits<float>::infinity(), current, dt, logstr);
    EXPECT_EQ("sp: 5.000000, cv: 4.000000, e: 1.000000, p: 0.040000, i: 0.010000, d: 0.000500, map: 0.200000, fp: 0.200000, mfp: 0.200000, mp: 0.200000, o: 0.050500", logstr);
}

TEST(PIDTest, reach_setpoint) {
    auto delta = 0.00001f;

    PID pid(0.2, 0.05f, 0.05f, 0.2, 0.2, 0.1f);

    std::string logstr;

    float dt = 10.f;
    float setpoint = 5.f;
    float current = 0.f;

    for (uint32_t i = 0; i < 2; ++i)
        current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_NEAR(current, 0.5761437416, 0.00001);

    for (uint32_t i = 0; i < 5; ++i)
        current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_NEAR(current, 3.2680168151, 0.00001);

    for (uint32_t i = 0; i < 100; ++i)
        current += pid.compute(setpoint, current, dt, logstr);
    EXPECT_NEAR(current, 5.0076870918, 0.00001);
}