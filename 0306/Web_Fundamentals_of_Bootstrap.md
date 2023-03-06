# Web - Fundamentals of Bootstrap

## Bootstrap
    프론트엔드 라이브러리(Toolkit)
- <span style="color:red">반응형 웹 디자인 & CSS 및 JS 기반의 컴포넌트와 스타일 제공</span>

--- 

## Bootstrap 클래스명 맛보기
```html
<p class="mt-5">Hello, World!</p>
```
- mt-5 : {property}{sides}-{size} 

---

### Property

|클래스명|내용|
|:------:|:---:|
|m|margin|
|p|padding|


### Sides

|클래스명|내용|
|:------:|:---:|
|t|top|
|b|bottom|
|s|left|
|e|right|
|y|top, bottom|
|x|left, right|
|blank|4 sides|

### Size

|클래스명|rem|px|
|:------:|:---:|:---:|
|0|0 rem|0px|
|1|0.25 rem|4px|
|2|0.5 rem|8px|
|3|1 rem|16px|
|4|1.5 rem|24px|
|5|3 rem|48px|
|auto|auto|auto|

---

## Typography 및 Color

### Typography
    문서 상에 제목, 본문 텍스트, 목록 등

---
### Headings
    HTML h1 ~ h6 태그와 스타일을 일치시키고 싶지만 관련 HTML 태그를 더 사용할 수 없는 경우

```HTML
<p class="h1">h1. Bootstrap heading</p>
<p class="h2">h2. Bootstrap heading</p>
<p class="h3">h3. Bootstrap heading</p>
<p class="h4">h4. Bootstrap heading</p>
<p class="h5">h5. Bootstrap heading</p>
<p class="h6">h6. Bootstrap heading</p>
```

### Display Headings
    기존 Heading보다 더 눈에 띄는 제목이 필요한 경우
    (더 크고 약간 다른 스타일)

```HTML
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
<h1 class="display-5">Display 5</h1>
<h1 class="display-6">Display 6</h1>
```

### Inline text elements
    HTML inline 요소에 대한 스타일

```HTML
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
```


### List
    HTML list 요소에 대한 스타일
```HTML
<ul class="list-unstyled">
  <li>This is a list.</li>
  <li>It appears completely unstyled.</li>
  <li>Structurally, it's still a list.</li>
  <li>However, this style only applies to immediate child elements.</li>
  <li>Nested lists:
    <ul>
      <li>are unaffected by this style</li>
      <li>will still show a bullet</li>
      <li>and have appropriate left margin</li>
    </ul>
  </li>
  <li>This may still come in handy in some situations.</li>
</ul>
```
---

### Bootstrap Color system
    Bootstrap이 지정하고 제공하는 색상 시스템
### Colors
    Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap 색상 키워드

---

## Component

### Bootstrap Component
    Bootstrap에서 제공하는 UI 관련 요소
 - <span style="color:red">버튼, 폼, 카드, 드롭다운, 네비게이션 바 등</span>
 - <span style="color:red">for 일관된 디자인, 쉬운 프로토타입 제작 및 사용자 경험</span>

---

## 참고

### CDN (Content Delivery Network)
     지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
 - <span style="color:red">서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 (웹 페이지 로드 속도를 높임)</span>

### Bootstrap CDN
 1. 부트스트랩 홈페이지에서 Compiled CSS and JS 다운로드
 2. CDN을 통해 가져오는 부트스트랩 css와 js 파일을 확인
 3. bootstrap.css 파일을 참고하여, 작성한 클래스에 적용된 스타일을 직접 확인해 볼 수 있음

### Bootstrap을 사용하는 이유

 - 손쉬운 반응형 웹 디자인 구현
 - 빠른 개발과 유지보수
     - 미리 디자인된 다양한 컴포넌트 및 기능
     - 일관된 코드와 문서
 - 커스터마이징(customizing)이 용이
 - 크로스 브라우징(Cross browsing) 지원
     - 모든 주요 브라우저에서 작동하도록 설계되어 있음