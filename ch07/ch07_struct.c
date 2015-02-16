#include <stdio.h>

typedef struct {
    char a;
    unsigned long b;
    int c;
    float d;
    char e;
    double f;
} Data;

int main(int argc, char *argv[])
{
    Data d = {'a', 0x12AB34CD, 100, 3.4, 'b', 5.6};
    FILE *fp = fopen("test.bin", "wb");
    fwrite(&d, 1, sizeof(Data), fp);
    fclose(fp);
    return 0;
}

