import logging


logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    force=True
)


FILEPATHS = {
    'model_artifact': 'misc/model_artifact.json',
    'venue_preparation': 'misc/venue_preparation.csv'
}
