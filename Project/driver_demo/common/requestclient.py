import requests


def httpClient(method, url, request):
    res = requests.request(
        method=method, url=url, **request
    )
    return res




if __name__ == '__main__':
    pass
