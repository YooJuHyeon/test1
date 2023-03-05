# Web-Flexible box for CSS layout

## 1. CSS Flexbox
 - 요소를 행과 열 형태로 배치하는 <span style ="color:red">1차원</span> 레이아웃 방식

     - <span style ="color:red">요소간 '공간배열'과 '정렬'</span>
     - (1차원이기 때문에 4가지 방향 : → ← ↑ ↓)

---

### Flexbox 기본 사항

 - **main axis (주 축)**
     - flex item들이 배치되는 기본 축
     - main start에서 시작하여 main end 방향으로 배치
     - → 가 기본 방향이지만, 꼭 가로 방향은 아님   

 - **cross axis (교차 축)**
     - main axis에 수직인 축
     - cross start에서 시작하여 cross end 방향으로 배치
     - ↓ 가 기본 방향이지만, 꼭 세로 방향은 아님 (그저 메인축에 수직인 축일 뿐임)

 - **Flex Container**
     - <span style ="color:blue">display: flex;</span> 혹은 <span style ="color:blue">display: inline-flex;</span>가 설정된 부모 요소
     - 이 컨테이너의 1차 자식 요소들이 Flex item이 됨
     - flexbox 속성 값들을 사용하여 자식 요소 Flex item들을 배치

 - **Flex item**
     - Flex Container 내부에 레이아웃 되는 항목 

 ---

 ## 2. Flexbox 레이아웃 구성

 ### Flexbox 관련 속성
  - Flex Container 관련 속성
  ```
  display, flex-direction, flex-wrap, justify-content, align-items, align-content
  ```
 
 ### Flex item 관련 속성 
 ```
 align-self, flew-grow, flex-shrink, flex-basis, order
 ```
---

 ### 1. Flex Container 지정

 ```css
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;
    }
 ```
 - flex item은 행으로 나열
 - flex item은 주축의 시작 선에서 시작
 - flex item은 교차축의 크기를 채우기 위해 늘어남


### 2. flex-direction 지정

 ```css
    .container {
      flex-direction: column;
    }
 ```
 - flex item이 나열되는 방향을 지정
 - column으로 지정할 경우 주 축이 변경됨
 - -reverse로 지정하면 시작 선과 끝 선이 서로 바뀜


### 3. flex-wrap
 ```css
.container {
    /* flex wrap: nowrap; */
    flex-wrap: wrap;
}
 ```
 - flex item 목록이 flex container의 하나의 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정
 - (화면 너비를 줄여서 확인해보기)


### 4. justify-content

 ```css
 .container {
    /* justify-content: flex-start;*/
    justify-content: center;
 }
 ```
 - 주 축을 따라 flex item과 주위에 공간을 분배


### 5. align-content

 ```css
 .container {
    flex-wrap: wrap;

    align-content: center;
 }
 ```
 - 교차축을 따라 flex item과 주위에 공간을 분배
 - *flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨*
 - *한 줄 짜리 행에는 (flex-wrap이 nowrap으로 설정된 경우) 효과 없음*


### 6. align-items

 ```css
 .container {
    align-items: center;
 }
 ```
 - 교차 축을 따라 flex item 행을 정렬

### 7. align-self

 ```CSS
 .item1 {
    align-self: center;
 }

 .item2 {
    align-self: flex-end;
 }
 ```
 - 교차 축을 따라 개별 flex item을 정렬


### 8. flex-grow
 ```css
 .item1 {
    flex-grow: 1;
 }

 .item2 {
    flex-grow: 2;
 }
 ```
 - 남는 행 여백을 비율에 따라 각 flex item에 분배
 - flex-grow의 반대는 flex-shrink
     - 넘치는 너비를 분배해서 줄임


### 9. flex-basis
 ```CSS
 .item1 {
    flex-basis: 300px;
 }

 .item2 {
    flex-basis: 600px;
 }

 ```
 - flex item의 초기 크기 값을 지정
 - flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선!


---

### 목적에 따른 분류

 - 배치 설정
     - flex-direction
     - flex-wrap

 - 공간 분배
     - justify-content
     - align-content

 - 정렬
     - align-items
     - align-self

```
속성명 Tip

- justify : 주 축
- align : 교차 축
```

---

## 3. Flexbox 반응형 레이아웃 
 - flex-wrap을 사용해 반응형 레이아웃 작성 (feat.flex-grow & flex-basis)

---

## 4. 참고

### justify-items 및 justify-self 속성이 없는 이유
 - 필요 없기 때문
 - margin auto를 통해 정렬 및 배치가 가능

---

### Shorthand - "flex-flow"
```css
.container {
    flex-flow: flex-direction flex-wrap;
}
```

### Shorthand - "flex"

```css
/* One value, unitless number: flex-grow */
flex: 2;

/* One value, length or percentage: flex-basis */
flex: 10rem;

/* Two values: flex-grow ¦ flex-basis */
flex: 1 30px;

/* Two values: flex-grow ¦ flex-shrink */
flex: 2 2;

/* Three values: flex-grow ¦ flex-shrink ¦ flex-basis */
flex: 2 2 10%;
```