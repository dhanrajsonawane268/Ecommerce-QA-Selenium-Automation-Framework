import configparser
from pathlib import Path

class ConfigReader:
    _config = None

    @classmethod
    def _load(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            cfg_path = Path(__file__).parent.parent / "config" / "config.ini"
            cls._config.read(cfg_path, encoding="utf-8")

    @classmethod
    def get(cls, section, key, fallback=None):
        cls._load()
        try:
            return cls._config.get(section, key, fallback=fallback)
        except Exception:
            return cls._config.get("DEFAULT", key, fallback=fallback)
