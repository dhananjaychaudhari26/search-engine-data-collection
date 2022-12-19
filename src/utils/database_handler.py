import pymongo
import os
import certifi
from dotenv import load_dotenv
load_dotenv()

class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(
                f"mongodb+srv://{os.getenv('ATLAS_CLUSTER_USERNAME')}:{os.getenv('ATLAS_CLUSTER_PASSWORD')}@cluster0.gi9pe2t.mongodb.net/?retryWrites=true&w=majority",
                tlsCAFile=certifi.where()
            )
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
