from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    # Sử dụng UUID làm khoá chính để bảo mật và tránh trùng lặp
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    title = Column(String, nullable=False, default="New Conversation")

    # Tự động lưu thời gian tạo và thời gian cập nhật
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationship với Message: 1 Session có nhiều Messages.
    # cascade="all, delete" đảm bảo khi xoá session thì tất cả message liên quan sẽ bị xoá
    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan")


class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    session_id = Column(String, ForeignKey("chat_sessions.id", ondelete="CASCADE"), nullable=False)

    # Phân biệt người gửi tin nhắn, ví dụ: 'user' hoặc 'ai'
    role = Column(String, nullable=False)

    # Nội dung tin nhắn
    content = Column(Text, nullable=False)

    # Thời gian tạo tin nhắn
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship ngược lại với Session
    session = relationship("ChatSession", back_populates="messages")
