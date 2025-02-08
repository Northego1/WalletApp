from sqlalchemy.exc import IntegrityError



templates = {
    ''
}


class DatabaseErrorParser:
    @staticmethod
    def parse_integrity_error(error: IntegrityError) -> str:
        pass