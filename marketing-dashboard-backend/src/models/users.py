from dataclasses import dataclass

@dataclass
class Users:
    id: str
    username: str
    password: str  
    role: str      

    def is_admin(self) -> bool:
        return self.role.lower() == "admin"
