from csv_handler import *
from crawler_api.siksin_api import *
from crawler_api.google_api import *
from crawler_api.naver_api import *
from crawler_api.diningcode_api import *
from preprocessing import *

# 다이닝코드 리뷰 크롤링 함수
def diningcode_crawling(path):
    # store_info 파일 읽어오는 함수 실행
    info_df = read_csv(path)
    # 다이닝코드 리뷰 크롤링 함수 실행
    link_df = diningcode_link(info_df)
    review_df_da = diningcode_review(link_df)
    # # csv 파일로 저장
    # save_csv(review_df_da, path, name)
    return review_df_da


# 구글 리뷰 크롤링 함수
def google_crawling(path):
    # store_info 파일 읽어오는 함수 실행
    info_df = read_csv(path)

    # 특정 가게만 지정할 때
    # info_df = info[1800:1900].reset_index(drop=True)

    # 리뷰데이터 크롤링
    storeInfo, review_df_go = google(info_df)

    # 영어리뷰 번역리뷰 제거
    review_df_go = google_eng_transfer_del(review_df_go)

    # csv 파일로 저장
    # save_csv(review_df_goo, path, name)

    return review_df_go

# 네이버 리뷰 크롤링 함수
def naver_crawling(path):
    return 1

def siksin_crawling(path):
    return 1