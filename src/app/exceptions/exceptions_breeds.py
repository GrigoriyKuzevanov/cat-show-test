from fastapi import HTTPException, status


class BreedNotExistException(HTTPException):
    def __init__(self, breed_id: int, headers: dict[str, str] | None = None) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = f"Breed with id: {breed_id} does not exist"
        super().__init__(self.status_code, self.detail, headers)
