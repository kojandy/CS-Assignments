# 알고리즘 설명

알고리즘의 아이디어는 가장 아랫 줄의 픽셀에서부터 seam line을 아래로 긋는다고 하면 각각 자기 자신이 seam line이 된다는 것에서 착안하였다. 이렇게 아래에서부터 첫 번째 줄의 픽셀까지 seam line을 그을 수 있는 후보 3개의 점끼리 비교하여 가장 작은 disruption measure를 갖는 픽셀을 선택해 테이블을 채워나간다. 이렇게 테이블을 채워나가면 가장 첫 줄은 그 곳에서 그은 가장 작은 disruption measure를 갖는 seam line의 disruption measure의 수치가 기입되게 된다. 이것을 이용해서 찻 줄에서 가장 작은 숫자의 픽셀을 찾으면 그곳에서 seam line을 그으면 된다는 것을 알 수 있다. seam line을 다시 복원하는 방법은 첫 픽셀을 찾은 후 seam line을 그을 수 있는 후보 세 개의 픽셀 중 가장 작은 값을 갖는 픽셀을 계속 이으면 된다. 이렇게 찾은 것이 바로 가장 작은 disruption measure를 갖는 seam line이다.

# 시간복잡도 계산

주어진 함수인 calculate_disruption_measure와 get_similarity_of_pixels는 O(1)만에 실행될 수 있는 함수이다.

- 17: 가장 아랫 픽셀의 disruption measure로 초기화하는 연산으로 열의 수만큼 실행된다. O(n)
- 21-27: 표의 내용을 채우는 단계이다. 이중 for문 구조이며 총 (m-1)*n번 실행되게 된다. 내부의 각각의 연산은 모두 상수시간 내에 실행이 가능하다. O(mn)
- 29-30: 변수를 초기화하는 과정이다. O(1)
- 32-34: 완성된 행렬의 첫 번째 행에서 가장 작은 값의 위치를 찾는다. O(n)
- 37-48: 행렬을 행방향으로 하나씩 내려가면서 seam line을 찾는 과정이다. 처음 픽셀을 제외한 행렬의 행의 개수인 m-1회 실행된다. O(m)

코드의 각 행의 실행 횟수와 시간복잡도를 계산했으므로 이를 전부 더해보면 O(mn)의 시간복잡도가 된다.

__O(mn)__