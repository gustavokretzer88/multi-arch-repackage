from conans import ConanFile, CMake


class DriverConan(ConanFile):
    name = "Driver"
    version = "0.1"
    settings = {
        "os": ["Windows", "Linux", "Macos"], 
        "arch": ["x86", "x86_64"],
        "compiler" : ["gcc", "Visual Studio", "apple-clang"],
        "build_type": ["Debug", "Release"]
    }
    generators = "cmake", "visual_studio"   
    build_requires = "Dependencies/0.1@user/testing"
    exports_sources = "*"

    def build(self):
    	cmake = CMake(self)
    	cmake.configure()
    	cmake.build()

    def package(self):
        self.copy("*.dll", src="bin", dst="bin")

    def deploy(self):
        self.copy("*.dll", src="bin", dst="deployed")
