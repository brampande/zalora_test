import requests
from clint.textui import progress


class GCSHelpers:
    """
        Helpers related to GCS operation like download file and etc
    """

    @staticmethod
    def download_file_from_gcs_by_url(file_path: str, url: str) -> str:
        """
        :param file_path:
        :param url:
        :return:
        """

        local_file = file_path
        try:
            print(f'Downloading file from {url}')
            with requests.get(url, timeout=600, stream=True) as r:
                r.raise_for_status()
                with open(local_file, 'wb') as f:
                    total_length = int(r.headers.get('content-length'))
                    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                        f.write(chunk)
                        f.flush()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Can't do perform request get method with error {e}")

        return local_file

