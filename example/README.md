Для создания DLL необходимо выполнить в командной строке:

1. Команду на создание обьектного файла

```
gcc -Wall -Werror -fPIC -O3 -o NAME.o -c NAME.c
```
где NAME - название исходного файла;

2. Команду на создание самой DLL

```
gcc -shared -o NAME.so NAME.o
```