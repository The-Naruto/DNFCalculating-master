﻿from PublicReference.base import *
class 湮灭之瞳主动技能(主动技能):
    元素之力蓄力数量 = 0
    关联技能4 = ['无']

    # def 等效CD(self, 武器类型):
    #     if 武器类型 == '魔杖':
    #         return round(self.CD / self.恢复 * 1, 1)
    #     if 武器类型 == '法杖':
    #         return round(self.CD / self.恢复 * 1.1, 1)

class 湮灭之瞳被动技能(被动技能):
    关联技能4 = ['无']
    元素之力蓄力数量 = 0

class 湮灭之瞳技能0(湮灭之瞳被动技能):
    名称 = '元素循环'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 湮灭之瞳技能1(湮灭之瞳被动技能):
    名称 = '元素之力'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    每层加成 = [0, 7, 8, 10, 11, 13, 14, 15, 17, 18, 20, 21, 22, 24, 25, 27, 28, 29, 31, 32, 34, 35, 36, 38, 39, 41, 42, 43, 45, 46, 48, 49, 50, 52, 53, 55, 56, 57, 59, 60, 62, 63, 64, 66, 67, 69, 70, 71, 73, 74, 76, 77, 78, 80, 81, 83, 84, 85, 87, 88, 90, 91, 92, 94, 95, 97, 98, 99, 101, 102, 104]
    关联技能 = ['无']
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.01*self.每层加成[self.等级],5)


class 湮灭之瞳技能2(湮灭之瞳主动技能):
    名称 = '元素环绕'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '所有属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (6 + self.等级 * 3)


class 湮灭之瞳技能3(湮灭之瞳被动技能):
    名称 = '元素融合'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['无']
    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '所有属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (37 + self.等级 * 3)
#要玩换装就自己手动给他调到满级

class 湮灭之瞳技能4(湮灭之瞳被动技能):
    名称 = '元素爆发'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 16:
                return round(1.015 + 0.015 * self.等级, 5)
            else:
                return round(1.255 + 0.020 * (self.等级 - 16), 5)


class 湮灭之瞳技能5(湮灭之瞳被动技能):
    名称 = '黑瞳'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class 湮灭之瞳技能6(湮灭之瞳被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 湮灭之瞳技能7(湮灭之瞳被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 湮灭之瞳技能8(湮灭之瞳被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


class 湮灭之瞳技能9(湮灭之瞳主动技能):
    名称 = '元素炮'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    基础 = 490
    成长 = 10
    CD = 4.0
#   元素炮吃两次被动的bug写在最下面的
#
#       技能单次伤害计算  里
#
#   啥时候修复了把那几个被动的二次加成删一删就好了
#


class 湮灭之瞳技能10(湮灭之瞳主动技能):
    名称 = '属性变换'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 19
    是否有伤害 = 1
    是否主动 = 1
    数据 = [0, 254, 312, 371, 430, 489, 548, 606, 665, 724, 783, 842, 900, 959, 1018, 1077, 1136, 1194, 1253, 1312, 1371, 1430, 1488, 1547, 1606, 1665, 1724, 1782, 1841, 1900, 1959, 2018, 2077, 2135, 2194, 2253, 2312, 2371, 2429, 2488, 2547, 2606, 2665, 2723, 2782, 2841, 2900, 2959, 3017, 3076, 3135, 3194, 3253, 3312, 3370, 3429, 3488, 3547, 3606, 3664, 3723, 3782, 3841, 3900, 3958, 4017, 4076, 4135, 4194, 4252, 4311]
    攻击次数 = 1
    TP成长 = 0.08
    TP上限 = 5
    CD = 5.0
    演出时间 = 5.0
    关联技能 = ['元素炮','魔球连射']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round((self.数据[self.等级]*0.01 )* (1+0.08 * self.TP等级), 5)
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    
class 湮灭之瞳技能11(湮灭之瞳主动技能):
    名称 = '魔球连射'
    所在等级 = 5
    等级上限 = 11
    基础等级 = 1
    基础 = 108
    成长 = 2
    攻击次数 = 5
    CD = 2.4
    演出时间 = 1.5



class 湮灭之瞳技能12(湮灭之瞳主动技能):
    名称 = '地炎'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 244, 269, 293, 318, 343, 368, 393, 418, 442, 467, 491, 517, 542, 566, 591, 615, 640, 666, 690, 715, 740, 764, 789, 814, 839, 864, 888, 913, 938, 963, 988, 1012, 1037, 1062, 1087, 1112, 1136, 1161, 1186, 1210, 1236, 1260, 1285, 1310, 1334, 1359, 1384, 1409, 1434, 1458, 1483, 1508, 1533, 1558, 1582, 1607, 1632, 1657, 1682, 1707, 1731, 1756, 1780, 1805, 1831, 1855, 1880, 1904, 1929, 1954]
    攻击次数 = 9
    CD = 4.0
    TP成长 = 0.04
    TP上限 = 5
    演出时间 = 1.8
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
#   打满是12hit
#   实际上站位不对的话很容易丢3或6hit
#   跟游戏里对不上的话可以试试调整下站位再打沙袋 hit对上了的话伤害应该是一致的

class 湮灭之瞳技能13(湮灭之瞳主动技能):
    名称 = '冰晶坠'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据 = [0, 470, 517, 565, 613, 661, 708, 756, 804, 852, 900, 946, 994, 1042, 1090, 1138, 1185, 1233, 1281, 1329, 1376, 1424, 1472, 1519, 1567, 1614, 1662, 1710, 1758, 1805, 1853, 1901, 1949, 1997, 2044, 2091, 2139, 2187, 2235, 2282, 2330, 2378, 2426, 2473, 2521, 2569, 2617, 2664, 2711, 2759, 2807, 2855, 2903, 2950, 2998, 3046, 3094, 3141, 3189, 3236, 3284, 3332, 3379, 3427, 3475, 3523, 3570, 3618, 3666, 3714, 3762]
    攻击次数 = 7
    CD = 6.4
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 1.5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
#   随机丢1到2hit
#   打满是7hit

class 湮灭之瞳技能14(湮灭之瞳主动技能):
    名称 = '雷光链'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据 = [0, 1036, 1141, 1246, 1350, 1456, 1561, 1666, 1771, 1876, 1981, 2086, 2192, 2297, 2402, 2507, 2612, 2717, 2822, 2928, 3032, 3137, 3243, 3348, 3453, 3558, 3663, 3768, 3873, 3979, 4083, 4188, 4294, 4399, 4504, 4608, 4714, 4819, 4924, 5029, 5135, 5239, 5344, 5450, 5555, 5660, 5765, 5870, 5975, 6080, 6186, 6290, 6395, 6501, 6606, 6711, 6816, 6921, 7026, 7131, 7237, 7341, 7446, 7551, 7657, 7762, 7867, 7972, 8077, 8182, 8287]
    攻击次数 = 4
    CD = 9.6
    TP成长 = 0.20
    TP上限 = 5
    演出时间 = 1.6
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 湮灭之瞳技能15(湮灭之瞳主动技能):
    名称 = '暗域扩张'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据 = [0, 5887, 6485, 7081, 7679, 8277, 8874, 9471, 10068, 10666, 11263, 11860, 12458, 13055, 13652, 14250, 14846, 15444, 16042, 16638, 17236, 17833, 18430, 19028, 19625, 20222, 20820, 21417, 22014, 22611, 23209, 23806, 24403, 25001, 25598, 26195, 26793, 27389, 27987, 28585, 29181, 29779, 30376, 30973, 31571, 32168, 32766, 33363, 33960, 34558, 35154, 35752, 36350, 36946, 37544, 38141, 38738, 39336, 39933, 40530, 41128, 41725, 42322, 42919, 43517, 44114, 44711, 45309, 45906, 46503, 47101]
    攻击次数 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.4
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率



class 湮灭之瞳技能16(湮灭之瞳主动技能):
    名称 = '冰晶之浴'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据 = [0, 434, 478, 522, 566, 610, 654, 699, 742, 786, 831, 874, 919, 963, 1006, 1051, 1095, 1139, 1183, 1227, 1271, 1315, 1359, 1403, 1448, 1491, 1536, 1580, 1623, 1668, 1712, 1756, 1800, 1844, 1888, 1932, 1976, 2020, 2065, 2108, 2152, 2197, 2240, 2285, 2329, 2373, 2417, 2460, 2505, 2549, 2593, 2637, 2682, 2725, 2769, 2813, 2857, 2902, 2945, 2990, 3034, 3077, 3122, 3166, 3210, 3254, 3298, 3342, 3386, 3430, 3474]
    攻击次数 = 14
    CD = 12.0
    TP成长 = 0.0
    TP上限 = 1
    演出时间 = 3.0
    def 等效CD(self, 武器类型,输出类型):
        if self.TP等级 > 0:
            self.CD = self.CD - 3
        return super().等效CD(武器类型,输出类型)

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
class 湮灭之瞳技能17(湮灭之瞳主动技能):
    名称 = '旋炎破'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 690, 760, 830, 900, 970, 1040, 1110, 1180, 1250, 1321, 1390, 1461, 1530, 1601, 1670, 1741, 1810, 1881, 1950, 2021, 2090, 2161, 2231, 2301, 2371, 2441, 2511, 2581, 2651, 2721, 2792, 2861, 2932, 3001, 3072, 3141, 3212, 3281, 3352, 3422, 3492, 3562, 3632, 3702, 3772, 3842, 3912, 3982, 4052, 4122, 4192, 4262, 4332, 4402, 4472, 4542, 4613, 4682, 4753, 4822, 4893, 4962, 5033, 5102, 5173, 5242, 5313, 5382, 5453, 5523]
    攻击次数1 = 6
    数据2 = [0, 2761, 3041, 3322, 3602, 3882, 4162, 4442, 4723, 5003, 5283, 5563, 5843, 6123, 6403, 6684, 6964, 7244, 7524, 7804, 8084, 8364, 8644, 8925, 9205, 9485, 9765, 10045, 10325, 10605, 10886, 11167, 11447, 11727, 12007, 12287, 12567, 12847, 13127, 13408, 13688, 13968, 14248, 14528, 14808, 15088, 15369, 15649, 15929, 16209, 16489, 16769, 17049, 17329, 17610, 17890, 18170, 18450, 18731, 19011, 19291, 19571, 19851, 20132, 20412, 20692, 20972, 21252, 21532, 21812, 22093]
    攻击次数2 = 1
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    
    def 装备护石(self, x):
        if x  == 0:
            self.攻击次数1 *= 1.15
            self.攻击次数2 *= 1.34
        elif x == 1:
            self.攻击次数1 *= 1.30
            self.攻击次数2 *= 1.34
#       下面这些是向前放的数据
#       虽然向前还是原地放伤害都一样 带护石也一样（
#
#   数据1 = [0, 690, 760, 830, 900, 970, 1040, 1110, 1180, 1250, 1321, 1390, 1461, 1530, 1601, 1670, 1741, 1810, 1881, 1950, 2021, 2090, 2161, 2231, 2301, 2371, 2441, 2511, 2581, 2651, 2721, 2792, 2861, 2932, 3001, 3072, 3141, 3212, 3281, 3352, 3422, 3492, 3562, 3632, 3702, 3772, 3842, 3912, 3982, 4052, 4122, 4192, 4262, 4332, 4402, 4472, 4542, 4613, 4682, 4753, 4822, 4893, 4962, 5033, 5102, 5173, 5242, 5313, 5382, 5453, 5523]
#   攻击次数1 = 10
#   数据2 = [0, 2761, 3041, 3322, 3602, 3882, 4162, 4442, 4723, 5003, 5283, 5563, 5843, 6123, 6403, 6684, 6964, 7244, 7524, 7804, 8084, 8364, 8644, 8925, 9205, 9485, 9765, 10045, 10325, 10605, 10886, 11167, 11447, 11727, 12007, 12287, 12567, 12847, 13127, 13408, 13688, 13968, 14248, 14528, 14808, 15088, 15369, 15649, 15929, 16209, 16489, 16769, 17049, 17329, 17610, 17890, 18170, 18450, 18731, 19011, 19291, 19571, 19851, 20132, 20412, 20692, 20972, 21252, 21532, 21812, 22093]
#   攻击次数2 = 0
#



        
class 湮灭之瞳技能18(湮灭之瞳主动技能):
    名称 = '雷光屏障'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 7659, 8436, 9213, 9991, 10768, 11545, 12322, 13099, 13876, 14653, 15430, 16206, 16983, 17760, 18538, 19315, 20092, 20869, 21646, 22423, 23200, 23977, 24754, 25531, 26308, 27085, 27862, 28639, 29417, 30194, 30971, 31748, 32525, 33302, 34079, 34856, 35633, 36410, 37187, 37964, 38741, 39519, 40296, 41073, 41850, 42627, 43404, 44180, 44957, 45734, 46511, 47288, 48066, 48843, 49620, 50397, 51174, 51951, 52728, 53505, 54282, 55059, 55836, 56613, 57390, 58168, 58945, 59722, 60499, 61276]
    攻击次数 = 1
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.2
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 4 * (1 - 0.72)
        elif x == 1:
            self.攻击次数 *= 1.08 * 4 * (1 - 0.72)
#现在这技能的护石有个bug
#
#解除僵直时追加的感电解除攻击对部分怪物不生效（大部分建筑型 （包括沙袋
#
#沙袋会触发 所以护石加成按bug触发时的伤害写了
#
#啥时候bug修了 或者有人想看看没bug条件下的伤害 把下面那条抄上去覆盖下就好了
#
    #护石bug修复后
    #   self.攻击次数 *= (4 + 0.4) * (1 - 0.72) 

class 湮灭之瞳技能19(湮灭之瞳主动技能):
    名称 = '黑暗禁域'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 7234, 7968, 8701, 9436, 10169, 10903, 11637, 12371, 13105, 13839, 14573, 15307, 16041, 16774, 17508, 18242, 18976, 19710, 20444, 21178, 21912, 22646, 23380, 24113, 24847, 25581, 26315, 27049, 27783, 28517, 29251, 29985, 30718, 31453, 32186, 32920, 33654, 34388, 35122, 35856, 36590, 37323, 38058, 38791, 39526, 40259, 40993, 41727, 42461, 43195, 43928, 44663, 45396, 46131, 46864, 47599, 48332, 49066, 49800, 50533, 51268, 52001, 52736, 53469, 54204, 54937, 55671, 56405, 57139, 57873]
    攻击次数 = 1
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 湮灭之瞳技能20(湮灭之瞳主动技能):
    名称 = '元素轰炸'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 2530, 2787, 3043, 3300, 3557, 3813, 4070, 4327, 4583, 4840, 5097, 5353, 5610, 5867, 6123, 6381, 6637, 6894, 7151, 7407, 7664, 7921, 8177, 8434, 8691, 8947, 9204, 9461, 9717, 9974, 10231, 10487, 10744, 11001, 11258, 11515, 11771, 12028, 12285, 12541, 12798, 13055, 13311, 13568, 13825, 14081, 14338, 14595, 14851, 15108, 15364, 15621, 15878, 16135, 16392, 16649, 16905, 17162, 17419, 17675, 17932, 18188, 18445, 18702, 18958, 19215, 19472, 19728, 19985, 20242]
    攻击次数1 = 1
    数据2 = [0, 5060, 5574, 6087, 6600, 7113, 7627, 8141, 8654, 9168, 9681, 10194, 10707, 11221, 11734, 12247, 12761, 13275, 13788, 14301, 14815, 15328, 15841, 16355, 16868, 17381, 17895, 18409, 18922, 19435, 19949, 20462, 20975, 21489, 22002, 22516, 23029, 23543, 24056, 24569, 25083, 25596, 26109, 26622, 27136, 27650, 28163, 28677, 29190, 29703, 30216, 30730, 31243, 31756, 32271, 32784, 33297, 33810, 34324, 34837, 35350, 35864, 36377, 36890, 37404, 37918, 38431, 38944, 39458, 39971, 40484]
    攻击次数2 = 1
    数据3 = [0, 232, 256, 280, 304, 327, 351, 374, 398, 422, 445, 469, 492, 516, 540, 564, 587, 610, 634, 658, 682, 705, 729, 752, 776, 800, 823, 847, 870, 895, 918, 942, 965, 989, 1012, 1036, 1060, 1083, 1107, 1130, 1155, 1178, 1202, 1225, 1248, 1273, 1296, 1320, 1343, 1367, 1390, 1414, 1438, 1461, 1485, 1508, 1533, 1556, 1580, 1603, 1627, 1651, 1674, 1698, 1721, 1745, 1769, 1793, 1816, 1839, 1863]
    攻击次数3 = 45
    CD = 32
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 += 2.26
            self.攻击次数2 += 1.45 + 0.31
            self.攻击次数3 = 0
        elif x == 1:
            self.攻击次数1 += 2.26 + 0.27
            self.攻击次数2 += 1.45 + 0.46
            self.攻击次数3 = 0

class 湮灭之瞳技能21(湮灭之瞳主动技能):
    名称 = '幻魔四重奏'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据 = [0, 1847, 2274, 2703, 3131, 3559, 3987, 4416, 4844, 5272, 5701, 6129, 6557, 6986, 7414, 7842, 8270, 8699, 9127, 9555, 9983, 10411, 10839, 11268, 11696, 12124, 12553, 12981, 13409, 13838, 14266, 14694, 15122, 15551, 15979, 16407, 16835, 17263, 17691, 18120, 18548, 18976, 19405, 19833, 20261, 20689, 21118, 21546, 21974, 22403, 22831, 23259, 23688, 24115, 24543, 24972, 25400, 25828, 26257, 26685, 27113, 27541, 27970, 28398, 28826, 29255, 29683, 30111, 30540, 30968, 31395]
    攻击次数 = 30
    CD = 145.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
#千重奏的话 能有正常放五倍差不多 想看千重奏的伤害就自己去给他释放次数改成五倍


class 湮灭之瞳技能22(湮灭之瞳主动技能):
    名称 = '元素浓缩球'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 4713, 5191, 5670, 6148, 6626, 7104, 7582, 8060, 8539, 9017, 9495, 9973, 10451, 10930, 11408, 11886, 12364, 12842, 13320, 13799, 14277, 14755, 15233, 15711, 16190, 16668, 17146, 17624, 18102, 18581, 19059, 19537, 20015, 20493, 20971, 21450, 21928, 22406, 22884, 23362, 23841, 24319, 24797, 25275, 25753, 26231, 26710, 27188, 27667, 28144, 28622, 29101, 29579, 30057, 30535, 31013, 31492, 31970, 32448, 32927, 33404, 33882, 34361, 34839, 35317, 35795, 36273, 36752, 37230, 37708]
    攻击次数1 = 1
    数据2 = [0, 10998, 12114, 13229, 14346, 15461, 16577, 17692, 18808, 19924, 21040, 22156, 23271, 24387, 25503, 26619, 27735, 28850, 29966, 31081, 32198, 33313, 34429, 35545, 36660, 37777, 38892, 40008, 41124, 42239, 43356, 44471, 45587, 46702, 47818, 48934, 50050, 51166, 52281, 53397, 54513, 55629, 56745, 57860, 58976, 60092, 61208, 62323, 63439, 64555, 65671, 66787, 67902, 69018, 70134, 71250, 72366, 73481, 74597, 75712, 76828, 77944, 79060, 80176, 81291, 82407, 83523, 84639, 85755, 86870, 87986]
    攻击次数2 = 1
    CD = 24
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 *= 1.32
            self.攻击次数2 *= 1 + 0.1 * 2
        if x == 1:
            self.攻击次数1 *= 1.60
            self.攻击次数2 *= 1 + 0.1 * 2
            
#划掉）我没这个护石 有没有人能帮我测测这个准不准啊（反正也没人用 就先这样了

    #准了准了 这护石描述把我看傻了 想破头也没想到加32%是加的第一段的32% 护石描述写错了


class 湮灭之瞳技能23(湮灭之瞳主动技能):
    名称 = '元素幻灭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 23318, 25683, 28049, 30415, 32781, 35146, 37511, 39877, 42243, 44609, 46974, 49339, 51705, 54071, 56437, 58802, 61167, 63533, 65899, 68265, 70630, 72995, 75361, 77727, 80093, 82458, 84823, 87189, 89555, 91921, 94286, 96652, 99017, 101383, 103749, 106114, 108480, 110845, 113211, 115576, 117942, 120308, 122674, 125039, 127404, 129770, 132136, 134502, 136867, 139232, 141598, 143964, 146330, 148695, 151060, 153426, 155792, 158158, 160524, 162888, 165254, 167620, 169986, 172351, 174716, 177082, 179448, 181814, 184179, 186545]
    攻击次数1 = 1
    数据2 = [0, 1227, 1351, 1476, 1601, 1725, 1849, 1974, 2099, 2223, 2347, 2472, 2597, 2721, 2845, 2970, 3094, 3219, 3344, 3468, 3592, 3717, 3842, 3966, 4090, 4215, 4340, 4464, 4588, 4713, 4838, 4962, 5087, 5211, 5336, 5460, 5585, 5709, 5833, 5958, 6083, 6207, 6331, 6456, 6581, 6705, 6829, 6954, 7079, 7203, 7328, 7452, 7577, 7701, 7826, 7950, 8075, 8199, 8324, 8449, 8572, 8697, 8822, 8946, 9070, 9195, 9320, 9444, 9569, 9693, 9818]
    攻击次数2 = 1
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.2
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 += 0.1
            self.攻击次数2 += 2.66
        elif x == 1:
            self.攻击次数1 += 0.1
            self.攻击次数2 += 4.40
    

class 湮灭之瞳技能24(湮灭之瞳主动技能):
    名称 = '元素禁域'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据 = [0, 40885, 45033, 49180, 53329, 57477, 61624, 65772, 69920, 74067, 78215, 82363, 86511, 90659, 94807, 98954, 103102, 107250, 111398, 115546, 119693, 123841, 127989, 132136, 136285, 140433, 144580, 148728, 152876, 157023, 161171, 165320, 169467, 173615, 177763, 181910, 186058, 190206, 194354, 198502, 202650, 206797, 210945, 215093, 219241, 223389, 227536, 231684, 235832, 239979, 244127, 248276, 252423, 256571, 260719, 264866, 269014, 273162, 277310, 281458, 285606, 289753, 293901, 298049, 302196, 306345, 310493, 314640, 318788, 322936, 327083]
    攻击次数 = 1
    CD = 32.0
    演出时间 = 0.4
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.24
        self.CD *= 0.95

class 湮灭之瞳技能25(湮灭之瞳主动技能):
    名称 = '聚能魔炮'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据 = [0, 50815, 55970, 61126, 66281, 71436, 76592, 81747, 86902, 92057, 97212, 102367, 107522, 112678, 117833, 122988, 128144, 133299, 138454, 143609, 148764, 153919, 159075, 164230, 169385, 174541, 179696, 184851, 190006, 195161, 200316, 205471, 210627, 215782, 220937, 226093, 231248, 236403, 241558, 246713, 251868, 257024, 262179, 267334, 272489, 277645, 282800, 287955, 293110, 298265, 303420, 308576, 313731, 318886, 324042, 329197, 334352, 339508, 344662, 349817, 354972, 360128, 365283, 370438, 375594, 380749, 385904, 391060, 396215, 401369, 406525]
    CD = 36.0
    演出时间 = 1.5
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.33
#要玩双响炮自己把释放次数乘个二
#带护石玩不了双响炮
class 湮灭之瞳技能26(湮灭之瞳主动技能):
    名称 = '末日湮灭'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 6248, 7697, 9146, 10595, 12044, 13493, 14942, 16390, 17840, 19289, 20737, 22186, 23636, 25084, 26533, 27982, 29431, 30880, 32329, 33778, 35226, 36676, 38125, 39573, 41023, 42471, 43920, 45370, 46818, 48267, 49717, 51165, 52614, 54063, 55512, 56961, 58410, 59859, 61307, 62757, 64206, 65654, 67104, 68552, 70001, 71450, 72899, 74348, 75797, 77246, 78695, 80144, 81593, 83042, 84490, 85940, 87388, 88837, 90287, 91735, 93184, 94633, 96082, 97531, 98980, 100429, 101878, 103327, 104776, 106224]
    攻击次数1 = 1
    数据2 = [0, 521, 641, 762, 883, 1003, 1124, 1244, 1366, 1486, 1607, 1728, 1848, 1969, 2090, 2211, 2332, 2452, 2573, 2694, 2814, 2935, 3056, 3177, 3298, 3418, 3539, 3660, 3780, 3901, 4022, 4143, 4264, 4384, 4505, 4625, 4746, 4867, 4988, 5109, 5229, 5350, 5471, 5591, 5712, 5833, 5954, 6075, 6195, 6316, 6437, 6557, 6678, 6799, 6920, 7041, 7161, 7282, 7403, 7523, 7645, 7765, 7886, 8007, 8127, 8248, 8368, 8490, 8610, 8731, 8852]
    攻击次数2 = 11
    数据3 = [0, 112473, 138554, 164635, 190716, 216797, 242877, 268958, 295039, 321120, 347201, 373282, 399362, 425443, 451524, 477605, 503686, 529767, 555847, 581928, 608009, 634090, 660171, 686252, 712332, 738413, 764494, 790575, 816656, 842737, 868817, 894898, 920979, 947060, 973141, 999222, 1025303, 1051383, 1077464, 1103545, 1129626, 1155707, 1181788, 1207868, 1233949, 1260030, 1286111, 1312192, 1338273, 1364353, 1390434, 1416515, 1442596, 1468677, 1494758, 1520838, 1546919, 1573000, 1599081, 1625162, 1651243, 1677323, 1703403, 1729484, 1755565, 1781646, 1807727, 1833808, 1859889, 1885969, 1912050]
    攻击次数3 = 1
    CD = 180.0
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))) * self.倍率


    
湮灭之瞳技能列表 = []
i = 0
while i >= 0:
    try:
        exec('湮灭之瞳技能列表.append(湮灭之瞳技能' + str(i) + '())')
        i += 1
    except:
        i = -1

湮灭之瞳技能序号 = dict()
for i in range(len(湮灭之瞳技能列表)):
    湮灭之瞳技能序号[湮灭之瞳技能列表[i].名称] = i

湮灭之瞳一觉序号 = 0
湮灭之瞳二觉序号 = 0
湮灭之瞳三觉序号 = 0
for i in 湮灭之瞳技能列表:
    if i.所在等级 == 50:
        湮灭之瞳一觉序号 = 湮灭之瞳技能序号[i.名称]
    if i.所在等级 == 85:
        湮灭之瞳二觉序号 = 湮灭之瞳技能序号[i.名称]
    if i.所在等级 == 100:
        湮灭之瞳三觉序号 = 湮灭之瞳技能序号[i.名称]

湮灭之瞳护石选项 = ['无']
for i in 湮灭之瞳技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        湮灭之瞳护石选项.append(i.名称)

湮灭之瞳符文选项 = ['无']
for i in 湮灭之瞳技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        湮灭之瞳符文选项.append(i.名称)


class 湮灭之瞳角色属性(角色属性):
    实际名称 = '湮灭之瞳'
    角色 = '魔法师(男)'
    职业 = '元素爆破师'

    武器选项 = ['魔杖', '法杖']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 2.07

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(湮灭之瞳技能列表)
        self.技能序号 = deepcopy(湮灭之瞳技能序号)

    def 伤害指数计算(self):
        self.所有属性强化(self.技能栏[self.技能序号['元素环绕']].属强加成() + self.技能栏[self.技能序号['元素融合']].属强加成())
        super().伤害指数计算()

    def 技能单次伤害计算(self, y):
        #y切装标记
        技能单次伤害 = []
        for i in self.技能栏:
            if i.是否主动 == 1 and i.名称 != '元素炮' :
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率)
            elif i.名称 == '元素炮':
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率*
                                 (1.0 + self.技能栏[self.技能序号['元素之力']].加成倍率(self.武器类型)*5))
            else:
                技能单次伤害.append(0)
        return 技能单次伤害

class 湮灭之瞳(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 湮灭之瞳角色属性()
        self.角色属性A = 湮灭之瞳角色属性()
        self.角色属性B = 湮灭之瞳角色属性()
        self.一觉序号 = 湮灭之瞳一觉序号
        self.二觉序号 = 湮灭之瞳二觉序号
        self.三觉序号 = 湮灭之瞳三觉序号
        self.护石选项 = deepcopy(湮灭之瞳护石选项)
        self.符文选项 = deepcopy(湮灭之瞳符文选项)
    def 界面(self):
        super().界面()
        self.地火hit=MyQComboBox(self.main_frame2)
        for i in range(6,13):
            self.地火hit.addItem('地炎攻击次数:' + str(i))
        self.地火hit.setCurrentIndex(6)
        self.地火hit.resize(140,20)
        self.地火hit.move(325,505)
        self.地火hit.setToolTip('打满为12hit')

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.技能栏[属性.技能序号['地炎']].攻击次数 = 6 + self.地火hit.currentIndex()



