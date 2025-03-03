#pragma once

#include "esphome/components/daikin_rotex_can/daikin_rotex_can.h"
#include "esphome/components/button/button.h"
#include "esphome/components/number/number.h"

namespace esphome {
namespace daikin_rotex_can {

class DHWRunButton : public button::Button, public Parented<DaikinRotexCanComponent> {
public:
    DHWRunButton() = default;
protected:
    void press_action() override;
};

class DumpButton : public button::Button, public Parented<DaikinRotexCanComponent> {
public:
    DumpButton() = default;
protected:
    void press_action() override;
};

class CustomNumber : public number::Number, public Parented<DaikinRotexCanComponent> {
    public:
    CustomNumber() = default;
protected:
    virtual void control(float value) override;
};

}
}
