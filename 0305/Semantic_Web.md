# Web - Semantic Web

## 1. Semantic Web
 - 웹 데이터를 **의미론적**으로 표현하고 연결하는 개념
     - <span style ="color:red">컴퓨터가 데이터의 내용과 문맥을 더 효율적으로 이해하고 더 지능적으로 활용하기 위해</span>
---
## 2. Semantics in HTML

### HTML Semantic Element
 - 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
     - <span style ="color:red">검색엔진 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 만들어줌</span>
---
```HTML
<h1>Heading</h1>
```
- **페이지 최상위 제목 의미**를 제공하는 semantic 요소 h1
- 브라우저에 의해 제목처럼 보이도록 큰 글꼴로 스타일이 지정됨

```html
<span style="font-size: 32px;">Heading</span>
```
 - 모든 요소를 최상위 제목"처럼" 보이게 할 수는 있으나 **의미론적 가치는 없음**

---

### 페이지 구조화를 위한 대표적인 semantic element
 - header
 - nav
 - main
 - article
 - section
 - aside
 - footer

---

## 3. Semantics in CSS

### OOCSS
     Object-Oriented CSS
     - 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

```css
/* 예시는 style태그 부분만 발췌 */

<style>
	/* 기본 카드 구조 */
	.card {
		border: 1px solid black;
		border-radius: 5px;
		padding: 1rem;
	}

	/* 카드 제목 */
	.card-title {
		font-size: 1rem;
		font-weight: bold;
	}

	/* 카드 내용 */
	.card-description {
		font-size: 0.7rem;
	}

	/* 기본 버튼 구조 */
	.btn {
		padding: 1rem;
		cursor: pointer;
	}
    /* 빨간 배경 */
	.bg-red {
		background-color: crimson;
	}
    /* 파란 배경 */
	.bg-blue {
		background-color: lightblue;
	}

  </style>
```

---
### BEM
     블록(Block), 요소(Element), 수정자(Modifier)를 사용해 클래서 이름을 구조화하는 방법론

### BEM 구성

```css
/* Block */
.block {}

/* Element */
.block__element {}

/* Modifier */
.block--modifier {}
```

 - Block
     - **문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너**
     - 재사용 가능한 독립적 블록, 가장 바깥쪽 상위 요소
     - *재사용을 위해 margin 또는 padding을 적용하지 않음*

 - Element
     - block이 포함하고 있는 한 조각
     - 블록을 구송하는 *종속적인 하위요소*

 - Modifier
     - block 또는 element의 속성 (컬러, 사이즈 등의 속성들)

---

## 4. 참고

### 의미론적인 마크업의 이점

 - **검색 엔진**이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
 - **시각 장애 사용자**가 스크린 리더기로 웹 페이지를 사용할 때 추가적으로 도움
    ```
    예를들어 strong 태그는 시각적+문법적 강조의 의미가 있어서 스크린리더기를 사용했을 때 강조가 됨

    반면 b 태그는 문법적인 강조의 의미 없이 시각적인 스타일만 볼드체로 바꾸기 때문에 스크린 리더기를 사용하면 강조되지 않음

    웹 접근성은 법적 의무사항이기도 하기 때문에 충분히 고려하기!
    ```
---

### 클래스 이름이 너무 길어지는 건 아닐까?
 - 클래스를 만들 때 가장 중요한 부분은 *클래스 이름이 무엇을 나타내는지 분명하게 전달할 수 있는가*에 대한 것
 - 각각의 명명법은 개인적인 취향에 따라 다르지만, **빠르고 명확한 표기**를 우선적으로 해야 함
 - 이 부분에 대해 너무 고민하지 않도록 하는 것도 중요!

---

### OOCSS & BEM의 목적
 - **재사용** 가능한 모듈로 분리함으로써 유지보수성과 확장성을 향상
 - 개발자 간의 협력이 향상되어 공통 언어와 코드 이해를 확립
     - Airbnb CSS 스타일 가이드의 경우 OOCSS 및 BEM 방법론을 조합하여 사용
        - [Airbnb](https://github.com/airbnb/css)