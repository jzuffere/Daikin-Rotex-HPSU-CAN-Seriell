#include <gtest/gtest.h>
#include "esphome/components/daikin_rotex_can/scheduler.h"

using namespace esphome::daikin_rotex_can;

TEST(SchedulerTest, CallLaterReturnsValidHandle) {
    auto& scheduler = Scheduler::getInstance();

    bool called = false;
    auto handle = scheduler.call_later([&called]() {
        called = true;
    }, 100);

    EXPECT_TRUE(handle.is_valid());
    EXPECT_FALSE(called);
}

TEST(SchedulerTest, CancelCallWorks) {
    auto& scheduler = Scheduler::getInstance();

    bool called = false;
    auto handle = scheduler.call_later([&called]() {
        called = true;
    }, 100);

    EXPECT_TRUE(handle.cancel());
    EXPECT_FALSE(handle.is_valid());
    EXPECT_FALSE(called);
}

TEST(SchedulerTest, AccelerateCallWorks) {
    auto& scheduler = Scheduler::getInstance();

    bool called = false;
    auto handle = scheduler.call_later([&called]() {
        called = true;
    }, 100);

    EXPECT_TRUE(handle.accelerate());

    scheduler.update();
    EXPECT_TRUE(called);
}