#include <stdio.h>

typedef struct {
    char a;
    unsigned long c;
    int b;
    float d;
    char e;
    double f;
} Data;

int main(int argc, char *argv[])
{
    printf("sizeof(char) = %d\n", sizeof(char));
    printf("sizeof(int) = %d\n", sizeof(int));
    printf("sizeof(unsigned long) = %d\n", sizeof(unsigned long));
    printf("sizeof(float) = %d\n", sizeof(float));
    printf("sizeof(double) = %d\n", sizeof(double));
    printf("sizeof(Data) = %d\n", sizeof(Data));
    return 0;
}

