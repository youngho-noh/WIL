# Python

### 1. 기초 문법

#### 1. 주석

한 줄 주석은 `#`으로 표현한다.

여러 줄의 주석은 

1. 한 줄 씩 `#` 을 사용
2. `'''` 또는 `"""`를 사용



#### 2. 코드 라인

한 줄에 한 문장

문장은 파이썬이 실행가능(executable)한 최소한의 코드 단위

`;`을 사용하여 코드를 한줄로 표현가능 (but, 쓰지 않음)

```python
print('hi~'); print('there:)')   # 가능함
```

`\`로 코드에는 여러 줄, 결과 값은 한 줄로 표현 가능

```python
print('hi,\
there')
>> hi, there    # 가능함
```

`[]` `{}` `()`는 `\` 없이 인자들들 여러줄로 작성 가능



#### 3. 변수 

1.  할당 연산자

   `=`를 통해 할당 가능

   `type()`을 통해 데이터의 유형 파악 가능

   `id()`를 이용하여 해당 값의 메모리 주소 확인 가능

   같은 값을 동시에 할당 가능

   ```python
   a = b = 100
   ```

   다른 값을 동시에 할당 가능

   ```python
   a, b = 10, 20
   ```

   cf)  아래 두 경우는 비슷해 보이는 상황이나 다른 Error 코드가 뜬다 **(주의)**

   변수의 개수가 적을 때 오류 발생

   ```python
   x, y = 1
   
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-7-d58918a14868> in <module>
   ----> 1 x, y = 1
   
   TypeError: cannot unpack non-iterable int object
   ```

   변수의 개수가 더 많을 때 오류 발생

   ```python
   x, y, z = 1, 2
   
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)
   <ipython-input-9-b95546393cb7> in <module>
   ----> 1 x, y, z = 1, 2
   
   ValueError: not enough values to unpack (expected 3, got 2)
   ```

   

2. 식별자(identifiers)

   > 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름

   식별자의 이름은 **영문 알파벳(대, 소), underscore(_), 숫자**로 구성

   첫 글자로 숫자 불가능

   길이 제한 없음

   대소문자 구분

   다음의 키워드들은 사용 불가

   ```python
   False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
   ```

   **(주의)** 내장함수나 모듈등의 이름으로 만들면 안됨

   만약 만들었을 경우 `del`을 사용하여 변수를 제거해 줘야 함



#### 4. 데이터 타입(Data Type)

1. 숫자 타입

   - int(정수, integar)

     8진수 : `0o`, 2진수 : `0b`, 16진수 : `0x`

   - float(부동소수점, 실수)

     실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치하지는 않음

     크게 중요하지는 않으나, 간혹 값이 같은지 비교하는 과정에서 문제가 발생

     컴퓨터식 지수 표현 방식 : `e` 또는 `E`

     기본 적인 처리 방법

     1. `1e - 10`

     ```python
     a = 3.5 - 3.12
     b = 0.38
     
     abs(a - b) <= 1e-10   # 왜냐하면 a - b의 값이 0.38이 아니라 0.3799999999999999로 나옴
     
     >> True
     ```

     2. sys 모듈 사용(epsilon)

     ```python
     import sys
     abs(a - b) <= sys.float_info.epsilon
     # 충분히 작은 값인 epsilon보다 작은가
     ```

     3. math 모듈 사용

     ```python
     import math
     math.isclose(a, b)
     a, b가 충분히 가까운가
     ```

   - comples(복소수)

     실수부와 허수부를 가진다

     허수부는 `j`로 표현한다

     ```python
     1. a = 3 - 4j
     
     2. complex('2-3j')
     # 두 번째의 경우 +,-연산자 주위에 공백을 포함해서는 안됨!!
     ```

   

2. 문자 타입(string)

   - 기본 활용법

     `''`, `""`,  `'''`, `"""` 사용가능

   - 문자열 내에 `''`, `""` 사용 : `\`를 활용하여 사용

   - 문자열은 `+`로 붙이고, `*`로 반복시킬 수 있다

   - 이스케이프 시퀀시

     `\`을 활용하여 이를 구분할 수 있다.

     `\n` : 줄 바꿈

     `\t` : 탭

     `\r` : 캐리지리턴

     `\0` : 널(Null)

     `\\` : \

     `\'` : '

     `\"` : "

   - String interpolation

     1. `%-formation`

     %d : 정수

     %f : 실수

     %s : 문자열

     2. `str.format()`

     3. `f-string` :  자주 쓰는 것!!

        형식 지정 가능

        ```python
        import datetime
        today = datetime.datetime.now()
        
        f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
        ```

        연산과 출력형식도 지정가능

        ```python
        pi = 3.141592
        f'원주율은 {pi:.4}! 반지름이 2일때 원의 넓이는 {pi*2*2}'
        # 출력형식 지정: 원주율             # 연산 : 넓이
        ```

   

3. 참/거짓(Boolean) 타입

   True와 False로 이루어진 bool타입이 있다.

   1. 다음은 `False`로 반환

      `0`, `0.0`, `()`, `[]`, `{}`, `None`

   2. `None` 타입

   ```python
   print(type(None))
   >> <class 'NoneType'>
   
   a = print(b)
   print(type(a))
   >> <class 'NoneType'>     # print는 NoneType
   ```



4. 형변환

   1.  암시적 형변환(Implicit Type Conversion)

      ```python
      True + 5
      >> 6
      
      * 다음은 type별 연산의 결과를 나타낸 것이다
      int + float
      >> float
      
      int + complex
      >> complex
      ```

   2. 명시적 형변환

      > 위의 상황을 제외하고는 모두 명시적 형변환을 해야함

      - string --> integer : 형식에 맞는 숫자만 가능
      - integer --> string : 모두 가능

      암시적으로 되면 명시적으로 가능

      - `int()` : string, float를 int로 변환
      - `float()` : string, int를 float로 변환
      - `str()` : int, float, list, tuple, dictionary를 문자열로 변환



#### 5. 연산자(Operator)

 1. 산술 연산자

    ```python
    + : 덧셈
    - : 뺄셈
    * :곱셈
    / : 나눗셈
    // : 몫
    % : 나머지(modulo)
    ** : 거듭제곱
    ```

    `/` 나눗셈은 항상 `float`를 돌려준다

    정수부(몫)만 얻으려면 `//`연산자 사용

    cf) `divmod(x, y)` 는 몫과 나머지를 반환

    

	2. 비교 연산자

    ```python
    < : 미만
    <= : 이하
    > : 초과
    >= : 이상
    == : 같음
    != : 같지않음
    is : 객체 아이덴티티
    is not : 부정된 객체 아이덴티티
    ```

    

3. 논리 연산자

   `a and b` : a와 b 모두 True 시에만 True

   `a or b` : a와 b 모두 False 시에만 False

   `not a` : True -> False,  False -> True

   - 단축평가!!

     `and`와 `or` 가 있음

     ```python
     'a' and 'b'
     >> 'b'
     # 첫번째가 True면 두번째 값 확인
     # 첫번째가 False면 그냥 False (why? 어차피 False이니까)
     -----------------------------------------------------
     'a' or 'b'
     >> 'a'
     # 첫번째가 True면 그냥 True (why? 어차피 하나만 True이면 되니까)
     # 첫번째가 False면 두번째 값 확인
     ```



4. 복합 연산자

   ```python
   a += b    a = a + b
   a -= b    a = a - b
   a *= b    a = a * b
   a /= b    a = a / b
   a //= b   a = a // b
   a %= b    a = a % b
   a **= b   a = a ** b
   ```



5. 기타 주요 연산자

   - Concatenation

     숫자가 아닌 자료형은 `+`로 합칠 수 있다

     ex) 문자열, 리스트, 튜플 ...

   - Containment Test

     `in` 연산자를 통해 요소가 있는지 여부 확인 가능

     ```python
     'a' in 'apple'
     >> True
     ```

   - Identity

     `is` 연산자를 통해 동일한 object인지 확인

     `==` 는 겉모습만 같으면 True

     `is` 연산자는 주소가 같아야 True

     **(주의)** -5 부터 256 까지의 id는 동일 ==>  따라서 `is` 연산자를 사용해도 True나옴

     ​           공백없는 알파벳 문자열도 같게끔 설정!!

     ```python
     a = 1
     b = 1
     print(a is b)
     >> True
     ---------------
     a = 'hi'
     b = 'hi'
     print(a is b)
     >> True
     ```

   - Indexing / Slicing

     `[]`를 통해 접근, `[:]`를 통해 slicing



6. 연산자 우선순위

   ```python
   0. `()`을 통한 grouping
   1. Slicing
   2. Indexing
   3. 제곱연산자 `**`
   4. 단항연산자 `+`, `-` (음수/양수 부호)
   5. 산술연산자 `*`, `/`, `%`
   6. 산술연산자 `+`, `-`
   7. 비교연산자 `in`, `is`
   8. `not`
   9. `and` 
   10. `or`
   [파이썬 문서](https://docs.python.org/ko/3/reference/expressions.html#operator-precedence)
   ```





### 2. 컨테이너

1. 시퀀스(sequence) 형 : 나열된 형식

   > vs non-sequence : set, dictionary
   >
   > 종류 : List, Tuple, String, Range, Binary

   \* 튜플

   - 새로 알게 된 것

     ```python
     new_tuple = 1, 2
     print(new_tuple)
     print(type(new_tuple))
     >> (1, 2)
     >> <class 'tuple'>
     ---------------------
     x, y = 1, 2
     print(x, y)
     >> 1 2
     ```

     변수를 swap하는 코드 역시 tuple을 활용

     ```python
     x = 1
     y = 100
     x, y = y, x
     print(x, y)
     >> 100 1
     ```

     뒤에 ,(쉼표)와 구성된 튜플은 하나의 항목으로 구성되어 있습니다.

     ```python
     single_tuple = ('hello',)
     print(type(single_tuple))
     print(len(single_tuple))
     >> <class 'tuple'>
     >> 1
     ```

     

   - 시퀀스에서 활용할 수 있는 연산자/함수

       ```python
       x `in` s	   containment test
       x `not in` s   containment test
       s1 `+` s2      concatenation
       s `*` n        n번만큼 반복하여 더하기
       `s[i]`         indexing
       `s[i:j]`       slicing
       `s[i:j:k]`     k간격으로 slicing
       len(s)         길이
       min(s)         최솟값
       max(s)         최댓값
       s.count(x)     x의 개수
       ```

   

2. 비 시퀀스(non-sequence)형

   \* set

    - 새로 알게 된 것

      ```python
      # 빈 set 만들기
      empty_set = set()
      # 차집합
      set_a - set_b
      # 합집합
      set_a | set_b   # 엔터 위 shift + 달러
      # 교집합
      set_a & set_b
      ```

   

   \* dictionary

    - 새로 알게 된 것

      **key**는 **변경 불가능한 데이터**만 가능(immutable : string, integer, float, boolean, tuple, range)

      중복된 키 존재 불가



 3. 컨테이너 형변환

    리스트, 튜플, 레인지, string, set, dictionary 서로 전환 가능 (단, 아래 상황 제외)

    dictionary는 range가 될 수 없음. 또한 key 값만 다른 것들로 변환 가능(**string으로는 변환가능**하다)

    모든 것들은 range와 dictionary가 될 수 없다



4. 데이터 분류

   > mutable vs immutable

   - mutable(변경 가능) : list, dict, set
   
   - immutable(변경 불가능) : 리터럴(숫자(number), 글자(string), 참/거짓(bool), range(), tuple())
   





### 3. 제어문





  





















