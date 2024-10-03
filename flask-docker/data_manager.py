from sqlalchemy.orm import sessionmaker

class DataManager:
    def __init__(self, session):
        self.session = session

    def fetch_data(self, model, keys):
        try:
            results = self.session.query(model).all()
            return [{key: getattr(result, key) for key in keys} for result in results]
        except Exception as e:
            return {"error": str(e)}
