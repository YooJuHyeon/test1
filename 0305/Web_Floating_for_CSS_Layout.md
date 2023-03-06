# Web - Floating for CSS layout

# 1. CSS Float

### CSS Float
 - 요소를 <span style ="color:red">띄워서</span> 텍스트 및 인라인 요소가 그 주위를 감싸도록 하는 배치
     - <span style ="color:red">왼쪽 혹은 오른쪽으로 띄워 Normal flow에서 벗어남</span> 

### Float 탄생 배경
 - 텍스트 열 내부에 떠다니는 이미지를 포함하면서도 해당 이미지 좌우에 텍스트를 둘러싸는 간단한 레이아웃을 구현하기 위해 도입
     - ex) 신문 레이아웃

### Float 활용 예시 (style 태그만 발췌)
```css
 <style>
    .box {
      width: 10rem;
      height: 10rem;
      border: 1px solid black;
      background-color: lightcoral;
    }

    .float-left {
      float: left;
    }

    .float-right {
      float: right;
    }

  </style>
```
---
### 참고

 - Float는 원래 탄생 목적에서 더 나아가 웹 페이지 전체 레이아웃을 구성하는 데 사용되었으나, Flexbox와 Grid의 등장으로 인해 다시 원래의 목적으로 돌아감

