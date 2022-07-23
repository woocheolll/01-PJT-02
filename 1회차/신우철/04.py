import requests
from pprint import pprint


def recommendation(title):
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
    
     
    res_id = response[0].get('id')
    movie_id = res_id
    
    base_url2 = 'https://api.themoviedb.org/3'
    path2 =  f'/movie/{movie_id}/recommendations'
    params2 ={
        'api_key' : '0ab879f391429794c9400595a8749c11',
        'language' : 'ko-KR',
        'query':title
    }
    response2 = requests.get(base_url2+path2, params=params2).json().get('results')

    titles = []
    for result in response2:
        titles.append(result.get('title'))

    if titles == []:
        return []
    else:
        return titles


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
