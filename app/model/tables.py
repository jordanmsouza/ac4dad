from app import db
# crio a tabela Aluno
class Aluno(db.Model):
    __tablename__ = "tb_Ac4_jordan2"
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100))
    cep = db.Column(db.String(10))
    numero = db.Column(db.String(20))
    rua = db.Column(db.String(50))
    complemento = db.Column(db.String(120))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    uf = db.Column(db.String(10))

    def __init__(self, name, email, cep, rua, numero, complemento, bairro, cidade, uf):
        self.name = name
        self.email = email
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
