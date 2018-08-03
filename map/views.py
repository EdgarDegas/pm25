from django.shortcuts import render

from datetime import date

from .WeatherData import pm25
from .models import AQI, Query, City

def index(request):
    city_lst = ['海门', '鄂尔多斯', '招远', '舟山', '齐齐哈尔', '盐城', '赤峰', '青岛', '乳山', '金昌', '泉州', '莱西', '日照', '胶南', '南通', '拉萨', '云浮', '梅州', '文登', '上海', '攀枝花', '威海', '承德', '厦门', '汕尾', '潮州', '丹东', '太仓', '曲靖', '烟台', '福州', '瓦房店', '即墨', '抚顺', '玉溪', '张家口', '阳泉', '莱州', '湖州', '汕头', '昆山', '宁波', '湛江', '揭阳', '荣成', '连云港', '葫芦岛', '常熟', '东莞', '河源', '淮安', '泰州', '南宁', '营口', '惠州', '江阴', '蓬莱', '韶关', '嘉峪关', '广州', '延安', '太原', '清远', '中山', '昆明', '寿光', '盘锦', '长治', '深圳', '珠海', '宿迁', '咸阳', '铜川', '平度', '佛山', '海口', '江门', '章丘', '肇庆', '大连', '临汾', '吴江', '石嘴山', '沈阳', '苏州', '茂名', '嘉兴', '长春', '胶州', '银川', '张家港', '三门峡', '锦州', '南昌', '柳州', '三亚', '自贡', '吉林', '阳江', '泸州', '西宁', '宜宾', '呼和浩特', '成都', '大同', '镇江', '桂林', '张家界', '宜兴', '北海', '西安', '金坛', '东营', '牡丹江', '遵义', '绍兴', '扬州', '常州', '潍坊', '重庆', '台州', '南京', '滨州', '贵阳', '无锡', '本溪', '克拉玛依', '渭南', '马鞍山', '宝鸡', '焦作', '句容', '北京', '徐州', '衡水', '包头', '绵阳', '乌鲁木齐', '枣庄', '杭州', '淄博', '鞍山', '溧阳', '库尔勒', '安阳', '开封', '济南', '德阳', '温州', '九江', '邯郸', '临安', '兰州', '沧州', '临沂', '南充', '天津', '富阳', '泰安', '诸暨', '郑州', '哈尔滨', '聊城', '芜湖', '唐山', '平顶山', '邢台', '德州', '济宁', '荆州', '宜昌', '义乌', '丽水', '洛阳', '秦皇岛', '株洲', '石家庄', '莱芜', '常德', '保定', '湘潭', '金华', '岳阳', '长沙', '衢州', '廊坊', '菏泽', '合肥', '武汉', '大庆']

    # what we need: query_id, city_id, value

    # compare today & recent query date
    # with a flag: query_outdated
    today = date.today()
    recent_query = Query.recent_query()

    if recent_query is None:
        query_outdated = True
        query_id, _ = Query.create_new_query(date.today)

    else:
        recent_query_date = recent_query.date

        if recent_query_date == today:
            query_outdated = False
            query_id = recent_query.id

        elif recent_query_date < today:
            query_outdated = True
            query_id, _ = Query.create_new_query(date.today)

        else:
            raise Exception('Last query date > today. Might caused by timezone staff.')


    # need a list of dict anyway
    # do not add None value dicts into it
    city_value_lst = []


    if query_outdated is not True:
        aqi_records = AQI.fetch_by_query_id(query_id)

        for aqi_record in aqi_records:
            city_id = aqi_record.city_id
            city_name = City.fetch_by_id(city_id).name
            value = aqi_record.value

            if value is not None:
                city_value_lst.append({
                    'name' : city_name,
                    'value': value
                })



    else:  # if the recent query is outdated

        for city in city_lst:
            # get city_id, create one if not exists
            try:
                city_id = City.fetch_by_name(city).id
            except City.DoesNotExist:
                city_id, _ = City.create_new_city(city)
            except: continue

            # get aqi_pm25 value
            value = pm25.aqi_pm25(city)
            if value is not None:
                city_value_lst.append({
                    'name' : city,
                    'value': value
                })

            # create new aqi record and save
            new_record = AQI()
            new_record.city_id = city_id
            new_record.query_id = query_id
            new_record.value = value
            new_record.save()




    context = {
        'city_value_lst': city_value_lst
    }

    return render(request, 'map/index.html', context=context)