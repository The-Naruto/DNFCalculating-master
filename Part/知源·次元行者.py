from PublicReference.base import *

等级 = 100 + 5

class 知源·次元行者主动技能(主动技能):
    攻击次数1 = 1
    数据1 = []
    数据2 = []
    数据3 = []

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            总倍率 = 1
            if not self.数据1 == []:
                总倍率 += self.攻击次数1 * self.数据1[self.等级]
            if not self.数据2 == []:
                总倍率 += self.攻击次数2 * self.数据2[self.等级]
            if not self.数据3 == []:
                总倍率 += self.攻击次数3 * self.数据3[self.等级]
            总倍率 *= (1 + self.TP成长 * self.TP等级) * self.倍率
            return 总倍率


class 知源·次元行者技能0(被动技能):
    名称 = '次元扭曲装置'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(1.15 + 0.02 * (self.等级-10), 5)

class 知源·次元行者技能1(被动技能):
    名称 = '乖离虚无'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['次元虚影', '次元跃迁', '次元离子束', '次元坠落', '次元万花镜', '次元粒子风暴', '次元时空磁场', '次元粒子波',
            '次元思维聚爆', '次元奇点', '禁断之盛宴', '次元乖离理性崩坏'] #次元系技能

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1. + 0.015 * self.等级, 5)

class 知源·次元行者技能2(被动技能):
    名称 = '虚空之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 知源·次元行者技能3(被动技能):
    名称 = '混沌源能石'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class 知源·次元行者技能4(知源·次元行者主动技能):
    名称 = '次元坠落'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 1
    # 基础伤害
    攻击次数1 = 1

    数据1 = [ int(i*1.131) for i in [0, 392, 432, 472, 512, 551, 591, 631, 671, 711, 750, 790, 830, 870, 910, 950, 989, 1029, 1069, 1109, 1149,
          1189, 1228, 1268, 1308, 1348, 1388, 1428, 1467, 1507, 1547, 1587, 1627, 1666, 1706, 1746, 1786, 1826, 1866,
          1905, 1945, 1985, 2025, 2065, 2105, 2144, 2184, 2224, 2264, 2304, 2343, 2383, 2423, 2463, 2503, 2543, 2582,
          2622, 2662, 2702, 2742, 2782, 2821, 2861, 2901, 2941, 2981, 3021, 3060, 3100, 3140]]
    数据2 = [ int(i*1.131) for i in [0, 1333, 1468, 1603, 1739, 1874, 2009, 2144, 2280, 2415, 2550, 2685, 2821, 2956, 3091, 3226, 3362, 3497,
           3632, 3767, 3903, 4038, 4173, 4309, 4444, 4579, 4714, 4850, 4985, 5120, 5255, 5391, 5526, 5661, 5796, 5932,
           6067, 6202, 6337, 6473, 6608, 6743, 6879, 7014, 7149, 7284, 7420, 7555, 7690, 7825, 7961, 8096, 8231, 8366,
           8502, 8637, 8772, 8907, 9043, 9178, 9313, 9448, 9584, 9719, 9854, 9990, 10125, 10260, 10395, 10531, 10666]]
    #基础 = 1549.886
    #成长 = 175.090

    攻击次数2 = 1
    # 30%概率触发箱子，额外伤害
    攻击次数3 = 1
    数据3 = [ int(i*1.131) for i in [0, 1680, 1850, 2021, 2191, 2362, 2532, 2703, 2873, 3044, 3214, 3384, 3555, 3725, 3896, 4066, 4237, 4407,
           4578, 4748, 4919, 5089, 5260, 5430, 5601, 5771, 5941, 6112, 6282, 6453, 6623, 6794, 6964, 7135, 7305, 7476,
           7646, 7817, 7987, 8158, 8328, 8498, 8669, 8839, 9010, 9180, 9351, 9521, 9692, 9862, 10033, 10203, 10374,
           10544, 10715, 10885, 11055, 11226, 11396, 11567, 11737, 11908, 12078, 12249, 12419, 12590, 12760, 12931,
           13101, 13272, 13442]]
    #基础2 = 1509.534
    #成长2 = 170.466
    TP成长 = 0.08
    TP上限 = 5
    CD = 4.



class 知源·次元行者技能5(知源·次元行者主动技能):
    名称 = '次元跃迁'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    数据1 = [ int(i*1.121) for i in [0, 4943, 5731, 6519, 7307, 8095, 8883, 9671, 10459, 11248,
          12036, 12824, 13612, 14400, 15188, 15976, 16764, 17552, 18340, 19128,
          19916, 20704, 21493, 22281, 23069, 23857, 24645, 25433, 26221, 27009,
          27797]]
    #基础 = 4154.954
    #成长 = 788.050
    攻击次数1 = 1
    CD = 15.0
    CD数据 = [15.0, 15.0, 14.8, 14.7, 14.5, 14.4, 14.2, 14.0, 13.9, 13.8, 13.6, 13.4, 13.3, 13.1, 13.0,
            12.8, 12.7, 12.5, 12.4, 12.2, 12.0, 11.9, 11.7, 11.6, 11.4, 11.3, 11.1, 11.0, 10.8, 10.7, 10.5]

    def 等效CD(self, 武器类型,输出类型):
        if self.等级 <= 30:
            return round(self.CD数据[self.等级] / self.恢复, 1)
        else:
            return round(10.5 / self.恢复, 1)

class 知源·次元行者技能6(知源·次元行者主动技能):
    名称 = '次元虚影'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 1
    数据1 = [ int(i*1.121) for i in [0, 2639, 2907, 3175, 3443, 3711, 3978, 4246, 4514, 4782, 5050, 5318, 5585, 5853, 6121, 6389, 6657, 6924, 7192,
          7460, 7728, 7996, 8263, 8531, 8799, 9067, 9335, 9603, 9870, 10138, 10406, 10674, 10942, 11209, 11477, 11745,
          12013, 12281, 12549, 12816, 13084, 13352, 13620, 13888, 14155, 14423, 14691, 14959, 15227, 15494, 15762,
          16030, 16298, 16566, 16834, 17101, 17369, 17637, 17905, 18173, 18440, 18708, 18976, 19244, 19512, 19780,
          20047, 20315, 20583, 20851, 21119]]
    #基础 = 2371.133
    #成长 = 267.834
    攻击次数1 = 1
    TP成长 = 0.10
    TP上限 = 5
    CD = 5.0

class 知源·次元行者技能7(知源·次元行者主动技能):
    名称 = '乖离禁忌的奈雅丽'
    备注 = '(近战普攻)'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 5
    数据1 = [ int(i*1.12) for i in [0, 812, 894, 976, 1059, 1142, 1223, 1306, 1388, 1470, 1553, 1635, 1718, 1800, 1882, 1965, 2048, 2129, 2212,
           2294, 2376, 2459, 2541, 2624, 2706, 2788, 2871, 2954, 3035, 3118, 3200, 3282, 3365, 3447, 3530, 3612, 3694,
           3777, 3860, 3941, 4024, 4106, 4188, 4271, 4353, 4436, 4518, 4600, 4683, 4764, 4847, 4930, 5012, 5094, 5177,
           5259, 5342, 5424, 5506, 5589, 5670, 5753, 5836, 5918, 6000, 6083, 6165, 6248, 6330, 6412, 6495]]
    #基础 = 729.662
    #成长 = 82.356
    攻击次数1 = 1
    CD = 60.
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ["所有"]
    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '独立攻击力增加{:.1%}'.format( self.独立攻击力倍率进图(武器类型)-1 )
    def 独立攻击力倍率进图(self, 武器类型):
        return 1.10
    def 加成倍率(self, 武器类型):
        return 1.10

class 知源·次元行者技能8(知源·次元行者主动技能):
    名称 = '次元离子束'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 不强化
    数据1 = [ int(i*1.121) for i in [0, 588, 647, 707, 767, 826, 886, 946, 1005, 1065, 1125, 1184, 1244, 1304, 1363, 1423, 1483, 1542, 1602, 1662,
          1721, 1781, 1841, 1900, 1960, 2020, 2079, 2139, 2199, 2258, 2318, 2378, 2437, 2497, 2557, 2616, 2676, 2736,
          2795, 2855, 2915, 2974, 3034, 3094, 3153, 3213, 3273, 3332, 3392, 3452, 3511, 3571, 3631, 3690, 3750, 3810,
          3869, 3929, 3989, 4048, 4108, 4168, 4227, 4287, 4347, 4406, 4466, 4526, 4585, 4645, 4705]]
    #基础 = 3169.986
    #成长 = 357.901
    攻击次数1 = 6
    # 强化
    数据2 = [ int(i*1.121) for i in [0, 4569, 5032, 5496, 5960, 6423, 6887, 7350, 7814, 8277, 8741, 9204, 9668, 10132, 10595, 11059, 11522, 11986,
           12449, 12913, 13376, 13840, 14304, 14767, 15231, 15694, 16158, 16621, 17085, 17548, 18012, 18476, 18939,
           19403, 19866, 20330, 20793, 21257, 21720, 22184, 22648, 23111, 23575, 24038, 24502, 24965, 25429, 25892,
           26356, 26820, 27283, 27747, 28210, 28674, 29137, 29601, 30064, 30528, 30992, 31455, 31919, 32382, 32846,
           33309, 33773, 34236, 34700, 35164, 35627, 36091, 36554]]
    #基础2 = 4105.465
    #成长2 = 463.549
    攻击次数2 = 1
    TP成长 = 0.10
    TP上限 = 5
    CD = 7.

class 知源·次元行者技能9(知源·次元行者主动技能):
    名称 = '次元万花镜'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 不强化
    数据1 = [ int(i*1.121) for i in [0, 1799, 1982, 2164, 2347, 2530, 2712, 2895, 3077, 3260, 3443, 3625, 3808, 3990, 4173, 4355, 4538, 4721, 4903,
          5086, 5268, 5451, 5634, 5816, 5999, 6181, 6364, 6546, 6729, 6912, 7094, 7277, 7459, 7642, 7825, 8007, 8190,
          8372, 8555, 8738, 8920, 9103, 9285, 9468, 9650, 9833, 10016, 10198, 10381, 10563, 10746, 10929, 11111, 11294,
          11476, 11659, 11841, 12024, 12207, 12389, 12572, 12754, 12937, 13120, 13302, 13485, 13667, 13850, 14032,
          14215, 14398]]
    #基础 = 1616.371
    #成长 = 182.596
    攻击次数1 = 4
    # 强化
    数据2 = [ int(i*1.121) for i in [0, 1444, 1591, 1738, 1884, 2031, 2177, 2324, 2470, 2617, 2764, 2910, 3057, 3203, 3350, 3497, 3643, 3790,
           3936, 4083, 4230, 4376, 4523, 4669, 4816, 4962, 5109, 5256, 5402, 5549, 5695, 5842, 5989, 6135, 6282, 6428,
           6575, 6721, 6868, 7015, 7161, 7308, 7454, 7601, 7748, 7894, 8041, 8187, 8334, 8480, 8627, 8774, 8920, 9067,
           9213, 9360, 9507, 9653, 9800, 9946, 10093, 10239, 10386, 10533, 10679, 10826, 10972, 11119, 11266, 11412,
           11559]]
    #基础2 = 1297.444
    #成长2 = 146.593
    攻击次数2 = 4
    TP成长 = 0.10
    TP上限 = 5
    CD = 12.

class 知源·次元行者技能10(知源·次元行者主动技能):
    名称 = '乖离魅魔之舞'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 不强化
    数据1 = [ int(i*1.119) for i in [0, 190, 209, 228, 248, 267, 286, 306, 325, 344, 364, 383, 402, 422, 441, 460, 480, 499, 518, 537, 557, 576,
           595, 615, 634, 653, 673, 692, 711, 731, 750, 769, 789, 808, 827, 846, 866, 885, 904, 924, 943, 962, 982,
           1001, 1020, 1040, 1059, 1078, 1098, 1117, 1136, 1155, 1175, 1194, 1213, 1233, 1252, 1271, 1291, 1310, 1329,
           1349, 1368, 1387, 1407, 1426, 1445, 1464, 1484, 1503, 1522]]
    数据2 = [ int(i*1.119) for i in [0, 3238, 3566, 3895, 4224, 4552, 4881, 5209, 5538, 5866, 6195, 6523, 6852, 7180, 7509, 7837, 8166, 8494,
           8823, 9152, 9480, 9809, 10137, 10466, 10794, 11123, 11451, 11780, 12108, 12437, 12765, 13094, 13422, 13751,
           14080, 14408, 14737, 15065, 15394, 15722, 16051, 16379, 16708, 17036, 17365, 17693, 18022, 18350, 18679,
           19008, 19336, 19665, 19993, 20322, 20650, 20979, 21307, 21636, 21964, 22293, 22621, 22950, 23278, 23607,
           23936, 24264, 24593, 24921, 25250, 25578, 25907]]
    #基础 = 5470.737
    #成长 = 617.995
    攻击次数1 = 15
    攻击次数2 = 1
    CD = 10.
    TP成长 = 0.10
    TP上限 = 5

class 知源·次元行者技能11(知源·次元行者主动技能):
    名称 = '次元粒子风暴'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 不强化
    数据1 = [ int(i*1.11) for i in [0, 2576, 2837, 3098, 3360, 3621, 3882, 4144, 4405, 4666, 4928, 5189, 5450, 5712, 5973, 6234, 6496, 6757, 7018,
          7280, 7541, 7802, 8064, 8325, 8586, 8848, 9109, 9370, 9632, 9893, 10154, 10416, 10677, 10938, 11200, 11461,
          11722, 11984, 12245, 12506, 12768, 13029, 13290, 13552, 13813, 14074, 14336, 14597, 14858, 15120, 15381,
          15642, 15904, 16165, 16426, 16688, 16949, 17210, 17472, 17733, 17994, 18256, 18517, 18778, 19040, 19301,
          19562, 19824, 20085, 20346, 20608]]
    #基础 = 2314.648
    #成长 = 261.315
    攻击次数1 = 3
    # 强化
    数据2 = [ int(i*1.11) for i in [0, 9864, 10865, 11866, 12866, 13867, 14868, 15869, 16869, 17870, 18871, 19872, 20872, 21873, 22874, 23875,
           24876, 25876, 26877, 27878, 28879, 29879, 30880, 31881, 32882, 33882, 34883, 35884, 36885, 37885, 38886,
           39887, 40888, 41888, 42889, 43890, 44891, 45891, 46892, 47893, 48894, 49895, 50895, 51896, 52897, 53898,
           54898, 55899, 56900, 57901, 58901, 59902, 60903, 61904, 62904, 63905, 64906, 65907, 66907, 67908, 68909,
           69910, 70910, 71911, 72912, 73913, 74913, 75914, 76915, 77916, 78917]]
    #基础2 = 8863.268
    #成长2 = 1000.770
    攻击次数2 = 1
    CD = 16.
    是否有护石 = 1
    TP成长 = 0.10
    TP上限 = 5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
            self.攻击次数1 = 0
            self.攻击次数2 = 1
        elif x == 1:
            self.倍率 *= 1.31
            self.攻击次数1 = 0
            self.攻击次数2 = 1
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>边界之限</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 粒子风暴]<br>"
            temp += "以次元边界效果发动 (不消耗次元石)<br>"
            temp += "攻击力 +12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸速度 +50%<br>"
            temp += "冲击波范围 +10%<br>"
            temp += "攻击力 +10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>边界之限</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 粒子风暴]<br>"
            temp += "以次元边界效果发动 (不消耗次元石)<br>"
            temp += "攻击力 +12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸速度 +50%<br>"
            temp += "冲击波范围 +10%<br>"
            temp += "攻击力 +19%"
        return temp


class 知源·次元行者技能12(知源·次元行者主动技能):
    名称 = '次元时空磁场'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [ int(i*1.12) for i in [0, 3442, 3792, 4141, 4490, 4840, 5189, 5538, 5887, 6237, 6586, 6935, 7285, 7634, 7983, 8332, 8682, 9031, 9380,
          9730, 10079, 10428, 10777, 11127, 11476, 11825, 12174, 12524, 12873, 13222, 13572, 13921, 14270, 14619, 14969,
          15318, 15667, 16017, 16366, 16715, 17064, 17414, 17763, 18112, 18462, 18811, 19160, 19509, 19859, 20208,
          20557, 20907, 21256, 21605, 21954, 22304, 22653, 23002, 23352, 23701, 24050, 24399, 24749, 25098, 25447,
          25796, 26146, 26495, 26844, 27194, 27543]]
    #基础 = 3092.684
    #成长 = 349.684
    攻击次数1 = 2
    TP成长 = 0.10
    TP上限 = 5
    CD = 15.

class 知源·次元行者技能13(知源·次元行者主动技能):
    名称 = '乖离异界蜂群'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 20 + 6
    数据1 = [ int(i*1.119) for i in [0, 712, 785, 857, 929, 1002, 1074, 1146, 1219, 1291, 1363, 1436, 1508, 1580, 1653, 1725, 1797, 1870, 1942,
           2014, 2087, 2159, 2231, 2304, 2376, 2448, 2521, 2593, 2665, 2738, 2810, 2882, 2955, 3027, 3099, 3172, 3244,
           3316, 3388, 3461, 3533, 3605, 3678, 3750, 3822, 3895, 3967, 4039, 4112, 4184, 4256, 4329, 4401, 4473, 4546,
           4618, 4690, 4763, 4835, 4907, 4980, 5052, 5124, 5197, 5269, 5341, 5414, 5486, 5558, 5631, 5703]]
    数据2 = [ int(i*1.119) for i in [0, 151, 167, 182, 197, 213, 228, 244, 259, 274, 290, 305, 320, 336, 351, 367, 382, 397, 413, 428, 444, 459,
           474, 490, 505, 521, 536, 551, 567, 582, 597, 613, 628, 644, 659, 674, 690, 705, 721, 736, 751, 767, 782, 798,
           813, 828, 844, 859, 874, 890, 905, 921, 936, 951, 967, 982, 998, 1013, 1028, 1044, 1059, 1074, 1090, 1105,
           1121, 1136, 1151, 1167, 1182, 1198, 1213]]
    #基础 = 13606.954
    #成长 = 1539.337
    攻击次数1 = 20
    攻击次数2 = 6
    CD = 25.
    是否有护石 = 1
    TP成长 = 0.10
    TP上限 = 5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 23
            self.倍率 *= 1.06
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数1 = 23
            self.倍率 *= 1.14
            self.CD *= 0.9
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>苦痛引导</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乖离 : 异界蜂群]<br>"
            temp += "虫群数量 +3只<br>"
            temp += "奈雅丽在地图上时， 奈雅丽代替施放者发动技能 (不消耗HP)<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "蜂群登场时间 -0.5秒<br>"
            temp += "攻击力 +6%<br>"
            temp += "冷却时间 -10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>苦痛引导</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乖离 : 异界蜂群]<br>"
            temp += "虫群数量 +3只<br>"
            temp += "奈雅丽在地图上时， 奈雅丽代替施放者发动技能 (不消耗HP)<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "蜂群登场时间 -0.5秒<br>"
            temp += "攻击力 +14%<br>"
            temp += "冷却时间 -10%"
        return temp

class 知源·次元行者技能14(知源·次元行者主动技能):
    名称 = '次元粒子波'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 一类裂隙
    数据1 = [ int(i*1.083) for i in [0, 966, 1063, 1162, 1258, 1357, 1456, 1552, 1651, 1750, 1847, 1945, 2042, 2141, 2239, 2336, 2435, 2531, 2630,
          2729, 2825, 2924, 3021, 3119, 3218, 3315, 3414, 3510, 3609, 3708, 3804, 3903, 4002, 4098, 4197, 4294, 4392,
          4491, 4588, 4687, 4783, 4882, 4981, 5077, 5176, 5273, 5371, 5470, 5567, 5665, 5762, 5861, 5960, 6056, 6155,
          6254, 6350, 6449, 6546, 6644, 6743, 6840, 6938, 7035, 7134, 7232, 7329, 7428, 7525, 7623, 7722]]
    #基础 = 868.110
    #成长 = 97.900
    攻击次数1 = 10
    # 二类裂隙
    数据2 = [ int(i*1.07) for i in [0, 693, 764, 834, 905, 975, 1045, 1116, 1186, 1256, 1327, 1397, 1468, 1538, 1608, 1679, 1749, 1820, 1890,
           1960, 2031, 2101, 2172, 2242, 2312, 2383, 2453, 2524, 2594, 2664, 2735, 2805, 2875, 2946, 3016, 3087, 3157,
           3227, 3298, 3368, 3439, 3509, 3579, 3650, 3720, 3791, 3861, 3931, 4002, 4072, 4143, 4213, 4283, 4354, 4424,
           4494, 4565, 4635, 4706, 4776, 4846, 4917, 4987, 5058, 5128, 5198, 5269, 5339, 5410, 5480, 5550]]
    #基础2 = 622.557
    #成长2 = 70.401
    攻击次数2 = 20
    CD = 40.
    是否有护石 = 1
    TP成长 = 0.10
    TP上限 = 5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.11
            self.倍率 *= 1.10
        elif x == 1:
            self.倍率 *= 1.10
            self.倍率 *= 1.17
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>重力爆炸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 粒子波]<br>"
            temp += "施放技能时将敌人聚拢到中心<br>"
            temp += "攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "吸附范围 +20%<br>"
            temp += "技能中心点设置时空爆雷， 造成[次元 : 粒子波]总攻击力10%的伤害"
        elif x == 1:
            temp = "<font color='#FF00FF'>重力爆炸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 粒子波]<br>"
            temp += "施放技能时将敌人聚拢到中心<br>"
            temp += "攻击力 +17%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "吸附范围 +20%<br>"
            temp += "技能中心点设置时空爆雷， 造成[次元 : 粒子波]总攻击力10%的伤害"
        return temp

class 知源·次元行者技能15(知源·次元行者主动技能):
    名称 = '乖离扭曲之恐惧'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 出现
    数据1 = [ int(i*1.108) for i in [0, 5803, 7149, 8494, 9840, 11186, 12532, 13877, 15223, 16569, 17914, 19260, 20606, 21952, 23297, 24643, 25989,
          27334, 28680, 30026, 31372, 32717, 34063, 35409, 36754, 38100, 39446, 40792, 42137, 43483, 44829, 46175,
          47520, 48866, 50212, 51557, 52903, 54249, 55595, 56940, 58286, 59632, 60977, 62323, 63669, 65015, 66360,
          67706, 69052, 70397, 71743, 73089, 74435, 75780, 77126, 78472, 79817, 81163, 82509, 83855, 85200, 86546,
          87892, 89238, 90583, 91929, 93275, 94620, 95966, 97312, 98658]]
    #基础 = 4458.014
    #成长 = 1345.666
    攻击次数1 = 1
    # 触须
    数据2 = [ int(i*1.108) for i in [0, 1261, 1554, 1846, 2139, 2431, 2724, 3016, 3309, 3601, 3894, 4187, 4479, 4772, 5064, 5357, 5649, 5942,
           6234, 6527, 6820, 7112, 7405, 7697, 7990, 8282, 8575, 8867, 9160, 9452, 9745, 10038, 10330, 10623, 10915,
           11208, 11500, 11793, 12085, 12378, 12670, 12963, 13256, 13548, 13841, 14133, 14426, 14718, 15011, 15303,
           15596, 15888, 16181, 16474, 16766, 17059, 17351, 17644, 17936, 18229, 18521, 18814, 19107, 19399, 19692,
           19984, 20277, 20569, 20862, 21154, 21447]]
    #基础2 = 968.875
    #成长2 = 292.508
    攻击次数2 = 22
    # 结束爆发
    数据3 = [ int(i*1.108) for i in [0, 23213, 28596, 33979, 39362, 44745, 50128, 55510, 60893, 66276, 71659, 77042, 82425, 87808, 93191, 98573,
           103956, 109339, 114722, 120105, 125488, 130871, 136254, 141636, 147019, 152402, 157785, 163168, 168551,
           173934, 179317, 184700, 190082, 195465, 200848, 206231, 211614, 216997, 222380, 227763, 233145, 238528,
           243911, 249294, 254677, 260060, 265443, 270826, 276208, 281591, 286974, 292357, 297740, 303123, 308506,
           313889, 319271, 324654, 330037, 335420, 340803, 346186, 351569, 356952, 362334, 367717, 373100, 378483,
           383866, 389249, 394632]]
    #基础3 = 17829.336 *1.1
    #成长3 = 5382.970 *1.1
    攻击次数3 = 1 * 1.1
    CD = 145.

class 知源·次元行者技能16(知源·次元行者主动技能):
    名称 = '次元思维聚爆'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    # 持续伤害
    数据1 = [ int(i*1.121) for i in [0, 502, 553, 603, 654, 705, 756, 807, 858, 909, 960, 1011, 1062, 1113, 1164, 1215, 1266, 1317, 1368, 1418,
          1469, 1520, 1571, 1622, 1673, 1724, 1775, 1826, 1877, 1928, 1979, 2030, 2081, 2132, 2183, 2233, 2284, 2335,
          2386, 2437, 2488, 2539, 2590, 2641, 2692, 2743, 2794, 2845, 2896, 2947, 2998, 3048, 3099, 3150, 3201, 3252,
          3303, 3354, 3405, 3456, 3507, 3558, 3609, 3660, 3711, 3762, 3813, 3863, 3914, 3965, 4016]]
    #基础 = 451.063
    #成长 = 50.909
    攻击次数1 = 1
    # 爆发伤害
    数据2 = [ int(i*1.121) for i in [0, 16227, 17873, 19519, 21165, 22811, 24458, 26104, 27750, 29396, 31043, 32689, 34335, 35981, 37628, 39274,
           40920, 42566, 44212, 45859, 47505, 49151, 50797, 52444, 54090, 55736, 57382, 59028, 60675, 62321, 63967,
           65613, 67260, 68906, 70552, 72198, 73844, 75491, 77137, 78783, 80429, 82076, 83722, 85368, 87014, 88660,
           90307, 91953, 93599, 95245, 96892, 98538, 100184, 101830, 103477, 105123, 106769, 108415, 110061, 111708,
           113354, 115000, 116646, 118293, 119939, 121585, 123231, 124877, 126524, 128170, 129816]]
    #基础2 = 14580.815
    #成长2 = 1646.227
    攻击次数2 = 1
    CD = 30.
    是否有护石 = 1
    TP成长 = 0.10
    TP上限 = 5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 *= 1.25
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数2 *= 1.25
            self.CD *= 0.9
            self.倍率 *= 1.08
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>次元扭曲学说</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 思维聚爆]<br>"
            temp += "没有敌人被[乖离 : 迷雾]附身的状态下也可以施放该技能 (在前方250px处发动)<br>"
            temp += "最后爆炸攻击力 +25%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "施放过程中发动[次元边界]时， 不消耗次元石<br>"
            temp += "最后爆炸范围 +40%<br>"
            temp += "冷却时间 -10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>次元扭曲学说</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 思维聚爆]<br>"
            temp += "没有敌人被[乖离 : 迷雾]附身的状态下也可以施放该技能 (在前方250px处发动)<br>"
            temp += "最后爆炸攻击力 +25%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "施放过程中发动[次元边界]时， 不消耗次元石<br>"
            temp += "最后爆炸范围 +40%<br>"
            temp += "冷却时间 -10%"
            temp += "攻击力 +8%"

class 知源·次元行者技能17(知源·次元行者主动技能):
    名称 = '次元奇点'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    是否有护石 = 1
    CD = 40.
    护石选项 = ['圣痕']
    def 普通形态(self):
        self.数据1 = [ int(i*1.149) for i in [0, 23123, 25469, 27815, 30161, 32507, 34853, 37199, 39545, 41891, 44236, 46582, 48928, 51274, 53620,
               55966, 58312, 60658, 63004, 65349, 67695, 70041, 72387, 74733, 77079, 79425, 81771, 84117, 86463, 88808,
               91154, 93500, 95846, 98192, 100538, 102884, 105230, 107576, 109921, 112267, 114613]]
        self.数据2 = [ int(i*1.149) for i in [0, 28191, 31051, 33911, 36771, 39631, 42491, 45351, 48211, 51071, 53931, 56791, 59651, 62511, 65371,
               68231, 71091, 73951, 76811, 79671, 82531, 85391, 88251, 91111, 93971, 96831, 99691, 102551, 105411,
               108271, 111131, 113991, 116851, 119711, 122571, 125431, 128291, 131151, 134011, 136871, 139731]]
        self.攻击次数1 = 1
        self.攻击次数2 = 1
    def 强化形态(self):
        self.数据1 = [ int(i*1.121) for i in [0, 7127, 7850, 8573, 9297, 10020, 10743, 11466, 12189, 12912, 13635, 14358, 15081, 15804, 16528, 17251,
               17974, 18697, 19420, 20143, 20866, 21589, 22312, 23035, 23759, 24482, 25205, 25928, 26651, 27374, 28097,
               28820, 29543, 30266, 30990, 31713, 32436, 33159, 33882, 34605, 35328]]
        self.数据2 = [ int(i*1.121) for i in [0, 4751, 5233, 5715, 6198, 6680, 7162, 7644, 8126, 8608, 9090, 9572, 10054, 10536, 11018, 11500, 11982,
               12464, 12946, 13429, 13911, 14393, 14875, 15357, 15839, 16321, 16803, 17285, 17767, 18249, 18731, 19213,
               19695, 20177, 20660, 21142, 21624, 22106, 22588, 23070, 23552]]
        self.攻击次数1 = 4
        self.攻击次数2 = 4
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.倍率 *= 1.30
    def 护石无效化(self):
            self.CD /= 0.9
            self.倍率 /= 1.30
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>刻印咏唱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[次元 : 奇点]<br>"
            temp += "删除施放动作，立即施放<br>"
            temp += "普通使用时，不存在敌人时，能量领域也会生次元水晶<br>"
            temp += "攻击力 +12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "普通使用时，能量领域一定范围内的无法抓取敌人进入控制状态，持续2秒<br>"
            temp += "攻击力增加量额外增加 18%<br>"
            temp += "冷却时间 -10%"
        return temp


class 知源·次元行者技能18(知源·次元行者主动技能):
    名称 = '乖离禁锢'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [ int(i*1.118) for i in [0, 29878, 32909, 35940, 38971, 42002, 45033, 48065, 51096, 54127, 57158, 60189, 63220, 66251, 69282, 72314,
          75345, 78376, 81407, 84438, 87469, 90500, 93532, 96563, 99594, 102625, 105656, 108687, 111718, 114749, 117781,
          120812, 123843, 126874, 129905, 132936, 135967, 138998, 142030, 145061, 148092, 151123, 154154, 157185,
          160216, 163248, 166279, 169310, 172341, 175372, 178403, 181434, 184465, 187497, 190528, 193559, 196590,
          199621, 202652, 205683, 208714, 211746, 214777, 217808, 220839, 223870, 226901, 229932, 232964, 235995,
          239026]]
    #基础 = 26846.910
    #成长 = 3031.118
    攻击次数1 = 1
    CD = 50.
    是否有护石 = 1
    TP成长 = 0.10
    TP上限 = 5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.07
        elif x == 1:
            self.倍率 *= 1.15
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>妥善安置</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乖离 : 禁锢]<br>"
            temp += "[乖离 : 禁锢]命中时初始化[乖离 : 魅魔之舞]的冷却时间<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "技能命中后强制中断并施放其他奈雅丽技能时， 束缚效果不消失<br>"
            temp += "攻击力 +7%"
        elif x == 1:
            temp = "<font color='#FF00FF'>妥善安置</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乖离 : 禁锢]<br>"
            temp += "[乖离 : 禁锢]命中时初始化[乖离 : 魅魔之舞]的冷却时间<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "技能命中后强制中断并施放其他奈雅丽技能时， 束缚效果不消失<br>"
            temp += "攻击力 +15%"
        return temp

class 知源·次元行者技能19(知源·次元行者主动技能):
    名称 = '乖离沉沦'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    是否有护石 = 1
    数据1 = [ int(i*1.118) for i in [0, 36493, 40196, 43898, 47600, 51302, 55006, 58708, 62410, 66112, 69815, 73517, 77219, 80921, 84624, 88326,
          92028, 95730, 99433, 103135, 106837, 110539, 114242, 117944, 121646, 125348, 129052, 132754, 136456, 140158,
          143861, 147563, 151265, 154967, 158670, 162372, 166074, 169776, 173479, 177181, 180883]]
    #基础 = 32790.618
    #成长 = 3702.340
    攻击次数1 = 1
    数据2 = [ int(i*1.118) for i in [0, 1214, 1338, 1462, 1585, 1708, 1831, 1955, 2078, 2201, 2324, 2448, 2572, 2694, 2818, 2941, 3065, 3187,
           3311, 3434, 3558, 3680, 3804, 3928, 4051, 4174, 4297, 4421, 4544, 4667, 4790, 4914, 5038, 5160, 5284, 5407,
           5531, 5653, 5777, 5900, 6024]]
    #基础2 = 1090.657
    #成长2 = 123.333
    攻击次数2 = 24
    CD = 45.
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>异界的断末魔</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乖离 : 沉沦]<br>"
            temp += "技能变更为彼端的存在爆炸后给予1次伤害<br>"
            temp += "变更后，攻击力为变更前总攻击力的110%<br>"
            temp += "召唤媒介时，向媒介对象刻下印章，即使脱离爆炸范围，也会造成伤害<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "攻击力增加量额外增加 +20%"
        return temp


class 知源·次元行者技能20(知源·次元行者主动技能):
    名称 = '禁断之盛宴'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    迷雾数据 = [ int(i*1.108) for i in [0, 5976, 7362, 8748, 10134, 11520, 12906, 14292, 15678, 17064, 18450, 19836, 21222, 22608, 23994, 25380, 26766,
            28151, 29537, 30923, 32309, 33695, 35081, 36467, 37853, 39239, 40625, 42011, 43397, 44783, 46169, 47555, 48941,
            50327, 51713, 53098, 54484, 55870, 57256, 58642, 60028]]
    炮击数据 = [ int(i*1.108) for i in [0, 4980, 6135, 7290, 8445, 9600, 10755, 11910, 13065, 14220, 15375, 16530, 17685, 18840, 19995, 21150, 22305,
     23459, 24614, 25769, 26924, 28079, 29234, 30389, 31544, 32699, 33854, 35009, 36164, 37319, 38474, 39629, 40784,
     41939, 43094, 44249, 45404, 46559, 47714, 48868, 50023]]
    普通炮击数据 = [ int(i*1.108) for i in [0, 2973, 3663, 4353, 5042, 5732, 6421, 7111, 7801, 8490, 9180, 9869, 10559, 11249, 11938, 12628, 13317, 14007,
     14697, 15386, 16076, 16765, 17455, 18144, 18834, 19524, 20213, 20903, 21592, 22282, 22972, 23661, 24351, 25040,
     25730, 26420, 27109, 27799, 28488, 29178, 29868]]
    强化炮击数据 = [ int(i*1.108) for i in [0, 2787, 3433, 4080, 4726, 5373, 6019, 6665, 7312, 7958, 8605, 9251, 9897, 10544, 11190, 11837, 12483, 13129,
     13776, 14422, 15069, 15715, 16361, 17008, 17654, 18300, 18947, 19593, 20240, 20886, 21532, 22179, 22825, 23472,
     24118, 24764, 25411, 26057, 26704, 27350, 27996]]
    终结伤害 = [ int(i*1.108) for i in [0, 98842, 121761, 144681, 167601, 190521, 213441, 236361, 259281, 282201, 305121, 328040, 350960, 373880, 396800,
     419720, 442640, 465560, 488480, 511400, 534320, 557239, 580159, 603079, 625999, 648919, 671839, 694759, 717679,
     740599, 763518, 786438, 809358, 832278, 855198, 878118, 901038, 923958, 946878, 969797, 992717]]
    # 不强化
    # 10次迷雾伤害和13次炮击伤害
    攻击次数1 = 10
    攻击次数2 = 12
    # 强化后公共伤害部分
    # 18次强化炮击+1次终结伤害
    攻击次数4 = 18
    攻击次数5 = 1
    # 强化后可取消的部分
    攻击次数3 = 10  # 10次普通炮击
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数1 * self.迷雾数据[self.等级] + \
                         self.攻击次数2 * self.炮击数据[self.等级] + \
                         self.攻击次数3 * self.普通炮击数据[self.等级] + \
                         self.攻击次数4 * self.强化炮击数据[self.等级] + \
                         self.攻击次数5 * self.终结伤害[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率)
    CD = 180.

class 知源·次元行者技能21(知源·次元行者主动技能):
    名称 = '乖离境界之兽'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 10
    脱手 = 1
    技能施放时间 = 3
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    CD = 60.0
    # 韩服面板粗略计算
    数据1 = [0, 160074, 176313, 192553, 208792, 225032, 241271, 257511, 273750, 289990, 306229, 322468, 338708, 354947, 371187, 387426, 403666]
    攻击次数1 = 1

class 知源·次元行者技能22(被动技能):
    名称 = '时空碎片'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 知源·次元行者技能23(知源·次元行者主动技能):
    名称 = '次元乖离理性崩坏'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['无']
    CD = 290.0
    脱手 = 0
    技能施放时间 = 6.5
    # 韩服面板粗略计算，忽略伤害结构
    数据1 = [0, 415012, 511249, 607486, 703723, 799959, 896196, 992433, 1088670, 1281144]
    攻击次数1 = 1
    def 加成倍率(self, 武器类型):
        return 0.0



知源·次元行者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('知源·次元行者技能列表.append(知源·次元行者技能' + str(i) + '())')
        i += 1
    except:
        i = -1

知源·次元行者技能序号 = dict()
for i in range(len(知源·次元行者技能列表)):
    知源·次元行者技能序号[知源·次元行者技能列表[i].名称] = i

知源·次元行者一觉序号 = 0
知源·次元行者二觉序号 = 0
知源·次元行者三觉序号 = 0
for i in 知源·次元行者技能列表:
    if i.所在等级 == 50:
        知源·次元行者一觉序号 = 知源·次元行者技能序号[i.名称]
    if i.所在等级 == 85:
        知源·次元行者二觉序号 = 知源·次元行者技能序号[i.名称]
    if i.所在等级 == 100:
        知源·次元行者三觉序号 = 知源·次元行者技能序号[i.名称]

知源·次元行者护石选项 = ['无']
for i in 知源·次元行者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·次元行者护石选项.append(i.名称)

知源·次元行者符文选项 = ['无']
for i in 知源·次元行者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·次元行者符文选项.append(i.名称)


class 知源·次元行者角色属性(角色属性):
    实际名称 = '知源·次元行者'
    角色 = '魔法师(男)'
    职业 = '次元行者'

    武器选项 = ['扫把', '矛', '魔杖', '法杖', '棍棒']

    类型选择 = ['魔法固伤']

    类型 = '魔法固伤'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.850

    远古记忆 = 0

    坠落形态 = 0
    离子束形态 = 0
    万花镜形态 = 0
    粒子风暴形态 = 0
    粒子波形态 = 0
    奇点形态 = 0
    聚爆形态 = 0
    装备奇点护石 = 0

    二觉形态 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(知源·次元行者技能列表)
        self.技能序号 = deepcopy(知源·次元行者技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()

        if self.离子束形态 == 0:
            self.技能栏[self.技能序号['次元离子束']].攻击次数1 = 6
            self.技能栏[self.技能序号['次元离子束']].攻击次数2 = 0
        if self.离子束形态 == 1:
            self.技能栏[self.技能序号['次元离子束']].攻击次数1 = 0
            self.技能栏[self.技能序号['次元离子束']].攻击次数2 = 1

        if self.坠落形态 == 0:
            self.技能栏[self.技能序号['次元坠落']].攻击次数1 = 1
            self.技能栏[self.技能序号['次元坠落']].攻击次数2 = 1
            self.技能栏[self.技能序号['次元坠落']].攻击次数3 = 0
        if self.坠落形态 == 1:
            self.技能栏[self.技能序号['次元坠落']].攻击次数1 = 0
            self.技能栏[self.技能序号['次元坠落']].攻击次数2 = 0
            self.技能栏[self.技能序号['次元坠落']].攻击次数3 = 1

        if self.万花镜形态 == 0:
            self.技能栏[self.技能序号['次元万花镜']].攻击次数1 = 4
            self.技能栏[self.技能序号['次元万花镜']].攻击次数2 = 0
        if self.万花镜形态 == 1:
            self.技能栏[self.技能序号['次元万花镜']].攻击次数1 = 0
            self.技能栏[self.技能序号['次元万花镜']].攻击次数2 = 4

        if self.粒子风暴形态 == 1:
            self.技能栏[self.技能序号['次元粒子风暴']].攻击次数1 = 0
            self.技能栏[self.技能序号['次元粒子风暴']].攻击次数2 = 1
        if self.粒子风暴形态 == 0:
            self.技能栏[self.技能序号['次元粒子风暴']].攻击次数1 = 3
            self.技能栏[self.技能序号['次元粒子风暴']].攻击次数2 = 0

        if self.粒子波形态 == 0:
            self.技能栏[self.技能序号['次元粒子波']].攻击次数1 = 10
            self.技能栏[self.技能序号['次元粒子波']].攻击次数2 = 20
        if self.粒子波形态 == 1:
            self.技能栏[self.技能序号['次元粒子波']].攻击次数1 = 0
            self.技能栏[self.技能序号['次元粒子波']].攻击次数2 = 30

        if self.聚爆形态 == 0:
            self.技能栏[self.技能序号['次元思维聚爆']].攻击次数1 = 12
        if self.聚爆形态 == 1:
            self.技能栏[self.技能序号['次元思维聚爆']].攻击次数1 = 1

        if self.奇点形态 == 0:
            self.技能栏[self.技能序号['次元奇点']].普通形态()
        if self.奇点形态 == 1:
            self.技能栏[self.技能序号['次元奇点']].强化形态()

        if self.二觉形态 == 0: # 不强化
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数1 = 10
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数2 = 12
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数3 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数4 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数5 = 0
        if self.二觉形态 == 1: # 强化:取消后摇
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数1 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数2 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数3 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数4 = 17
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数5 = 1
        if self.二觉形态 == 2: # 强化：不取消后摇
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数1 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数2 = 0
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数3 = 10
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数4 = 17
            self.技能栏[self.技能序号['禁断之盛宴']].攻击次数5 = 1

class 知源·次元行者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·次元行者角色属性()
        self.角色属性A = 知源·次元行者角色属性()
        self.角色属性B = 知源·次元行者角色属性()
        self.一觉序号 = 知源·次元行者一觉序号
        self.二觉序号 = 知源·次元行者二觉序号
        self.三觉序号 = 知源·次元行者三觉序号
        self.护石选项 = deepcopy(知源·次元行者护石选项)
        self.符文选项 = deepcopy(知源·次元行者符文选项)

    def 护石判断(self):
        sign = 0
        sign2 = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '次元粒子风暴':
                sign = 1
        if sign == 1:
            self.强化粒子风暴.setChecked(True)
            self.强化粒子风暴.setEnabled(False)
            self.强化粒子风暴.setStyleSheet(不可勾选复选框样式)
        else:
            self.强化粒子风暴.setEnabled(True)
            self.强化粒子风暴.setStyleSheet(复选框样式)

    def 界面(self):
        super().界面()
        
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())

        self.坠落触发箱子 = QCheckBox("坠落触发箱子", self.main_frame2)
        self.坠落触发箱子.setStyleSheet(复选框样式)
        self.坠落触发箱子.setChecked(False)
        self.坠落触发箱子.resize(120, 20)
        self.坠落触发箱子.move(325, 380)

        self.离子束强化=QCheckBox("强化离子束", self.main_frame2)
        self.离子束强化.setStyleSheet(复选框样式)
        self.离子束强化.setChecked(False)
        self.离子束强化.resize(120, 20)
        self.离子束强化.move(325, 405)

        self.强化万花镜 = QCheckBox("强化万花镜", self.main_frame2)
        self.强化万花镜.setStyleSheet(复选框样式)
        self.强化万花镜.setChecked(True)
        self.强化万花镜.resize(120, 20)
        self.强化万花镜.move(325, 430)

        self.强化粒子风暴 = QCheckBox("强化粒子风暴", self.main_frame2)
        self.强化粒子风暴.setStyleSheet(复选框样式)
        self.强化粒子风暴.setChecked(True)
        self.强化粒子风暴.resize(120, 20)
        self.强化粒子风暴.move(325, 455)
        self.强化粒子风暴.setToolTip('选择粒子风暴护石时常驻为强化模式')

        self.强化粒子波 = QCheckBox("强化粒子波", self.main_frame2)
        self.强化粒子波.setStyleSheet(复选框样式)
        self.强化粒子波.setChecked(True)
        self.强化粒子波.resize(120, 20)
        self.强化粒子波.move(325, 480)

        self.聚爆是否瞬爆 = QCheckBox("聚爆取消持续伤害", self.main_frame2)
        self.聚爆是否瞬爆.setStyleSheet(复选框样式)
        self.聚爆是否瞬爆.setChecked(True)
        self.聚爆是否瞬爆.resize(120, 20)
        self.聚爆是否瞬爆.move(325, 505)
        self.聚爆是否瞬爆.setToolTip('是否按C取消直接引爆')

        self.强化奇点 = QCheckBox("强化奇点", self.main_frame2)
        self.强化奇点.setStyleSheet(复选框样式)
        self.强化奇点.setChecked(True)
        self.强化奇点.resize(120, 20)
        self.强化奇点.move(325, 530)
        self.强化奇点.setToolTip('')

        self.二觉形态选择 = MyQComboBox(self.main_frame2)
        self.二觉形态选择.addItem('不强化二觉')
        self.二觉形态选择.addItem('二觉:取消后摇')
        self.二觉形态选择.addItem('二觉:保留后摇')
        self.二觉形态选择.setCurrentIndex(2)
        self.二觉形态选择.resize(120, 20)
        self.二觉形态选择.move(325, 555)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)

        if self.坠落触发箱子.isChecked():
            属性.坠落形态 = 1
        if self.离子束强化.isChecked():
            属性.离子束形态 = 1
        if self.强化万花镜.isChecked():
            属性.万花镜形态 = 1
        if self.强化粒子风暴.isChecked():
            属性.粒子风暴形态 = 1
        if self.强化奇点.isChecked():
            属性.奇点形态 = 1
        if self.强化粒子波.isChecked():
            属性.粒子波形态 = 1
        if self.聚爆是否瞬爆.isChecked():
            属性.聚爆形态 = 1
        属性.二觉形态 = self.二觉形态选择.currentIndex()

    def 载入配置(self, path = 'set'):
        super().载入配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in [ self.坠落触发箱子, self.离子束强化, self.强化万花镜, self.强化粒子风暴,
                       self.强化粒子波, self.聚爆是否瞬爆, self.强化奇点 ]:
                if setfile[num].replace('\n', '') == 'True':
                    i.setChecked(True)
                else:
                    i.setChecked(False)
                num += 1
            self.二觉形态选择.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

    def 保存配置(self, path = 'set'):
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill4.ini', 'w', encoding='utf-8')
            setfile.write(str(self.坠落触发箱子.isChecked()) + '\n')
            setfile.write(str(self.离子束强化.isChecked()) + '\n')
            setfile.write(str(self.强化万花镜.isChecked()) + '\n')
            setfile.write(str(self.强化粒子风暴.isChecked()) + '\n')
            setfile.write(str(self.强化粒子波.isChecked()) + '\n')
            setfile.write(str(self.聚爆是否瞬爆.isChecked()) + '\n')
            setfile.write(str(self.强化奇点.isChecked()) + '\n')
            setfile.write(str(self.二觉形态选择.currentIndex()) + '\n')
        except:
            pass