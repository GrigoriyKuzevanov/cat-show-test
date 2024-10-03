from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.core.database import Base

from . import Breed


class Kitten(Base):
    __tablename__ = "kitten"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    age_months: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    breed_id: Mapped[int] = mapped_column(
        ForeignKey("breed.id", ondelete="CASCADE"), nullable=False
    )
    breed: Mapped[Breed] = relationship("Breed", back_populates="kittens")
