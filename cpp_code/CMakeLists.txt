cmake_minimum_required(VERSION 3.4)
project(statistic)
add_subdirectory(pybind11)
pybind11_add_module(module_name statistic_counter.cpp)
