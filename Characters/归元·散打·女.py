from PublicReference.base import *


class 主动技能(主动技能):
    def 等效CD(self, 武器类型,输出类型):
        return round(self.CD  / self.恢复, 1)    

class 归元·散打·女技能0(主动技能):
    名称 = '崩拳'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2485.356 
    成长 = 280.644 
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 5


class 归元·散打·女技能1(主动技能):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3569.925
    成长 = 403.075 
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.5


class 归元·散打·女技能2(主动技能):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3654.35 
    成长 = 412.65
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5


class 归元·散打·女技能3(被动技能):
    名称 = '柔化肌肉'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.125 + 0.015 * self.等级, 5)

class 归元·散打·女技能4(被动技能):
    名称 = '弱点感知'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级<=10:
                return round(1.01 + 0.01 * self.等级, 5)
            else :
                return round(1.11 + 0.02 * (self.等级-10), 5)

class 归元·散打·女技能5(主动技能):
    名称 = '寸拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8153.429
    成长 = 920.572 
    CD = 15
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09

class 归元·散打·女技能6(主动技能):
    名称 = '升龙拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 1762.0286
    成长 = 198.9714
    攻击次数=4
    基础2=1526.6286
    成长2=172.3714
    攻击次数2=1
    倍率 =  1.073
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 2.0


class 归元·散打·女技能7(主动技能):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1903.96875
    成长 = 215.03125
    攻击次数=7
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间=1
    是否有护石 = 1
    演出时间 = 2.2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.92
            self.攻击次数 += 2
            self.CD *= 0.85
            self.演出时间 = 2.7
        elif x == 1:
            self.倍率 *= 0.99
            self.攻击次数 += 2
            self.CD *= 0.85
            self.演出时间 = 2.7


class 归元·散打·女技能8(主动技能):
    名称 = '纷影连环踢'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 526.5
    成长 = 59.5
    攻击次数=10
    基础2=11692
    成长2=1320.166666
    攻击次数2=1 
    倍率 =  1.099
    CD = 40.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4
    

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.演出时间 = 4.4
            self.倍率 *= 0.87
            self.攻击次数 = 20
        elif x == 1:
            self.演出时间 = 4.4
            self.倍率 *= 0.98
            self.攻击次数 = 20

class 归元·散打·女技能9(主动技能):
    名称 = '武神强踢'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 37261*1.1*1.007253 
    成长 = 11248.5*1.1*1.007253
    CD = 145.0
    演出时间 = 0.5

class 归元·散打·女技能10(被动技能):
    名称 = '武神步'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.05 + 0.02 * self.等级, 5)


class 归元·散打·女技能11(主动技能):
    名称 = '破碎拳'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 18861.4546 
    成长 = 2129.5454
    CD = 30
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.19 + 0.09


class 归元·散打·女技能12(主动技能):
    名称 = '回天连环击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 2855.53
    成长 =322.470
    攻击次数=1
    基础2=26260.765
    成长2=2965.234
    攻击次数2=1
    CD = 50
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 *= 1.34
        elif x == 1:
            self.攻击次数 = 0
            self.攻击次数2 *= 1.34 + 0.08


class 归元·散打·女技能13(被动技能):
    名称 = '神武之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.22 + 0.02 * self.等级, 5)


class 归元·散打·女技能14(主动技能):
    名称 = '虎啸神拳'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 1581.4
    成长 =178.6
    攻击次数=15
    基础2 = 15453.2
    成长2 =1744.8
    攻击次数2=1
    基础3=4083.8667
    成长3=461.1333
    攻击次数3=1
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击次数 *= 2 * 0.83

class 归元·散打·女技能15(主动技能):
    名称 = '无影脚'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础=4892.76666 
    成长=646.233333 
    攻击次数=1
    基础2=2473.33333 + 2475.9 #第二段+第三段
    成长2=326.666666 + 327.1
    攻击次数2=1
    基础3=38686.4
    成长3=5109.6
    攻击次数3=1
    CD = 45.0
    是否有护石 = 1
    演出时间 = 2

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击次数 = 0
           self.攻击次数2 = 0
           self.攻击次数3 *= 1.66

class 归元·散打·女技能16(主动技能):
    名称 = '极尽霸皇断空拳'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 =87153.5 *1.006068
    成长 =26310.5 *1.006068
    CD = 180.0
    演出时间 = 1.2

class 归元·散打·女技能17(被动技能):
    名称 = '疾风劲'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 归元·散打·女技能18(主动技能):
    名称 = '雷霆之舞'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 95264.6
    成长 = 10754.4
    CD = 60.0
    演出时间 = 6.2

class 归元·散打·女技能19(主动技能):
    名称 = '真烈空星鸣拳'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    基础 = 259160
    成长 = 78240
    CD = 290
    def 加成倍率(self, 武器类型):
        return 0
    演出时间 = 6.1

#CDR: 拳套精通(10%) 
#不包含觉醒
class 归元·散打·女技能20(被动技能):
    名称 = '拳套精通'
    所在等级 = 15
    等级上限 = 10
    基础等级 = 10
    #拳套精通cd
    关联技能 = ['无']
    冷却关联技能 = ['崩拳','铁山靠','碎骨','寸拳','升龙拳','闪电之舞','纷影连环踢','破碎拳','回天连环击','虎啸神拳','无影脚','雷霆之舞']
    def 加成倍率(self, 武器类型):
        return 1.0
    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '拳套':
            if self.等级==0:
                return 1.0
            else :
                return (1 - 0.01 * self.等级)
        else:
            return 1.0
    #拳套自带全技能10cd
    冷却关联技能2 = ['所有']
    def CD缩减倍率2(self, 武器类型):
        if 武器类型 == '拳套':
            return 0.9
        elif 武器类型 == '臂铠':
            return 1.1
        else:
            return 1.0


#CDR 一觉cdr buff
class 归元·散打·女技能21(被动技能):
    名称='武神强踢buff'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    冷却关联技能 = ['所有']
    def CD缩减倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else :
            return 0.9

归元·散打·女技能列表 = []
i = 0
while i >= 0:
    try:
        exec('归元·散打·女技能列表.append(归元·散打·女技能' + str(i) + '())')
        i += 1
    except:
        i = -1

归元·散打·女技能序号 = dict()
for i in range(len(归元·散打·女技能列表)):
    归元·散打·女技能序号[归元·散打·女技能列表[i].名称] = i

归元·散打·女一觉序号 = 0
归元·散打·女二觉序号 = 0
归元·散打·女三觉序号 = 0
for i in 归元·散打·女技能列表:
    if i.所在等级 == 50:
        归元·散打·女一觉序号 = 归元·散打·女技能序号[i.名称]
    if i.所在等级 == 85:
        归元·散打·女二觉序号 = 归元·散打·女技能序号[i.名称]
    if i.所在等级 == 100:
        归元·散打·女三觉序号 = 归元·散打·女技能序号[i.名称]

归元·散打·女护石选项 = ['无']
for i in 归元·散打·女技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·散打·女护石选项.append(i.名称)

归元·散打·女符文选项 = ['无']
for i in 归元·散打·女技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·散打·女符文选项.append(i.名称)

class 归元·散打·女角色属性(角色属性):
    
    实际名称 = '归元·散打·女'
    角色 = '格斗家(女)'
    职业 = '散打'

    武器选项 = ['拳套', '臂铠']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.13

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(归元·散打·女技能列表)
        self.技能序号 = deepcopy(归元·散打·女技能序号)

    def CD倍率计算(self):
        if "武神强踢" in self.技能栏[self.技能序号['真烈空星鸣拳']].关联技能:
            self.技能栏[self.技能序号['武神强踢buff']].等级 = 0
        super().CD倍率计算()

class 归元·散打·女(角色窗口):

    def 窗口属性输入(self):
        self.初始属性 = 归元·散打·女角色属性()
        self.角色属性A = 归元·散打·女角色属性()
        self.角色属性B = 归元·散打·女角色属性()
        self.一觉序号 = 归元·散打·女一觉序号
        self.二觉序号 = 归元·散打·女二觉序号
        self.三觉序号 = 归元·散打·女三觉序号
        self.护石选项 = deepcopy(归元·散打·女护石选项)
        self.符文选项 = deepcopy(归元·散打·女符文选项)



