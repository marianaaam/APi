from flaskr import create_app
from .modelos import db, Cancion
from .modelos import db, Usuario
from .modelos import db, Album

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba

with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Kiss')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    u = Usuario(nombre_usuario='Mariana', contrasena=123)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())

with app.app_context():
    a = Album(titulo='mix', año=123, descripcion='variedad de canciones')
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())