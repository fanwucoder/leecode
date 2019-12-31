cmake_minimum_required(VERSION 3.13)
project(leecode)

set(CMAKE_CXX_STANDARD 14)


set(googleTestDir ./googletest)

#Add the google test subdirectory
add_subdirectory(${googleTestDir})
#include googletest/include dir
include_directories(${googleTestDir}/googletest/include)
#include the googlemock/include dir
include_directories(${googleTestDir}/googlemock/include)

set(SOURCE_FILE
        src/add.cpp
        test/addTest.cpp
        src/add.h test/addTest.cpp test/addTest.h src/Solution.cpp src/Solution.h src/StrStr.cpp src/StrStr.h src/IsPalindromelink.h)
add_executable(GTest ${SOURCE_FILE})

# Link with GoogleTest
target_link_libraries(GTest gtest gtest_main)
#Link with GoogleMock
target_link_libraries(GTest gmock gmock_main)
