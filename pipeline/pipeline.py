from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from logging import getLogger,exception

logger = getLogger(__name__)

class AnimeRecommenadtionpipeline:
    def __init__(self,persist_dir = 'chroma_db'):
        try:
            logger.info('Initializing Recommendation pipeline')
            vector_bulider = VectorStoreBuilder(csv_path=" ",persist_dir=persist_dir)
            retriver = vector_bulider.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever=retriver,api_key=GROQ_API_KEY,model_name=MODEL_NAME)
            logger.info('Intilize the pipline successfully')

        except exception as e:
            logger.error(f'Failed to Initialize the pipeline {str(e)}')
            raise exception('Error During the pipeline Initialization',e)
        
    def recommand(self,query:str) ->str:
        try:
            logger.info(f"Recevied Query is {query}")
            recommandation = self.recommender.get_recommendation(query)
            logger.info(f'Recommendation generated successfully')
            return recommandation
        except exception as e:
            logger.error(f'Failed to get Recommandation {str(e)}')
            raise exception('Error During the getting the recommandation',e)
            