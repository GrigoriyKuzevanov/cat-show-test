from fastapi import HTTPException, status


class KittenNotExistException(HTTPException):
    def __init__(self, kitten_id: int, headers: dict[str, str] | None = None) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = f"Kitten with id: {kitten_id} does not exist"
        super().__init__(self.status_code, self.detail, headers)
