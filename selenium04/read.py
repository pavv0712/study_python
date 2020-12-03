import time
from model_finance import finance 



def createhtml(code):

    flis = list()

    f = open('c:/python/finance/{0}.csv'.format(code), 'r', encoding='utf8')

    for line in f.readlines()[1:]:
        items = line.split(',')
        _date, _open, _high, _low, _close, _adj_close, _volume = items
        fin = finance(code, _date, _open, _high, _low, _close, _adj_close, _volume)
        flis.append(fin)

    f.close()




    css_text = '''
         table {
                        border-collapse: collapse;
                    }
                    td, th {
                        border: 1px solid #cccccc; 
                        padding-left: 10px;
                        padding-right: 10px;
                        padding-top: 5px;
                        padding-bottom: 5px;
                    }
                    th {
                        background-color: #cce6ff
                    }

                    .main-div-style {
                        margin: 100px
                    }
                    .table-header-style {
                        margin-bottom:5px;
                        color:#777777;    
                    }
                    .nation-table-style {
                    }
                    .merge-td-style {
                        text-align: center;
                        background-color:#eeeeee;
                    }
                    .number-td-style {
                        text-align: right;
                        font-weight: bold;
                        width: 200px;
                    }

                    .flag-img-style {
                        width: 40px;
                        height: 20px;
                    }

                    .first-th-style {
                        padding: 20px;
                        font-size: 20px;
                        color: #ffffff;
                        background-color: #004080;
                    }
            '''
            
            
    style_text = '<style>{0}</style>'.format(css_text)
    head_text = '<head>{0}</head>'.format(style_text)
            
    th_text = '<th>코드</th>'
    th_text += '<th>날짜</th>'
    th_text += '<th>시가</th>'
    th_text += '<th>상한가</th>'
    th_text += '<th>하한가</th>'
    th_text += '<th>종가</th>'
    th_text += '<th>adj_close</th>'
    th_text += '<th>거래량</th>'
    th_list_text = '<tr>{0}</tr>'.format(th_text)
    thead_text = '<thead>{0}</thead>'.format(th_list_text)
            
    tr_list_text = ''
            
    for fli in flis:
            
                
        td_text = '<td>{0}</td>'.format(fli.code)

        td_text += '<td>{0}</td>'.format(fli.date)
                
        td_text += '<td>{0}</td>'.format(fli.open)

        td_text += '<td>{0}</td>'.format(fli.high)
                
        td_text += '<td>{0}</td>'.format(fli.low)
                
        td_text += '<td>{0}</td>'.format(fli.close)
            
        td_text += '<td>{0}</td>'.format(fli.adj_close)
                
        td_text += '<td>{0}</td>'.format(fli.volume)

        tr_text = '<tr>{0}</tr>'.format(td_text)

        tr_list_text += tr_text


    tbody_text = '<tbody>{0}</tbody>'.format(tr_list_text)
    table_text = '<table>{0}{1}</table>'.format(thead_text, tbody_text)
    body_text = '<body>{0}</body>'.format(table_text)
    html_text = '<html>{0}{1}</html>'.format(head_text, body_text)
                


    f = open('c:/python/finance/{0}.html'.format(code),'w', encoding = 'utf8')
            
    f.write(html_text)

    f.close()







