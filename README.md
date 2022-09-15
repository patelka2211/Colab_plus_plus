# Colab plus plus

Run programs written in languages other than Python in Colab.

![](https://opengraph.githubassets.com/1/patelka2211/Colab_plus_plus)

## ⚙️ Setup

To setup Colab_plus_plus in your Jupyter Notebook first run this command in first cell.

```bash
# Setting up Colab_plus_plus environment
!curl https://raw.githubusercontent.com/patelka2211/Colab_plus_plus/main/Colab_plus_plus.py --output Colab_plus_plus.py

from Colab_plus_plus import Colab_plus_plus
```

## 🔥 Usage

Suppose you want to use Colab for C++ the below code is what you need.

```py
# Running C++ in Colab
cpp_file_obj = Colab_plus_plus('main.cpp')

cpp_file_obj.source_code('''
#include <bits/stdc++.h>
using namespace std;

int main()
{
    cout<<"Hello world"<<endl;
    return 0;
}
''')

!sh $cpp_file_obj.bash_file
```

```py
# Running JavaScript in Colab
js_file_obj = Colab_plus_plus('main.js')

js_file_obj.source_code('''
console.log('Hello world');
''')

!sh $js_file_obj.bash_file
```

`Also see which extensions you can use with which language.` click [here](./alternative-extensions.json) to know more.

## ⚡️ Example

Here is the example on [Colab](https://colab.research.google.com/drive/1GJnRiw_JkWBGbat7VjCzEAkJkSENBNLO?usp=sharing "Go to example").

## ✅ Supported languages

|  Language  | Support |
| :--------: | :-----: |
|    C++     |   ✅    |
| JavaScript |   ✅    |

## 📝 License

Copyright (c) [Kartavya Patel](https://github.com/patelka2211 "Kartavya Patel on Github"). All rights reserved.

Licensed under the [MIT](./LICENSE "See license") license.
