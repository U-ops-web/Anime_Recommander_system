from src.vector_store import VectorStoreBuilder
from src.data_loader import AnimeDataLoader

from dotenv import load_dotenv
import logging
from logging import exception

load_dotenv()

logger = logging.getLogger(__name__)

def main():
    try:
        logger.info('Starting to build the vector store')
        loader = AnimeDataLoader(original_csv='C:/Users/IMMANUEL RAJ KUMAR/desktop/new folder (2)/myenv/Anime Recommander/Data/anime_with_synopsis.csv',processed_csv='C:/Users/IMMANUEL RAJ KUMAR/desktop/new folder (2)/myenv/Anime Recommander/Data/updated_synopsis.csv')
        processed_csv = loader.load_and_process()
        vector_store = VectorStoreBuilder(processed_csv)
        vector_store.bulid_and_save_vector_store()
        logger.info('Succesfully build the vector store')

    except exception as e:
            logger.error(f'Failed to create vector store {str(e)}')
            raise exception('Error During the creting the vector store',e)
            
if __name__ == "__main__":
     main()