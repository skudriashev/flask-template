from app.models import db, User


def create_dummy_data():
    user1 = User(
        first_name='User',
        last_name='One',
        email='user1@gmail.com',
    )
    db.session.add(user1)
    db.session.commit()


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    create_dummy_data()
