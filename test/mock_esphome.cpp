#include <chrono>
#include <cstdint>
#include <iostream>

namespace esphome {

uint32_t millis() {
    return std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now().time_since_epoch()
    ).count();
}

void delay(uint32_t ms) {
}

} // namespace esphome