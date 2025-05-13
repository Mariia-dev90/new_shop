# Dockerfile

FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем библиотеки
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

#CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && yes | python manage.py search_index --rebuild && python manage.py runserver 0.0.0.0:8000"]



# Порт по умолчанию для Gunicorn
EXPOSE 8000

# Копируем скрипт запуска
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]