cmake_minimum_required(VERSION 3.19)

project(lib123)

message(INFO ${PROJECT_SOURCE_DIR})

add_library(lib123 SHARED lib.h)
set_target_properties(lib123 PROPERTIES LINKER_LANGUAGE CXX)
