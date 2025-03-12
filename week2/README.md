## task3 javascript
-
```javascript
    for (let name of data) { 
        let middleName;
        // middleName = name[2]，字串本身也是一個 array ，所以可以直接取裡面的字元
        // middleName = '明'
        if (name.length === 2) {
        middleName = name[name.length - 1]; // 如果名字只有兩個字，取最後一個字
        } else {
        middleName = name[name.length - 2]; // 取倒數第二個字
        }  

        // count 。 新增進 object 及計算同時進行
        // key (明) 如果有值就「值+1」 ，沒有的話「0+1」
        // 舉例來說：middleNameCount[明] = 1 就是, middleNameCount = {明：1} ，但現在在這個值寫了判斷式
        middleNameCount[middleName] = (middleNameCount[middleName] || 0) + 1;

        // if it the first time, record it 。 如果 middleNameMap[明] 不存在，就新增進 object 
        // middleNameMap[明] = 陳王明雅, middleNameMap = {明：陳王明雅}
        // 這邊改寫簡單一點，直接定義  middleNameMap[middleName] = name;
        if (!middleNameMap[middleName]) {
        middleNameMap[middleName] = name;
        }
    }
```
  
## task2 javascript
- `Object.entries(obj)` 靜態方法回傳給定之物件自己的可枚舉字串以字串為鍵的屬性之鍵值對**陣列**。
- 說明中有提到可以用：屬性鍵，可改用 `Object.keys()`。屬性值，可改用 `Object.values()`
- 所以試著這樣寫，但發現找到 value: count =1 要取 key ，所以還是要同時找到兩個
-
```javascript
    // 找出唯一的中間名
    let uniqueMiddleName = null;
    for (let [key, count] of Object.entries(middleNameCount)) {
        if (count === 1) {
        uniqueMiddleName = key;
        break;
        }
    }
    
    // 輸出結果
    if (uniqueMiddleName) {
        console.log(middleNameMap[uniqueMiddleName]);
    } else {
        console.log("沒有");
    }
```

## task1 javascript
- 箭頭函式
- 條件運算子 (ternary operator) `condition ? expressionIfTrue : expressionIfFalse;`
-
```javascript
    const friendLocations = Object.entries(messages).map(([name, message]) => {
    for (const station of stations) {
        if (message.includes(station)) {
        return { name, station };
        }
    }
    return null;
    }).filter(Boolean)
```
- `Object.entries(messages)` 將 `messages` 物件轉換為一個陣列，其中每個元素是 `[key, value]` 的形式。
-
```javascript
    const messages = {
        "Bob": "I'm at Ximen MRT station.",
        "Mary": "I have a drink near Jingmei MRT station."
    };
    Object.entries(messages);
    // 結果:
    [
        ["Bob", "I'm at Ximen MRT station."],
        ["Mary", "I have a drink near Jingmei MRT station."]
    ]
```
- `map(([name, message]) => {...})`
	- 使用解構賦值語法 `[name, message]` 提取每個陣列元素的 key 與 value，分別對應於朋友的名稱和訊息。
	- 每次執行 `map` 的回呼函數，會返回新的資料。
- `if (message.includes(station))`
	- 檢查該訊息是否包含目前正在迭代的車站名稱。
	- 如果找到匹配的車站：返回一個物件，格式為 `{ name, station }`，例如：`{ name: "Bob", station: "Ximen" }`。
- `turn null`
	- 如果遍歷完所有車站名稱後，訊息中沒有提及任何車站，則返回 `null` 表示無效結果。
- `.filter(Boolean)`
	- 過濾掉 `null` 或 `undefined` 的結果。
	- `Boolean` 是一個內建函數，用於將值轉換為布林值：
		- `Boolean(value)` 的結果為：
			- `true`：如果 `value` 是非空字串、非零數字、物件、陣列等。
			- `false`：如果 `value` 是 `null`、`undefined`、`0`、`""` (空字串)、或 `false`。
	- `filter(Boolean)` 可以簡單地過濾掉那些為 `null` 的結果。


## task2,3,4 python
- `item()` 回傳 dict 中的 key-value
	- 對照： `Object.entries(obj)` 靜態方法回傳給定之物件自己的可枚舉字串以字串為鍵的屬性之鍵值對**陣列**。
- `get()` 利用 key 取得 item 的 value
- `list.sort()` 讓列表依升冪排列
	- 對照： `Array.prototype.sort([compareFunction])` 儲存任何類型的唯一值（unique）
- `x = sorted()` 讓可迭代物件（iterable)(列表、字典、元組、集合)依升冪排列

| 特性 | `sort()` | `sorted()` |
| ---- | ---- | ---- |
| 使用範圍 | 只能用於列表（list）。 | 可以用於所有可迭代物件（iterable）。 |
| 是否改變原始資料 | **會**改變原列表，直接在原地進行排序。 | **不**改變原資料，返回排序後的新物件。 |
| 返回值 | 返回值為 `None`（因為改變是原地進行的）。 | 返回排序後的新列表（list）。 |
| 語法形式 | `<list>.sort(key=..., reverse=...)` | `sorted(iterable, key=..., reverse=...)` |
 
- 問題
-  
```python
   if criteria == "price":
          sorted_consultants = sorted(consultants, key=lambda x: x["price"])
```

- **`lambda`** 定義一個匿名函數的關鍵字，這種函數沒有名字，常用於簡單的操作或臨時的邏輯。
- **`x`** 表示函數的輸入參數，這裡的 `x` 是一個變數，代表傳遞進來的物件（例如字典）。
- **`x["price"]`** 函數的運算邏輯，從輸入物件 `x` 中取出鍵為 `"price"` 的值。
- **返回值** 該匿名函數的返回值是 `x["price"]` 的值。
- 為什麼不能寫：  
```python
    if criteria == "price":  
    sorted_consultants = sorted(consultants, key="price")  
```
- **`key` 參數要求提供一個函數或可調用物件**，而不是一個字串。
	- 在 Python 的排序函數中，`key` 是用來指定排序的依據。`key` 參數需要是一個 **函數**，這個函數會作用於每個元素，返回用於比較的值。  
	- 例如：
        	- 如果提供 `key=lambda x: x["price"]`，排序函數會使用字典中 `"price"` 的值來排序。
        	- 但如果提供 `key="price"`，Python 無法理解如何使用這個字串來處理每個元素，因此會引發錯誤。

## task1 python
- `list.index(elmnt)` 取得 value 的對應 key (int)
- `list.append(elmnt)` 在列表後面加上 element