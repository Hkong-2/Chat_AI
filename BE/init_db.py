from database import engine, Base
# Cần import models để SQLAlchemy nhận diện được các bảng cần tạo
import models

def init_db():
    print("Đang tạo các bảng trong cơ sở dữ liệu...")
    # Lệnh này sẽ tạo toàn bộ các bảng đã được định nghĩa trong file models
    Base.metadata.create_all(bind=engine)
    print("Khởi tạo thành công!")

if __name__ == "__main__":
    init_db()
