project(driver CXX)
cmake_minimum_required(VERSION 2.8)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

IF(NOT "${CMAKE_CL_64}" MATCHES "0") # WINDOWS 64
	SET(LIBRARY_NAME ${PROJECT_NAME}64)
ELSE() #WINDOWS 32
	SET(LIBRARY_NAME ${PROJECT_NAME}32)
ENDIF()

add_library(${LIBRARY_NAME} SHARED
    src/hello.cpp
)
conan_target_link_libraries(${LIBRARY_NAME})