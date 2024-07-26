from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class BaseModel(DeclarativeBase):
  pass

class Feed(BaseModel):
  __tablename__ = "feeds"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(255))
  link: Mapped[str] = mapped_column(String(255))
  summary: Mapped[str] = mapped_column()
  
  def __repr__(self) -> str:
    return f"Feed(id={self.id!r}, title={self.title!r}, link={self.link!r}, summary={self.summary!r})"