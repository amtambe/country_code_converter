class IsoCountryConverter:
    """
    Read in iso csv file and convert isos to countries back and forth
    
    iso_path: path for a file containing ISO data. 1st column must be ISO code,
    2nd column must be country name. If not specified, it searches its own
    directory for a file titled "iso_country.csv" (this file is in this repo)
    """
    
    def __init__(self, iso_path=None):
        if iso_path is None:
            iso_path = os.path.join(os.path.split(os.path.abspath(__file__))[0], "iso_country.csv")
        
        self.__iso_dict__ = {}
        counter = 0
        try:
            with open(iso_path, mode='r', newline='') as infile:
                reader = csv.reader(infile)
                for row in reader:
                    counter += 1
                    self.__iso_dict__[row[0]] = row[1] 
        except Exception as e:
            warnings.warn("Failed to read dict: row {}".format(str(counter)))
            print(e)
        infile.close()

        self.__country_dict__ = {}
        for k in self.__iso_dict__.keys():
            self.__country_dict__[self.__iso_dict__[k]] = k

    def to_country(self, iso):
        return self.__iso_dict__[iso]

    def to_iso(self, country):
        return self.__country_dict__[country]
