import requests
from bs4 import BeautifulSoup


def getArticleData(articleTag):
    data = {}
    try:
        publisherInfo = articleTag.select(".gs_a")[0].text
        citationInfo = articleTag.select(".gs_fl > a")[2].text

        data["title"] = articleTag.select(".gs_rt")[0].text
        data["year"] = int(publisherInfo.split("-")[-2].split(",")[-1].strip())
        data["abstract"] = articleTag.select(".gs_rs")[0].text
        data["citation"] = int(citationInfo.split(" ")[-1].strip())
    except Exception as ex:
        data["error"] = ex

    return data


def getScholarData(searchText):
    try:
        article_results = []
        searchText = searchText.replace(" ", "+")

        url = "https://scholar.google.com/scholar"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.361681261652"
        }
        params = {
            "hl": "en",
            "q": searchText,
        }

        response = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        for el in soup.select(".gs_r"):
            data = getArticleData(el)
            article_results.append(data)

    except Exception as ex:
        print("Fail to request for scholar data.")

    return article_results


def _printArticleInfo(articleList):
    for data in articleList:
        print(data["citation"])


searchText = "synthetic biology AND screening automation"
result = getScholarData(searchText)
# _printArticleInfo(result)
pass
