import os
import requests

from settings import TOKEN


class YaUploader:
    def __init__(self, token: str) -> None:
        self.token = token

    def get_headers(self) -> dict:
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)

        return response.json()

    def upload(self, file_path: str, file_list: list) -> None:
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file_name in file_list:
            path = os.getcwd() + '/uploads/' + file_name
            href = self._get_upload_link(disk_file_path=file_path + '/' + file_name).get("href", "")
            response = requests.put(href, data=open(path, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'netology'  # каталог на диске
    token = TOKEN

    # Список файлов для загрузки из директории uploads
    file_list = [file for file in os.listdir('./uploads')]

    uploader = YaUploader(token)
    uploader.upload(file_path=path_to_file, file_list=file_list)
