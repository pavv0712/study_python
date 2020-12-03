# from model_movie2 import Movie2
# from adp_movie2 import Searchmovie
# from model_staff import Staff

# def MovieHtmlDetail(movies, staff):

#     for m in movies:
        
    
#         f = open('c:/python/새 폴더/새 영화/moviedetail/detail.html', 'w', encoding='utf8')
        
#         for d in staff:

#             tr_list_text = ''

#             td_text = '<td>{0}</td>'.format(d.k_name)
#             td_text += '<td>{0}</td>'.format(d.e_name)
#             tr_text = '<tr>{0}</tr>'.format(td_text)
#             tr_list_text += tr_text
#             f.write(tr_list_text)


#     f.close()






# def CreatemovieHtml(movie):

#     f = open('C:/python/새 폴더/새 영화/movies.html', 'w', encoding='utf8')
    
#     for m in movie:

#         tr_list_text = ''
#         a_link = '<a href={0}.html>{0}</a>'.format(m.code)
#         td_text = '<td>{0}</td>'.format(m.title)
#         td_text += '<td>{0}</td>'.format(a_link)
#         td_text += '<td>{0}</td>'.format(m.genre)
#         td_text += '<td><img src="{0}"></td>'.format(m.img_src)
#         tr_text = '<tr>{0}</tr>'.format(td_text)
#         tr_list_text += tr_text
#         tbody_text = '<tbody>{0}</tbody>'.format(tr_list_text)
#         table_text = '<table>{0}</table>'.format(tbody_text)
#         body_text = '<body>{0}</body>'.format(table_text)
#         html_text = '<html>{0}</html>'.format(body_text)
#         f.write(html_text)
#     f.close()

tu = (1,2,3,)

for t in tu:
    print(t)