## 01.18(Mon)

> 객체의 life cycle

- 파이썬 실행했을 때 메모리와 cpu에서 일어나는 일

  : creation : class를 정의하고 인스턴스를 생성 ; 이 때 객체 메모릭 할당되고, 객체가 조작될 준비를 마침 `__init__`

   handling : 

   destruction : 객체의 reference count가 0이 될 때, 더 이상 참조하는 값이 없을 때 객체가 삭제된다. 객체가 필요 없어졌을 대 제거하는 것을 garbage collection이라고 한다. `__del__`






## 01.19(Tue)

> Array  vs  Linked list

#### Array

가장 기본적인 자료구조인 `Array` 자료구조는, 논리적 저장 순서와 물리적 저장 순서가 일치한다. 따라서 `Index` 로 해당 원소에 접근할 수 있다. 즉, **random access** 가 가능하다는 장점이 있다.

but, 삭제 또는 삽입의 과정에서 해당 원소에 접근하여 작업을 완료한 뒤 ***O(1)***, 또 한 가지 작업을 추가로 해줘야하기 때문에 시간이 더 걸린다. 

- 삭제의 경우 : 배열의 연속적인 특징이 깨지게 된다. (빈 공간 발생) 따라서, 삭제한 원소보다 큰 인덱스를 갖는 원소들을 `shift` 해줘야하는 비용이 발생하고, 이러한 경우 `시간의 복잡도`는 ***O(n)***이 된다. 그렇기 때문에 Array 자료구조에서 삭제 기능에 대한 `time complexity`의 worst case는 ***O(n)***이다.
- 삽입의 경우 : (위와 동일) 만약 첫번째 자리에 새로운 원소를 추가하고자 한다면 모든 원소들의 `Index`를 1씩 `shift`해줘야 함으로 이 경우도 O(n)의 시간을 요구하게 된다.

정적 메모리 할당 (`stack` 영역에 메모리 할당)

size가 선언시점에 정해짐

새로운 데이터를 받았을 때 공간이 다 차있으면, 새로운 메모리 공간을 할당 받는다.



#### Linked List

위의 문제를 해결하기 위한 자료구조가 `linked list`이다. 각각의 원소들은 자기 자신 다음에 어떤 원소인지만 기억한다. 따라서 이 부분만 다른 값으로 바꿔주면 삭제와 삽입을 ***O(1)*** 만에 해결할 수 있다.

but, Linked List 또한 한 가지 문제를 가지고 있다.  원하는 위치에 삽입을 하고자 하면, 원하는 위치를 search과정에 있어서 첫번째 원소부터 다 확인해봐야 한다는 것이다***(O(n)의 time complexity)***. Array와는 달리 논리적 저장 순서와 물리적 저장 순서가 일치하지 않기 때문이다. 이것은 일단 삽입하고 정렬하는 것과 마찬가지이다. 이 과정으로 인해, 어떠한 원소를 삭제 또는 추가하고자 했을 때, 해당 원소를 찾기 위해 O(n)의 시간이 추가적으로 발생한다.

- 삽입과 삭제의 경우 : 맨 앞과 맨 뒤의 경우 O(1)의 시간 복잡도를 갖지만,

  ​                                    그 외에 중간에 삽입이나 삭제를 하는 경우 O(n)의 시간 복잡도를 갖는다. --> 그럼에도 array보다 빠른 속도를 보인다.

동적 메모리 할당(`heap`영역에 메모리 할당) : 새로운  node가 추가될 때, runtime에 할당된다.

추가할 때마다 동적으로 위치를 할당받는다.

size는 다양할 수 잆다 ; node들이 추가될 때 runtime시점에서 size가 커질 수 있다.

Linked List 자료구조는 search에도 O(n)의 time complexity를 갖는다.) Linked List는 **Tree 구조**의 근간이 되는 자료구조이며, Tree에서 사용되었을 때 그 유용성이 들어난다.



#### 차이

전반적으로 linked list가 더 유용해보인다. 그러나 알고리즘 문제를 풀 때는 메모리 공간의 범위를 파악할 수 있도록 주기 때문에 array가 훨씬 빠르고 좋다.

linked list에서는 list 입력과 삭제 시마다 메모리 할당과 해제가 발생한다. 이때 시간복잡도에는 포함되지 않지만 `시스템콜(system call)`을 사용하는 구문은 시간이 더 걸린다.





## 01.22(Fri)

> 컴퓨터 부품 & 역할

- CPU (central Process Unit) : 컴퓨터의 두뇌 (인텔 & AMD): intel(R) Core(TM) **i7 8565U** CPU @ 1.80GHz  1.99 GHz

  1. 코어의 수 : 부릴 노예의 수 : **8세대**

  2. 쓰레드 : 노예가 부릴 손의 수

  3. 오버클럭 : 노예가 발까지 사용해서 일함 : **(클럭 스피드 : 1.80 or 1.99)**

  4. 캐쉬메모리 : 노예가 짊어지고 있는 백팩(CPU가 가지고 있는 저장 공간, 임시) : 

     > 코어와 메모리 사이의 데이터처리 속도 완충해주는 고속기억장치

- GPU : 다른 일을 시킬 노예(CPU가 옥수수를 잘 캔다면, 얘는 감자를 잘 캠)

     (NVIDIA : 지포스 / AMD : RADEON)

- 램(Memory) : 노예가 준비한 리어카

     16GB / DDR4 / 2,133MHz / 8G X 1

     **메모리 용량** / **데이터 전송률(CPU와 호환되는지 확인 필)** / **CPU와 통신할 수 있는 대역폭(도로의 차선 개념)** / **물리적으로 몇개의 메모리가 장착되어 있는지**

- HDD(hard disk drive) : 수확물의 저장 창고

- SSD(solid state disk) : 최신식 저장 창고(하드디스크보다 빠름)

- 파워 : 노예한테 주는 월급(적게 주면 일 못함, 약간 여유있게 주는 것이 좋음)

- ODD(optical disc drive) : cd 드라이버
- 파워 서플라이





## 01.26(Tue)

> Stack & Queue

- Stack이란?

  Stack is an **abstract data type** that serves as a collection of elements, with *two main principal operations* : **Push** & **Pop**

  -- push ; add an element to the collection

  -- pop ; removes the data, which was added the most recently & was not yet removed

**LIFO** (last in, first out)

(for example) cache


![](https://www.der-wirtschaftsingenieur.de/bilder/stack.PNG)





- Queue란?

  Queue is a particular kind of abstract data type or collection in which the entities(개체) in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as **enqueue**, and removal of entities from the front terminal position, known as **dequeue**.
  
  --enqueue : add entities to the rear terminal position
  
  --dequeue : remove entities from the front terminal position

**FIFO** (first in, first out) **/** linear data structure



![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/300px-Data_Queue.svg.png)



## 01.29(Fri)

> 













