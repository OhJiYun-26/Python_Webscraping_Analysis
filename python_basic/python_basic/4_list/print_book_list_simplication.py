books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'A', '쪽수':248, '추천유무':True})

#비추코드

many_page_books = []
for book in books:
        if book['쪽수'] > 250:
            many_page_books.append(book['제목'])
print(many_page_books)


# 추천 코드
many_page = [book['제목'] for book in books if book['쪽수'] > 250]      # 쪽수 많은 책 리스트 만들기

print('쪽수가 250 쪽 넘는 책 리스트:', many_page)

print(type(many_page))
