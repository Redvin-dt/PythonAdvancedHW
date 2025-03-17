# Описание дз
- lib: библиотека загруженная на PYPI
- scripts: скрипт который содержит библиотеку в dependency и генерирует тех файл
# Запуск докера под linux
```sh
    sudo docker build -t texgen_app -f artifacts/Dockerfile . # сборка docker image из корневой директории hw_2
    sudo docker container run -d --name mycontainer texgen_app sleep infinity # запуск контейнера который висит в sleep
    sudo docker exec -it mycontainer sh # подключение к контейнеру чтоб проверить что файлы собрались

    sudo docker stop mycontainer # остановка контейнера  
    sudo docker rm mycontainer  # удаление контейнера
```