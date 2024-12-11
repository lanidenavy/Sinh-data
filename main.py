from faker import Faker
import random
from datetime import datetime

faker = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        document = {
            "_id": faker.uuid4(),
            "name": faker.sentence(nb_words=3),  # Tên món ăn
            "price": random.randint(10000, 100000),  # Giá tiền
            "tags": [faker.word(), faker.word()],  # Tags
            "favorite": faker.boolean(),  # Có yêu thích không
            "stars": random.randint(1, 5),  # Số sao
            "imageUrl": faker.image_url(),  # URL ảnh
            "origins": [faker.city()],  # Nguồn gốc
            "cookTime": str(random.randint(10, 300)),  # Thời gian nấu
            "createdAt": faker.date_time_between(start_date='-1y', end_date='now').isoformat(),
            "updatedAt": faker.date_time_between(start_date='-1y', end_date='now').isoformat(),
            "shop_id": random.randint(1, 10),  # ID shop
        }
        data.append(document)
    return data

# Tạo 10 tài liệu giả
fake_data = generate_fake_data(10)
for doc in fake_data:
    print(doc)
