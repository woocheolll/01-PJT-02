
import requests
# base_url = 'https://api.themoviedb.org/3'
# path = '/movie/76341'

def popular_count():
    params ={
        'api_key' : '0ab879f391429794c9400595a8749c11',
        'language' : 'ko-KR',

    }
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    response = requests.get(base_url+path, params=params).json().get('results')
    return len(response)

    # 여기에 코드를 작성합니다.  

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    
    # 20
    
    
    
#base_url =https://api.themoviedb.org/3/movie/76341?api_key=<<#0ab879f391429794c9400595a8749c11>>