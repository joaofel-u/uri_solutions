#include <stdio.h>

int main(){
	int hr, min, seg, vel = 0, time_stamp = 0;
	double distancia = 0;
	char c;

	while(scanf("%d:%d:%d%c", &hr, &min, &seg, &c) != EOF) {
		distancia += (double)(((hr*3600 + min*60 + seg)-time_stamp)*vel)/3600;
		time_stamp = hr*3600 + min*60 + seg;

		if (c == ' ')
		    scanf("%d%*c", &vel);
		else
		     printf("%02d:%02d:%02d %.2lf km\n", hr, min, seg, distancia);
	}

	return 0;
}
