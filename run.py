from app import app, db
import os

if __name__== "__main__":
    #cria Banco
    db.create_all()
    # executa a aplicação
    app.run(debug=True)
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
