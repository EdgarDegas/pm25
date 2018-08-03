from datetime import date

from . import datatool
from ..models import Query

def city_value_lst():
    # compare today & recent query date, create a flag
    today = date.today(); recent_query = Query.objects.last()

    if recent_query is None or not recent_query.date == today:
        # create a new query, use id of this new query
        query_id = Query.objects.create_query(date.today()).id
        return datatool.request_from_web(query_id)
    else:  # if recent_query_up_to_date
        query_id = recent_query.id
        return datatool.fetch_from_db(query_id)