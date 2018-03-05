REM conan create dependencies user/testing -s arch=x86
REM conan create dependencies user/testing -s arch=x86_64

REM conan create driver user/testing -s arch=x86
REM conan create driver user/testing -s arch=x86_64

conan create installer user/testing -s arch=x86
conan create installer user/testing -s arch=x86_64

conan install Installer/0.1@user/testing -s arch=x86
conan install Installer/0.1@user/testing -s arch=x86_64