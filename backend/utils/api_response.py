from dataclasses import dataclass

@dataclass 
class ApiResponse:
    status_code: int
    message: str
    data: dict | None=None
