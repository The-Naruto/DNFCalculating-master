from PublicReference.base import *
from math import *

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '太刀':
#             return round(self.CD / self.恢复 * 1, 1)
#         if 武器类型 == '短剑':
#             return round(self.CD / self.恢复 * 1.05, 1)

class 极诣·鬼泣技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['鬼影步']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

class 极诣·鬼泣技能1(主动技能):
    名称 = '鬼斩'
    备注 = '(蓄力&噬灵鬼斩)'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 51
    CD = 6.0
    TP成长 = 0.08
    TP上限 = 5
    data1 = [0, 923, 1036, 1151, 1264, 1376, 1488, 1602, 1718, 1831, 1944, 2054, 2171, 2280, 2392, 2505, 2621, 2731, 2844, 2959, 3069, 3188, 3300, 3411, 3524, 3638, 3749, 3865, 3977, 4090, 4202, 4316, 4428, 4545, 4658, 4769, 4881, 4994, 5109, 5220, 5334, 5445, 5558, 5673, 5785, 5898, 6013, 6125, 6238, 6353, 6465, 6578, 6691, 6806, 6915, 7032, 7143, 7256, 7372, 7484, 7596, 7710, 7823, 7934, 8049, 8160, 8271, 8384, 8500, 8612, 8727]
    data2 = [0, 897, 1008, 1121, 1230, 1338, 1447, 1558, 1670, 1781, 1889, 1997, 2108, 2218, 2328, 2441, 2549, 2657, 2766, 2878, 2988, 3102, 3208, 3319, 3427, 3538, 3647, 3761, 3870, 3978, 4087, 4197, 4308, 4421, 4529, 4638, 4746, 4858, 4968, 5079, 5190, 5298, 5406, 5518, 5629, 5737, 5849, 5957, 6065, 6179, 6288, 6396, 6507, 6620, 6727, 6838, 6949, 7057, 7169, 7281, 7388, 7498, 7608, 7716, 7829, 7939, 8046, 8156, 8270, 8376, 8490]
    额外倍率 = 0 #噬灵鬼斩部分
    def 等效百分比(self, 武器类型):
        return self.倍率 * (self.data1[self.等级]* (1 + self.TP成长 * self.TP等级) + self.data2[self.等级] * self.额外倍率)

class 极诣·鬼泣技能2(被动技能):
    名称 = '刀魂之卡赞'
    是否主动 = 1
    所在等级 = 5
    等级上限 = 20
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04 + 0.01 * self.等级, 5)

class 极诣·鬼泣技能3(被动技能):
    名称 = '侵蚀之普戾蒙'
    是否主动 = 1
    所在等级 = 15
    等级上限 = 11
    基础等级 = 2
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.01 * self.等级, 5)

class 极诣·鬼泣技能4(被动技能):
    名称 = '太刀精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能 = ['所有']
    data = [0, 13, 28, 41, 54, 68, 82, 96, 109, 123, 137, 150, 164, 177, 191, 205, 219, 233, 245, 259, 273, 287, 301, 314, 328, 341, 355, 369, 382, 396, 410, 424, 437, 450, 464, 478, 492, 506, 520, 532, 546, 560, 574, 588, 601, 615, 628, 642, 656, 669, 683, 697, 711, 724, 737, 751, 765, 779, 793, 806, 819, 833, 847, 861, 874, 888, 902, 915, 929, 942, 956]
    
    def 加成倍率(self, 武器类型):
        if 武器类型 == '太刀':
            return self.data[self.等级] / 1000 + 1
        else:
            self.关联技能 = ['无']
            return 1.0

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 极诣·鬼泣技能5(被动技能):
    名称 = '短剑精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能 = ['所有']

    data = [0, 12, 26, 39, 51, 64, 77, 90, 103, 116, 129, 141, 154, 167, 180, 193, 206, 219, 231, 244, 257, 270, 283, 296, 309, 321, 334, 347, 360, 373, 386, 399, 411, 424, 437, 450, 463, 476, 489, 501, 514, 527, 540, 553, 566, 579, 591, 604, 617, 630, 643, 656, 669, 681, 694, 707, 720, 733, 746, 759, 771, 784, 797, 810, 823, 836, 849, 861, 874, 887, 900]
    
    def 加成倍率(self, 武器类型):
        if 武器类型 == '短剑':
            return self.data[self.等级] / 1000 + 1
        else:
            self.关联技能 = ['无']
            return 1.0

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 极诣·鬼泣技能6(被动技能):
    名称 = '暗月降临'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['无']

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '暗属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        if self.等级 <= 10:
            return round(self.等级 * 3)
        else:
            return round(30 + (self.等级-10) * 5)

class 极诣·鬼泣技能7(主动技能):
    名称 = '月光斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    CD = 4.0
    TP成长 = 0.08
    TP上限 = 5
    data1 = [0, 491, 539, 590, 640, 689, 739, 789, 838, 888, 939, 988, 1038, 1088, 1137, 1187, 1237, 1286, 1336, 1387, 1436, 1486, 1536, 1585, 1635, 1685, 1734, 1784, 1835, 1884, 1934, 1984, 2033, 2083, 2133, 2182, 2233, 2283, 2332, 2382, 2431, 2481, 2531, 2580, 2630, 2681, 2730, 2780, 2830, 2879, 2929, 2979, 3028, 3078, 3129, 3178, 3228, 3278, 3327, 3377, 3427, 3476, 3526, 3577, 3626, 3676, 3726, 3775, 3825, 3875, 3924]
    data2 = [0, 555, 612, 667, 724, 780, 837, 894, 950, 1007, 1062, 1119, 1175, 1231, 1288, 1344, 1401, 1456, 1513, 1569, 1625, 1681, 1738, 1795, 1851, 1908, 1965, 2020, 2077, 2133, 2190, 2245, 2302, 2359, 2414, 2471, 2527, 2584, 2639, 2696, 2753, 2809, 2866, 2923, 2979, 3035, 3091, 3148, 3205, 3260, 3317, 3373, 3429, 3485, 3542, 3599, 3654, 3711, 3767, 3824, 3881, 3937, 3994, 4049, 4106, 4162, 4218, 4275, 4331, 4388, 4443]
    data3 = [0, 780, 859, 939, 1017, 1097, 1175, 1254, 1334, 1414, 1492, 1572, 1651, 1729, 1809, 1887, 1967, 2047, 2126, 2204, 2284, 2363, 2442, 2521, 2601, 2681, 2758, 2838, 2917, 2996, 3076, 3154, 3234, 3313, 3391, 3471, 3551, 3629, 3709, 3788, 3866, 3946, 4025, 4105, 4184, 4263, 4343, 4421, 4500, 4580, 4658, 4738, 4818, 4896, 4975, 5055, 5133, 5213, 5292, 5371, 5451, 5529, 5608, 5688, 5767, 5847, 5925, 6005, 6083, 6162, 6242]
    数据 = [data1, data2, data3]
    次数 = [1, 1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率      

class 极诣·鬼泣技能8(主动技能):
    名称 = '鬼影步'
    备注 = '(一轮)'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 20
    基础 = 361
    成长 = 0
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 3

class 极诣·鬼泣技能9(被动技能):
    名称 = '噬灵鬼斩'
    所在等级 = 25
    等级上限 = 5
    基础等级 = 1
    关联技能 = ['无']

    def 加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(1.0 + 0.1 * self.等级, 5)

class 极诣·鬼泣技能10(主动技能):
    名称 = '鬼影鞭'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 945, 1097, 1248, 1398, 1549, 1701, 1851, 2002, 2153, 2305, 2454, 2606, 2757, 2907, 3058, 3208, 3360, 3510, 3662, 3812, 3963, 4114, 4265, 4416, 4567, 4717, 4869, 5019, 5171, 5321, 5472, 5623, 5773, 5925, 6074, 6226, 6377, 6528, 6678, 6830, 6981, 7131, 7282, 7434, 7583, 7735, 7886, 8037, 8187, 8339, 8490, 8640, 8791, 8942, 9092, 9243, 9395, 9546, 9696, 9847, 9999, 10148, 10300, 10451, 10601, 10752, 10904, 11054, 11205, 11356]
    data2 = [0, 2207, 2560, 2912, 3264, 3615, 3968, 4320, 4672, 5024, 5375, 5728, 6080, 6432, 6784, 7135, 7488, 7841, 8192, 8544, 8897, 9248, 9601, 9952, 10304, 10657, 11008, 11360, 11712, 12064, 12417, 12769, 13120, 13472, 13825, 14177, 14528, 14881, 15232, 15585, 15937, 16288, 16641, 16992, 17345, 17697, 18048, 18401, 18754, 19105, 19457, 19809, 20161, 20514, 20865, 21217, 21569, 21921, 22272, 22625, 22977, 23330, 23682, 24032, 24385, 24738, 25090, 25441, 25794, 26145, 26498]
    数据 = [data1, data2]
    次数 = [1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

class 极诣·鬼泣技能11(主动技能):
    名称 = '冰霜之萨亚'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 39
    CD = 15.0
    TP上限 = 5
    演出时间 = 5
    data = [0, 482, 531, 580, 629, 678, 726, 775, 824, 873, 922, 971, 1020, 1069, 1118, 1167, 1216, 1265, 1314, 1363, 1411, 1460, 1509, 1558, 1607, 1656, 1705, 1754, 1803, 1852, 1901, 1950, 1999, 2048, 2096, 2145, 2194, 2243, 2292, 2341, 2390, 2439, 2488, 2537, 2586, 2635, 2684, 2733, 2781, 2830, 2879, 2928, 2977, 3026, 3075, 3124, 3173, 3222, 3271, 3320, 3369, 3418, 3466, 3515, 3564, 3613, 3662, 3711, 3760, 3809, 3858]
    def 等效百分比(self, 武器类型):
        return (self.data[self.等级]) * ceil(10 / (1 - 0.07 * self.TP等级)) * self.倍率

class 极诣·鬼泣技能12(主动技能):
    名称 = '死亡墓碑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    CD = 18
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 402, 443, 484, 525, 566, 607, 648, 689, 729, 770, 811, 852, 893, 934, 975, 1016, 1056, 1097, 1138, 1179, 1220, 1261, 1302, 1343, 1383, 1424, 1465, 1506, 1547, 1588, 1629, 1670, 1710, 1751, 1792, 1833, 1874, 1915, 1956, 1997, 2037, 2078, 2119, 2160, 2201, 2242, 2283, 2324, 2364, 2405, 2446, 2487, 2528, 2569, 2610, 2651, 2691, 2732, 2773, 2814, 2855, 2896, 2937, 2978, 3018, 3059, 3100, 3141, 3182, 3223]
    数据 = [data1]
    次数 = [18]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

class 极诣·鬼泣技能13(主动技能):
    名称 = '瘟疫之罗刹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 37
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 5
    data1 = [0, 684, 753, 821, 892, 960, 1030, 1100, 1169, 1239, 1308, 1378, 1447, 1517, 1586, 1656, 1725, 1795, 1864, 1934, 2002, 2072, 2140, 2211, 2279, 2350, 2418, 2489, 2558, 2628, 2696, 2766, 2835, 2905, 2974, 3044, 3113, 3181, 3252, 3320, 3390, 3458, 3530, 3599, 3669, 3738, 3807, 3877, 3946, 4014, 4084, 4153, 4223, 4293, 4362, 4432, 4500, 4571, 4640, 4710, 4778]
    数据 = [data1]
    次数 = [10]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  
    
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.5 * 1.1 + 1.1 * 0.5 * 1.08
        elif x== 1:
            self.倍率 *= 0.5 * 1.1 + 1.1 * 0.5 * 1.24
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>无尽瘟疫</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[瘟疫之罗刹]<br>"
            temp += "施放时直接使罗刹分身附到敌人身上<br>"
            temp += "- 不设置召唤领域<br>"
            temp += "罗刹分身5秒内对附着的敌人造成持续伤害后爆炸<br>"
            temp += "- 多段攻击次数 -5次<br>"
            temp += "- 爆炸攻击力为腐蚀攻击力的500%<br>"
            temp += "腐蚀攻击力 +10%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "寻敌范围 +30%<br>"
            temp += "爆炸攻击力 +8%"
        elif x == 1:
            temp = "<font color='#FF00FF'>无尽瘟疫</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[瘟疫之罗刹]<br>"
            temp += "施放时直接使罗刹分身附到敌人身上<br>"
            temp += "- 不设置召唤领域<br>"
            temp += "罗刹分身5秒内对附着的敌人造成持续伤害后爆炸<br>"
            temp += "- 多段攻击次数 -5次<br>"
            temp += "- 爆炸攻击力为腐蚀攻击力的500%<br>"
            temp += "腐蚀攻击力 +10%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "寻敌范围 +30%<br>"
            temp += "爆炸攻击力 +24%"
        return temp  

class 极诣·鬼泣技能14(主动技能):
    名称 = '鬼斩：狂怒'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.5
    data1 = [0, 7746, 8532, 9318, 10103, 10889, 11675, 12461, 13247, 14033, 14819, 15604, 16390, 17176, 17962, 18748, 19534, 20320, 21106, 21891, 22677, 23463, 24249, 25035, 25821, 26607, 27392, 28178, 28964, 29750, 30536, 31322, 32108, 32893, 33679, 34465, 35251, 36037, 36823, 37609, 38395, 39180, 39966, 40752, 41538, 42324, 43110, 43896, 44681, 45467, 46253, 47039, 47825, 48611, 49397, 50182, 50968, 51754, 52540, 53326, 54112, 54898, 55683, 56469, 57255, 58041, 58827, 59613, 60399, 61185, 61970]

    数据 = [data1]
    次数 = [1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        self.演出时间 = 1.2
        if x == 0:
            self.倍率 *= 1.26
        elif x== 1:
            self.倍率 *= 1.35
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>灵魂呼啸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[鬼斩 : 狂怒]<br>"
            temp += "地面攻击后发动上斩， 生成对前方造成持续伤害的灵魂旋风<br>"
            temp += "- 灵魂旋风攻击力为[鬼斩 : 狂怒]攻击力的20%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "灵魂旋风命中时将敌人聚到中心<br>"
            temp += "灵魂旋风范围 +30%<br>"
            temp += "灵魂旋风攻击力 +6%"
        elif x == 1:
            temp = "<font color='#FF00FF'>灵魂呼啸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[鬼斩 : 狂怒]<br>"
            temp += "地面攻击后发动上斩， 生成对前方造成持续伤害的灵魂旋风<br>"
            temp += "- 灵魂旋风攻击力为[鬼斩 : 狂怒]攻击力的20%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "灵魂旋风命中时将敌人聚到中心<br>"
            temp += "灵魂旋风范围 +30%<br>"
            temp += "灵魂旋风攻击力 +15%"
        return temp  
        

class 极诣·鬼泣技能15(主动技能):
    名称 = '鬼影闪'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 6371, 7017, 7663, 8310, 8956, 9602, 10249, 10895, 11541, 12187, 12834, 13480, 14126, 14773, 15419, 16065, 16712, 17358, 18004, 18651, 19296, 19943, 20588, 21236, 21881, 22529, 23174, 23821, 24466, 25114, 25759, 26407, 27052, 27699, 28344, 28992, 29637, 30285, 30930, 31577, 32222, 32870, 33515, 34163, 34808, 35455, 36100, 36748, 37393, 38040, 38686, 39333, 39978, 40626, 41271, 41918, 42563, 43211, 43856, 44502, 45149, 45795, 46441, 47088, 47734, 48380, 49027, 49673, 50319, 50966]

    数据 = [data1]
    次数 = [1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

class 极诣·鬼泣技能16(主动技能):
    名称 = '冥炎之卡洛'
    备注 = '(一轮)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 32
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 209, 231, 252, 273, 294, 315, 337, 358, 380, 401, 421, 443, 464, 485, 507, 528, 549, 570, 592, 613, 635, 655, 676, 698, 719, 740, 762, 783, 803, 826, 846, 868, 889, 910, 931, 953, 975, 995, 1017, 1037, 1059, 1080, 1103, 1124, 1145, 1166, 1187, 1209, 1230, 1252, 1272, 1294, 1315, 1337, 1358, 1379, 1400, 1421, 1442, 1464, 1485, 1506, 1527, 1549, 1570, 1592, 1613, 1634, 1655, 1676]
    数据 = [data1]
    次数 = [3]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

class 极诣·鬼泣技能17(主动技能):
    名称 = '冥炎之卡洛(灼烧)'
    备注 = '(1秒3次)'
    所在等级 = 45
    等级上限 = 1
    基础等级 = 1
    CD = 1.0
    TP成长 = 0.10
    data1 = [0, 128, 142, 154, 167, 180, 193, 207, 219, 232, 245, 258, 271, 285, 298, 311, 323, 337, 351, 362, 376, 389, 402, 415, 428, 441, 454, 466, 480, 494, 505, 519, 532, 545, 558, 571, 584, 597, 610, 623, 636, 649, 663, 676, 689, 701, 715, 728, 740, 754, 767, 780, 792, 805, 819, 833, 844, 857, 870, 884, 897, 910, 923, 935, 948, 962, 975, 988, 1001, 1014, 1028]
    数据 = [data1]
    次数 = [3]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

class 极诣·鬼泣技能18(主动技能):
    名称 = '冥炎剑'
    所在等级 = 45
    等级上限 = 1
    基础等级 = 1
    CD = 45.0
    TP成长 = 0.10
    data1 = [0, 785, 865, 945, 1024, 1104, 1184, 1263, 1343, 1423, 1503, 1582, 1662, 1742, 1821, 1901, 1981, 2061, 2140, 2220, 2300, 2379, 2459, 2539, 2618, 2698, 2778, 2858, 2937, 3017, 3097, 3176, 3256, 3336, 3416, 3495, 3575, 3655, 3734, 3814, 3894, 3974, 4053, 4133, 4213, 4292, 4372, 4452, 4532, 4611, 4691, 4771, 4850, 4930, 5010, 5089, 5169, 5249, 5329, 5408, 5488, 5568, 5647, 5727, 5807, 5887, 5966, 6046, 6126, 6205, 6285]
    data2 = [0, 1151, 1268, 1385, 1502, 1619, 1736, 1852, 1969, 2086, 2203, 2320, 2437, 2553, 2670, 2787, 2904, 3021, 3138, 3255, 3371, 3488, 3605, 3722, 3839, 3956, 4072, 4189, 4306, 4423, 4540, 4657, 4774, 4890, 5007, 5124, 5241, 5358, 5475, 5591, 5708, 5825, 5942, 6059, 6176, 6293, 6409, 6526, 6643, 6760, 6877, 6994, 7110, 7227, 7344, 7461, 7578, 7695, 7812, 7928, 8045, 8162, 8279, 8396, 8513, 8629, 8746, 8863, 8980, 9097, 9214]
    data3 = [0, 2469, 2720, 2970, 3221, 3472, 3722, 3973, 4223, 4474, 4724, 4975, 5225, 5476, 5727, 5977, 6228, 6478, 6729, 6979, 7230, 7481, 7731, 7982, 8232, 8483, 8733, 8984, 9234, 9485, 9736, 9986, 10237, 10487, 10738, 10988, 11239, 11489, 11740, 11991, 12241, 12492, 12742, 12993, 13243, 13494, 13745, 13995, 14246, 14496, 14747, 14997, 15248, 15498, 15749, 16000, 16250, 16501, 16751, 17002, 17252, 17503, 17753, 18004, 18255, 18505, 18756, 19006, 19257, 19507, 19758]
    data4 = [0, 4012, 4419, 4826, 5233, 5640, 6047, 6454, 6861, 7268, 7675, 8082, 8489, 8896, 9303, 9710, 10117, 10524, 10931, 11338, 11745, 12152, 12559, 12966, 13373, 13780, 14187, 14594, 15001, 15408, 15815, 16222, 16629, 17036, 17443, 17851, 18258, 18665, 19072, 19479, 19886, 20293, 20700, 21107, 21514, 21921, 22328, 22735, 23142, 23549, 23956, 24363, 24770, 25177, 25584, 25991, 26398, 26805, 27212, 27619, 28026, 28433, 28840, 29247, 29654, 30061, 30468, 30875, 31282, 31689, 32096]
    数据 = [data1, data2, data3, data4]
    次数 = [2, 2, 2, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x== 1:
            self.倍率 *= 1.28
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>速效冥炎</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冥炎剑]<br>"
            temp += "施放时召唤冥炎剑立即斩击敌人<br>"
            temp += "斩击攻击范围 +30%<br>"
            temp += "斩击攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "按向前方向键时增加移动距离<br>"
            temp += "斩击攻击力 +9%"
        elif x == 1:
            temp = "<font color='#FF00FF'>速效冥炎</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冥炎剑]<br>"
            temp += "施放时召唤冥炎剑立即斩击敌人<br>"
            temp += "斩击攻击范围 +30%<br>"
            temp += "斩击攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "按向前方向键时增加移动距离<br>"
            temp += "斩击攻击力 +17%"
        return temp  

class 极诣·鬼泣技能19(被动技能):
    名称 = '恐惧光环'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 极诣·鬼泣技能20(主动技能):
    名称 = '第七鬼神：邪神怖拉修'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    CD = 140.0
    data1 = [0, 5301, 6530, 7758, 8988, 10218, 11446, 12677, 13905, 15135, 16364, 17592, 18822, 20052, 21281, 22509, 23739, 24968, 26197, 27426, 28656, 29885, 31114, 32345, 33573, 34802, 36032, 37260, 38490, 39719, 40949, 42177, 43407, 44636, 45865, 47094, 48324, 49553, 50782, 52012, 53241]
    data2 = [0, 7166, 8828, 10489, 12151, 13814, 15476, 17137, 18800, 20461, 22123, 23785, 25447, 27108, 28770, 30433, 32095, 33756, 35418, 37080, 38741, 40404, 42065, 43727, 45390, 47052, 48713, 50375, 52037, 53699, 55360, 57023, 58684, 60345, 62009, 63669, 65332, 66994, 68656, 70317, 71979]
    data3 = [0, 1427, 1759, 2088, 2419, 2751, 3082, 3413, 3744, 4075, 4406, 4737, 5068, 5400, 5729, 6060, 6392, 6723, 7053, 7385, 7716, 8047, 8378, 8709, 9041, 9370, 9701, 10033, 10364, 10694, 11026, 11357, 11688, 12019, 12350, 12682, 13011, 13342, 13675, 14005, 14335]
    数据 = [data1, data2, data3]
    次数 = [1.8, 1.8, 5]
    倍率 = 1.1
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

class 极诣·鬼泣技能21(主动技能):
    名称 = '鬼斩：炼狱'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 1024, 1128, 1232, 1336, 1440, 1544, 1648, 1752, 1856, 1960, 2064, 2168, 2272, 2376, 2480, 2584, 2688, 2792, 2896, 2999, 3103, 3207, 3311, 3415, 3519, 3623, 3727, 3831, 3935, 4039, 4143, 4247, 4351, 4455, 4559, 4663, 4767, 4871, 4975, 5079, 5183, 5287, 5391, 5495, 5598, 5702, 5806, 5910, 6014, 6118, 6222, 6326, 6430, 6534, 6638, 6742, 6846, 6950, 7054, 7158, 7262, 7366, 7470, 7574, 7678, 7782, 7886, 7990, 8094, 8197]
    data2 = [0, 3985, 4389, 4793, 5197, 5602, 6006, 6410, 6815, 7219, 7623, 8027, 8432, 8836, 9240, 9645, 10049, 10453, 10858, 11262, 11666, 12070, 12475, 12879, 13283, 13688, 14092, 14496, 14900, 15305, 15709, 16113, 16518, 16922, 17326, 17730, 18135, 18539, 18943, 19348, 19752, 20156, 20560, 20965, 21369, 21773, 22178, 22582, 22986, 23390, 23795, 24199, 24603, 25008, 25412, 25816, 26220, 26625, 27029, 27433, 27838, 28242, 28646, 29050, 29455, 29859, 30263, 30668, 31072, 31476, 31880]
    data3 = [0, 3415, 3762, 4108, 4455, 4801, 5148, 5495, 5841, 6188, 6534, 6881, 7227, 7574, 7920, 8267, 8613, 8960, 9306, 9653, 9999, 10346, 10692, 11039, 11386, 11732, 12079, 12425, 12772, 13118, 13465, 13811, 14158, 14504, 14851, 15197, 15544, 15890, 16237, 16584, 16930, 17277, 17623, 17970, 18316, 18663, 19009, 19356, 19702, 20049, 20395, 20742, 21088, 21435, 21782, 22128, 22475, 22821, 23168, 23514, 23861, 24207, 24554, 24900, 25247, 25593, 25940, 26286, 26633, 26980, 27326]
    数据 = [data1, data2, data3]
    次数 = [1, 2, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率     

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [1, 2, 1.21 * (1 + 0.09 * 5)]
            self.CD *= 0.9
        elif x== 1:
            self.次数 = [1, 2, 1.43 * (1 + 0.09 * 5)]
            self.CD *= 0.9
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>刺骨炼狱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[鬼斩 : 炼狱]<br>"
            temp += "冥界刀刃命中时， 对敌人附着持续造成伤害的冥炎<br>"
            temp += "冥炎对敌人造成多段伤害后爆炸并消失<br>"
            temp += "- 删除僵直功能<br>"
            temp += "- 爆炸攻击力为原僵直解除时的爆炸攻击力<br>"
            temp += "- 多段攻击力为爆炸攻击力的9%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冥炎爆炸攻击力 +21%<br>"
            temp += "冷却时间 -10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>刺骨炼狱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[鬼斩 : 炼狱]<br>"
            temp += "冥界刀刃命中时， 对敌人附着持续造成伤害的冥炎<br>"
            temp += "冥炎对敌人造成多段伤害后爆炸并消失<br>"
            temp += "- 删除僵直功能<br>"
            temp += "- 爆炸攻击力为原僵直解除时的爆炸攻击力<br>"
            temp += "- 多段攻击力为爆炸攻击力的9%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冥炎爆炸攻击力 +43%<br>"
            temp += "冷却时间 -10%"
        return temp  

class 极诣·鬼泣技能22(主动技能):
    名称 = '冥祭之沼'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 16391, 18055, 19718, 21380, 23044, 24707, 26371, 28033, 29696, 31358, 33022, 34684, 36347, 38011, 39673, 41336, 43000, 44663, 46326, 47989, 49651, 51315, 52978, 54640, 56304, 57966, 59629, 61293, 62956, 64618, 66282, 67945, 69607, 71271, 72933, 74596, 76259, 77922, 79586, 81249, 82912, 84575, 86238, 87900, 89564, 91226, 92889, 94551, 96215, 97878, 99542, 101205, 102867, 104531, 106193, 107856, 109519, 111182, 112846, 114508, 116171, 117835, 119498, 121160, 122824, 124486, 126149, 127813, 129475, 131138]
    数据 = [data1]
    次数 = [1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率    

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x== 1:
            self.倍率 *= 1.28
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>百鬼夜行</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冥祭之沼]<br>"
            temp += "墓碑爆炸时对周围队友施加鬼神之力， 10秒内增加10%的攻击速度<br>"
            temp += "爆炸攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "队友攻击速度 +5%<br>"
            temp += "爆炸攻击力 +9%"
        elif x == 1:
            temp = "<font color='#FF00FF'>百鬼夜行</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冥祭之沼]<br>"
            temp += "墓碑爆炸时对周围队友施加鬼神之力， 10秒内增加10%的攻击速度<br>"
            temp += "爆炸攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "队友攻击速度 +5%<br>"
            temp += "爆炸攻击力 +17%"
        return temp  

class 极诣·鬼泣技能23(被动技能):
    名称 = '御鬼之极'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.20 + 0.02 * self.等级, 5)

class 极诣·鬼泣技能24(主动技能):
    名称 = '幽魂之布雷德'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    CD = 40.0
    data1 = [0, 257, 283, 309, 335, 361, 387, 413, 439, 465, 492, 518, 544, 570, 596, 622, 648, 674, 700, 726, 753, 779, 805, 831, 857, 883, 909, 935, 961, 987, 1013, 1040, 1066, 1092, 1118, 1144, 1170, 1196, 1222, 1248, 1274, 1300, 1327, 1353, 1379, 1405, 1431, 1457, 1483, 1509, 1535, 1561, 1588, 1614, 1640, 1666, 1692, 1718, 1744, 1770, 1796, 1822, 1848, 1875, 1901, 1927, 1953, 1979, 2005, 2031, 2057]
    data2 = [0, 2862, 3153, 3443, 3734, 4024, 4315, 4605, 4895, 5186, 5476, 5767, 6057, 6348, 6638, 6929, 7219, 7509, 7800, 8090, 8381, 8671, 8962, 9252, 9542, 9833, 10123, 10414, 10704, 10995, 11285, 11576, 11866, 12156, 12447, 12737, 13028, 13318, 13609, 13899, 14190, 14480, 14770, 15061, 15351, 15642, 15932, 16223, 16513, 16803, 17094, 17384, 17675, 17965, 18256, 18546, 18837, 19127, 19417, 19708, 19998, 20289, 20579, 20870, 21160, 21450, 21741, 22031, 22322, 22612, 22903]
    data3 = [0, 16103, 17737, 19371, 21004, 22638, 24272, 25906, 27539, 29173, 30807, 32440, 34074, 35708, 37342, 38975, 40609, 42243, 43876, 45510, 47144, 48778, 50411, 52045, 53679, 55313, 56946, 58580, 60214, 61847, 63481, 65115, 66749, 68382, 70016, 71650, 73283, 74917, 76551, 78185, 79818, 81452, 83086, 84719, 86353, 87987, 89621, 91254, 92888, 94522, 96155, 97789, 99423, 101057, 102690, 104324, 105958, 107591, 109225, 110859, 112493, 114126, 115760, 117394, 119028, 120661, 122295, 123929, 125562, 127196, 128830]
    数据 = [data1, data2, data3]
    次数 = [8 * 4, 4, 1]
    解放 = 1
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i] * (self.解放 if i == 0 else 1)
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率      

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [6 * 4, 4 * 1.61, 1.41]

class 极诣·鬼泣技能25(主动技能):
    名称 = '幽魂降临：式'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    CD = 45.0
    data1 = [0, 14285, 15734, 17183, 18633, 20082, 21531, 22980, 24430, 25879, 27328, 28777, 30227, 31676, 33125, 34574, 36024, 37473, 38922, 40371, 41821, 43270, 44719, 46168, 47618, 49067, 50516, 51965, 53415, 54864, 56313, 57762, 59212, 60661, 62110, 63559, 65009, 66458, 67907, 69356, 70806]
    data2 = [0, 21428, 23602, 25775, 27949, 30123, 32297, 34471, 36645, 38819, 40992, 43166, 45340, 47514, 49688, 51862, 54036, 56210, 58383, 60557, 62731, 64905, 67079, 69253, 71427, 73600, 75774, 77948, 80122, 82296, 84470, 86644, 88818, 90991, 93165, 95339, 97513, 99687, 101861, 104035, 106209]
    数据 = [data1, data2]
    次数 = [1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率     

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34

class 极诣·鬼泣技能26(主动技能):
    名称 = '王者号令：吉格降临'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    CD = 180.0
    data1 = [0, 13195, 16255, 19314, 22374, 25434, 28494, 31553, 34613, 37673, 40733, 43793, 46852, 49912, 52972, 56032, 59091, 62151, 65211, 68271, 71331, 74390, 77450, 80510, 83570, 86629, 89689, 92749, 95809, 98868, 101928, 104988, 108048, 111108, 114167, 117227, 120287, 123347, 126406, 129466, 132526, 135586, 138646, 141705, 144765, 147825, 150885, 153944, 157004, 160064, 163124, 166184, 169243, 172303, 175363, 178423, 181482, 184542, 187602, 190662, 193722, 196781, 199841, 202901, 205961, 209020, 212080, 215140, 218200, 221259, 224319]
    data2 = [0, 659, 812, 965, 1118, 1271, 1424, 1577, 1730, 1883, 2036, 2189, 2342, 2495, 2648, 2801, 2954, 3107, 3260, 3413, 3566, 3719, 3872, 4025, 4178, 4331, 4484, 4637, 4790, 4943, 5096, 5249, 5402, 5555, 5708, 5861, 6014, 6167, 6320, 6473, 6626, 6779, 6932, 7085, 7238, 7391, 7544, 7697, 7850, 8003, 8156, 8309, 8462, 8615, 8768, 8921, 9074, 9227, 9380, 9533, 9686, 9839, 9992, 10145, 10298, 10451, 10604, 10757, 10910, 11062, 11215]
    data3 = [0, 16494, 20318, 24143, 27968, 31792, 35617, 39442, 43267, 47091, 50916, 54741, 58566, 62390, 66215, 70040, 73864, 77689, 81514, 85339, 89163, 92988, 96813, 100637, 104462, 108287, 112112, 115936, 119761, 123586, 127410, 131235, 135060, 138885, 142709, 146534, 150359, 154183, 158008, 161833, 165658, 169482, 173307, 177132, 180957, 184781, 188606, 192431, 196255, 200080, 203905, 207730, 211554, 215379, 219204, 223028, 226853, 230678, 234503, 238327, 242152, 245977, 249801, 253626, 257451, 261276, 265100, 268925, 272750, 276574, 280399]
    data4 = [0, 26390, 32510, 38629, 44749, 50868, 56988, 63107, 69227, 75346, 81466, 87586, 93705, 99825, 105944, 112064, 118183, 124303, 130422, 136542, 142662, 148781, 154901, 161020, 167140, 173259, 179379, 185498, 191618, 197737, 203857, 209977, 216096, 222216, 228335, 234455, 240574, 246694, 252813, 258933, 265053, 271172, 277292, 283411, 289531, 295650, 301770, 307889, 314009, 320128, 326248, 332368, 338487, 344607, 350726, 356846, 362965, 369085, 375204, 381324, 387444, 393563, 399683, 405802, 411922, 418041, 424161, 430280, 436400, 442519, 448639]
    数据 = [data1, data2, data3, data4]
    次数 = [1, 15, 1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率   

class 极诣·鬼泣技能27(被动技能):
    名称 = '鬼神冠冕'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣·鬼泣技能28(主动技能):
    名称 = '鬼神剑·黄泉摆渡'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    CD = 60.0
    data1 = [0, 15007, 16530, 18052, 19575, 21097, 22620, 24143, 25665, 27188, 28710, 30233, 31755, 33278, 34800, 36323, 37845, 39368, 40890, 42413, 43935, 45458, 46981, 48503, 50026, 51548, 53071, 54593, 56116, 57638, 59161, 60683, 62206, 63728, 65251, 66773, 68296, 69819, 71341, 72864, 74386]
    data2 = [0, 7640, 8415, 9190, 9965, 10741, 11516, 12291, 13066, 13841, 14616, 15391, 16166, 16942, 17717, 18492, 19267, 20042, 20817, 21592, 22368, 23143, 23918, 24693, 25468, 26243, 27018, 27793, 28569, 29344, 30119, 30894, 31669, 32444, 33219, 33994, 34770, 35545, 36320, 37095, 37870]
    data3 = [0, 26741, 29454, 32167, 34880, 37593, 40306, 43019, 45732, 48445, 51158, 53871, 56584, 59297, 62010, 64723, 67436, 70149, 72862, 75575, 78288, 81000, 83713, 86426, 89139, 91852, 94565, 97278, 99991, 102704, 105417, 108130, 110843, 113556, 116269, 118982, 121695, 124408, 127121, 129834, 132547]
    data4 = [0, 2292, 2524, 2757, 2989, 3222, 3454, 3687, 3919, 4152, 4385, 4617, 4850, 5082, 5315, 5547, 5780, 6012, 6245, 6477, 6710, 6942, 7175, 7408, 7640, 7873, 8105, 8338, 8570, 8803, 9035, 9268, 9500, 9733, 9965, 10198, 10431, 10663, 10896, 11128, 11361]
    数据 = [data1, data2, data3, data4]
    次数 = [2, 1, 1, 5]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率       

class 极诣·鬼泣技能29(主动技能):
    名称 = '黄泉之门：万鬼渡灵'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    CD = 290.0
    data1 = [0, 13702, 16879, 20056, 23233, 26411, 29588, 32765, 35942, 39120, 42297, 45474, 48652, 51829, 55006, 58183, 61361, 64538, 67715, 70893, 74070, 77247, 80424, 83602, 86779, 89956, 93133, 96311, 99488, 102665, 105843, 109020, 112197, 115374, 118552, 121729, 124906, 128084, 131261, 134438, 137615]
    data2 = [0, 82212, 101275, 120339, 139403, 158466, 177530, 196594, 215657, 234721, 253785, 272848, 291912, 310976, 330039, 349103, 368167, 387230, 406294, 425358, 444421, 463485, 482549, 501612, 520676, 539740, 558803, 577867, 596931, 615994, 635058, 654122, 673186, 692249, 711313, 730377, 749440, 768504, 787568, 806631, 825695]
    data3 = [0, 3653, 4501, 5348, 6195, 7042, 7890, 8737, 9584, 10432, 11279, 12126, 12973, 13821, 14668, 15515, 16362, 17210, 18057, 18904, 19752, 20599, 21446, 22293, 23141, 23988, 24835, 25683, 26530, 27377, 28224, 29072, 29919, 30766, 31613, 32461, 33308, 34155, 35003, 35850, 36697]
    data4 = [0, 5138, 6329, 7521, 8712, 9904, 11095, 12287, 13478, 14670, 15861, 17053, 18244, 19436, 20627, 21818, 23010, 24201, 25393, 26584, 27776, 28967, 30159, 31350, 32542, 33733, 34925, 36116, 37308, 38499, 39691, 40882, 42074, 43265, 44457, 45648, 46840, 48031, 49223, 50414, 51605]
    数据 = [data1, data2, data3, data4]
    次数 = [1, 2, 15, 8]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率    

    关联技能 = ['无']
    def 加成倍率(self, 武器类型):
        return 0.0

极诣·鬼泣技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣·鬼泣技能列表.append(极诣·鬼泣技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣·鬼泣技能序号 = dict()
for i in range(len(极诣·鬼泣技能列表)):
    极诣·鬼泣技能序号[极诣·鬼泣技能列表[i].名称] = i

极诣·鬼泣一觉序号 = 0
极诣·鬼泣二觉序号 = 0
极诣·鬼泣三觉序号 = 0
for i in 极诣·鬼泣技能列表:
    if i.所在等级 == 50:
        极诣·鬼泣一觉序号 = 极诣·鬼泣技能序号[i.名称]
    if i.所在等级 == 85:
        极诣·鬼泣二觉序号 = 极诣·鬼泣技能序号[i.名称]
    if i.所在等级 == 100:
        极诣·鬼泣三觉序号 = 极诣·鬼泣技能序号[i.名称]

极诣·鬼泣护石选项 = ['无']
for i in 极诣·鬼泣技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·鬼泣护石选项.append(i.名称)

极诣·鬼泣符文选项 = ['无']
for i in 极诣·鬼泣技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣·鬼泣符文选项.append(i.名称)

class 极诣·鬼泣角色属性(角色属性):

    实际名称 = '极诣·鬼泣'
    角色 = '鬼剑士(男)'
    职业 = '鬼泣'

    武器选项 = ['太刀','短剑']
    
    类型选择 = ['魔法百分比']
    
    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.69
   
    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(极诣·鬼泣技能列表)
        self.技能序号= deepcopy(极诣·鬼泣技能序号)
    
    def 被动倍率计算(self):
        super().被动倍率计算()
        self.暗属性强化 += self.技能栏[self.技能序号['暗月降临']].属强加成()

        self.技能栏[self.技能序号['冥炎之卡洛(灼烧)']].等级 = self.技能栏[self.技能序号['冥炎之卡洛']].等级
        self.技能栏[self.技能序号['冥炎之卡洛(灼烧)']].TP等级 = self.技能栏[self.技能序号['冥炎之卡洛']].TP等级
        self.技能栏[self.技能序号['冥炎剑']].等级 = self.技能栏[self.技能序号['冥炎之卡洛']].等级
        self.技能栏[self.技能序号['冥炎剑']].TP等级 = self.技能栏[self.技能序号['冥炎之卡洛']].TP等级

        self.技能栏[self.技能序号['鬼斩']].额外倍率 = self.技能栏[self.技能序号['噬灵鬼斩']].加成倍率()

class 极诣·鬼泣(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·鬼泣角色属性()
        self.角色属性A = 极诣·鬼泣角色属性()
        self.角色属性B = 极诣·鬼泣角色属性()
        self.一觉序号 = 极诣·鬼泣一觉序号
        self.二觉序号 = 极诣·鬼泣二觉序号
        self.三觉序号 = 极诣·鬼泣三觉序号
        self.护石选项 = deepcopy(极诣·鬼泣护石选项)
        self.符文选项 = deepcopy(极诣·鬼泣符文选项)

    def 界面(self):
        super().界面()
        self.布雷德开关=QCheckBox('刀阵：直接解放',self.main_frame2)
        self.布雷德开关.setChecked(False)
        self.布雷德开关.resize(120,20)
        self.布雷德开关.move(325,450)
        self.布雷德开关.setStyleSheet(复选框样式)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.布雷德开关.isChecked():
            属性.技能栏[属性.技能序号['幽魂之布雷德']].解放 = 0