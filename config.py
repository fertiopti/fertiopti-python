import os

class Config:
    # MongoDB configuration
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://jijinjebanesh:XJdnv0shvUxXihqs@fertioptimizer.gjsww.mongodb.net/?retryWrites=true&w=majority&appName=FertiOptimizer")
