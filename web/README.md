# How to launch website

1) Stop all running containers:
    ```unix
    sudo docker rm -f $(sudo docker ps -a -q)
    ```

2) Spin up docker containers:
    ```unix
    sudo docker-compose up --detach
    ```

3) Enter docker container:
    ```unix
    sudo docker exec -it agile-web bash
    ```

4) Run `init_db.py` file:
    ```unix
    python init_db.py
    ```

## Note

If you want to delete MySQL completely(be in root directory of ECE-140B-Project):
```unix
sudo rm -rf db
```