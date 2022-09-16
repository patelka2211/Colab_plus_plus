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

import os
from google.colab import files
from zipfile import ZipFile


class Colab_plus_plus:
    def __init__(self, file_name):
        self.file_name = file_name.split('.')
        self.file_extension = self.file_name[-1]
        self.bash_file = f'{".".join(self.file_name[0:-1])}_{self.file_extension}.sh'
        self.file_name = '.'.join(self.file_name)
        self.error = False

    def __make_dir(self, folder_name):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

    def source_code(self, source):
        if self.file_extension in ['js']:

            self.folder_name = './JavaScript_codes'

            self.__make_dir(self.folder_name)

            with open("/".join([self.folder_name, self.file_name]), 'w', encoding='utf-8') as file:
                file.write(source)

            self.bash_file = '/'.join([self.folder_name, self.bash_file])

            with open(self.bash_file, 'w') as file:
                file.write(
                    f'node {"/".join([self.folder_name,self.file_name])}')

        elif self.file_extension in ['cpp', 'c++', 'c']:

            if self.file_extension in ['cpp', 'c++']:
                self.folder_name = './Cpp_codes'

            if self.file_extension in ['c']:
                self.folder_name = './C_codes'

            self.__make_dir(self.folder_name)

            with open("/".join([self.folder_name, self.file_name]), 'w', encoding='utf-8') as file:
                file.write(source)

            self.bash_file = '/'.join([self.folder_name, self.bash_file])

            with open(self.bash_file, 'w') as file:
                language = ''
                if self.file_extension in ['cpp', 'c++']:
                    language = 'cpp'
                else:
                    language = 'c'

                file.write(
                    f'g++ {"/".join([self.folder_name, self.file_name])} - o {"/".join(self.folder_name, f"{language}_output_file")} & & {"/".join(self.folder_name, f"{language}_output_file")}')

        elif self.file_extension in ['java']:

            self.folder_name = './Java_codes'

            self.__make_dir(self.folder_name)

            with open("/".join([self.folder_name, self.file_name]), 'w', encoding='utf-8') as file:
                file.write(source)

            self.bash_file = '/'.join([self.folder_name, self.bash_file])

            with open(self.bash_file, 'w', encoding='utf-8') as file:
                file.write(
                    f'''javac {'/'.join([self.folder_name,self.file_name])} && java -cp {self.folder_name} {self.file_name.split('.')[0:-1][0]}''')

        else:
            self.folder_name = './error'

            self.__make_dir(self.folder_name)

            self.bash_file = '/'.join([self.folder_name, 'error.sh'])

            with open(self.bash_file, 'w') as file:
                file.write(f'echo "\'.{self.file_extension}\' is not supported file extensions by \"Colab_plus_plus\" as of now."\necho "See supported file extensions at https://github.com/patelka2211/Colab_plus_plus#-supported-languages"\necho "or let me know what language you want to use, we will try to make it work if possible 🙌🏻. Just make a new issue at https://github.com/patelka2211/Colab_plus_plus/issues/new"')

            self.error = True

    def download(self):
        if not self.error:
            files.download("/".join([self.folder_name, self.file_name]))
        else:
            print('File can\'t download. There maybe some error in code.')
