cmake_minimum_required(VERSION 3.18)
project(paramcard Fortran)

add_library(paramcard src/paramcard.f90)

install(TARGETS paramcard ARCHIVE DESTINATION lib)
