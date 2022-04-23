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

# Информация про DLL
set(SOURCE_RC info.rc)

# Расположение заголовочных файлов
include_directories(${CORE}/ ${SOURCE}/)

# Установка переменной со списком исходников
set(SOURCE_LIB
    ${CORE}/interp.cpp
    ${SOURCE}/graph_3_2.cpp
    ${SOURCE}/graph_3_3.cpp
    ${SOURCE}/graph_3_4.cpp
    ${SOURCE}/graph_3_5.cpp
    ${SOURCE}/graph_3_13.cpp
    ${SOURCE}/graph_3_21.cpp
    ${SOURCE}/graph_3_22.cpp
    ${SOURCE}/graph_3_25.cpp
    ${SOURCE}/graph_3_28.cpp
    ${SOURCE}/graph_3_29.cpp
    ${SOURCE}/graph_3_32.cpp
    ${SOURCE}/graph_3_35.cpp
    ${SOURCE}/graph_4_2.cpp
    ${SOURCE}/graph_4_3.cpp
    ${SOURCE}/graph_4_5.cpp
    ${SOURCE}/graph_4_8.cpp
    ${SOURCE}/graph_4_9.cpp
    ${SOURCE}/graph_4_10.cpp
    ${SOURCE}/graph_4_11.cpp
    ${SOURCE}/graph_4_12.cpp
    ${SOURCE}/graph_4_13.cpp
    ${SOURCE}/graph_4_15.cpp
    ${SOURCE}/graph_4_24.cpp
    ${SOURCE}/graph_4_27.cpp
    ${SOURCE}/graph_4_28.cpp
    ${SOURCE}/graph_4_29.cpp
    ${SOURCE}/graph_4_30.cpp
    ${SOURCE}/graph_4_32.cpp
    ${SOURCE}/graph_4_34.cpp
    ${SOURCE}/graph_4_35.cpp
    ${SOURCE}/graph_4_36.cpp
    ${SOURCE}/graph_4_38.cpp
    ${SOURCE}/graph_4_40.cpp
    ${SOURCE}/graph_4_42.cpp
    ${SOURCE}/graph_4_43.cpp
    ${SOURCE}/graph_5_7.cpp
    ${SOURCE}/graph_5_8.cpp
    ${SOURCE}/graph_5_9.cpp
    ${SOURCE}/graph_5_11.cpp)

# Создание библиотеки с именем lebedev
# add_library(${PROJECT_NAME} STATIC ${SOURCE_LIB})
# add_library(${PROJECT_NAME} SHARED ${SOURCE_LIB})

add_library(${PROJECT_NAME} SHARED ${SOURCE_LIB} ${SOURCE_RC})