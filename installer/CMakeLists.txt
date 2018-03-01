project(myInstaller CXX)

cmake_minimum_required(VERSION 2.8)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(${PROJECT_NAME}
		src/main.cpp 
)

conan_target_link_libraries(${PROJECT_NAME})
SET(CPACK_GENERATOR "ZIP")

INSTALL(TARGETS ${PROJECT_NAME} COMPONENT myApp	RUNTIME DESTINATION .)

# Error while trying with -s arch = x86_64.
# How to get the driver reference generated with arch x86, when we use -s arch = x86_64.
INSTALL(FILES ${CONAN_BIN_DIRS_DRIVER}/driver32.dll COMPONENT biblioteca DESTINATION lib32/)

IF(NOT "${CMAKE_CL_64}" MATCHES "0") # WINDOWS 64
	INSTALL(FILES ${CONAN_BIN_DIRS_DRIVER}/driver64.dll COMPONENT biblioteca DESTINATION lib64/) # OK
ENDIF()

INCLUDE(CPack)