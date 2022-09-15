'''
MIT License

Copyright (c) 2022 Kartavya Patel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


class Colab_plus_plus:
    def __init__(self, file_name):
        self.file_name = file_name.split('.')
        self.file_extension = self.file_name[-1]
        self.bash_file = f'{".".join(self.file_name[0:-1])}_{self.file_extension}.sh'
        self.file_name = '.'.join(self.file_name)

    def source_code(self, source):
        if self.file_extension in ['js']:
            with open(self.file_name, 'w') as file:
                file.write(source)

            with open(self.bash_file, 'w') as file:
                file.write(f'node {self.file_name}')

        elif self.file_extension in ['cpp', 'c++']:
            with open(self.file_name, 'w') as file:
                file.write(source)

            with open(self.bash_file, 'w') as file:
                file.write(
                    f'g++ {self.file_name} -o cpp_output_file && ./cpp_output_file')
        else:
            self.bash_file = 'error.sh'
            with open(self.bash_file, 'w') as file:
                file.write(f'''echo "\'.{self.file_extension}\' is not supported file extensions by \"Colab_plus_plus\" as of now."
                echo "See supported file extensions at https://github.com/patelka2211/Colab_plus_plus#-supported-languages"
                echo "or let me know what language you want to use, we will try to make it work if possible 🙌🏻. Just make a new issue at https://github.com/patelka2211/Colab_plus_plus/issues/new"''')
