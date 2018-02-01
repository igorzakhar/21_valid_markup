import os

import requests


def get_list_of_files(directory):
    return os.listdir(directory)


def open_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


def save_file(file_path, response):
    with open(file_path, 'w') as file:
        file.write(response)


def minify(url, file_path):
    file_content = open_file(file_path)
    payload = {'input': file_content}
    response = requests.post(url, data=payload)
    save_file(file_path, response.text)


if __name__ == '__main__':
    dir_js = 'js/'
    dir_css = 'css/'
    api_js = 'https://javascript-minifier.com/raw'
    api_css = 'https://cssminifier.com/raw'
    list_js_files = list(map(lambda f: dir_js + f, os.listdir(dir_js)))
    list_css_files = list(map(lambda f: dir_css + f, os.listdir(dir_css)))
    list_all_files = [*list_js_files, *list_css_files]
    for filename in list_all_files:
        if filename.endswith('.css'):
            minify(api_css, filename)
        else:
            minify(api_js, filename)
