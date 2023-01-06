# Colab plus plus

You can now run programs written in different programming languages as well as Python in Colab. [View Notion page](https://kpverse.notion.site/Colab-f9eacc1c57334b1c86eed2798979dd44)

![](./Colab%2B%2B_by_KP.jpg)

<!-- ![](https://opengraph.githubassets.com/1/patelka2211/Colab_plus_plus) -->

## ⚙️ Setup

To setup Colab_plus_plus in your Jupyter Notebook first run this command in first cell.

```py
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

`Also see which extensions you can use with which language.` click [here](./language-extensions.json) to know more.

## ⬇ How to download

Example to download files

```py
cpp_file_obj.download()
```

## ⚡️ Example

Here is the example on [Colab](https://colab.research.google.com/github/patelka2211/Colab_plus_plus/blob/main/Colab%2B%2B.ipynb "Go to example") and or download [Jupyter Notebook](./Colab%2B%2B.ipynb) example.

## ✅ Supported languages

|  Language  | Support |
| :--------: | :-----: |
|    C++     |   ✅    |
|     C      |   ✅    |
|    Java    |   ✅    |
| JavaScript |   ✅    |

## 📝 License

Copyright (c) [Kartavya Patel](https://github.com/patelka2211 "Kartavya Patel on Github"). All rights reserved.

Licensed under the [MIT](./LICENSE "See license") license.
