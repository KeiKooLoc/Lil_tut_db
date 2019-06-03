import db


def put__user_in_db():
    # try to catch exceptions
    try:
        # initialize database session
        session = db.Session()
        # Create a User class instance
        user = db.User(user_id=1234, first_name='Yura', last_name='Pit', username='@keikoobro')
        print(f'user_id of user object before adding to db: ->     {user.user_id}')

        # Place an object in the Session
        session.add(user)
        # add to db
        session.commit()
        # Find user which user_id = 1234
        user_from_db = session.query(db.User).filter_by(username='@keikoobro').first()

        print(f'User object from db ->'
              f'\n id ->         {user_from_db.id}'
              f'\n user_id ->    {user_from_db.user_id}'
              f'\n first_name -> {user_from_db.first_name}'
              f'\n last_name  -> {user_from_db.last_name}'
              f'\n username  ->  {user_from_db.username}')

        # find user
        u = session.query(db.User).filter_by(username='@keikoobro').first()
        # set new username
        u.username = '@newusername'
        # Place an object in the Session
        session.add(user)
        # add to db
        session.commit()

        # print all records in User table
        print('All RECORDS')
        for user in session.query(db.User).all():
            print(f'-' * 50 +
                  f'\n id ->         {user.id}'
                  f'\n user_id ->    {user.user_id}'
                  f'\n first_name -> {user.first_name}'
                  f'\n last_name  -> {user.last_name}'
                  f'\n username  ->  {user.username}')
    except Exception as e:
        print(e)


put__user_in_db()
