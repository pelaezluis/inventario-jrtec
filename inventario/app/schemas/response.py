from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")

class ResponseBase(GenericModel, Generic[DataType]):
    message: str = ""
    data: Optional[DataType] = None

class GetResponse(ResponseBase[DataType], Generic[DataType]):
    message: str = "Data got correctly"

class PostResponse(ResponseBase[DataType], Generic[DataType]):
    message: str = "Data created correctly"

class PutResponse(ResponseBase[DataType], Generic[DataType]):
    message: str = "Data updated correctly"

class DeleteResponse(ResponseBase[DataType], Generic[DataType]):
    message: str = "Data deleted correctly"