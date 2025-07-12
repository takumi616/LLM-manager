import uuid
from sqlmodel import Field, SQLModel, UniqueConstraint

class LargeLanguageModelBase(SQLModel):
    name: str = Field(nullable=False, max_length=50)
    provider: str = Field(nullable=False, max_length=50)
    model: str = Field(nullable=False, max_length=50)
    free: bool = Field(nullable=False)
    description: str | None = Field(default=None)


class LargeLanguageModel(LargeLanguageModelBase, table=True):
    __tablename__ = "large_language_models"

    __table_args__ = (UniqueConstraint("name", "model"), )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    status: str = Field(default="active", nullable=False)


class LargeLanguageModelPublic(LargeLanguageModelBase):
    id: uuid.UUID


class LargeLanguageModelCreate(LargeLanguageModelBase):
    pass