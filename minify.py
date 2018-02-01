import os

import requests


def get_list_of_files(dir):
    return os.listdir(dir)


def open_file(file):
    with open(file, 'rb') as file:
        return file.read()


def save_file(file, response):
    with open(file, 'w') as file:
        file.write(response)


def minify(url, file):
    # path = '{}{}'.format(dir, file)
    fp = open_file(file)
    data = {'input': fp}
    response = requests.post(url, data=data)
    save_file(file, response.text)


if __name__ == '__main__':
    dir_js = 'js/'
    dir_css = 'css/'
    api_js = 'https://javascript-minifier.com/raw'
    api_css = 'https://cssminifier.com/raw'
    list_js_files = list(map(lambda f: dir_js + f, os.listdir(dir_js)))
    list_css_files = list(map(lambda f: dir_css + f, os.listdir(dir_css)))
    list_all_files = [*list_js_files, *list_css_files]
    for file in list_all_files:
        if file.endswith('.css'):
            minify(api_css, file)
        else:
            minify(api_js, file)
