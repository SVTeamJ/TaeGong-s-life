from sqlalchemy.orm import Session
from schemas import history_schema
from model.history import History
from model.fish import Fish
from model.user import User
from starlette import status



'''
 데이터 베이스에 History 모델 추가


'''


def create_history(db:Session, history:history_schema.HistoryCreate):

    # create fish here
    db_history=History(
        user_id=history.user_id,
        fish_url=history.fish_url,
        fish_name=history.fish_name,
        fish_id=history.fish_id
    )
    db.add(db_history)
    db.commit()
    return db_history
    
def get_history(db:Session,user_id:int):
    
    '''
    유저의 history불러오기 위해 user_id로 history객체 여러개 반환
    
    parameter
    ---------
    db:Session
    user_id:특정 유저의 history를 불러올 때 입력받는 user_id
    
    return
    --------
    user_id가진 history 전부
    '''


    return db.query(History.user_id,History.fish_id, Fish.description,
                    Fish.fish_type,History.fish_url,Fish.scientific_name,
                    Fish.classification,Fish.habitat,Fish.toxicity)\
                    .outerjoin(Fish,History.fish_id == Fish.fish_id).filter(History.user_id == user_id).all()
