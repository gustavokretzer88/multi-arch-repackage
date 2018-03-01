#include <hello.h>
#include <iostream>

void hello(const std::string &name) {
	std::cout << "Hello " << name;
#if _WIN64
	std::cout << " , I'm running in 64 bits\n";
#else
	std::cout << " , I'm running in 32 bits\n";
#endif
}