from spack import *

class PSDpp(CMakePackage):
    """A C++ library that does cool things."""

    homepage = 'https://github.com/adv-colloidal-materials-engineering'
    url = 'https://github.com/adv-colloidal-materials-engineering/PSDpp.git'
    git = 'https://github.com/adv-colloidal-materials-engineering/PSDpp.git'

    version('main', branch='main')

    depends_on('pkgconfig', type=('build'))
    depends_on('voropp')

    def cmake_args(self):
        args = []
        return args
