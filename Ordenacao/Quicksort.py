def quick(array,left,right):
    if(left<right):
        pivotIndex = partition(array,left,right);
        quick(array,left,pivotIndex)
        quick(array, pivotIndex + 1,right);
    return array;
def partition(array,left,right):
    pivotIndex = (left+right)//2;
    pivot = array[pivotIndex];
    i = left;
    j = right;
    while i<j:
        while (array[i] < pivot):
            i = i + 1;
        while (array[j] > pivot):
            j = j - 1;
        if i >= j:
            return j;
        temp = array[i];
        array[i]  = array[j];
        array[j] = temp;



arr = [64, 34, 25, 12, 22, 11, 90]
arr = [5, 2, 8, 4, 6, 1, 3, 9, 7]
print("Array antes da ordenação.: ", arr)
arr = quick(arr,0,len(arr)-1);
print("Array depois da ordenação: ", arr)
