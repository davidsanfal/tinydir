from conans import ConanFile, CMake, tools


class ArgparseConan(ConanFile):
    name = "tinydir"
    version = "0.1"

    def source(self):
        self.run("git clone https://github.com/cxong/tinydir")

    def package(self):
        self.copy("*.h", dst="include", src="tinydir")

    def package_id(self):
        self.info.header_only()

