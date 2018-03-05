project(myInstaller CXX)

cmake_minimum_required(VERSION 3.5)

# my app.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
ADD_EXECUTABLE(${PROJECT_NAME}
		src/main.cpp 
)
conan_target_link_libraries(${PROJECT_NAME})


SET(CPACK_GENERATOR "ZIP")

INSTALL(TARGETS ${PROJECT_NAME} COMPONENT myApp RUNTIME DESTINATION .)

ADD_CUSTOM_COMMAND(TARGET ${PROJECT_NAME} POST_BUILD COMMAND conan ARGS install Driver/0.1@user/testing -s arch=x86)
INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/deployed/driver32.dll COMPONENT biblioteca DESTINATION libs)


IF(NOT "${CMAKE_CL_64}" MATCHES "0") # WINDOWS 64
	ADD_CUSTOM_COMMAND(TARGET ${PROJECT_NAME} POST_BUILD COMMAND conan ARGS install Driver/0.1@user/testing -s arch=x86_64)
	INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/deployed/driver64.dll COMPONENT biblioteca DESTINATION libs)
ENDIF()

INCLUDE(CPack)