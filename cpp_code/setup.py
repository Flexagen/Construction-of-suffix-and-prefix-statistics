import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        'StatistiCuM',
        ['statistic_counter.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
        extra_compile_args=['-std=c++11'],  # используем с++11
    ),
]

setup(
    name='library',
    version='0.0.1',
    author='Scumer',
    author_email='user@user.ru',
    description='pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11']  # не забываем указать зависимость от pybind11
)   