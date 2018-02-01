# Сайт агенства недвижимости

Данный репозиторий содержит исправленный html шаблон сайта агенства недвижимости.   

# Демо сайт

[Демо версия сайта](https://igorzakhar.github.io/21_valid_markup/)

# HTML валидация

Исправлены ошибки полученные в ходе проверки через сервис [W3C Markup Validation Service](https://validator.w3.org/).

# Минификация js и css

Для минификации ```.css``` и ```.js``` файлов использовался скрипт ```minify.py``` основанный на запросах к api:  
Для ```.js``` файлов:
```
POST https://javascript-minifier.com/raw?input=...  
```

Для ```.css``` файлов.
```
POST https://cssminifier.com/raw?input=...
```

### Результаты минификации:
Файлы ```.js```  

| Файл           | До            | После |
| -------------- |:-------------:| -----:|
| jquery.js      | 276.1 KB | 93.0 KB |
| custom.js      | 1.2 KB      |   886.0 bytes |
| bootstrap.js   | 67.3 KB      |    35.8 KB |
| bootstrap.min.js | 36.0 KB      |    35.8 KB |


Файлы ```.css```  

| Файл           | До            | После |
| -------------- |:-------------:| -----:|
| bootstrap.css      | 142.6 KB | 114.2 KB |
| stylish-portfolio.css      | 3.4 KB      |   2.5 KB |
| bootstrap.min.css   | 118.4 KB      |    114.2 KB |


# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
