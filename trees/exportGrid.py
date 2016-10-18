# -*- coding: cp936 -*-
import arcpy
import json
import os

def mkdir(path):
 
    # ȥ����λ�ո�
    path=path.strip()
    # ȥ��β�� \ ����
    path=path.rstrip("\\")
 
    # �ж�·���Ƿ����
    # ����     True
    # ������   False
    isExists=os.path.exists(path)
 
    # �жϽ��
    if not isExists:
        # ����������򴴽�Ŀ¼
        print path+' �����ɹ�'
        # ����Ŀ¼��������
        os.makedirs(path)
        return True
    else:
        # ���Ŀ¼�����򲻴���������ʾĿ¼�Ѵ���
##        print path+' Ŀ¼�Ѵ���'
        return False

arcpy.env.workspace = r"F:\data\tree\workspace"
gridlowshp = "F:/data/tree/gridlow.shp"
count = 0
gridlow = arcpy.da.SearchCursor(gridlowshp,('Id','SHAPE@','lon','lat'))
for grid in gridlow:
    mkpath='F:/data/tree/workspace/gridlowID_'+'%d'%grid[0]
    mkdir(mkpath)
    print('gridlowID_{0}:'.format(grid[0]))
    centerX = grid[1].centroid.X
    centerY = grid[1].centroid.Y
    gridTable = {}
    gridTable['gridID'] = grid[0]
    gridTable['centerX'] = centerX
    gridTable['centerY'] = centerY
    gridTable['lon'] = grid[2]
    gridTable['lat'] = grid[3]

    str = json.dumps(gridTable)
    gdfile = open(mkpath+'/gridTable.json','w')
    gdfile.write(str)
    print('Save to '+mkpath+'/gridTable.json')
    print(str)
    gdfile.close() 
    ##����������ڸõͳ߶��������г߶�tree����    
    gridmidshp = "F:/data/tree/gridmid2.shp"
    count2 = 0
    gridmid = arcpy.da.SearchCursor(gridmidshp,('Id','SHAPE@','lon','lat'),""""Id_1"={0}""".format(grid[0]))
    for grid in gridmid:
        mkpath2=mkpath+'/gridmidID_'+'%d'%grid[0]
        mkdir(mkpath2)
        print('\tgridmidID_{0}:'.format(grid[0]))
        centerX = grid[1].centroid.X
        centerY = grid[1].centroid.Y
        gridTable = {}
        gridTable['gridID'] = grid[0]
        gridTable['centerX'] = centerX
        gridTable['centerY'] = centerY
        gridTable['lon'] = grid[2]
        gridTable['lat'] = grid[3]

        str = json.dumps(gridTable)
        gdfile = open(mkpath2+'/gridTable.json','w')
        gdfile.write(str)
        print('Save to '+mkpath2+'/gridTable.json')
        print(str)
        gdfile.close()
        ##����������ڸ��г߶������¸߳߶�tree����    
        gridhighshp = "F:/data/tree/gridhigh2.shp"
        count3 = 0
        gridhigh = arcpy.da.SearchCursor(gridhighshp,('Id_1','SHAPE@','lon','lat'),""""Id"={0}""".format(grid[0]))
        for grid in gridhigh:
            mkpath3=mkpath2+'/gridhighID_'+'%d'%grid[0]
            mkdir(mkpath3)
            print('\t\tgridhighID_{0}:'.format(grid[0]))
            centerX = grid[1].centroid.X
            centerY = grid[1].centroid.Y
            gridTable = {}
            gridTable['gridID'] = grid[0]
            gridTable['centerX'] = centerX
            gridTable['centerY'] = centerY
            gridTable['lon'] = grid[2]
            gridTable['lat'] = grid[3]

            str = json.dumps(gridTable)
            gdfile = open(mkpath3+'/gridTable.json','w')
            gdfile.write(str)
            print('Save to '+mkpath3+'/gridTable.json')
            print(str)
            gdfile.close()
##            count3=count3+1
##            if count3>5:
##                break
##        count2=count2+1
##        if count2>5:
##            break
##    count=count+1
##    if count>5:
##        break


