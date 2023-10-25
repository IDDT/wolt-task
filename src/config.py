import logging
import os


logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    force=True
)


REDIS_URI = os.getenv('REDIS_URI', 'redis://127.0.0.1:6379')
REDIS_EXPIRE_S = int(os.getenv('REDIS_EXPIRE_S', 300))


FILEPATHS = {
    'model_artifact': 'misc/model_artifact.json',
    'venue_preparation': 'misc/venue_preparation.csv'
}
