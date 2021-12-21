# 정렬

1. [Bubble Sort](#bubble)
2. [Selection Sort](#Select)
3. [Insert Sort](#Insert)
4. [Quick sort](#Quick)
5. [Merge sort](#Merge)
6. [Heap sort](#Heap)

계속 업데이트 예정!

## 1. Bubble Sort <a id="bubble"></a>
가장 기본적인 정렬 방법  
배열의 0번부터 n-1번까지 탐색으로 하면서 인접한 요소들을 비교, 교환하는 정렬 알고리즘  

| Space Complexity | Time Complexity (avg) | Time Complexity (worst) |
| :--------------: | :-------------: | :-------------: |
|       O(1)       |     O(n^2)      |     O(n^2)      |

```python
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
```

## 2. Selection Sort <a id="Select"></a>
버블정렬이 개선된 정렬방법
최소값(또는 최대값)이 들어갈 위치를 선택하고 그 뒤(앞)에 있는 요소들과 비교를 해서 최소값(최대값)찾아 교환하는 알고리즘  

| Space Complexity | Time Complexity (avg) | Time Complexity (worst) |
| :--------------: | :-------------: | :-------------: |
|       O(1)       |     O(n^2)      |     O(n^2)      |

시간복잡도는 Bubble 정렬과 같지만, 교환을 덜 하기때문에 좀 더 효율적이다.

```python
def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_dix = i
    for j in range(i + 1, n):
      if arr[min_dix] > arr[j]:
        min_dix = j
    arr[i], arr[min_dix] = arr[min_dix], arr[i]
  return arr
```

## 3. Insert Sort <a id="Insert"></a>
요소를 하나 선택하고, 그 앞(뒤)에 있는 배열과 비교하여 삽입할 위치를 찾는 알고리즘

| Space Complexity | Time Complexity (avg) | Time Complexity (worst) |
| :--------------: | :-------------: | :-------------: |
|       O(1)       |     O(n^2)      |     O(n^2)      |

평균 및 최악 시간복잡도는 위의 정렬들과 같으나, 정렬되어있는 배열을 재정렬할때 O(n)의 시간복잡도를 가진다.

```python
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key <= arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr
```

## 4. Merge Sort <a id="Merge"></a>

배열을 잘게 쪼갠 뒤에 2개씩 합치는 과정에서 크기를 비교해 배치하는 과정을 재귀적으로 진행하여 정렬된 배열을 완성하는 알고리즘 

| Space Complexity | Time Complexity (avg) | Time Complexity (worst) |
| :--------------: | :-------------: | :-------------: |
|       O(n)       |     O(n log n)      |     O(n log n)      |

* 배열의 배치상태에 상관없이 일정한 속도를 보장한다.  
* 나눈 배열들을 저장해야하기 때문에 다른 정렬들과 비교했을때 더 많은 메모리가 필요함 -> 공간복잡도가 크다
* 빅테이터를 정렬할 때 매우 유용하다 -> 메모리에 다 올라가지 않기 때문에 분할한뒤에 합쳐야하는데 이때 유용하게 사용할 수 있음

```python
def split(arr):
  n = len(arr)
  if n <= 1:
    return arr
  mid = n // 2
  left = arr[:mid]
  right = arr[mid:]
  return merge(split(left), split(right))


def merge(left, right):
  lp, rp = 0, 0
  merged_arr = []
  while lp < len(left) and rp < len(right):
    if left[lp] < right[rp]:
      merged_arr.append(left[lp])
      lp += 1
    else:
      merged_arr.append(right[rp])
      rp += 1
  while lp < len(left):
    merged_arr.append(left[lp])
    lp += 1

  while rp < len(right):
    merged_arr.append(right[rp])
    rp += 1

  return merged_arr


def merge_sort(arr):
  return split(arr)
```

## 5. Quick Sort <a id="Quick"></a>

pivot을 정하고 pivot보다 큰 수, 작은 수 별로 나누어 pivot 좌우로 배치하는 과정을 재귀적으로 반복하는 정렬 알고리즘이다.

| Space Complexity | Time Complexity (avg) | Time Complexity (worst) |
| :--------------: | :-------------: | :-------------: |
|       O(n)       |     O(n log n)      |     O(n^2)      |

* 평균적인 시간복잡도는 n log n 이지만, 배열이 정렬되어있을 경우에는 최악 O(n^2)의 시간복잡도를 가진다. 
  * 정렬된 배열을 다시 정렬할 때에는 좌우 배열의 불균형이 극대화(왼쪽은 길이 0의 배열, 오른쪽은 길이 n-1)되고, 재귀적으로 반복되기 때문에 정렬된 배열에서는 효율이 좋지 않다.
  * pivot 선택방법을 통해서 불균형을 어느정도 해소 할 수 있다. (다 같은값일때는 O(n^2))
  * 중앙값 지점 을 pivot으로 한다(Hoare partition) 등등...
* Heap, merge sort와 같이 평균적으로 n log n의 시간복잡도를 가지지만, Quick sort 가 조금 더 빠르다.
  * Locality(지역성)의 관점으로 접근하면 대답할 수 있음

```python
def quick_sort(arr):
  n = len(arr)
  if n <= 1:
    return arr
  left, right = [], []
  pivot = arr[0]  # Lomuto partition
  for i in range(n):
    if pivot > arr[i]:
      left.append(arr[i])
    else:
      right.append(arr[i])
  return quick_sort(left) + [pivot] + quick_sort(right)
```

## 6. Heap Sort <a id="Heap"></a>

우선순위트리 heap을 이용한 정렬 알고리즘


| Space Complexity | Time Complexity (avg) | Time Complexity (worst) |
| :--------------: | :-------------: | :-------------: |
|       O(n)       |     O(n log n)      |     O(n log n)      |



```python
def heapify(arr, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  if left < heap_size and arr[largest] < arr[left]:
    largest = left
  if right < heap_size and arr[largest] < arr[right]:
    largest = right
  if largest != index:
    arr[index], arr[largest] = arr[largest], arr[index]
    heapify(arr, largest, heap_size)


def heap_sort(arr):
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, i, n)
  for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, 0, i)
  return arr
```