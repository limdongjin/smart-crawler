from config.setting import config_selenium

category_map = {'selenium': config_selenium}


class ConfigReader:
    @classmethod
    def get(cls, category):
        config = category_map.get(category)
        return config
