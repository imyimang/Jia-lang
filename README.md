# 甲語言 Jia
一個基於brainfuck改編而成的程式語言

## 程式語法
`由` 輸出，對應brainfuck中的`.`

`甲` 輸入，對應brainfuck中的`,`

`左` 將指標往左移一格，對應brainfuck中的`<`

`右` 將指標往右移一格，對應brainfuck中的`>`

`申` 對當前的位元組+1，對應brainfuck中的`+`

`申` 對當前的位元組-1，對應brainfuck中的`-`

`始` 若指標所指位元組的值為零，則向後跳轉，跳轉到其對應的`終`的下一個指令處，對應brainfuck中的`[`

`終` 若指標所指位元組的值不為零，則向前跳轉，跳轉到其對應的`始`的下一個指令處，對應brainfuck中的`]`

除了上面八個符號的其他字都會被視為註解，不會執行

## 編輯器指令
輸入exit即可離開編輯器
- ### jia
    - 直接在 REPL(Read-Eval-Print Loop) 中運行Jia，輸入 `exit` 離開

- ### run <file name>
    - 執行指定的檔案，僅支援 `.txt` 和 `.jia`，如果沒有設定副檔名，預設情況下會先找尋 `<file name>.jia` 再找尋 `<file name>.txt`，如果兩者皆不存在則報錯

- ### edit <file name>
    - 在指定的檔案追加文字，僅支援 `.txt` 和 `.jia`，如果沒有設定副檔名，預設情況下會先找尋 `<file name>.jia` 再找尋 `<file name>.txt`，如果兩者皆不存在則創建 `<file name>.jia`，**該功能只能追加文字，無法編輯先前寫的內容**，按下 `Ctrl + C` 來結束編輯

## 執行
執行 `compiler.py`

# Not done yet