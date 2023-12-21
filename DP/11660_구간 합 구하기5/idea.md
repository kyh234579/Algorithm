**<맨 위쪽에서부터 누적합 구하기>**
![image](https://github.com/kyh234579/Algorithm/assets/132960024/f4f78c15-8b42-4858-af55-af1dbaef7985)

sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum[i-1][j-1] + arr[i-1][j-1] ( arr 배열은 -1씩 해줘야 sum_dp와 구조가 맞음)

**<(x1,y1)와 (x2,y2)까지의 구간합 구하기>**
![image](https://github.com/kyh234579/Algorithm/assets/132960024/90daee9a-6e57-4739-b0f6-59748017ba2d)

ans = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]



