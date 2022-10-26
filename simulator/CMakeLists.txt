cmake_minimum_required(VERSION 3.5)
project(demo)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cc engine.cc msg.pb.cc)
add_executable(main ${SOURCE_FILES})

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(main PUBLIC zmq)
target_link_libraries(main PUBLIC protobuf)