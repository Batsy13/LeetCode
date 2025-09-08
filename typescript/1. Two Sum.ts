function twoSum(nums: number[], target: number): number[] {

    const previous:object = {};

    for(let i = 0; i < nums.length; i++){
        let num:number = nums[i];
        let diff:number = target - num;

        if(diff in previous){
            let arr:number[] = [previous[diff], i] 
            return arr;
        }

        previous[num] = i
    }

    return []
}