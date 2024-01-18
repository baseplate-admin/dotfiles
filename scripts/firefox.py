import urllib.request

URL = "https://download.mozilla.org/?product=firefox-nightly-latest-ssl&os=linux64&lang=en-US"


def main():
    x = urllib.request.urlretrieve(URL)
    print(x[0])


if __name__ == "__main__":
    main()
