import uuid


from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, FLOAT

from app.common.db import Base


class WalletModel(Base):
    __tablename__ = 'wallets'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        primary_key=True,
        default_factory=uuid.uuid4
    )
    balance: Mapped[float] = mapped_column(
        FLOAT,
        nullable=False
    )

