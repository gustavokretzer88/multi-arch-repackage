from conans import ConanFile, CMake


class DriverConan(ConanFile):
    name = "Dependencies"
    version = "0.1"
    settings = {
        "os": ["Windows", "Linux", "Macos"], 
        "arch": ["x86", "x86_64"],
        "compiler" : ["gcc", "Visual Studio", "apple-clang"],
        "build_type": ["Debug", "Release"]
    }
    generators = "cmake", "visual_studio"   
    exports_sources = "*"

    def build(self):
    	cmake = CMake(self)
    	cmake.configure()
    	cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["dependencies"]
