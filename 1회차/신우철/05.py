import requests
from pprint import pprint


def credits(title):
    base_url = 'https://api.themoviedb.org/3'
    path =  '/search/movie'
    params ={
        'api_key' : '0ab879f391429794c9400595a8749c11',
        'language' : 'ko-KR',
        'query':title
    }
    response = requests.get(base_url+path, params = params).json().get('results', None)
    
    if response == []:
        return None
    
    result_dict = {'cast':[], 'crew':[]}
    res_id = response[0].get('id')
    movie_id = res_id
    
    base_url2 = 'https://api.themoviedb.org/3'
    path2 =  f'/movie/{movie_id}/credits'
    params2 ={
        'api_key' : '0ab879f391429794c9400595a8749c11',
        'language' : 'ko-KR',
        'query':title
    }
    response2 = requests.get(base_url2+path2, params = params2).json()
    
    cast_list = response2.get('cast')
    crew_list = response2.get('crew')
    


    for actor in response2['cast']:
        if actor['cast_id'] < 10:
            result_dict['cast'].append(actor['name'])
    
    for crew in response2['crew']:      
        if crew['department'] == 'Directing':
            result_dict['crew'].append(crew['name'])
    return result_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
