import requests
from bs4 import BeautifulSoup

class SkinScraper:
    """

    """

    def __init__(self):
        """

        """

        r = requests.get("https://valorant.fandom.com/wiki/Collection_Bundles")
        r.raise_for_status()
        self.soup = BeautifulSoup(r.text, 'html.parser')

    def get_skin_count(self):
        """
        Scrapes the Collection Bundles page's Table of Contents for newly released skins.
        :return: int value of number of released skins
        """

        unclean_released_list_ele = self.soup.find_all("a", href="#Released")[0].parent.ul
        clean_list = list(filter(lambda ele: ele != "\n", unclean_released_list_ele))

        return len(clean_list)

test = SkinScraper()
print(test.get_skin_count())