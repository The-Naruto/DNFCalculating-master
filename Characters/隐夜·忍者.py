from PublicReference.base import *
import math

等级 = 100 + 5


class 主动技能(主动技能):
    def 等效CD(self, 武器类型,输出类型):
        return round(self.CD  / self.恢复, 1)
class 技能0(主动技能):
    名称 = '火遁·豪火球之术'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 101, 112, 121, 133, 142, 154, 163, 174, 183, 195, 204, 215, 225, 236, 245, 257, 266, 277, 287, 298, 307,319, 328, 337, 348, 358, 369, 378, 390, 399, 410, 419, 431, 440, 452, 461, 472, 481, 493, 502, 513, 523, 534,543, 555, 564, 575, 584, 596, 605, 617, 626, 637, 646, 658, 667, 678, 688, 699, 708, 720, 729, 740, 750, 761,770, 782, 791, 800, 811]
    攻击次数1 = 12
    数据2 = [0, 406, 447, 488, 529, 571, 612, 652, 693, 735, 776, 817, 858, 900, 941, 982, 1023, 1065, 1105, 1146, 1187,1229, 1270, 1311, 1352, 1394, 1435, 1476, 1517, 1557, 1599, 1640, 1681, 1723, 1764, 1805, 1846, 1888, 1929,1970, 2010, 2051, 2093, 2134, 2175, 2216, 2258, 2299, 2340, 2381, 2423, 2463, 2504, 2545, 2587, 2628, 2669,2710, 2752, 2793, 2834, 2875, 2916, 2957, 2998, 3039, 3081, 3122, 3163, 3204, 3246]
    攻击次数2 = 1
    CD = 6.3
    攻击倍率 = 1.078
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1  + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能1(主动技能):
    名称 = '忍法：幻影手里剑'
    备注 = '(结印打满40hit)'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 154, 170, 186, 202, 217, 233, 249, 265, 279, 296, 312, 327, 342, 358, 374, 390, 405, 421, 437, 452, 468,484, 499, 515, 531, 546, 562, 578, 593, 609, 625, 641, 656, 672, 687, 704, 719, 734, 750, 767, 781, 797, 813,828, 844, 860, 876, 891, 907, 922, 939, 954, 969, 985, 1002, 1016, 1032, 1048, 1064, 1079, 1094, 1111, 1127,1141, 1157, 1174, 1189, 1204, 1220, 1236]
    攻击次数1 = 10
    数据2 = [0, 154, 170, 186, 202, 217, 233, 249, 265, 279, 296, 312, 327, 342, 358, 374, 390, 405, 421, 437, 452, 468,484, 499, 515, 531, 546, 562, 578, 593, 609, 625, 641, 656, 672, 687, 704, 719, 734, 750, 767, 781, 797, 813,828, 844, 860, 876, 891, 907, 922, 939, 954, 969, 985, 1002, 1016, 1032, 1048, 1064, 1079, 1094, 1111, 1127,1141, 1157, 1174, 1189, 1204, 1220, 1236]
    攻击次数2 = 10*2
    攻击倍率2 = 0.5
    数据3 = [0, 154, 170, 186, 202, 217, 233, 249, 265, 279, 296, 312, 327, 342, 358, 374, 390, 405, 421, 437, 452, 468,484, 499, 515, 531, 546, 562, 578, 593, 609, 625, 641, 656, 672, 687, 704, 719, 734, 750, 767, 781, 797, 813,828, 844, 860, 876, 891, 907, 922, 939, 954, 969, 985, 1002, 1016, 1032, 1048, 1064, 1079, 1094, 1111, 1127,1141, 1157, 1174, 1189, 1204, 1220, 1236]
    攻击次数3 = 10
    攻击倍率3 = 0.3
    攻击倍率 = 1.05
    CD = 10.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率2 + self.数据3[self.等级] * self.攻击次数3 * self.攻击倍率3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能2(主动技能):
    名称 = '火遁·飓风煞'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 94, 104, 114, 122, 132, 141, 151, 162, 170, 180, 189, 199, 208, 217, 227, 237, 247, 256, 265, 274, 285,294, 304, 313, 322, 332, 342, 352, 361, 370, 379, 389, 399, 409, 418, 427, 437, 446, 456, 466, 475, 485, 494,504, 512, 523, 533, 542, 552, 560, 570, 580, 590, 600, 608, 618, 627, 637, 647, 657, 665, 675, 685, 694, 705,713, 723, 732, 742, 752]
    攻击次数1 = 25
    数据2 = [0, 689, 759, 828, 898, 968, 1039, 1109, 1179, 1248, 1317, 1387, 1457, 1528, 1598, 1667, 1737, 1807, 1877,1947, 2017, 2087, 2156, 2226, 2296, 2366, 2435, 2505, 2576, 2646, 2716, 2786, 2855, 2925, 2994, 3065, 3135,3205, 3274, 3344, 3414, 3485, 3555, 3625, 3694, 3763, 3833, 3903, 3973, 4044, 4113, 4183, 4253, 4323, 4393,4464, 4533, 4602, 4672, 4742, 4812, 4881, 4951, 5022, 5092, 5162, 5232, 5301, 5370, 5440, 5511]
    攻击次数2 = 1
    CD = 14.3
    攻击倍率 = 1.194
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能3(被动技能):
    名称 = '苦无精通'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.01 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能4(被动技能):
    名称 = '烈焰印记'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.3 + 0.01 * self.等级, 5)

class 技能5(主动技能):
    名称 = '火遁·螺旋手里剑'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 142, 156, 170, 185, 199, 213, 228, 242, 257, 271, 285, 300, 314, 328, 343, 357, 372, 386, 400, 415, 429,443, 458, 472, 487, 501, 515, 530, 544, 558, 573, 587, 601, 616, 630, 645, 659, 673, 688, 702, 716, 731, 745,760, 774, 788, 803, 817, 831, 846, 860, 875, 889, 903, 918, 932, 946, 961, 975, 989, 1004, 1018, 1033, 1047,1061, 1076, 1090, 1104, 1119, 1133]
    攻击次数1 = 15
    数据2 = [0, 584, 644, 703, 762, 821, 881, 940, 999, 1058, 1118, 1177, 1236, 1296, 1355, 1414, 1473, 1533, 1592, 1651,1711, 1770, 1829, 1888, 1948, 2007, 2066, 2125, 2185, 2244, 2303, 2363, 2422, 2481, 2540, 2600, 2659, 2718,2777, 2837, 2896, 2955, 3015, 3074, 3133, 3192, 3252, 3311, 3370, 3430, 3489, 3548, 3607, 3667, 3726, 3785,3844, 3904, 3963, 4022, 4082, 4141, 4200, 4259, 4319, 4378, 4437, 4496, 4556, 4615, 4674]
    攻击次数2 = 1
    CD = 10.0
    攻击倍率 = 1.197
    TP成长 = 0
    TP基础 = 5
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        if self.TP等级 == 0:
            return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 * self.攻击倍率
        else:
            if self.TP等级 <= 5:
                return (self.数据1[self.等级] * (self.攻击次数1-self.TP等级*2-1) + (self.数据2[self.等级] * (self.TP等级+1))* self.攻击次数2)  * self.倍率 * self.攻击倍率

    #def 等效百分比(self, 武器类型):
        #return (self.数据1[self.等级] * (self.攻击次数1-self.TP等级*2-1) + (self.数据2[self.等级] * (self.TP等级+1))* self.攻击次数2)

class 技能6(主动技能):
    名称 = '忍法：替身术'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 3
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 1297, 1504, 1710, 1917, 2124, 2330, 2537, 2744, 2952, 3157, 3365, 3572, 3778, 3985, 4192, 4398, 4605,4812, 5018, 5225, 5432, 5638, 5846, 6053, 6259, 6466, 6673, 6879, 7086, 7293, 7499, 7706, 7913, 8119, 8326,8534, 8740, 8947, 9154, 9360, 9567, 9774, 9980, 10187, 10394, 10600, 10807, 11015, 11220, 11428, 11635,11841, 12048, 12255, 12461, 12668, 12875, 13081, 13288, 13495, 13701, 13909, 14116, 14322, 14529, 14736,14943, 15149, 15356, 15563]
    攻击次数1 = 1
    数据2 = [0, 778, 902, 1026, 1151, 1274, 1399, 1522, 1646, 1771, 1894, 2019, 2143, 2267, 2391, 2514, 2639, 2764, 2887,3011, 3135, 3259, 3384, 3507, 3632, 3755, 3879, 4004, 4127, 4252, 4375, 4500, 4624, 4748, 4872, 4995, 5120,5244, 5368, 5492, 5616, 5740, 5865, 5988, 6113, 6236, 6360, 6485, 6608, 6733, 6856, 6981, 7105, 7228, 7353,7476, 7601, 7725, 7849, 7973, 8097, 8221, 8346, 8469, 8593, 8718, 8841, 8966, 9089, 9214, 9338]
    攻击次数2 = 1
    数据3 = [0, 3424, 3969, 4515, 5061, 5607, 6153, 6699, 7244, 7791, 8336, 8882, 9428, 9973, 10520, 11065, 11612, 12157,12704, 13249, 13794, 14341, 14886, 15433, 15978, 16524, 17070, 17614, 18162, 18706, 19254, 19798, 20344,20890, 21436, 21982, 22527, 23073, 23619, 24165, 24711, 25257, 25802, 26349, 26894, 27440, 27986, 28532,29078, 29623, 30170, 30715, 31262, 31807, 32352, 32899, 33444, 33991, 34536, 35083, 35628, 36172, 36720,37264, 37812, 38356, 38902, 39448, 39994, 40540, 41085]
    攻击次数3 = 1
    攻击倍率 = 1.207
    CD = 26.2
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能7(主动技能):
    名称 = '火遁·炎天道'
    备注 = '(地面释放)'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1=[0, 189, 207, 229, 246, 265, 284, 304, 323, 342, 362, 379, 401, 418, 437, 456, 476, 496, 514, 535, 553, 573, 591, 610, 630, 649, 669, 686, 708, 725, 745, 762, 781, 802, 820, 840, 858, 879, 897, 917, 936, 955, 975, 992, 1013, 1031, 1051, 1070, 1089, 1109, 1127, 1147, 1165, 1186, 1204, 1224, 1243, 1262, 1282, 1300, 1320, 1336, 1359, 1376, 1395, 1414, 1434, 1453, 1471, 1491, 1510]#地面爆炸
    攻击次数1 = 1
    #空中数据2 = [0, 377, 416, 454, 493, 530, 571, 608, 647, 683, 722, 760, 799, 837, 877, 914, 952, 991, 1028, 1067, 1105,1145, 1183, 1222, 1258, 1297, 1335, 1373, 1411, 1451, 1489, 1528, 1565, 1604, 1642, 1680, 1719, 1757, 1796,1834, 1871, 1909, 1948, 1986, 2025, 2063, 2102, 2140, 2179, 2216, 2255, 2294, 2333, 2370, 2407, 2446, 2484,2522, 2560, 2600, 2638, 2677, 2714, 2753, 2791, 2829, 2869, 2907, 2945, 2983, 3021]
    #攻击次数2 = 1
    #数据1 = [0, 567, 623, 682, 738, 795, 854, 912, 969, 1027, 1085, 1141, 1198, 1256, 1313, 1372, 1428, 1486, 1544, 1601,1659, 1717, 1772, 1830, 1888, 1946, 2003, 2062, 2118, 2175, 2234, 2291, 2348, 2406, 2462, 2520, 2578, 2636,2692, 2752, 2808, 2864, 2923, 2980, 3036, 3095, 3152, 3210, 3268, 3326, 3383, 3440, 3497, 3554, 3612, 3670,3727, 3784, 3842, 3900, 3957, 4015, 4071, 4128, 4186, 4244, 4302, 4360, 4416, 4474, 4533]
    #攻击次数1 = 1
    数据2 = [0, 377, 416, 454, 493, 530, 571, 608, 647, 683, 722, 760, 799, 837, 877, 914, 952, 991, 1028, 1067, 1105,1145, 1183, 1222, 1258, 1297, 1335, 1373, 1411, 1451, 1489, 1528, 1565, 1604, 1642, 1680, 1719, 1757, 1796,1834, 1871, 1909, 1948, 1986, 2025, 2063, 2102, 2140, 2179, 2216, 2255, 2294, 2333, 2370, 2407, 2446, 2484, 2522, 2560, 2600, 2638, 2677, 2714, 2753, 2791, 2829, 2869, 2907, 2945, 2983, 3021]
    攻击次数2 = 1
    数据3 = [0, 3508, 3863, 4219, 4575, 4931, 5287, 5643, 5999, 6355, 6712, 7066, 7422, 7778, 8135, 8490, 8846, 9201,9557, 9914, 10269, 10626, 10982, 11337, 11694, 12050, 12405, 12761, 13117, 13473, 13829, 14185, 14538, 14895,15252, 15607, 15963, 16319, 16675, 17031, 17387, 17742, 18098, 18455, 18810, 19166, 19523, 19878, 20235,20591, 20946, 21302, 21659, 22013, 22369, 22724, 23080, 23437, 23792, 24149, 24505, 24860, 25217, 25573,25928, 26284, 26639, 26995, 27351, 27707, 28062]#火焰球爆炸
    攻击次数3 = 1
    CD = 15.1
    攻击倍率 = 1.205
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.攻击次数3 = 1 * 1.08
        elif x == 1:
            self.倍率 *= 1.1 + 0.08
            self.攻击次数3 = 1 * 1.08

class 技能8(主动技能):
    名称 = '忍法：残影术'
    所在等级 = 35
    等级上限 = 11
    基础等级 = 1
    是否有伤害 = 0
    关联技能 = ['火遁·豪火球之术', '忍法：幻影手里剑', '火遁·飓风煞', '火遁·螺旋手里剑', '忍法：替身术', '火遁·炎天道', '火遁·蟾蜍油炎弹', '火遁·炎舞天璇','火遁·冥炎业火阵','八岐大蛇',
            '火遁·风魔手里剑', '忍法：飞燕手里剑', '天照','勾玉之火·镰鼬','火炎灼空：草雉剑','火源限界·八咫乌']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.98 + 0.02 * self.等级, 5)


class 技能9(主动技能):
    名称 = '火遁·蟾蜍油炎弹'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 161, 178, 193, 210, 227, 242, 259, 275, 292, 308, 324, 341, 358, 373, 390, 406, 422, 439, 455, 473, 488,505, 522, 538, 554, 571, 587, 604, 619, 636, 653, 668, 685, 702, 718, 734, 750, 767, 784, 799, 816, 832, 848,865, 881, 898, 914, 930, 947, 962, 979, 997, 1013, 1030, 1046, 1062, 1079, 1094, 1111, 1128, 1144, 1160, 1177,1193, 1210, 1225, 1242, 1259, 1274, 1291]
    攻击次数1 = 3
    数据2 = [0, 644, 710, 776, 842, 907, 973, 1038, 1104, 1169, 1235, 1301, 1367, 1432, 1498, 1562, 1628, 1693, 1759,1824, 1891, 1956, 2021, 2087, 2152, 2218, 2282, 2348, 2414, 2480, 2545, 2611, 2676, 2742, 2807, 2873, 2939,3005, 3070, 3136, 3200, 3266, 3331, 3396, 3463, 3528, 3594, 3659, 3725, 3790, 3856, 3920, 3988, 4052, 4118,4183, 4249, 4314, 4380, 4445, 4512, 4577, 4643, 4708, 4774, 4838, 4903, 4969, 5035, 5101, 5166]
    攻击次数2 = 1
    数据3 = [0, 5166, 5690, 6215, 6739, 7264, 7788, 8311, 8836, 9360, 9884, 10409, 10933, 11456, 11981, 12505, 13028,13553, 14076, 14600, 15125, 15649, 16174, 16698, 17221, 17746, 18270, 18794, 19319, 19843, 20366, 20891,21415, 21940, 22464, 22988, 23512, 24036, 24560, 25085, 25609, 26134, 26657, 27181, 27706, 28230, 28754,29278, 29802, 30326, 30851, 31375, 31900, 32423, 32947, 33472, 33996, 34520, 35045, 35568, 36092, 36617, 37141, 37666, 38190, 38713, 39238, 39762, 40286, 40811, 41335]
    攻击次数3 = 1
    CD = 21.0
    攻击倍率 = 1.185
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.05
            self.攻击次数3 = 1 * 1.19
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.05 + 0.08
            self.攻击次数3 = 1 * 1.19
            self.CD *= 0.88

class 技能10(主动技能):
    名称 = '忍法：六道轮回'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['火遁·豪火球之术', '忍法：幻影手里剑', '火遁·飓风煞', '火遁·螺旋手里剑', '忍法：替身术', '火遁·炎天道','火遁·蟾蜍油炎弹','火遁·炎舞天璇','八岐大蛇','火遁·风魔手里剑','天照','勾玉之火·镰鼬']
    六道技能显示 = []
    CD = 31.5

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        temp = ''
        temp += '加成倍率:80%<br>'
        temp += '关联技能:'
        try:
            for i in range(len(self.六道技能显示) - 1):
                temp += self.六道技能显示[i] + ','
            temp += self.六道技能显示[len(self.六道技能显示) - 1]
        except:
            temp += '无'
        return temp

    def 加成倍率(self, 武器类型):
            return 1.0

class 技能11(主动技能):
    名称 = '火遁·炎舞天璇'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 403, 443, 485, 526, 566, 607, 647, 689, 730, 770, 811, 852, 893, 934, 974, 1016, 1056, 1097, 1137, 1178,1221, 1261, 1302, 1342, 1383, 1424, 1466, 1505, 1547, 1587, 1628, 1669, 1710, 1751, 1792, 1832, 1873, 1913,1955, 1997, 2036, 2078, 2118, 2159, 2200, 2241, 2282, 2323, 2363, 2404, 2444, 2487, 2527, 2568, 2609, 2649,2690, 2732, 2772, 2813, 2854, 2894, 2936, 2976, 3018, 3058, 3099, 3139, 3180, 3221]
    攻击次数1 = 8
    数据2 = [0, 122, 133, 145, 158, 169, 182, 194, 207, 219, 231, 243, 256, 268, 280, 292, 305, 317, 329, 341, 354, 366,378, 390, 403, 415, 426, 439, 452, 465, 477, 488, 501, 513, 526, 537, 550, 562, 575, 587, 598, 612, 623, 636,647, 661, 672, 684, 697, 709, 722, 733, 746, 758, 770, 782, 794, 807, 819, 833, 843, 856, 869, 881, 893, 905,918, 930, 942, 954, 967]
    攻击次数2 = 25
    数据3 = [0, 3323, 3660, 3996, 4333, 4670, 5007, 5344, 5681, 6018, 6354, 6691, 7029, 7367, 7704, 8040, 8377, 8713,9051, 9388, 9725, 10062, 10399, 10736, 11074, 11410, 11747, 12084, 12421, 12758, 13096, 13433, 13770, 14106,14442, 14779, 15117, 15455, 15792, 16129, 16465, 16802, 17139, 17476, 17813, 18150, 18487, 18823, 19161,19499, 19836, 20173, 20509, 20846, 21184, 21520, 21857, 22194, 22531, 22868, 23206, 23543, 23879, 24216,24553, 24890, 25228, 25565, 25902, 26239, 26575]
    攻击次数3 = 1
    CD = 33.6
    攻击倍率 = 1.129
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 8 - 5
            self.攻击次数2 = 25 * 2.15
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数1 = 8 - 5
            self.攻击次数2 = 25 * (2.15 + 0.23)
            self.CD *= 0.9

class 技能12(被动技能):
    名称 = '暗炎残星'
    所在等级 = 45
    等级上限 = 20
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.01 * self.等级, 5)

class 技能13(主动技能):
    名称 = '毕方之印'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    数据1=[0, 169, 196, 223, 250, 277, 304, 331, 358, 385, 412, 439, 466, 492, 519, 546, 573, 600, 627, 654, 681, 708, 735, 762, 789, 816, 843, 870, 897, 924, 951, 978, 1005, 1031, 1058, 1085, 1112, 1139, 1166, 1193, 1220, 1247, 1274, 1301, 1328, 1355, 1382, 1409, 1436, 1463, 1490, 1517, 1544, 1570, 1597, 1624, 1651, 1678, 1705, 1732, 1759, 1786, 1813, 1840, 1867, 1894, 1921, 1948, 1975, 2002, 2029]
    攻击次数1 = 8
    数据2=[0, 423, 490, 557, 625, 692, 760, 827, 894, 962, 1029, 1096, 1164, 1231, 1299, 1366, 1433, 1501, 1568, 1635, 1703, 1770, 1838, 1905, 1972, 2040, 2107, 2174, 2242, 2309, 2377, 2444, 2511, 2579, 2646, 2713, 2781, 2848, 2916, 2983, 3050, 3118, 3185, 3252, 3320, 3387, 3455, 3522, 3589, 3657, 3724, 3791, 3859, 3926, 3994, 4061, 4128, 4196, 4263, 4330, 4398, 4465, 4533, 4600, 4667, 4735, 4802, 4869, 4937, 5004, 5072]
    攻击次数2 = 1
    攻击倍率 = 0.991
    
    是否主动 = 0
    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '火属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (30 + 2 * self.等级)

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 ) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    def 等效CD(self, 武器类型,输出类型):
        return 1.0

class 技能14(主动技能):
    名称 = '火遁·冥炎业火阵'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    #数据1 = [0, 27341, 33687, 40028, 46370, 52709, 59053, 65397, 71737, 78078, 84421, 90761, 97102, 103446, 109787, 116126, 122469, 128813, 135153, 141494, 147835, 154178, 160518, 166861, 173204, 179543, 185887, 192228, 198569, 204911, 211251, 217594, 223936, 230279, 236618, 242961, 249300, 255646, 261987, 268329, 274669, 615050, 628926, 642810, 656687, 670567, 684449, 698329, 712209, 726088, 739970, 753851, 767728, 781612, 795489, 809371, 823248, 837131, 851009, 864885, 878771, 892648, 906531, 920408, 934289, 948170, 962047, 975928, 989814, 1003691, 1017570]
    data1 = [(i*1.0905*1.1/1.024) for i in[0, 3994, 4922, 5848, 6775, 7700, 8628, 9554, 10481, 11407, 12334, 13260, 14188, 15113, 16040, 16966, 17894, 18820, 19747, 20672, 21599, 22525, 23451, 24379, 25305, 26232, 27157, 28085, 29011, 29938, 30864, 31791, 32716, 33644, 34570, 35497, 36423, 37351, 38277, 39204, 40129, 89860, 91886, 93916, 95942, 97971, 99998, 102027, 104054, 106083, 108110, 110139, 112165, 114195, 116221, 118251, 120277, 122305, 124333, 126360, 128389, 130416, 132446, 134472, 136502, 138528, 140556, 142584, 144613, 146640, 148669]]
    data2 = [(i*1.0905*1.1/1.024) for i in[0, 5438, 6699, 7961, 9222, 10485, 11745, 13008, 14268, 15530, 16791, 18052, 19313, 20575, 21836, 23097, 24359, 25620, 26880, 28143, 29403, 30666, 31926, 33189, 34449, 35710, 36973, 38233, 39494, 40756, 42018, 43278, 44541, 45801, 47061, 48324, 49585, 50847, 52108, 53370, 54631, 122330, 125090, 127852, 130612, 133372, 136135, 138895, 141657, 144416, 147176, 149938, 152698, 155458, 158220, 160980, 163740, 166502, 169262, 172022, 174784, 177544, 180306, 183066, 185826, 188589, 191347, 194107, 196870, 199630, 202390]]
    data3 = [(i*1.0905*1.1/1.024) for i in[0, 7721, 9514, 11303, 13094, 14884, 16676, 18467, 20257, 22048, 23840, 25630, 27419, 29212, 31002, 32792, 34583, 36375, 38165, 39956, 41747, 43538, 45328, 47118, 48911, 50700, 52491, 54282, 56073, 57863, 59654, 61446, 63236, 65027, 66818, 68609, 70398, 72189, 73981, 75771, 77562, 173680, 177599, 181518, 185438, 189357, 193276, 197195, 201115, 205035, 208956, 212875, 216795, 220714, 224633, 228552, 232473, 236392, 240311, 244230, 248149, 252069, 255988, 259907, 263826, 267746, 271666, 275585, 279506, 283426, 287345]]
    data4 = [(i*1.0905*1.1/1.024) for i in[0, 9064, 11167, 13270, 15372, 17473, 19576, 21679, 23781, 25882, 27985, 30087, 32189, 34292, 36394, 38496, 40597, 42701, 44803, 46904, 49007, 51109, 53212, 55313, 57416, 59518, 61622, 63723, 65825, 67927, 70028, 72131, 74234, 76337, 78438, 80540, 82642, 84746, 86847, 88949, 91052, 203887, 208487, 213088, 217688, 222290, 226890, 231493, 236094, 240694, 245296, 249896, 254498, 259100, 263700, 268302, 272902, 277503, 282105, 286705, 291308, 295908, 300509, 305111, 309711, 314313, 318913, 323515, 328117, 332717, 337319]]
    data5 = [(i*1.0905*1.1/1.024) for i in[0, 1124, 1385, 1646, 1907, 2167, 2428, 2689, 2950, 3211, 3471, 3732, 3993, 4254, 4515, 4775, 5036, 5297, 5558, 5819, 6079, 6340, 6601, 6862, 7123, 7383, 7644, 7905, 8166, 8427, 8687, 8948, 9209, 9470, 9731, 9991, 10252, 10513, 10774, 11035, 11295, 25293, 25864, 26436, 27007, 27577, 28150, 28719, 29289, 29860, 30432, 31003, 31572, 32145, 32715, 33286, 33856, 34429, 34998, 35568, 36141, 36711, 37282, 37852, 38424, 38994, 39565, 40137, 40708, 41278, 41847]]
    data6 = [(i*1.0905*1.1/1.024) for i in[0, 0, 0, 776, 900, 1024, 1147, 1268, 1393, 1517, 1639, 1762, 1884, 2008, 2132, 2254, 2376, 2500, 2623, 2746, 2869, 2993, 3115, 3237, 3361, 3485, 3608, 3731, 3853, 3977, 4101, 4298, 4428, 4560, 4689, 4819, 4950, 5080, 5210, 5341, 5473, 12261, 12547, 12832, 13117, 13401, 13686, 13974, 14259, 14544, 14829, 15114, 15400, 15685, 15972, 16258, 16542, 16827, 17112, 17397, 17682, 17970, 18255, 18540, 18826, 19111, 19396, 19683, 19967, 20253, 20538]]
    数据 = [data1, data2, data3, data4, data5, data6]
    次数 = [1, 1, 1, 1, 1, 1, 9]
    CD = 152.3

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(6):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * self.倍率 * 1.0905 * 1.1

# 地面释放
class 技能15(主动技能):
    名称 = '忍法：飞燕手里剑'
    备注 = '(完全打满)'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 225, 248, 271, 293, 316, 338, 360, 388, 409, 430, 455, 476, 500, 522, 545, 568, 590, 616, 640, 658, 680, 705, 727, 752, 774, 797, 818, 841, 866, 888, 910, 931, 956, 980, 1002, 1027, 1047, 1071, 1094, 1118, 1139, 1162, 1185, 1208, 1229, 1251, 1275, 1299, 1323, 1345, 1369, 1393, 1416, 1440, 1463, 1487, 1511, 1534, 1558, 1582, 1606, 1629, 1653, 1677, 1701, 1724, 1747, 1772, 1795, 1819]
    攻击次数1 = 1
    数据2 = [0, 808, 887, 970, 1051, 1134, 1213, 1294, 1376, 1458, 1539, 1622, 1703, 1785, 1866, 1950, 2031, 2112, 2194, 2275, 2355, 2438, 2520, 2600, 2683, 2764, 2847, 2928, 3010, 3094, 3174, 3255, 3335, 3419, 3499, 3579, 3664, 3744, 3826, 3908, 3990, 4072, 4154, 4235, 4315, 4398, 4479, 4562, 4642, 4723, 4805, 4886, 4967, 5049, 5130, 5212, 5293, 5375, 5456, 5537, 5618, 5699, 5781, 5862, 5944, 6025, 6107, 6188, 6270, 6352, 6432]
    攻击次数2 = 15
    数据3 = [0, 444, 488, 535, 579, 623, 668, 713, 758, 803, 848, 893, 938, 983, 1029, 1073, 1118, 1163, 1208, 1253, 1297,1343, 1387, 1433, 1477, 1522, 1566, 1613, 1657, 1703, 1747, 1793, 1837, 1883, 1927, 1971, 2016, 2060, 2107,2151, 2197, 2241, 2287, 2331, 2377, 2421, 2466, 2510, 2556, 2600, 2646, 2690, 2734, 2779, 2824, 2868, 2913,2957, 3002, 3046, 3091, 3135, 3180, 3224, 3269, 3314, 3358, 3403, 3447, 3492, 3536]
    攻击次数3 = 10
    攻击倍率 = 0.68 * 1.154
    CD = 31.5
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.07
        elif x == 1:
            self.倍率 *= 1.07 + 0.09

class 技能16(主动技能):
    名称 = '火遁·风魔手里剑'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 222, 244, 267, 289, 312, 334, 357, 379, 402, 424, 447, 469, 492, 514, 537, 560, 582, 605, 627, 650, 672,695, 717, 740, 762, 785, 807, 830, 852, 875, 897, 920, 943, 965, 988, 1010, 1033, 1055, 1078, 1100, 1123,1145, 1168, 1190, 1213, 1235, 1258, 1280, 1303, 1326, 1348, 1371, 1393, 1416, 1438, 1461, 1483, 1506, 1528,1551, 1573, 1596, 1618, 1641, 1663, 1686, 1709, 1731, 1754, 1776]
    攻击次数1 = 15
    数据2 = [0, 499, 550, 601, 651, 702, 753, 803, 854, 905, 955, 1006, 1057, 1107, 1158, 1209, 1260, 1310, 1361, 1412,1462, 1513, 1564, 1614, 1665, 1716, 1766, 1817, 1868, 1919, 1969, 2020, 2071, 2121, 2172, 2223, 2273, 2324,2375, 2425, 2476, 2527, 2578, 2628, 2679, 2730, 2780, 2831, 2882, 2932, 2983, 3034, 3084, 3135, 3186, 3237,3287, 3338, 3389, 3439, 3490, 3541, 3591, 3642, 3693, 3743, 3794, 3845, 3896, 3946, 3997]
    攻击次数2 = 10
    数据3 = [0, 8327, 9172, 10017, 10862, 11707, 12552, 13397, 14241, 15086, 15931, 16776, 17621, 18466, 19311, 20155,21000, 21845, 22690, 23535, 24380, 25225, 26070, 26914, 27759, 28604, 29449, 30294, 31139, 31984, 32828,33673, 34518, 35363, 36208, 37053, 37898, 38742, 39587, 40432, 41277, 42122, 42967, 43812, 44656, 45501,46346, 47191, 48036, 48881, 49726, 50570, 51415, 52260, 53105, 53950, 54795, 55640, 56485, 57329, 58174,59019, 59864, 60709, 61554, 62399, 63243, 64088, 64933, 65778, 66623]
    攻击次数3 = 1
    CD = 42.0
    攻击倍率 = 1.124
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 = 10 + 10
            self.攻击次数3 = 1 * 1.14
        elif x == 1:
            self.攻击次数1 = 0
            self.攻击次数2 = 10 + 10
            self.攻击次数3 = 1 * (1.14 + 0.16)

class 技能17(主动技能):
    名称 = '八尺琼勾玉'
    备注 = '来回两次伤害'
    所在等级 = 70
    等级上限 = 1
    基础等级 = 1
    数据1 = [0, 740]
    攻击次数1 = 2
    数据2 = [0, 820]
    攻击次数2 = 2
    数据3 = [0, 850]
    攻击次数3 = 2
    CD = 3.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型,输出类型):
        # Will修改
        return round(self.CD  / self.恢复, 1)

class 技能18(被动技能):
    名称 = '八咫镜'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

class 技能19(主动技能):
    名称 = '八岐大蛇'
    备注 = '(者皆阵结印)'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 2139, 2271, 2404, 2536, 2668, 2800, 2933, 3066, 3198, 3331, 3462, 3595, 3727, 3860, 3992, 4125, 4257, 4389,4522, 4654, 4787, 4919, 5051, 5184, 5316, 5449, 5581, 5714, 5845, 5978, 6110, 6243, 6376, 6507, 6640, 6772,6905, 7037, 7170, 7301, 7434, 7567, 7699, 7832, 7964, 8096, 8228, 8361, 8494, 8626, 8759, 8890, 9023, 9155,9288, 9421, 9553, 9685, 9817, 9950, 10082, 10215, 10348, 10479, 10612, 10744, 10877, 11009, 11142, 11273]
    攻击次数1 = 1
    数据2 = [0, 2213, 2416, 2621, 2824, 3028, 3231, 3435, 3639, 3843, 4046, 4250, 4453, 4658, 4861, 5065, 5268, 5472,5676, 5880, 6083, 6287, 6490, 6695, 6898, 7101, 7305, 7508, 7713, 7916, 8120, 8323, 8527, 8731, 8935, 9138,9342, 9545, 9750, 9953, 10157, 10360, 10564, 10768, 10972, 11175, 11379, 11582, 11787, 11990, 12194, 12397,12600, 12805, 13008, 13212, 13415, 13619, 13823, 14027, 14230, 14434, 14637, 14842, 15045, 15249, 15452,15656, 15860, 16064, 16267]
    攻击次数2 = 10
    数据3 = [0, 346, 399, 453, 505, 558, 612, 664, 717, 770, 823, 876, 929, 982, 1034, 1088, 1141, 1193, 1247, 1300, 1352,1406, 1458, 1511, 1565, 1617, 1670, 1724, 1776, 1829, 1883, 1935, 1988, 2041, 2094, 2147, 2200, 2253, 2305,2359, 2412, 2464, 2518, 2571, 2623, 2677, 2729, 2782, 2836, 2888, 2941, 2995, 3047, 3100, 3154, 3206, 3259,3312, 3365, 3418, 3471, 3524, 3576, 3630, 3683, 3735, 3789, 3842, 3894, 3948, 4001]
    攻击次数3 = 22
    攻击倍率 = 0.94 * 1.125
    CD = 36.1
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 = (10 + 1) * 1.74
            self.攻击次数3 = 0

class 技能20(主动技能):
    名称 = '天照'
    备注 = '(者皆阵结印)'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 2695, 2968, 3242, 3515, 3789, 4062, 4335, 4609, 4882, 5156, 5429, 5702, 5976, 6250, 6523, 6796, 7070, 7342,7617, 7890, 8163, 8437, 8710, 8984, 9257, 9530, 9803, 10077, 10350, 10624, 10898, 11170, 11444, 11718, 11991,12264, 12538, 12811, 13085, 13358, 13631, 13905, 14178, 14452, 14725, 14998, 15272, 15546, 15819, 16092,16366, 16638, 16913, 17186, 17459, 17733, 18006, 18280, 18553, 18826, 19099, 19373, 19646, 19920, 20194,20466, 20740, 21014, 21287, 21560]
    攻击次数1 = 2
    数据2 = [0, 2869, 3160, 3451, 3742, 4034, 4325, 4616, 4907, 5198, 5489, 5780, 6071, 6362, 6653, 6944, 7235, 7526,7818, 8108, 8399, 8690, 8982, 9273, 9563, 9854, 10146, 10437, 10728, 11019, 11310, 11602, 11893, 12184,12474, 12766, 13057, 13348, 13638, 13930, 14221, 14512, 14803, 15094, 15385, 15676, 15967, 16258, 16549,16840, 17131, 17422, 17714, 18005, 18296, 18587, 18878, 19170, 19460, 19751, 20042, 20334, 20625, 20915,21206, 21498, 21789, 22080, 22370, 22662, 22953]
    攻击次数2 = 8
    攻击倍率 = 1.06 * 1.204#者皆阵倍率
    #攻击倍率 = 1.03  # 临兵斗倍率
    CD = 42.8
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 8 * 1.33
            self.CD *= 0.85

class 技能21(主动技能):
    名称 = '开二觉平x'
    备注 = '一轮平x'
    所在等级 = 85
    等级上限 = 1
    #学习间隔 = 5
    #等级精通 = 30
    基础等级 = 1
    #投掷火焰苦无
    数据1 = [0, 221, 237, 252, 267, 283, 298, 313, 329, 344, 359, 374, 389, 404, 419, 435, 450, 465, 481, 496, 511, 526,542, 557, 572, 587, 602, 617, 633, 648, 663, 678, 694, 709, 724, 740, 755, 770, 785, 800, 815, 830, 846, 861,876, 892, 907, 922, 938, 953, 968, 983, 998, 1013, 1028, 1044, 1059, 1074, 1090, 1105, 1120, 1135, 1151,1166, 1181, 1196, 1211, 1226, 1242, 1257, 1272]
    攻击次数1 = 6
    #火焰苦无爆炸 
    数据2 = [0, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 389, 400, 410, 419, 430, 440, 449, 460, 470, 479, 489,500, 509, 519, 530, 539, 549, 560, 569, 579, 589, 599, 609, 619, 629, 639, 649, 659, 669, 679, 689, 699, 709,719, 729, 739, 749, 759, 769, 779, 788, 799, 809, 818, 829, 839, 848, 859, 869, 878, 888, 899, 908, 918, 929,938, 948, 959, 968, 978]
    攻击次数2 = 6
    # 地面斩击
    数据3 = [0, 923, 949, 975, 1001, 1028, 1054, 1080, 1106, 1133, 1159, 1185, 1211, 1238, 1264, 1290, 1316, 1343, 1369,1395, 1421, 1448, 1474, 1500, 1526, 1553, 1579, 1605, 1631, 1658, 1684, 1710, 1736, 1763, 1789, 1815, 1841,1868, 1894, 1920, 1946, 1973, 1999, 2025, 2051, 2078, 2104, 2130, 2156, 2183, 2209, 2235, 2261, 2288, 2314,2340, 2366, 2393, 2419, 2445, 2471, 2498, 2524, 2550, 2576, 2603, 2629, 2655, 2681, 2708, 2734]
    攻击次数3 = 2
    攻击倍率3 = 0.65
    攻击倍率 = 1.05 * 1.12
    CD = 1.0
    
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 * self.攻击倍率3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    def 等效CD(self, 武器类型,输出类型):
        # Will修改
        return round(self.CD  / self.恢复, 1)


class 技能22(主动技能):
    名称 = '火炎灼空：草雉剑'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 3923, 4833, 5743, 6652, 7562, 8472, 9381, 10291, 11201, 12110, 13020, 13930, 14840, 15749, 16659, 17569,18478, 19388, 20299, 21209, 22118, 23028, 23938, 24847, 25757, 26667, 27576, 28486, 29396, 30305, 31215,32125, 33035, 33944, 34854, 35764, 36673, 37583, 38493, 39402, 40312, 41222, 42131, 43041, 43951, 44861,45770, 46680, 47590, 48499, 49409, 50319, 51230, 52139, 53049, 53959, 54868, 55778, 56688, 57597, 58507,59417, 60327, 61236, 62146, 63056, 63965, 64875, 65785, 66694]
    攻击次数1 = 1
    数据2 = [0, 19877, 24487, 29095, 33705, 38314, 42923, 47532, 52142, 56750, 61360, 65969, 70578, 75187, 79797, 84406,89015, 93625, 98233, 102843, 107452, 112061, 116670, 121280, 125888, 130498, 135106, 139716, 144325, 148934,153544, 158153, 162763, 167371, 171981, 176589, 181199, 185808, 190417, 195026, 199636, 204244, 208854,213464, 218072, 222682, 227291, 231900, 236509, 241119, 245727, 250337, 254945, 259555, 264164, 268774,273382, 277992, 282602, 287210, 291820, 296428, 301038, 305647, 310256, 314865, 319475, 324083, 328693,333302, 337911]
    攻击次数2 = 3
    攻击倍率 = 1.158
    CD = 189.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能23(被动技能):
    名称 = '三元刹'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能24(主动技能):
    名称 = '勾玉之火·镰鼬'
    备注 = '(者皆阵结印)'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    基础 = 8712.2 * 1.06 / 1.045
    成长 = 983.8 * 1.06  / 1.045
    攻击次数 = 1
    基础2 = 1161.8 * 1.06 / 1.045
    成长2 = 131.2 * 1.06 / 1.045
    攻击次数2 = 30
    基础3 = 41098 * 1.06  / 1.045
    成长3 = 4640 * 1.06  / 1.045
    攻击次数3 = 1
    CD = 50.4

    #def 等效百分比(self, 武器类型):
        #return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能25(主动技能):
    名称 = '火源限界·八咫乌'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    基础 = 4556.75
    成长 = 1375.25
    攻击次数 = 12
    基础2 = 5858.75
    成长2 = 1768.25
    攻击次数2 = 14
    基础3 = 136696.75
    成长3 = 41266.25
    攻击次数3 = 1
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

一觉序号 = 0
二觉序号 = 0
三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        三觉序号 = 技能序号[i.名称]

护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)


class 职业属性(角色属性):
    实际名称 = '隐夜·忍者'
    角色 = '暗夜使者'
    职业 = '忍者'

    武器选项 = ['苦无']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力', '力量']

    主BUFF = 2.04

    远古记忆 = 0

    六道绑定技能 = []

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['毕方之印']].攻击次数1 = int(self.时间输入/2.5)
        self.技能栏[self.技能序号['毕方之印']].攻击次数2 = math.ceil(self.时间输入 / 10) - 1
        self.火属性强化 += self.技能栏[self.技能序号['毕方之印']].属强加成()
        self.技能栏[21].等级 = self.技能栏[22].等级

    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        #初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        #六道伤害计算
        if self.技能栏[self.技能序号['忍法：六道轮回']].等级 != 0 and 技能释放次数[self.技能序号['忍法：六道轮回']] !=0 :
           self.技能栏[self.技能序号['忍法：六道轮回']].六道技能显示 = []
           默认宠物技能 = ['火遁·炎天道', '火遁·蟾蜍油炎弹', '火遁·炎舞天璇', '八岐大蛇', '火遁·风魔手里剑', '天照']
           if self.宠物次数[self.技能序号['忍法：六道轮回']] == 0 :
               self.宠物次数[self.技能序号['忍法：六道轮回']] = 0
           else:
               self.宠物次数[self.技能序号['忍法：六道轮回']] = 1
           for i in self.六道绑定技能:
               if 技能释放次数[self.技能序号[i]] != 0 and self.技能栏[self.技能序号[i]].等级 != 0:
                   if i in 默认宠物技能:
                       技能总伤害[self.技能序号[i]] += 0.8 * 技能单次伤害[self.技能序号[i]]  * (1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号['忍法：六道轮回']]+self.斗神之吼秘药*0.12)
                       默认宠物技能.remove(i)
                       self.技能栏[self.技能序号['忍法：六道轮回']].六道技能显示.append(i)
                   else:
                       技能总伤害[self.技能序号[i]] += 0.8 * 技能单次伤害[self.技能序号[i]]  * (1+self.白兔子技能*0.20 + self.斗神之吼秘药*0.12)
                       self.技能栏[self.技能序号['忍法：六道轮回']].六道技能显示.append(i)
        else:
            self.技能栏[self.技能序号['忍法：六道轮回']].自定义描述 = 0

        #返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)

class 隐夜·忍者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           num = 0
           for i in range(len(self.可绑定技能)):
               self.绑定技能次数[i].setCurrentIndex(int(setfile[num].replace('\n', '')));
               num += 1
        except:
            pass

    def 保存配置(self, path='set'):
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            for i in range(len(self.可绑定技能)):
                setfile.write(str(self.绑定技能次数[i].currentIndex()) + '\n')
        except:
            pass
        
    def 界面(self):
        super().界面()

        self.六道绑定按钮 = []
        self.可绑定技能 = ['火遁·豪火球之术', '忍法：幻影手里剑', '火遁·飓风煞', '火遁·螺旋手里剑','忍法：替身术','火遁·炎天道','火遁·蟾蜍油炎弹', '火遁·炎舞天璇', '八岐大蛇','火遁·风魔手里剑', '天照']
        self.绑定技能次数 = []

        水平间隔 = 210
        竖直间隔 = 30

        for i in range(len(self.可绑定技能)):
            self.六道绑定按钮.append(QLabel(self.可绑定技能[i], self.main_frame2))
            self.六道绑定按钮[i].setAlignment(Qt.AlignCenter)
            self.六道绑定按钮[i].resize(100, 20)
            self.六道绑定按钮[i].move(325 + (i % 2) * 水平间隔, 420 + int(i / 2) * 竖直间隔)
            self.六道绑定按钮[i].setStyleSheet(白色字体标签)
            self.绑定技能次数.append(MyQComboBox(self.main_frame2))
            self.绑定技能次数[i].resize(48, 20)
            self.绑定技能次数[i].move(440 + (i % 2) * 水平间隔, 420 + int(i / 2) * 竖直间隔)
            self.绑定技能次数[i].addItem('0')
            self.绑定技能次数[i].addItem('1')
            self.绑定技能次数[i].addItem('2')


    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        for i in range(len(self.可绑定技能)):
            if self.次数输入[self.角色属性A.技能序号[self.可绑定技能[i]]].currentIndex() != 0:
                self.绑定技能次数[i].setCurrentIndex(min(self.绑定技能次数[i].currentIndex(), self.次数输入[self.角色属性A.技能序号[self.可绑定技能[i]]].currentIndex() - 1))
        temp = []
        for i in range(len(self.可绑定技能)):
            if self.绑定技能次数[i].currentIndex() == 1:
                temp.append(self.可绑定技能[i])
            elif self.绑定技能次数[i].currentIndex() == 2:
                temp.append(self.可绑定技能[i])
                temp.append(self.可绑定技能[i])
        属性.六道绑定技能 = deepcopy(temp)
    
    

