---
marp: true
title: sample
theme: gaia
class: lead
backgroundColor: #fff
style: |
  * {
    font-family: Arial, sans-serif;
    font-size: 19pt;
    line-height: 1.35em;
    color: black;
    }
  .scripture {
    text-align: left;
    text-align-last: left;
    padding-left: 1em;
    padding-right: 2em;
  }
  .scriptures {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .image-container {
    display: flex;
    align-items: center; /* Vertically center image */
    justify-content: center; /* Horizontally center image */
    height: 100%; /* Full height of the column */
  }
  img {
    width: 550px;
    height: 600px;
    object-fit: contain;
  }
---

<div class="columns">
  <div class="scriptures">
    <br>
    <div class="scripture">
      <b>Mark 막1:1 하나님의 아들 예수 그리스도의 복음의 시작이라
      </b>
    </div>
    <br>
    <div class="scripture">The beginning of the gospel of Jesus Christ, the Son of God;
    </div>
    <br>
    <div class="scripture">
      <b>Mark 막1:2 선지자 들의 글에 기록된 바 보라 내가 나의 사자를 너의 얼굴 앞에 보내노니 그가 너 앞에서 너의 길을 예비하리라
      </b>
    </div>
    <br>
    <div class="scripture">as it is written in the prophets, Behold, I send my messenger before thy face, which shall prepare thy way before thee.
    </div>         
  </div>
  <div class="image-container">
    <img src='pictures\picture_2.jpg'>
  </div>
</div>
