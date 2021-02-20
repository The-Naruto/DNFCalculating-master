from math import *
from PublicReference.base import *

归元·气功师·男等级 = 100 + 5


# 武器手套
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '手套':
#             return round(self.CD / self.恢复 * 1.05, 1)


# 蓄念炮 618不变
class 归元·气功师·男技能0(被动技能):
    名称 = '蓄念炮'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    # 基础 = 159
    # 成长 = 6
    关联技能 = ['念气波：蓄念炮']

    def 加成倍率(self, 武器类型):
        return round(2.59 + 0.06 * self.等级, 5)


# 分身 618不变
class 归元·气功师·男技能1(主动技能):
    名称 = '分身'
    所在等级 = 5
    等级上限 = 20
    基础等级 = 10
    基础个数 = 0
    是否有伤害 = 0
    TP上限 = 0
    关联技能 = ['幻影爆碎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.基础个数 + self.等级), 5)


# 念之奥义
class 归元·气功师·男技能2(被动技能):
    名称 = '念之奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    # 增伤倍率 *= 1 + self.暴击伤害
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.055 + 0.015 * self.等级, 5)


# 二觉被动
class 归元·气功师·男技能3(被动技能):
    名称 = '风雷啸'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.11 + 0.02 * self.等级, 5)


# 禅意：万象
class 归元·气功师·男技能4(被动技能):
    名称 = '禅意：万象'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 基础精通
class 归元·气功师·男技能5(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    TP成长 = 0.1
    TP上限 = 3
    关联技能 = ['念兽：龙虎啸']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


# 幻影爆碎*=（分身个数+tp个数）
class 归元·气功师·男技能6(主动技能):
    名称 = '幻影爆碎'
    是否主动 = 0
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 基础等级 = 38
    # 基础 = 652
    # 成长 = 74
    数据 = [0, 728, 802, 876, 950, 1024, 1098, 1172, 1246, 1320, 1394, 1468, 1542, 1616, 1690, 1764, 1838, 1912, 1986,
          2059, 2133, 2207, 2281, 2355, 2429, 2503, 2577, 2651, 2725, 2799, 2873, 2947, 3021, 3095, 3169, 3243, 3317,
          3391, 3464, 3538, 3612, 3686, 3760, 3834, 3908, 3982, 4056, 4130, 4204, 4278, 4352, 4426, 4500, 4574, 4648,
          4722, 4796, 4870, 4944, 5018, 5092]

    CD = 12
    TP上限 = 5


    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率

    # def 等效CD(self, 武器类型):
    #     if 武器类型 == '手套':
    #         return round(self.CD * 1.05, 1)


# 念气波 数组
class 归元·气功师·男技能7(主动技能):
    名称 = '念气波'
    所在等级 = 15
    等级上限 = 60
    # 基础等级 = 46
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 基础 = 1301
    # 成长 = 145
    数据 = [0, 1432, 1577, 1723, 1868, 2013, 2159, 2304, 2449, 2595, 2740, 2885, 3030, 3176, 3321, 3466, 3612, 3757, 3902,
          4048, 4193, 4338, 4484, 4629, 4774, 4920, 5065, 5210, 5356, 5501, 5646, 5792, 5937, 6082, 6228, 6373, 6518,
          6664, 6809, 6954, 7100, 7245, 7390, 7535, 7681, 7826, 7971, 8117, 8262, 8407, 8553, 8698, 8843, 8989, 9134,
          9279, 9425, 9570, 9715, 9861, 10006]
    攻击次数 = 1
    CD = 2.6
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


# 念气波：蓄念炮 
class 归元·气功师·男技能8(主动技能):
    名称 = '念气波：蓄念炮'
    所在等级 = 15
    等级上限 = 60
    # 基础等级 = 46
    # 基础 = 1301
    # 成长 = 145
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1432, 1577, 1723, 1868, 2013, 2159, 2304, 2449, 2595, 2740, 2885, 3030, 3176, 3321, 3466, 3612, 3757,
           3902, 4048, 4193, 4338, 4484, 4629, 4774, 4920, 5065, 5210, 5356, 5501, 5646, 5792, 5937, 6082, 6228, 6373,
           6518, 6664, 6809, 6954, 7100, 7245, 7390, 7535, 7681, 7826, 7971, 8117, 8262, 8407, 8553, 8698, 8843, 8989,
           9134, 9279, 9425, 9570, 9715, 9861, 10006]
    攻击次数1 = 1
    数据2 = [0, 159, 175, 191, 207, 223, 239, 256, 272, 288, 304, 320, 336, 352, 369, 385, 401, 417, 433, 449, 465, 482,
           498, 514, 530, 546, 562, 578, 595, 611, 627, 643, 659, 675, 692, 708, 724, 740, 756, 772, 788, 805, 821, 837,
           853, 869, 885, 901, 918, 934, 950, 966, 982, 998, 1014, 1031, 1047, 1063, 1079, 1095, 1111]
    攻击次数2 = 1
    CD = 8.4
    TP成长 = 0.08
    TP上限 = 5

    #TP不加感电
    def 等效百分比(self, 武器类型):
       return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率 +(self.数据2[self.等级] * self.攻击次数2 * 0.07)  * self.倍率
       # return (self.数据2[self.等级] * self.攻击次数2*0.077) * self.倍率

# 念气罩
class 归元·气功师·男技能9(主动技能):
    名称 = '念气罩'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    基础 = 7700
    成长 = 0
    CD = 8
    TP上限 = 3


# 念气环绕
class 归元·气功师·男技能10(主动技能):
    名称 = '念气环绕'
    所在等级 = 20
    等级上限 = 35
    学习间隔 = 3
    等级精通 = 25
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 基础等级 = 25
    # 基础 = 48
    # 成长 = 8
    数据 = [0, 51, 59, 67, 76, 84, 92, 100, 108, 117, 125, 133, 141, 149, 158, 166, 174, 182, 190, 199, 207, 215, 223,
          231, 240, 248, 256, 264, 272, 281, 289, 297, 305, 313, 322, 330]
    攻击次数 = 1
    CD = 0.9
    关联技能 = ['念气环绕：御']
    关联技能2 = ['所有']


    def 加成倍率(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数  * self.倍率/100


    def 加成倍率2(self, 武器类型):
       if (self.等级 <= 25):
           return round(1.00 + 0.01 * self.等级, 5)
       else:
           return round(1.25 + 0.02 * (self.等级 - 25), 5)


# 念气环绕：袭 618改2秒演戏 遗漏
class 归元·气功师·男技能11(主动技能):
    名称 = '念气环绕：袭'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    # 基础 = 16854
    # 成长 = 367
    数据 = [0, 17219, 17586, 17954, 18321, 18688, 19056, 19423, 19791, 20158, 20526, 20893]
    攻击次数 = 1
    CD = 4.7
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数  * self.倍率


# 念气环绕：御  TP加算
class 归元·气功师·男技能12(主动技能):
    名称 = '念气环绕：御'
    所在等级 = 30
    等级上限 = 20
    # 基础等级 = 10
    # 基础 = 121
    # 成长 = 3
    学习间隔 = 2
    等级精通 = 10
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 128, 127, 130, 133, 136, 139, 142, 145, 148, 151, 154, 157, 160, 163, 166, 169, 172, 175, 178, 181]
    攻击次数 = 10
    CD = 1
    TP成长 = 4
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] + self.TP成长 * self.TP等级) * self.攻击次数


# 念兽：龙虎啸
class 归元·气功师·男技能13(主动技能):
    名称 = '念兽：龙虎啸'
    所在等级 = 30
    等级上限 = 35
    基础等级 = 25
    基础 = 1000
    成长 = 0
    CD = 1.0

    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if (self.等级 <= 22):
            return round(1.02 + 0.01 * self.等级, 5)
        else:
            return round(1.24 + 0.02 * (self.等级 - 22), 5)


# 狮子吼 618加强1.079 数组
class 归元·气功师·男技能14(主动技能):
    名称 = '狮子吼'
    所在等级 = 35
    等级上限 = 60
    # 基础等级 = 36
    # 基础 = 8156.8
    # 成长 = 916.8
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 5653, 6226, 6800, 7373, 7947, 8520, 9094, 9667, 10240, 10814, 11388, 11961, 12535, 13108, 13682, 14255,
          14829, 15402, 15976, 16549, 17123, 17696, 18270, 18843, 19417, 19990, 20564, 21138, 21711, 22285, 22858,
          23432, 24005, 24579, 25152, 25726, 26299, 26873, 27446, 28020, 28593, 29167, 29740, 30314, 30887, 31461,
          32034, 32608, 33181, 33755, 34328, 34902, 35475, 36049, 36622, 37196, 37769, 38343, 38917, 39490]
    攻击次数 = 1
    风雷啸 = 1.6
    CD = 17.9
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
        elif x == 1:
            self.倍率 *= 1.37

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸

# 螺旋念气场 618加强1.095
class 归元·气功师·男技能15(主动技能):
    名称 = '螺旋念气场'
    所在等级 = 40
    等级上限 = 60
    # 基础等级 = 33
    # 基础 = 12539.2
    # 成长 = 1414.4
    # 基础2 = 625.6#4390.4 * 1.095 # 940.8 测试3段
    # 成长2 = 67.2#470.4 * 1.095 # 100.8 测试3段
    # 攻击次数2 = 1
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 512, 564, 616, 668, 720, 772, 824, 876, 928, 980, 1032, 1084, 1136, 1188, 1240, 1293, 1345, 1397, 1449,
           1501, 1553, 1605, 1657, 1709, 1761, 1813, 1865, 1917, 1969, 2021, 2073, 2125, 2177, 2229, 2281, 2333, 2385,
           2437, 2489, 2541, 2593, 2645, 2697, 2749, 2801, 2853, 2905, 2957, 3009, 3061, 3113, 3165, 3217, 3269, 3321,
           3373, 3425, 3477, 3529, 3581]
    攻击次数1 = 17
    数据2 = [0,229,252,275,299,322,345,369,392,415,438,462,485,508,531,555,578,601,624,648,671,694,718,741,764,787,811,834,857,880,904,927,950,974,997,1020,1043,1067,1090,1113,1136,1160,1183,1206,1229,1252,1275,1298,1321,1344,1367,1390,1413,1436,1459,1482,1505,1528,1551,1574,1597]
    攻击次数2 = 1.5
    风雷啸 = 1.6
    CD = 21
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.09
            self.CD *= 0.83
        elif x == 1:
            self.倍率 *= 1.18
            self.CD *= 0.83

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸 + self.数据2[
            self.等级] * self.攻击次数2 * self.倍率* (1 + self.TP成长 * self.TP等级)


# 念兽：猛虎震地 618加强1.13，tp10，风雷60
class 归元·气功师·男技能16(主动技能):
    名称 = '念兽：猛虎震地'
    所在等级 = 45
    等级上限 = 60
    # 基础等级 = 31
    # 基础 = 21940.8
    # 成长 = 2459.2
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1896, 2089, 2281, 2474, 2666, 2859, 3051, 3243, 3436, 3628, 3821, 4013, 4206, 4398, 4591, 4783, 4975,
           5168, 5360, 5553, 5745, 5938, 6130, 6322, 6515, 6707, 6900, 7092, 7285, 7477, 7670, 7862, 8054, 8247, 8439,
           8632, 8824, 9017, 9209, 9401, 9594, 9786, 9979, 10171, 10364, 10556, 10748, 10941, 11133, 11326, 11518,
           11711, 11903, 12095, 12288, 12480, 12673, 12865, 13058, 13250]
    攻击次数1 = 4
    数据2 = [0, 7587, 8357, 9127, 9896, 10666, 11436, 12206, 12975, 13745, 14515, 15285, 16054, 16824, 17594, 18364, 19133,
       19903, 20673, 21443, 22212, 22982, 23752, 24522, 25291, 26061, 26831, 27601, 28370, 29140, 29910, 30680, 31449,
       32219, 32989, 33759, 34528, 35298, 36068, 36838, 37607, 38377, 39147, 39917, 40686, 41456, 42226, 42995, 43765,
       44535, 45305, 46074, 46844, 47614, 48384, 49153, 49923, 50693, 51463, 52232, 53002]
    攻击次数2 = 1
    风雷啸 = 1.6
    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.36
            self.风雷啸 = 1.44
        elif x == 1:
            self.倍率 *= 1.49
            self.风雷啸 = 1.44
    def 等效百分比(self, 武器类型):
         return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (
            1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸

# 念兽：审判之金雷虎-一觉
class 归元·气功师·男技能17(主动技能):
    名称 = '念兽：审判之金雷虎'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 54843
    成长 = 16550
    CD = 145


# 念之战矛  618加强1.122
class 归元·气功师·男技能18(主动技能):
    名称 = '念之战矛'
    所在等级 = 60
    等级上限 = 40
    # 基础等级 = 23
    # 基础 = 20768
    # 成长 = 2344
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 =  [0, 2888, 3181, 3474, 3767, 4060, 4353, 4646, 4939, 5232, 5525, 5818, 6111, 6404, 6697, 6990, 7283, 7576, 7869,
         8162, 8455, 8749, 9042, 9335, 9628, 9921, 10214, 10507, 10800, 11093, 11386, 11679, 11972, 12265, 12558, 12851,
         13144, 13437, 13730, 14023, 14316]
    攻击次数1 = 1
    数据2 = [0, 11553, 12725, 13897, 15070, 16242, 17414, 18586, 19758, 20930, 22102, 23274, 24446, 25619, 26791, 27963,
       29135, 30307, 31479, 32651, 33823, 34996, 36168, 37340, 38512, 39684, 40856, 42028, 43200, 44372, 45544, 46716,
       47888, 49060, 50232, 51404, 52576, 53748, 54920, 56092, 57264]
    攻击次数2 = 1
    风雷啸 = 1.6
    CD = 30
    TP成长 = 0.10
    TP上限 = 5


    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率* self.风雷啸


# 冲云念气场 618感电分离1次
class 归元·气功师·男技能19(主动技能):
    名称 = '冲云念气场'
    所在等级 = 70
    等级上限 = 40
    # 基础等级 = 18
    # 基础 = 28694.4
    # 成长 = 3244.8
    # 基础2= 584
    # 成长2= 67.2
    # 攻击次数2= 1
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 3330, 3668, 4005, 4343, 4681, 5019, 5357, 5695, 6033, 6370, 6708, 7046, 7384, 7722, 8060, 8397, 8735,
           9073, 9411, 9749, 10087, 10425, 10762, 11100, 11438, 11776, 12114, 12452, 12789, 13127, 13465, 13803, 14141,
           14479, 14817, 15154, 15492, 15830, 16168, 16506]
    攻击次数1 = 6
    数据2 = [0, 411, 453, 495, 536, 578, 620, 662, 703, 745, 787, 829, 870, 912, 954, 996, 1037, 1079, 1121, 1163, 1204, 1246,
       1288, 1330, 1371, 1413, 1455, 1497, 1538, 1580, 1622, 1664, 1705, 1747, 1789, 1831, 1872, 1914, 1956, 1997, 2039]
    攻击次数2 = 4.5
    风雷啸 = 1.674
    CD = 50
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
       # return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (
       #     1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸
        return self.数据1[self.等级] * self.攻击次数1  * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸 + self.数据2[self.等级] * self.攻击次数2* (1 + self.TP成长 * self.TP等级) * self.倍率


# 奔雷螺旋击 618加强1.074
class 归元·气功师·男技能20(主动技能):
    名称 = '奔雷螺旋击'
    所在等级 = 75
    等级上限 = 40
    # 基础等级 = 16
    # 基础 = 46472.16
    # 成长 = 5247.2
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 46179, 50864, 55549, 60234, 64919, 69604, 74289, 78974, 83659, 88343, 93028, 97713, 102398, 107083, 111768,
          116453, 121138, 125823, 130508, 135192, 139877, 144562, 149247, 153931, 158616, 163301, 167986, 172670,
          177355, 182040, 186725, 191409, 196094, 200779, 205464, 210148, 214833, 219518, 224202, 228887]
    攻击次数 = 1
    风雷啸 = 1.12
    CD = 44
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 2.02
            self.风雷啸 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸

# 月辉念气破 618加强1.075
class 归元·气功师·男技能21(主动技能):
    名称 = '月辉念气破'
    所在等级 = 80
    等级上限 = 40
    # 基础等级 = 13
    # 基础 = 54860
    # 成长 = 6200
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 6109, 6728, 7348, 7968, 8588, 9208, 9827, 10447, 11067, 11687, 12306, 12926, 13546, 14166, 14786, 15405,
          16025, 16645, 17265, 17885, 18505, 19125, 19745, 20365, 20985, 21605, 22225, 22845, 23465, 24085, 24705,
          25325, 25945, 26565, 27185, 27805, 28425, 29045, 29665, 30285]
    攻击次数 = 10
    CD = 45
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3
            self.cd = 0.9

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

# 月华万象-二觉
class 归元·气功师·男技能22(主动技能):
    名称 = '月华万象'
    所在等级 = 85
    等级上限 = 40
    # 基础等级 = 5
    # 基础 = 112750.8838
    # 成长 = 34039.7054
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 4447, 5479, 6510, 7542, 8574, 9605, 10637, 11668, 12700, 13731, 14763, 15794, 16826, 17857, 18889, 19920,
           20952, 21983, 23015, 24047, 25078, 26110, 27141, 28173, 29204, 30236, 31267, 32299, 33330, 34362, 35393,
           36425, 37456, 38488, 39519, 40551, 41582, 42614, 43645, 44677]
    攻击次数1 = 12
    数据2 = [0, 93415, 115076, 136738, 158399, 180061, 201722, 223383, 245045, 266706, 288368, 310029, 331691, 353352,
           375014,
           396675, 418336, 439998, 461659, 483321, 504982, 526644, 548305, 569966, 591628, 613289, 634951, 656612,
           678274,
           699935, 721596, 743258, 764919, 786581, 808242, 829904, 851565, 873226, 894888, 916549, 938211]
    攻击次数2 = 1
    CD = 180
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (
            1 + self.TP成长 * self.TP等级) * self.倍率

    # 禅语：形灭


class 归元·气功师·男技能23(主动技能):
    名称 = '禅语：形灭'
    所在等级 = 95
    等级上限 = 40
    # 基础等级 = 6
    # 基础 = 117321.7
    # 成长 = 13247
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 4080, 4494, 4908, 5322, 5736, 6150, 6564, 6978, 7392, 7806, 8220, 8634, 9048, 9462, 9876, 10290, 10704,
           11118, 11532, 11946, 12360, 12774, 13188, 13602, 14016, 14430, 14844, 15258, 15672, 16086, 16500, 16914,
           17328, 17742, 18156, 18570, 18984, 19398, 19812, 20226]
    攻击次数1 = 10
    数据2 = [0, 40806, 44945, 49085, 53225, 57365, 61504, 65644, 69784, 73923, 78063, 82203, 86343, 90482, 94622, 98762,
       102901, 107041, 111181, 115321, 119460, 123600, 127740, 131879, 136019, 140159, 144299, 148438, 152578, 156718,
       160857, 164997, 169137, 173276, 177416, 181556, 185695, 189835, 193974, 198114, 202254]
    攻击次数2 = 1
    风雷啸 = 1.6
    CD = 60.0


    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (
            1 + self.TP成长 * self.TP等级) * self.倍率 * self.风雷啸


# 禅念：归一
class 归元·气功师·男技能24(主动技能):
    名称 = '禅念：归一'
    所在等级 = 100
    等级上限 = 40
    # 基础等级 = 2
    # 基础 = 343382.3361
    # 成长 = 103689.33
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((归元·气功师·男等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 268255, 330459, 392663, 454867, 517071, 579275, 641479, 703683, 765887, 828091, 890295, 952499, 1014703,
           1076907, 1139111, 1201315, 1263519, 1325723, 1387927, 1450131, 1512335, 1574539, 1636743, 1698947, 1761151,
           1823355, 1885559, 1947763, 2009967, 2072171, 2134375, 2196579, 2258783, 2320987, 2383191, 2445395, 2507599,
           2569803, 2632007, 2694211]
    攻击次数1 = 1
    数据2 = [0, 29806, 36717, 43629, 50540, 57452, 64363, 71275, 78186, 85098, 92009, 98921, 105832, 112744, 119655, 126567,
       133478, 140390, 147301, 154213, 161124, 168036, 174947, 181859, 188770, 195682, 202593, 209505, 216416, 223328,
       230239, 237151, 244062, 250974, 257885, 264797, 271708, 278620, 285531, 292443, 299354]
    攻击次数2 = 6
    CD = 290.0
    关联技能 = ['无']


    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率
    def 加成倍率(self, 武器类型):
         return 0.0

归元·气功师·男技能列表 = []
i = 0
while i >= 0:
    try:
        exec('归元·气功师·男技能列表.append(归元·气功师·男技能' + str(i) + '())')
        i += 1
    except:
        i = -1

归元·气功师·男技能序号 = dict()
for i in range(len(归元·气功师·男技能列表)):
    归元·气功师·男技能序号[归元·气功师·男技能列表[i].名称] = i

归元·气功师·男一觉序号 = 0
归元·气功师·男二觉序号 = 0
归元·气功师·男三觉序号 = 0
for i in 归元·气功师·男技能列表:
    if i.所在等级 == 50:
        归元·气功师·男一觉序号 = 归元·气功师·男技能序号[i.名称]
    if i.所在等级 == 85:
        归元·气功师·男二觉序号 = 归元·气功师·男技能序号[i.名称]
    if i.所在等级 == 100:
        归元·气功师·男三觉序号 = 归元·气功师·男技能序号[i.名称]

归元·气功师·男护石选项 = ['无']
for i in 归元·气功师·男技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·气功师·男护石选项.append(i.名称)

归元·气功师·男符文选项 = ['无']
for i in 归元·气功师·男技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·气功师·男符文选项.append(i.名称)
        # 归元·气功师·男符文选项.append('幻影爆碎') #符文计算报错，被动技能没有倍率


class 归元·气功师·男角色属性(角色属性):
    实际名称 = '归元·气功师·男'
    角色 = '格斗家(男)'
    职业 = '气功师'

    武器选项 = ['手套']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.43
    BUFF属强 = 86

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(归元·气功师·男技能列表)
        self.技能序号 = deepcopy(归元·气功师·男技能序号)

    def 面板魔法攻击力(self):
        面板魔法攻击 = self.主BUFF * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻) * (
                1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try:
                面板魔法攻击 *= i.魔法攻击力倍率(self.武器类型)
            except:
                pass
        return 面板魔法攻击

    def 被动倍率计算(self):
        self.技能栏[self.技能序号['分身']].基础个数 = self.技能栏[self.技能序号['幻影爆碎']].TP等级
        super().被动倍率计算()

    def 伤害指数计算(self):
        self.光属性强化 += self.BUFF属强
        super().伤害指数计算()


class 归元·气功师·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元·气功师·男角色属性()
        self.角色属性A = 归元·气功师·男角色属性()
        self.角色属性B = 归元·气功师·男角色属性()
        self.一觉序号 = 归元·气功师·男一觉序号
        self.二觉序号 = 归元·气功师·男二觉序号
        self.三觉序号 = 归元·气功师·男三觉序号
        self.护石选项 = deepcopy(归元·气功师·男护石选项)
        self.符文选项 = deepcopy(归元·气功师·男符文选项)

    def 界面(self):
        super().界面()

        self.BUFF.move(self.BUFF.x() - 18, self.BUFF.y())
        self.BUFF输入.move(self.BUFF输入.x() - 20, self.BUFF输入.y())
        self.BUFF输入.resize(40, 25)

        self.BUFF输入2 = QLineEdit(self.main_frame2)
        self.BUFF输入2.setText(str(self.初始属性.BUFF属强))
        self.BUFF输入2.resize(40, 25)
        self.BUFF输入2.move(self.BUFF输入.x() + 45, self.BUFF输入.y())
        self.BUFF输入2.setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QLineEdit:hover{background-color:rgba(65,105,225,0.8)}")
        self.BUFF输入2.setAlignment(Qt.AlignCenter)



    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        try:
            self.BUFF光强 = int(self.BUFF输入2.text())
        except:
            self.BUFF光强 = self.初始属性.BUFF属强
