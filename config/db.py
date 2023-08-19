from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


def create_db_connection():
    global client_od
    client_od = AsyncIOMotorClient(f'mongodb://localhost:27017/')


def create_db_engine():
    engine = AIOEngine(client=client_od, database='orrs')
    return engine


def close_db_connection():
    client_od.close()