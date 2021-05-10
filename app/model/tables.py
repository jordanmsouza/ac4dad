from app import db
# crio a tabela cliente
class Cliente(db.Model):
    __tablename__ = "tb_Ac4_jordan"
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    comment = db.Column(db.String(120))
    email = db.Column(db.String(100))
    cep = db.Column(db.String(10))
    rua = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    uf = db.Column(db.String(10))
    numero = db.Column(db.String(20))

    def __init__(self, name, comment, email, cep, rua, bairro, cidade, uf, numero):
        self.name = name
        self.comment = comment
        self.email = email
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.numero = numero
