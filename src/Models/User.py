from Models.BaseClasses.DatabaseModel import DatabaseModel
from Models.BaseClasses.EncryptableModel import EncryptableModel
from Models.BaseClasses.SerializeableModel import SerializeableModel


class User(EncryptableModel, DatabaseModel, SerializeableModel):
    ENCRYPTED_FIELDS = ['username', 'password', 'role', 'firstName', 'lastName', 'registrationDate']

    id: int = None
    username: str = None
    password: bytes = None
    role: str = None
    firstName: str = None
    lastName: str = None
    registrationDate: str = None  # String because this works easier with encryption
