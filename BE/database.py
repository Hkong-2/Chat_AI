import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Lấy chuỗi kết nối từ biến môi trường
# Mặc định sử dụng một connection string giả định để tránh lỗi nếu .env chưa được tạo
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/chat_db")

# Tạo engine kết nối tới PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tạo class SessionLocal để quản lý phiên kết nối
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Lớp cơ sở (Base class) cho tất cả các models kế thừa
Base = declarative_base()

# Dependency để lấy database session sử dụng trong FastAPI (khi nào bạn viết API sẽ dùng)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
