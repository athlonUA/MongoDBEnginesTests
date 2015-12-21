# MongoDB 3.2 Engines insert speed testing

OS: Ubuntu 14.04.3

CPU: Intel Core i5-3210M 2.5GHz

Interpreter: Python 2.7.6

MongoDB Connection Tools: Pymongo 3.2


| Engine      | Number of documents | Insert method      | time           |
| ----------- | ------------------- | ------------------ | -------------- |
| inMemory    | 1K                  | insert_one()       | 0:00:00.256019 |
| inMemory    | 10K                 | insert_one()       | 0:00:02.555137 |
| inMemory    | 100K                | insert_one()       | 0:00:25.371257 |
| inMemory    | 1M                  | insert_one()       | 0:04:25.501858 |
|             |                     |                    |                |
| wiredTiger  | 1K                  | insert_one()       | 0:00:00.262877 |
| wiredTiger  | 10K                 | insert_one()       | 0:00:02.622586 |
| wiredTiger  | 100K                | insert_one()       | 0:00:26.450679 |
| wiredTiger  | 1M                  | insert_one()       | 0:04:25.172383 |
|             |                     |                    |                |
| mmapv1      | 1K                  | insert_one()       | 0:00:00.258589 |
| mmapv1      | 10K                 | insert_one()       | 0:00:02.719752 |
| mmapv1      | 100K                | insert_one()       | 0:00:27.077982 |
| mmapv1      | 1M                  | insert_one()       | 0:04:21.461826 |
|             |                     |                    |                |
| inMemory    | 1K                  | insert_many()      | 0:00:00.025174 |
| inMemory    | 10K                 | insert_many()      | 0:00:00.223759 |
| inMemory    | 100K                | insert_many()      | 0:00:02.304617 |
| inMemory    | 1M                  | insert_many()      | 0:00:25.498137 |
|             |                     |                    |                |
| wiredTiger  | 1K                  | insert_many()      | 0:00:00.025317 |
| wiredTiger  | 10K                 | insert_many()      | 0:00:00.246260 |
| wiredTiger  | 100K                | insert_many()      | 0:00:02.494182 |
| wiredTiger  | 1M                  | insert_many()      | 0:00:27.500170 |
|             |                     |                    |                |
| mmapv1      | 1K                  | insert_many()      | 0:00:00.023795 |
| mmapv1      | 10K                 | insert_many()      | 0:00:00.219049 |
| mmapv1      | 100K                | insert_many()      | 0:00:02.322669 |
| mmapv1      | 1M                  | insert_many()      | 0:00:24.511715 |


***

##Insert method - insert_one()

- `insert_one results`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_one.png)

- `insert_one results - 1K (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_one_1K.png)

- `insert_one results - 10K (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_one_10K.png)

- `insert_one results - 100K (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_one_100K.png)

- `insert_one results - 1M (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_one_1M.png)

***

##Insert method - insert_many()

- `insert_many results`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_many.png)

- `insert_many results - 1K (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_many_1K.png)

- `insert_many results - 10K (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_many_10K.png)

- `insert_many results - 100K (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_many_100K.png)

- `insert_many results - 1M (scaling)`
![insert_one](https://raw.github.com/athlonUA/MongoDBEnginesTests/master/img/insertProcess/insert_many_1M.png)
