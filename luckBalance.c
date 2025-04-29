//Luck Balance Hackerrank Code Snippet;

int luckBalance(int k, int contests_rows, int contests_columns, int** contests) { 
    int sum1=0,sum2=0,min=100000,count=0,pos;
    for(int i=0;i<contests_rows;i++){
        sum1+=contests[i][0];
    }for(int i=0;i<contests_rows;i++){
        if(contests[i][1]==1)
        count++;
    }for(int i=1;i<=count-k;i++){
        for(int j=0;j<contests_rows;j++){
            if(contests[j][0]<min && contests[j][1]!=0 && contests[j][0]>0){
                min=contests[j][0];pos=j;
            }
        }sum2+=min;contests[pos][0]=0;min=100000;
    }return (sum1-2*sum2);
}