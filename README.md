temperature_database
===============

# Установка

### Перейти в каталог с настройками docker

```
cd docker/termometr-web-app-instances
```

### Создать файл конфигурации из примера

```
cp .env.sample .env
```

### Собрать контейнеры

```
./build
```

### Запустить контейнеры

```
./start
```

### Исполнить миграции

```
curl "http://localhost:82/?command=migration"
```

# Вызов методов из консоли

### Получение записей о температуре

```
curl "http://localhost:82/?command=site-database-pull"
```

### Добавление записи о температуре

```
curl -X POST "http://localhost:82/?command=put" -H "Content-Type: application/x-www-form-urlencoded" -d "user_id=1&temperature=36.6"
```
