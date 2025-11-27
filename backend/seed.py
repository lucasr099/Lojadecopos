from db import engine
from models import Base, Product
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)

products = [
    ("Copo Azul", "Copo de plástico azul", 12.90, 30),
    ("Copo Vermelho", "Copo vermelho brilhante", 11.50, 20),
    ("Copo Verde", "Copo verde translúcido", 12.00, 18),
    ("Copo Roxo", "Copo roxo premium", 13.50, 15),
    ("Copo Lilás", "Copo lilás suave", 12.20, 22),
    ("Copo Preto", "Copo preto elegante", 14.50, 30),
    ("Copo Laranja", "Copo laranja resistente", 12.90, 16),
    ("Copo Branco", "Copo branco clássico", 9.90, 50),
    ("Copo Cinza", "Copo cinza minimalista", 11.90, 27),
]

def seed():
    Base.metadata.create_all(bind=engine)  # garante as tabelas
    db = SessionLocal()

    for name, desc, price, stock in products:
        item = Product(name=name, description=desc, price=price, stock=stock)
        db.add(item)

    db.commit()
    db.close()
    print("🍀 Banco populado com sucesso!")

if __name__ == "__main__":
    seed()
