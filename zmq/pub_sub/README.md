# PUB_SUB

## How to run

```bash
python pub_server.py # default: 5556
python pub_server.py 5557
python sub_client.py 5556 5557 # subscribe 2 publisher


# python sub_client.py 5557
```
## scenarios
### 一個subscriber可以訂閱多個publisher
### 多個subscriber可以訂閱同個publisher

## [ref](https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html)
