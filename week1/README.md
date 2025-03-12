- 紀錄 01: week1 rwd 判斷： 原本只有判斷 (min-width: 600px) and (max-width: 1200px)，現在全部用 DOM 判斷
	- before
        ```html
        <ol class="big-boxes">
        <li>
            <i class="mdi mdi-star"></i>
            <p></p>
        </li>
        </ol>
        ```
        ```css
        .big-boxes{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
        grid-gap: 20px 20px;
        margin: 8px 8px 20px 8px; 
        }
        
        .big-boxes li:nth-child(5n+1) {
        grid-column: span 2;
        }
        @media (min-width: 600px) and (max-width: 1200px) {
            .big-boxes{
            grid-template-columns: 1fr 1fr 1fr 1fr;
            }
        
            .big-boxes li:nth-child(5n+1) {
            grid-column: span 1; 
            }
        }
        @media (max-width: 600px) {
            .big-boxes{
            grid-template-columns: 1fr;
            }
        
            .big-boxes li:nth-child(5n+1) {
            grid-column: span 1; 
            } 
        }
        ```
        ```javascript
        function checkGridColumn(){
        const bigBoxes = document.querySelectorAll('.big-boxes li');
        if(window.matchMedia("(min-width: 600px) and (max-width: 1200px)").matches){
            bigBoxes.forEach(box => {
            box.style.gridColumn = 'span 1';
            });
            if(currentIndex % 4 !== 0){
            bigBoxes[currentIndex-1].style.gridColumn = 'span 2';
            bigBoxes[currentIndex-2].style.gridColumn = 'span 2';
            }
        }
        }
        ```
	- after
        ```html
        <ol class="big-boxes">
        <li>
            <i class="mdi mdi-star"></i>
            <p></p>
        </li>
        </ol>
        ```
        ```css
        .big-boxes{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
        grid-gap: 20px 20px;
        margin: 8px 8px 20px 8px; 
        }
        
        @media (min-width: 600px) and (max-width: 1200px) {
            .big-boxes{
            grid-template-columns: 1fr 1fr 1fr 1fr;
            }
        }
        @media (max-width: 600px) {
            .big-boxes{
            grid-template-columns: 1fr;
            }
        }
        ```
        ```javascript
        function checkGridColumn(){
            const bigBoxes = document.querySelectorAll('.big-boxes li');
            if(window.matchMedia("(min-width: 600px) and (max-width: 1200px)").matches){
                bigBoxes.forEach(box => {
                    box.style.gridColumn = 'span 1';
                });
                if(currentIndex % 4 !== 0){ //計算總數
                    bigBoxes[currentIndex-1].style.gridColumn = 'span 2';
                    bigBoxes[currentIndex-2].style.gridColumn = 'span 2';
                }
            }
            else if(window.matchMedia("(max-width: 600px)").matches){
                bigBoxes.forEach(box => {
                    box.style.gridColumn = 'span 1';
                });
            } else {
                bigBoxes.forEach((box, index) => { //計算該 box 是第幾個
                    if((index + 1) % 5 == 1){
                        box.style.gridColumn = 'span 2';
                    } else {
                        box.style.gridColumn = 'span 1'; 
                    }
                });
            }
        }
        
        ```
- 紀錄 02: 增加 `window.addEventListener('resize', checkGridColumn); // 新增只要畫面尺寸不同就改變，不需要整頁 refresh`