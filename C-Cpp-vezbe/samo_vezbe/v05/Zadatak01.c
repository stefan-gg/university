#include <stdio.h>
#include <math.h>

struct point
{
	int x;
	int y;
};

float rastojane(struct point A, struct point B) {
	int dx = A.x - B.x;
	int dy = A.y - B.y;

	return sqrt(dx * dx + dy * dy);
};

float povrsinaTrougla(struct point A, struct point B, struct point C) {
	float a = rastojane(B, C);
	float b = rastojane(A, C);
	float c = rastojane(A, B);
	float s = (a + b + c) / 2;
	return sqrt(s * (s - a) * (s - b) * (s - c));
}

float obim(struct point A, struct point B, struct point C) {
	float a = rastojane(B, C);
	float b = rastojane(A, C);
	float c = rastojane(A, B);
	return a + b + c;
}

float obimTrouglaNiz(struct point niz[]) {
	float a = rastojane(niz[1], niz[2]);
	float b = rastojane(niz[0], niz[2]);
	float c = rastojane(niz[0], niz[1]);
	return a + b + c;
}

int main() {
	struct point a = {1, 2};
	//printf("%d", a.x);

	struct point trougao[3];
	trougao[0].x = 0;
	trougao[0].y = 0;

	trougao[0].x = 0;
	trougao[1].y = 1;

	trougao[0].x = 0;
	trougao[2].y = 1;



	return 0;
}