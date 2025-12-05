cmake_minimum_required(VERSION 3.14)
project(HPSUTests)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.14.0
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# ESPHome
FetchContent_Declare(
    esphome_src
    GIT_REPOSITORY https://github.com/esphome/esphome.git
    GIT_TAG dev
)
FetchContent_MakeAvailable(esphome_src)
set(ESPHOME_INCLUDE_ROOT ${esphome_src_SOURCE_DIR})

# main

add_executable(hpsu_tests
    src/test_bidi_map.cpp
    src/test_pid.cpp
    src/test_scheduler.cpp
    src/test_utils.cpp
    ../components/daikin_rotex_can/scheduler.cpp
    ../components/daikin_rotex_can/pid.cpp
    ../components/daikin_rotex_can/bidi_map.cpp
    ../components/daikin_rotex_can/utils.cpp
    mock_esphome.cpp
)

target_include_directories(hpsu_tests PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${ESPHOME_INCLUDE_ROOT}
    ../components/daikin_rotex_can
    ../../../
)

target_link_libraries(hpsu_tests
    gtest_main
)

include(GoogleTest)
gtest_discover_tests(hpsu_tests)
enable_testing()