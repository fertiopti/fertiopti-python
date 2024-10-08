import os

class Config:
    # MongoDB configuration
    MONGO_URI = os.getenv("MONGO_URI", "")
