project(SCPro)
cmake_minimum_required(VERSION 2.8)
aux_source_directory(. SRC_LIST)
link_libraries("/usr/local/lib/libgmp.a")
find_package(Threads)
add_executable(${PROJECT_NAME} ${SRC_LIST})
