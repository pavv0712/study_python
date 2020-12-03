def createstockhtml(company_list):
    tr_list_text = ''
    for com in company_list:

        a_link = '<a herf="{0}.html">{0}</a>'.format(com.symbol)
        td_text = '<td>{0}</td>'.format(com.name)
        td_text += '<td>{0}</td>'.format(a_link)
        td_text += '<td>{0}</td>'.format(com.marketcap)
        td_text += '<td>{0}</td>'.format(com.ipoyear)
        tr_text = '<tr>{0}</tr>'.format(td_text)
        tr_list_text += tr_text

    table_text = '<table>{0}</table>'.format(tr_list_text)
    f = open('c:/python/finance/stocklist.html', 'w', encoding='utf8')
    f.write(table_text)
    f.close()

