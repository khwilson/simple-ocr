import os
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Config:
    tesseract_path: str = "tesseract"
    imagemagick_path: str = "convert"

    @classmethod
    def from_env(cls) -> Self:
        c = cls()
        return cls(
            tesseract_path=os.environ.get("IJF_TESSERACT_PATH", c.tesseract_path),
            imagemagick_path=os.environ.get("IJF_IMAGEMAGICK_PATH", c.imagemagick_path),
        )


_config: Config | None  = None


def get_config() -> Config:
    global _config
    if not _config:
        _config = Config()
    return _config


def set_config(cfg: Config):
    global _config
    _config = cfg


def set_config_from_env() -> Config:
    set_config(Config.from_env())
