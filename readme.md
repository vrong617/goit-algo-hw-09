### Порівняння жадібного алгоритму та динамічного програмування для розв'язання задачі "Розбиття суми на монети"
## Опис завдання
У цьому проекті розроблені дві функції для касової системи, яка визначає оптимальний спосіб видачі решти покупцеві:

Жадібний алгоритм (Greedy Algorithm) — використовує підхід, при якому для кожної суми вибирається найбільший доступний номінал монети.
Алгоритм динамічного програмування (Dynamic Programming) — дозволяє знайти мінімальну кількість монет, необхідну для видачі решти, використовуючи метод динамічного програмування.
## Реалізовані функції
find_coins_greedy(amount):

Функція, яка повертає словник із номіналами монет та їх кількістю для формування суми, застосовуючи жадібний підхід.
Приклад: для суми 113 результатом буде {50: 2, 10: 1, 2: 1, 1: 1}.
find_min_coins(amount):

Функція, що реалізує динамічне програмування для знаходження мінімальної кількості монет для заданої суми.
Приклад: для суми 113 результатом буде {50: 2, 10: 1, 2: 1, 1: 1}.

## Порівняння алгоритмів
## Жадібний алгоритм
Часова складність: 
𝑂(𝑛), де 𝑛 — кількість монетних номіналів.
Переваги: швидке рішення, особливо на практиці для стандартних наборів монет.
Недоліки: не завжди гарантує мінімальну кількість монет для всіх наборів номіналів. Наприклад, при деяких специфічних наборах монет може вибирати неоптимальні шляхи.

## Динамічне програмування
Часова складність: 
𝑂(𝑛⋅𝑚) де 𝑛 — кількість номіналів монет, а 
𝑚 — сума, яку потрібно видати.
Переваги: завжди знаходить мінімальну кількість монет, навіть для складних випадків.
Недоліки: працює повільніше на великих значеннях суми через більшу обчислювальну складність.

## Висновки
Жадібний алгоритм добре підходить для ситуацій, де набір монет дозволяє отримати оптимальне рішення швидко, особливо для великих сум.
Алгоритм динамічного програмування забезпечує оптимальне рішення для будь-якого набору монет, але має більшу складність і споживає більше ресурсів для великих сум.
Для систем касових апаратів жадібний алгоритм може бути більш практичним через швидкість виконання, але для випадків з нестандартними наборами монет доцільніше використовувати динамічне програмування.
