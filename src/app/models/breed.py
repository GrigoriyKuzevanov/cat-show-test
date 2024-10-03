from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Breed(Base):
    __tablename__ = "breed"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    kittens: Mapped[list["Kitten"] | None] = relationship(
        "Kitten", back_populates="breed", cascade="all, delete"
    )
