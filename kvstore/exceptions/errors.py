

class KVStoreError(Exception):
    ''' Base Exception for this whole project ''' 

class StorageError(Exception):
    ''' Base Exception for this whole project ''' 

class SerializationError(Exception):
    ''' Base Exception for this whole project ''' 

class KeyExpiredError(Exception):
    ''' Base Exception for this whole project ''' 

class KeyNotFoundError(Exception):
    ''' Base Exception for this whole project ''' 

class CacheFullError(Exception):
    ''' Base Exception for this whole project ''' 

class InvalidTTLError(Exception):
    ''' Base Exception for this whole project ''' 
