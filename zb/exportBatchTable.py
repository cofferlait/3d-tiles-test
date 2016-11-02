# -*- coding: cp936 -*-
import arcpy
import numpy
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
        print path+' Ŀ¼�Ѵ���'
        return False

arcpy.env.workspace = r"F:\data\ECNU"  
input = "F:/data/ECNU/zbbuilding_sj.shp"
table = arcpy.da.TableToNumPyArray(input,('full_id','name','int_name','building','gridID'))
##print(json.dumps(obj,indent=4))
gridNum = 122
for i in range(0,gridNum):
    gridmodels = table[table['gridID']==i]
    grid = '%d'%i
    batchTable = {}
    
    full_id = []
    name = []
    building = []
    int_name = []
    gridID = []
    
    mkpath='F:/data/ECNU/workspace/gridID_'+grid
    mkdir(mkpath)
    for row in gridmodels:
        full_id.append(row['full_id'])
        name.append(row['name'])
        building.append(row['building'])
        int_name.append(row['int_name'])
        gridID.append(int(row['gridID']))
        
    batchTable['full_id']=full_id
    batchTable['name']=name
    batchTable['building']=building
    batchTable['int_name']=int_name
    batchTable['gridID']=gridID

##    print(batchTable)
    str = json.dumps(batchTable,encoding="utf-8")

    btfile = open(mkpath+'/batchTable.json','w')
    btfile.write(str)
    btfile.close()



 
