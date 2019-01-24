from lmf.dbv2 import db_command




from os.path import join, dirname


import time

from zhulong.util.conf import get_conp,get_conp1


# 1
def task_baoshan(**args):
    conp = get_conp(baoshan._name_)
    baoshan.work(conp, **args)


# 2
def task_chuxiong(**args):
    conp = get_conp(chuxiong._name_)
    chuxiong.work(conp, **args)


# 3
def task_dali(**args):
    conp = get_conp(dali._name_)
    dali.work(conp,**args)


# 4
def task_lijiang(**args):
    conp = get_conp(lijiang._name_)
    lijiang.work(conp, **args)


# 5
def task_puer(**args):
    conp = get_conp(puer._name_)
    puer.work(conp , **args)



# 6
def task_tengchong(**args):
    conp = get_conp(tengchong._name_)
    tengchong.work(conp, **args)


# 7
def task_wenshan(**args):
    conp = get_conp(wenshan._name_)
    wenshan.work(conp, **args)




# 8
def task_yunnan(**args):
    conp = get_conp(yunnan._name_)
    yunnan.work(conp, **args)


# 9
def task_yuxi(**args):
    conp = get_conp(yuxi._name_)
    yuxi.work(conp, **args)


# 10
def task_zhaotong(**args):
    conp = get_conp(zhaotong._name_)
    zhaotong.work(conp, **args)


# 11
def task_lincang(**args):
    conp = get_conp(lincang._name_)
    lincang.work(conp ,**args)

def task_kunming(**args):
    conp = get_conp(kunming._name_)
    kunming.work(conp,**args)




def task_all():
    bg = time.time()
    try:
        task_baoshan()
        task_chuxiong()
        task_dali()
        task_lijiang()
        task_lincang()
    except:
        print("part1 error!")

    try:
        task_puer()
        task_tengchong()
        task_wenshan()
        task_yunnan()
        task_yuxi()


    except:
        print("part2 error!")

    try:
        task_zhaotong()
        task_kunming()
    except:
        print("part3 error!")


    ed = time.time()

    cos = int((ed - bg) / 60)

    print("共耗时%d min" % cos)


# write_profile('postgres,since2015,127.0.0.1,shandong')


def create_schemas():
    conp = get_conp1('yunnan')
    arr = ['baoshan','chuxiong','dali','lijiang','lincang','puer','tengchong','wenshan','yunnan','yuxi','zhaotong','kunming']
    for diqu in arr:
        sql = "create schema if not exists %s" % diqu
        db_command(sql, dbtype="postgresql", conp=conp)




