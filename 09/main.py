"""main module"""
import sys
import logging.config
from lru import LRUCache


FLAG = False
PARAM = sys.argv
if '-s' in PARAM:
    FLAG = True

logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    format="%(asctime)s\t%(levelname)s\t%(message)s"
)

logger = logging.getLogger()

log_config = {
    "version": 1,
    "formatters": {
        "first": {
            "format": "%(levelname)s\t%(message)s",
        },
        "second": {
            "format": "%(message)s",
        }
    },
    "handlers": {
        "file": {
            "level": "NOTSET",
            "class": "logging.FileHandler",
            "filename": "example.log",
            "formatter": "first",
        },
        "stream": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "second",
        },
    },
    "loggers": {
        "my": {
             "handlers": ["stream"],
        },
    }
}

logging.config.dictConfig(log_config)
if FLAG:
    logger = logging.getLogger("my")

CACHE = LRUCache(100)

CACHE.set("k1", "val1")
logger.info("k1 set")
CACHE.set("k2", "val2")
logger.info("k2 set")

try:
    CACHE = LRUCache(-2)
except BufferError:
    logger.critical("negative size")

if CACHE.get("k3") is None:
    logger.error("there is no such element")

CACHE.set("k3", 10_000_001)
if CACHE.get("k3") > 10_000_000:
    logger.warning("very big number")

logger.debug("finished logging tests")
