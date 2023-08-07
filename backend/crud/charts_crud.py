from sqlalchemy.orm import Session
from model.history import History
from model.fish import Fish
from sqlalchemy import func

def get_charts(db: Session):
    """
    차트 정보 불러오는 API
    :param db:
    :return: fish_type, count(fish_id)
    아무것도 없을시 0으로 반환
    """
    # create an alias for the right table
    # right_table = aliased(Fish)

    # perform the right join
    # query = db.query(LeftTable).join(right_table, LeftTable.id == right_table.left_id, isouter=True)

    return db.query(Fish.fish_type,func.count(History.fish_id)).group_by(Fish.fish_type).group_by(History.fish_id).outerjoin(History,History.fish_id == Fish.fish_id)
