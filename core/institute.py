
class Institute(object):
    def __init__(self, name):
        self._name = name
        self._freq_articles = 0
        self._research_fields = list()

    def add_freq_articles(self, increment):
        self._freq_articles += increment

    def get_freq_articles(self):
        return self._freq_articles

    def get_name(self):
        return self._name



class InstituteOccurance(object):
    def __init__(self, institute_a, institute_b):
        self._institute_a = institute_a
        self._institute_b = institute_b
        self._occurance = 1

    def get_occurance(self):
        return self._occurance

    def add_occurance(self, increment):
        self._occurance += increment

    def get_institute(self):
        return self._institute_a + ';' + self._institute_b