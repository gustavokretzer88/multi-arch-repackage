from conans import ConanFile, CMake, tools

class InstallerConan(ConanFile):
    name = "Installer"
    version = "0.1"
    settings = {
        "os": ["Windows", "Linux", "Macos"], 
        "arch": ["x86", "x86_64"],
        "compiler" : ["gcc", "Visual Studio", "apple-clang"],
        "build_type": ["Debug", "Release"]
    }
    generators = "cmake", "visual_studio"
    exports_sources = "*"

    def generateInstaller(self):
        if self.settings.os == "Windows":
            self.run("%s && %s" % (tools.vcvars_command(self.settings), tools.build_sln_command(self.settings, "PACKAGE.vcxproj")))
        else:
            pass#... 

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self.generateInstaller()

    def package(self):
        self.copy("*.zip") # final artifact

    def deploy(self):
        self.copy("*.zip") # final artifact


