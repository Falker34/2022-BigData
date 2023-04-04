# 2022-BigData
Рабочий репозиторий курсов "Большие данные" и "Интеллектуальный анализ данных"

Библиотеки для работы по Интеллектуальному анализу:

- [Pandas](https://pandas.pydata.org);
- [Matplotlib](https://matplotlib.org);
- [TensorFlow](https://www.tensorflow.org);
- [Keras](https://keras.io);

Презентация по курсу БД (обновляемая): https://docs.google.com/presentation/d/1xZ51nq1IWvccSrLzHo_QyaDQPvMBiWeUhoyPND-ARzo/edit?usp=sharing

Презентация по интеллектуальному анализу: https://docs.google.com/presentation/d/1rMirhHDHlBHSE8TmHPv4mUuaSaGsJ82O2CVv8BqwssI/edit?usp=sharing

Для работы необходим python 3.9 и выше.
Библиотеки: numpy, pandas, matplotlib, tensorflow, sklearn
Редактор любой. Из неплохих: IDLE (родной, идёт вместе с установщиком), Visual Studio Code, notepad++, PyCharm, vim (для любителей сначала страдать, потом наслаждаться)

Работа с блокнотами онлайн, с возможностью подключения удалённых мощностей гугла (GPU, TPU): https://colab.research.google.com/

Таблица, где я буду отмечать сданные работы: https://docs.google.com/spreadsheets/d/1uwrUXtU0zR_B6aV6mVqvk2tPqOVT76PW5CwtZ9rLoIk/edit?usp=sharing

Сервер в Дискорд, где буду дублировать: https://discord.gg/MzPkCYf4Dh
Мой контакт: nsmorozov@rf.unn.ru

В своей папке можете делать все что угодно, в чужие не залезать, в корневую тоже. Я буду ориентироваться на файлы, где в названии будет номер лабораторной.

## Интеллектуальный анализ
# [5] Построение модели по данным психических заболеваний

- сделать признаковое описание объекта: Age привести к нужным границам (не попадающие писать NaN); Gender оцифровать до 3; leave, no_employees, work_interfere привести к значениям по количеству уникальных;

- остальные бинарные признаки из текстовых сделать цифровыми, поля "not sure" пока заменить на NaN

1. провести статистический анализ данных (по всем полям вывести долю каждого варианта, дисперсию, среднее для возраста и т.д.)
2. выделить поля, по которым доля была выше мат.ожидания, потенциальные ключевые признаки наличия заболевания
3. построить графики для этих полей
4. используя теорему Байеса, проверить значимость не менее трех полей п.2 (да, формула получится страшноватой, но по сути она простая)

# [6] Обучение на основе изображений постеров фильмов

- загрузить обучающую и тренировочную выборки (соотношение 0.8 - 0.2);

- метки на плакаты брать из столбца "genres_list" (можно для проверки брать не жанры, а год выпуска);

- задать топологию сети;

- ...

-------------------------------------
<details>
  <summary># Задачи по сетям:</summary>

Выкладывать в свою же папку, но в отдельной подпапке

# [2] С использованием модуля socket создать чат:

- сервер на локальной машине, который ожидает запроса на соединение, создает отдельный поток, в котором все полученное по этому соединению пересылает по всему списку активных клиентов. Первое сообщение от клиента сохраняется как его псевдоним.

- клиент, который по указанному IP стучится к серверу, после чего может вводимую в отдельном потоке строку отправить. А все полученные строки во втором потоке (ожидающего данных от сервера) просто печатает.

Для референса: https://www.binarytides.com/code-chat-application-server-client-sockets-python/ ,
https://habr.com/ru/post/151623/

Рекомендую не копировать код, а писать самостоятельно.

# [3] Для игры из папки __ написать сетевой код:

- для игры вдвоем (один - "сервер", второй - "клиент"),

- каждый отправляет сопернику результат своего выбора,

- результат подсчитывается только после и получения выбора оппонента и после собственного,

- добавить справа небольшое окно чата,

- игровые сообщения и сообщения чата не должны мешать друг другу.
</details>
---------------------------------------
<details>
# [1] Симуляция HDFS

Дописать имплементации методов:

- разбиение пространства хостов на блоки;

- проверка количества репликаций и дозаписывание недостающих копий;

- обработку запроса "complete" от клиенгта;

- список блоков на каждой DataNode;

- методы DataNode для записи блоков: обновления статуса в списке, ответ на запрос "какие блоки хранишь" от NameNode (его тоже написать).

# [2] Простые случаи Map-Reduce

Для нескольких файлов с оценками какао посчитать количество суммарных упоминаний каждой из стран.

# [3] Сбор данных с сайта

Для https://royallib.com/ собрать информацию (название и год издания) о книгах жанра и сохранить в csv, в каждой строке Название, год:

1. Любовные романы

2. Религия и духовность

3. Справочная литература

4. Детское

5. Наука, Образование

Свой вариант определяется как:

len('Фамилия Имя Отчество') * (номер дня рождения, считая 27 ноября 1997 днем номер 0) % 5 + 1

# [4] Анализ текстовых данных

Для данных, полученных из предыдущего задания:

1. посчитать частоту слов с помощью map-reduce цепочек 

2. визуализировать результат диаграммой

3. обосновать и выделить значимые статистические параметры
</details>
