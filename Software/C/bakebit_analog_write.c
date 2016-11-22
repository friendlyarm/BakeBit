// BakeBit Example for using the analog write 

#include "bakebit.h"
//gcc bakebit_analog_write.c bakebit.c -Wall
int main(void)
{		
	int i;
	
	//Exit on failure to start communications with the BakeBit
	if(init()==-1)
		exit(1);
	
	while(1)
	{
		for(i=0;i<256;i++)
		{
			printf("%d\n", i);
			//Write the PWM value
			analogWrite(3,i);
			//Sleep for 10ms
			pi_sleep(10);
		}
	}
   	return 1;
}
