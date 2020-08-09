<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./static/icon.png" alt="Project logo" ></a>
 <br>

 
</p>

<h3 align="center">Memory Cache</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/da-huin/memory_cache.svg)](https://github.com/da-huin/memory_cache/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/da-huin/memory_cache.svg)](https://github.com/da-huin/memory_cache/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> It is a package that simply stores and uses a cache in memory.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

You can use following functions.

* [put](#put)
* [get](#get)

## 🏁 Getting Started <a name = "getting_started"></a>

### Installing

```
pip install memory_cache
```

### Tutorial

#### Execute the code below.

```python
import memory_cache
import time
import random

cache = memory_cache.MemoryCache()

cache_time = 10
working_time = 4
while True:
    print("\n=== Press any key to get started. ===")
    input()

    key = "fruit"
    data = cache.get(key)

    if data == None:
        print(f"working for {working_time} seconds ...")

        time.sleep(working_time)

        data = {"name": "apple", "price": "120"}
        cache.put(key, data, cache_time=cache_time)

        print("working complete!")
    else:
        print("cached!")

    print(data)
```

Execution Result:
```
=== Press any key to get started. ===

working for 3 seconds ...
working complete!
{'name': 'apple', 'price': '120'}

=== Press any key to get started. ===

cached!
{'name': 'apple', 'price': '120'}

=== Press any key to get started. ===

cached!
{'name': 'apple', 'price': '120'}

...
```

#### If open saved data, You can see that it is saved in the format below.

```python
{
    "value": {
        "name": "apple",
        "price": "120"
    },
    "cache_time": 10,
    "put_time": 1596727712.0505128
}
```

## 🎈 Usage <a name="usage"></a>

Please check [Prerequisites](#prerequisites) before starting `Usage`.

### 🌱 put <a name="put"></a>

**Parameters**

* `key`: str

    It is a key for storing data and finding data.

* `value`: any type

    The data to be saved.

* `cache_time`: int (default: -1)

    Cache time. If this value is -1, it is not cached

### 🌱 get <a name="get"></a>

**Parameters**

* `key`: str

    It is a key for storing data and finding data.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Title icon made by [Freepik](https://www.flaticon.com/kr/authors/freepik).

- If you have a problem. please make [issue](https://github.com/da-huin/memory_cache/issues).

- Please help develop this project 😀

- Thanks for reading 😄
