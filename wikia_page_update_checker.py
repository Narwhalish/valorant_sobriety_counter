import requests
import dateutil.parser
import datetime

class WikiaPageUpdateChecker:
    """
    Main event loop for checking if the Wikia page has been recently updated.
    """

    def __init__(self):
        """
        Create member variable to locally store the live latest revision time.
        """

        self.stored_revision_time = self.get_lastest_revision_time()

    def get_lastest_revision_time(self):
        """
        Parses Wikia API to acquire live latest revision time of Collection Bundles page.
        :return: dateutil.dateutil instance of the live latest revision time
        """

        r = requests.get(
            "https://valorant.fandom.com/api.php?action=query&titles=Collection%20Bundles&prop=revisions&format=json")
        r.raise_for_status()
        tree = r.json()

        return dateutil.parser.parse(tree["query"]["pages"]["945"]["revisions"][0]["timestamp"])

    def check_for_update(self):
        """
        Compares stored latest revision time with the live latest revision time.
        :return: True if stored equals latest, False otherwise
        """

        return self.stored_revision_time == self.get_lastest_revision_time()

test = WikiaPageUpdateChecker()
print(datetime.datetime.now(datetime.timezone.utc) - test.get_lastest_revision_time())
print(test.check_for_update())
