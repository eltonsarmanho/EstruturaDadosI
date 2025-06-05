void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int left, int right)
{
    int pivotIndex = (left + right) / 2;
    int pivot = arr[pivotIndex];
    int i = left;
    int j = right;
    while(i<j)
    {
        while(arr[j]>pivot)
            j--;
        while(arr[i]<pivot)
            i++;
        if(i>=j)
         return j;
        int temp =arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        //swap(&arr[i], &arr[j]);
    }
}
void quickSort(int arr[], int left, int right)
{
   if (left < right) {
        int pi = partition(arr, left, right);

        quickSort(arr, left, pi);
        quickSort(arr, pi + 1, right);
    }
}

void selectionSort()
{
    int A[] = {4,3,5,1};
    printf("Vetor nao ordenado\n");
    int n = sizeof(A)/sizeof(A[0]);
    for(int i =0;i<n;i++)
        printf("%d ", A[i]);


    for(int i =0;i<n;i++)
    {
        int minIndex = i;
        for(int j = i+1;j<n;j++)
        {
            if(A[j]<A[minIndex])
                minIndex = j;
        }
        if(minIndex != i)
        {
            int aux = A[minIndex];
            A[minIndex] = A[i];
            A[i] = aux;
        }
    }
    printf("\nVetor Ordenado\n");

    for (int i=0; i < n; i++)
        printf("%d ", A[i]);

  printf("\n");
}
