Упрощенный скрипт установки (setup.sh)
bash
#!/usr/bin/env bash
# Минимальная установка Docker и Docker Compose на Ubuntu

# Обновление системы
sudo apt-get update && sudo apt-get -y upgrade

# Установка необходимых утилит
sudo apt-get install -y \
    file \   # file ./docker/init/01_init.sql  # Должно показать "UTF-8 text"
    curl


# Установка зависимостей
sudo apt-get install -y curl git

# Установка Docker
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker ${USER}

# Установка Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Создание рабочей директории
sudo mkdir -p /var/projects
sudo chown -R $USER:$USER /var/projects

