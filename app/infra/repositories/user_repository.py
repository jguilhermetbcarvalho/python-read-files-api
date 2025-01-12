from app.domain.models import User, UserScope
from app.dto import UserDTO
from app.exceptions import CreateUserException


class UserRepository:

    def __init__(self, session):
        self.session = session

    def create_user(self, params: UserDTO):
        fullname = params.fullname
        username = params.username
        password = params.password
        is_admin = params.is_admin
        scopes = params.scopes

        if not self.verify_user(username):
            try:
                new_user = User(fullname= fullname, username=username, password=password, is_admin=is_admin)
                self.session.add(new_user)
                self.session.flush()

                for scope in scopes:
                    new_scope = UserScope(user_id=new_user.id, scope_id=scope)
                    self.session.add(new_scope)

                self.session.commit()
                return self.get_user_by_username(username)

            except Exception as e:
                self.session.rollback()
                raise CreateUserException(f'Error creating user: {e}')
        else:
            raise CreateUserException(username)

    def verify_user(self, username: str) -> bool:
        user = self.session.query(User).filter_by(username=username).first()

        if user:
            return True
        else:
            return False

    def get_user_by_username(self, username: str) -> User | None:
        user = self.session.query(User).filter_by(username=username).first()

        if user:
            return user
        else:
            return None

    def check_user_is_admin(self, user_id) -> bool:
        user = self.session.query(User).filter_by(id=user_id).first()

        if user.is_admin:
            return True
        return False
