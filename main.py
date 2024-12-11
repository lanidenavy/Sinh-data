import random
from faker import Faker
from datetime import datetime
import bson

# Khởi tạo Faker
faker = Faker()

# Danh sách các tags, xuất xứ và cặp tên món ăn - hình ảnh
tags = ["Canh cá", "Món ăn Việt", "Đặc sản", "Ẩm thực", "Bún", "Cơm"]
origins = ["Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Huế", "Thái Bình"]
dish_image_pairs =  [
    ("Phở Bò", "https://blog.onelife.vn/wp-content/uploads/2021/10/cach-lam-pho-bo-nam-mon-chinh-287846867397.jpg"),
    ("Bún Chả", "https://i1-giadinh.vnecdn.net/2021/01/08/Anh-2-8146-1610099449.jpg?w=0&h=0&q=100&dpr=2&fit=crop&s=a5Jo_jPDrhPaFGetZC6tlQ"),
    ("Bánh Mì", "https://i.ex-cdn.com/vntravellive.com/files/news/2023/05/15/luu-ngay-5-quan-banh-mi-ngon-nen-thu-tai-sai-gon-151953.jpg"),
    ("Gỏi Cuốn", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Summer_roll.jpg/330px-Summer_roll.jpg"),
    ("Bún Bò Huế", "https://i2.ex-cdn.com/crystalbay.com/files/content/2024/08/15/bun-bo-hue-2-0933.jpg"),
    ("Bánh Xèo", "https://www.huongnghiepaau.com/wp-content/uploads/2017/02/cach-lam-banh-xeo-mien-trung.jpg"),
    ("Cơm Tấm", "https://sakos.vn/wp-content/uploads/2024/10/bia-4.jpg"),
    ("Bánh Cuốn", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Banh_cuon.jpg/1024px-Banh_cuon.jpg"),
    ("Chả Giò", "https://cdn.tgdd.vn/Files/2017/03/28/965860/bi-quyet-lam-mon-cha-gio-vang-gion-thom-ngon-tai-nha-202205241601315587.jpg"),
    ("Bún Ngan", "https://dienmaynewsun.com/wp-content/uploads/2021/02/cach-nau-bun-ngan-mang-tuoi-1.jpg")
]

# Tạo danh sách các món ăn Việt Nam
vietnamese_dishes = []
for _ in range(995):
    dish_name, dish_image = random.choice(dish_image_pairs)
    dish = {
        "_id": { "$oid": str(bson.ObjectId()) },  # Định dạng ObjectId chuẩn
        "name": dish_name,
        "price": random.randint(10000, 200000),
        "tags": random.sample(tags, k=random.randint(1, 3)),
        "favorite": faker.boolean(),
        "stars": random.randint(1, 5),
        "imageUrl": dish_image,
        "origins": random.sample(origins, k=random.randint(1, 2)),
        "cookTime": str(random.randint(10, 120)),
        "createdAt": { "$date": faker.date_time_this_year().isoformat() },  # Định dạng ISODate
        "updatedAt": { "$date": datetime.now().isoformat() },  # Định dạng ISODate
        "shop_id": random.randint(1, 10)
    }
    vietnamese_dishes.append(dish)
import json
# In danh sách các món ăn Việt Nam
with open("vietnamese_dishes.txt", "w", encoding="utf-8") as f:
    for dish in vietnamese_dishes:
        # Ghi mỗi món ăn vào file dưới dạng chuỗi JSON với dấu nháy kép
        f.write(json.dumps(dish, ensure_ascii=False) + ",\n")
