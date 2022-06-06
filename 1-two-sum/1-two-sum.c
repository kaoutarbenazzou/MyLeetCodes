

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i,j;
    *returnSize=2;
    int*arr = malloc((*returnSize)*sizeof(int));
    for (i=0; i<numsSize; i++){
        for(j = i+1; j < numsSize; j++){
            if (nums[i]+nums[j]==target){
                arr[0]=j;
                arr[1]=i;
           
            }
        }
}
     return arr;
}