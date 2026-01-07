#include <stdio.h>
#include <math.h>
#include "struct.h"

#define MAX_AIRPORTS 21
#define BUFFER_SIZE 1024

void printAirport(const Airport *x) {
    printf("%s %s (%.6f %.6f)\n",
           x->code,
           x->name,
           x->latitude,
           x->longitude);
}

int main(int argc, char *argv[]) {

    FILE *fileIn = fopen("coordinates.csv", "r");
    if (fileIn == NULL) {
        perror("Failed to open coordinates.csv");
        return 1;
    }

    Airport airports[MAX_AIRPORTS];
    char buffer[BUFFER_SIZE];
    int count = 0;

    while (fgets(buffer, BUFFER_SIZE, fileIn) != NULL && count < MAX_AIRPORTS) {
        if (sscanf(buffer,
                   " %[^,], %[^,], %lf, %lf",
                   airports[count].code,
                   airports[count].name,
                   &airports[count].latitude,
                   &airports[count].longitude) == 4) {
            count++;
        }
    }

    fclose(fileIn);

    for (int i = 0; i < count; i++) {
        printAirport(&airports[i]);
    }

    /*
    Flight flight1 = {"AA", "SAT", "LAX", 550, 1200, 1450};
    Flight flight2 = {"UA", "SAT", "ORD", 50, 1800, 2050};

    printf("This flight has %d seats and the other has %d seats\n",
           flight1.seats, flight2.seats);

    printf("This flight departs from %s and the other departs from %s\n",
           flight1.origin, flight2.origin);

    Player P1;
    */

    return 0;
}