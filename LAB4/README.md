# LAB 4

Напишіть програму, яка надає статистику щодо заданого файлу. Програма повиненна
надрукувати наступну статистику про довільний файл:
1. Кількість рядків
2. Кількість порожніх рядків
3. Кількість рядків з літерою "z"
4. Кількість літер “z” у файлі
5. Кількість рядків з групою символів “and” (наприклад, "andromeda" містить "and" так
само, як і "you and me").
Обов’язкові вимоги до програми.
• Програми повинна запитувати користувача шлях до файлу
• Програми повинна запитувати користувача, чи потрібно проаналізувати ще один файл
• Програми повинна зупинитись тільки тоді, коли цього хоче користувач

## Приклад виконаної програми
```txt
PS C:\Users\lookandhate\Desktop\nulp_trash> & C:/Users/lookandhate/AppData/Local/Programs/Python/Python311/python.exe c:/Users/lookandhate/Desktop/nulp_trash/LAB4/main.py      
Введіть шлях до файлу: c:\Users\lookandhate\Desktop\123.txt
File: c:\Users\lookandhate\Desktop\123.txt
 total lines: 6
 empty lines: 0
 lines with "z": 4
 "z" count: 32
 lines with "and": 3
Аналізувати ще один файл? (y/n): y
Введіть шлях до файлу: c:\Users\lookandhate\Desktop\123.txt
File: c:\Users\lookandhate\Desktop\123.txt
 total lines: 7
 empty lines: 1
 lines with "z": 4
 "z" count: 32
 lines with "and": 3
Аналізувати ще один файл? (y/n): y
Введіть шлях до файлу: c:\Users\lookandhate\Desktop\123.txt
File: c:\Users\lookandhate\Desktop\123.txt
 total lines: 7
 empty lines: 1
 lines with "z": 4
 "z" count: 32
 lines with "and": 3
Аналізувати ще один файл? (y/n):
PS C:\Users\lookandhate\Desktop\nulp_trash>
```
## Запуск програми з консолі
```bash
python3 main.py
```


