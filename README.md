# Тестовое задание от компании ItFox
## djnago_news веб приложение, где будут новости.

## Используемые технологии:
- Django/DRF (Backend)
- Docker/docker-compose
- Nginx
- Gunicorn

### **Build - Собрать проект**
```
docker-compose build
```
### **Run - Запуск проекта**
```
docker-compose up
```
### **Можно зарегистрировать полььзователя по ссылке:**
```
localhost/user/create/
```
### **Получить токен можно по ссылке:**
```
localhost/auth/
```
### **Можно запросить новый токен по ссылке:**
```
localhost/auth/refresh
```
### **Список новостей по ссылке:**
```
localhost/news/
```