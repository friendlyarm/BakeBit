// BakeBit Example for using the digital read command

#include "bakebit.h"
//gcc bakebit_digital_read.c bakebit.c -Wall
int main(void)
{		
	int dval;
	
	//Exit on failure to start communications with the BakeBit
	if(init()==-1)
		exit(1);
	
	//Set pin mode to input
	pinMode(4,0);
	while(1)
	{
		dval=digitalRead(2);
		printf("Digital read %d\n", dval);
		//Sleep for 50ms
		pi_sleep(50);
	}
   	return 1;
}
