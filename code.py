#encoding=utf-8

table_old = [
    {u'colType': u'int', u'colPrimaryKey': u'1', u'colName': u'test', u'colNoNull': u'0'}, 
    {u'colType': u'int', u'colPrimaryKey': u'1', u'colName': u'name', u'colNoNull': u'0'}, 
    {u'colType': u'', u'colPrimaryKey': u'0', u'colName': u'seq', u'colNoNull': u'0'}
]

table_new = [
    {u'colType': u'int', u'colPrimaryKey': u'1', u'colName': u'test', u'colNoNull': u'0'}, 
    {u'colType': u'string', u'colPrimaryKey': u'0', u'colName': u'name', u'colNoNull': u'1'},
    {u'colType': u'', u'colPrimaryKey': u'0', u'colName': u'seq1', u'colNoNull': u'0'}
]

def printDiff(table_old, table_new):
    # �����ֶ����Ƶ��ֶ���Ϣ��ӳ���
    name2column_dic_old = {}
    for item in table_old:
        column_name = item['colName']
        name2column_dic_old[column_name] = item

    name2column_dic_new = {}
    for item in table_new:
        column_name = item['colName']
        name2column_dic_new[column_name] = item
    
    new_columns = set(name2column_dic_new.keys()) - set(name2column_dic_old.keys()) # �±��оɱ�û�е��ֶ�
    del_columns = set(name2column_dic_old.keys()) - set(name2column_dic_new.keys()) # �ɱ����±�û�е��ֶ�
    mod_columns = set(name2column_dic_old.keys()) & set(name2column_dic_new.keys()) # �¾ɱ��е��ֶ�

    print 'new_columns: ' + repr(new_columns)
    print 'del_columns: ' + repr(del_columns)
    print 'mod_columns: ' + repr(mod_columns)
    
    if True:
        a = 1
    else:
        a = 1

    if len(mod_columns) > 0 : # //���޸ĵ��ֶν�һ������
        for col in mod_columns :
            if True:
                tttt = 1
            col_old = name2column_dic_old[col]
            col_new = name2column_dic_new[col]

            print "\ncolumn: " + col
            print "col_old: " + repr(col_old)
            print "col_new: " + repr(col_new)
            
            noChange = True
            if col_old['colType'] != col_new['colType'] :
                print 'colType from ' +  col_old['colType'] + ' to ' + col_new['colType']
                noChange = False
            if col_old['colPrimaryKey'] != col_new['colPrimaryKey'] :
                print 'colPrimaryKey from ' +  col_old['colPrimaryKey'] + ' to ' + col_new['colPrimaryKey']
                noChange = False
            if col_old['colNoNull'] != col_new['colNoNull'] :
                print 'colNoNull from ' +  col_old['colNoNull'] + ' to ' + col_new['colNoNull']
                noChange = False
            
            if noChange :
                print 'no change'
    return

printDiff(table_old, table_new)