**DP 배열이 가지는 의미**</br>
- DP[n]의 의미
1. n번째를 선택했을 때의 최적값
2. n번째까지 고려했을 떄의 최적값 (n번쨰를 선택하지 않을 경우도 고려)

해당 문제는 1번에 해당한다. </br>
그 이유는 총 n열의 스티커가 주어졌을 때, 최대값을 구할 때 마지막 n열을 택하지 않을 수 없다.</br>
n-1번째의 어떤 선택을 했더라도 n열(마지막)의 스티커가 남아있어서 하나 더 고를 수 있기 떄문이다.</br>
그래서, 최대값은 항상 마지막 n열에서 스티커를 고르는 경우로 한정된다.</br>


![image](https://github.com/kyh234579/Algorithm/assets/132960024/740111d4-d8f2-4019-8ec1-d7c7bf97f8cf) </br>

이렇게 코드로 구현하면 된다.</br>
하지만, 스티커 길이가 1이나 2일 경우는 예외처리 (index오류 가능성)</br>
</br>
[참고 링크](https://beyond-common-sense.tistory.com/10)

   
