# Указание на необходимую версию CMake
cmake_minimum_required(VERSION 3.19)

# Название проекта
project(lebedev VERSION 0.1)

# Команды для компилятора
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-Wall")

# Указание на библиотеку
set(LEBEDEV "lebedev")

set(CORE ${LEBEDEV}/core)
set(SOURCE ${LEBEDEV}/source)

# Расположение заголовочных файлов
include_directories(${CORE}/ ${SOURCE}/)

# Установка переменной со списком исходников
set(SOURCE_LIB
    ${CORE}/interp.cpp
    ${SOURCE}/graph_3_2.cpp
    ${SOURCE}/graph_5_11.cpp)

# Создание библиотеки с именем lebedev
# add_library(${PROJECT_NAME} STATIC ${SOURCE_LIB})
# add_library(${PROJECT_NAME} SHARED ${SOURCE_LIB})

add_library(${PROJECT_NAME} SHARED ${SOURCE_LIB})