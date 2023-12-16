#include <stdio.h>
void waitingTime(int at[], int bt[], int n)
{
    int wt[n];
    wt[0] = 0;
    printf("Process\tAT\tBT\tWT\n");
    printf("1\t%d\t%d\t%d\n", at[0], bt[0], wt[0]);
    for (int i = 1; i < n; i++)
    {
        wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i];
        printf("%d\t%d\t%d\t%d\n", i, at[i], bt[i], wt[i]);
    }
    float average, sum;
    for (int i = 0; i < n; i++)
    {
        sum += wt[i];
    }
    average = sum / 5;
    printf("Average Waiting time = %f", average);
}
int main()
{
    printf("Devesh Raichandani\n08817711921");
    int n = 5;
    int at[] = {0, 1, 2, 3, 4};
    int bt[] = {4, 3, 1, 2, 5};
    waitingTime(at, bt, n);
    return 0;
}
