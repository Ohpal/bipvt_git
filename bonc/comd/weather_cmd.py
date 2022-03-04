import requests
import json
import datetime

weather_key = '%2Fpzii%2FnCk4v97X%2BC0lU4UjeGQZj7S3fvLqXTJIPzLlZb3ZSOlQs46YXTaGCstuzn60xPa8O2tEpEyI7noEGTEw%3D%3D'

site_list = ['아산']


# 현재시간 변환함수
def getDate(type):
    now = datetime.datetime.now()
    before = now - datetime.timedelta(minutes=10)

    if type == 'normal':
        now = now.strftime('%Y%m%d %H00').split(' ')
    elif type == 'thunder':
        now = before.strftime('%Y%m%d%H%M')

    return now


# 기상청 초단기실황 데이터 수집
def weather_korea(site):
    # try:
    nowMonth, nowTime = getDate('normal')
    nx, ny = find_site(site)
    weather_api = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={4}&numOfRows=10&pageNo=1&dataType=JSON&base_date={0}&base_time={1}&nx={2}&ny={3}'.format(
        nowMonth, nowTime, nx, ny, weather_key)
    headers2 = {'content-type': 'application/json;charset=utf-8'}
    tp = requests.get(weather_api, headers=headers2).text
    print('-1', tp)
    tp = json.loads(tp)

    print('0', tp)
    errCode = tp['response']['header']['resultCode']

    if errCode != '00':
        raise Exception('Weather Waiting...', errCode)

    items = tp['response']['body']['items']['item']

    print('1')
    weatherList = []
    search_date = date_changer(str(items[0]['baseDate']) + str(items[0]['baseTime']))
    weatherList.append(search_date)

    print('2')

    for item in items:
        category = item['category']
        val = item['obsrValue']
        nowWeather = {category: val}
        weatherList.append(nowWeather)

    return weatherList

    # except Exception as ex:
    #     print('weather_korea() Exception -> ', ex)


def find_site(site):
    if site == '아산':
        nx = 60
        ny = 110

    return nx, ny


# 날짜 변경 함수
def date_changer(data):
    try:
        if len(data) >= 12:
            year = data[0:4]
            month = data[4:6]
            day = data[6:8]
            hour = data[8:10]
            minute = data[10:12]

            result = '{0}-{1}-{2} {3}:{4}'.format(year, month, day, hour, minute)
        else:
            raise Exception

        return result
    except Exception as ex:
        print('date_changer() Exception -> ', ex)


# 데이터 패킷화
def weather_process(site):
    # try:
    weather = weather_korea(site)

    packet = [
        weather[0],
        site,
        weather[4]['T1H'],
        weather[2]['REH'],
        weather[1]['PTY'],
        weather[3]['RN1'],
        weather[6]['VEC'],
        weather[8]['WSD'],
    ]
    # print(packet)

    return packet
    # except:
    #     print('Waiting... for ', site)


if __name__ == '__main__':
    aa = weather_process(site_list[0])
    print(aa)
