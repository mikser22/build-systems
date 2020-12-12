cmake_minimum_required(VERSION 3.19)

project(C)

set(CMAKE_CXX_STANDARD 11)

message(INFO ${PROJECT_SOURCE_DIR})
add_custom_command( 
  OUTPUT ${PROJECT_SOURCE_DIR}/A/index.h
  COMMAND python ${PROJECT_SOURCE_DIR}/A/preparing.py ${PROJECT_SOURCE_DIR}/A/index.h
  DEPENDS ${PROJECT_SOURCE_DIR}/A/preparing.py
  COMMENT "Generating index.h"
)

set(SOURCES C/main.cpp)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

add_custom_target( RunGenerator DEPENDS ${PROJECT_SOURCE_DIR}/A/index.h COMMENT "Checking if re-generation is required" )

include_directories(${PROJECT_SOURCE_DIR} "A")
add_subdirectory(${PROJECT_SOURCE_DIR}/B ${PROJECT_SOURCE_DIR}/B/build)
add_executable(C ${SOURCES})
add_dependencies( C RunGenerator )

target_include_directories(C PRIVATE ${CMAKE_BINARY_DIR})