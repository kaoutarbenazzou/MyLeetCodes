
int findGCD(int* nums, int numsSize){
    int max = nums[0];
    int min = nums[numsSize-1];
    
    for(int i=0;i<numsSize;i++){
        if(nums[i] > max){max = nums[i];}
        if(nums[i] < min){min = nums[i];}
    }
    
    //printf("max is %d and min is %d\n",max,min);
    int gcd = 1;
    
    for(int i=2;i<=max;i++){
        if( (max % i==0) && (min % i ==0)){
            gcd = i;
        }
    }
    return gcd;
}