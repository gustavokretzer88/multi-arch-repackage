#pragma once

#ifdef WIN32
  #define HELLO_EXPORT __declspec(dllexport)
#else
  #define HELLO_EXPORT
#endif

#include <string>

HELLO_EXPORT void hello(const std::string &name);