# Finn은 편의점에서 야간 아르바이트를 하고 있습니다. 야간에 손님이 너무 없어 심심한 Finn은 손님들께 거스름돈을 n 원을 줄 때 방법의 경우의 수를 구하기로 하였습니다.
#
# 예를 들어서 손님께 5원을 거슬러 줘야 하고 1원, 2원, 5원이 있다면 다음과 같이 4가지 방법으로 5원을 거슬러 줄 수 있습니다.
#
# 1원을 5개 사용해서 거슬러 준다.
# 1원을 3개 사용하고, 2원을 1개 사용해서 거슬러 준다.
# 1원을 1개 사용하고, 2원을 2개 사용해서 거슬러 준다.
# 5원을 1개 사용해서 거슬러 준다.
# 거슬러 줘야 하는 금액 n과 Finn이 현재 보유하고 있는 돈의 종류 money가 매개변수로 주어질 때, Finn이 n 원을 거슬러 줄 방법의 수를 return 하도록 solution 함수를 완성해 주세요.
#
# 제한 사항
# n은 100,000 이하의 자연수입니다.
# 화폐 단위는 100종류 이하입니다.
# 모든 화폐는 무한하게 있다고 가정합니다.
# 정답이 커질 수 있으니, 1,000,000,007로 나눈 나머지를 return 해주세요.
# 입출력 예
# n	money	result
# 5	[1,2,5]	4
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.

def solution(n, money):
    # dp생성
    dp = [[0] * (n + 1) for _ in range(len(money))]

    # 0원은 지불 가능하니까 1로 시작
    dp[0][0] = 1

    # 첫번째 금액으로 n원을 구성 가능하면 1로 변경
    for i in range(money[0], n + 1, money[0]):
        dp[0][i] = 1

    # y: 지불가능한 동전
    for y in range(1, len(money)):
        # x: 거슬러줘야하는 금액
        for x in range(n + 1):
            # 거슬러줘야하는 금액을 지불가능한 동전보다 클 경우
            if x >= money[y]:
                dp[y][x] = (dp[y - 1][x] + dp[y][x - money[y]]) % 1000000007
            # 반대의 경우
            else:
                dp[y][x] = dp[y - 1][x]

    # 마지막 값 출력
    return dp[-1][-1]

solution(5, [1,2,5]	)