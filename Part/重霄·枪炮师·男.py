from PublicReference.base import *

class 主动技能(主动技能):
    def 等效CD(self, 武器类型,输出类型):
        return round(self.CD  / self.恢复, 1)

class 重霄·枪炮师·男技能0(主动技能):
    名称 = 'M137格林机枪'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 51
    基础 = 1416.2
    成长 = 161.3
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5

class 重霄·枪炮师·男技能1(被动技能):
    名称 = '重火器精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    关联技能2 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率2(武器类型)

class 重霄·枪炮师·男技能2(主动技能):
    名称 = '加农炮'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 44
    数据 = [0, 1055, 1162, 1269, 1376, 1483, 1590, 1697, 1805, 1911, 2018, 2125, 2233, 2339, 2446, 2554, 2661, 2767, 2875, 2982, 3089, 3195, 3303, 3410, 3517, 3624, 3731, 3838, 3945, 4052, 
    4159, 4266, 4374, 4481, 4587, 4695, 4802, 4909, 5015, 5123, 5230, 5337, 5444, 5551, 5658, 5765, 5872, 5979, 6086, 6194, 6300, 6407, 6515, 6622, 6728, 6835, 6943, 7050, 7156, 7264, 7371, 7478, 7585, 7692, 7799, 7906, 8014, 8120, 8227, 8335, 8442]
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5
    
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * 2 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 重霄·枪炮师·男技能3(主动技能):
    名称 = '反坦克炮'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 44
    数据1 =[0, 490, 540, 590, 640, 689, 739, 789, 839, 888, 938, 988, 1038, 1087, 1137, 1187, 1237, 
    1286, 1336, 1386, 1436, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1934, 1984, 2034, 2084, 2133, 2183, 2233, 2283, 2332, 2382, 2432, 2482, 2531, 2581, 2631, 2681, 2730, 2780, 2830, 2880, 2929, 2979, 3029, 3079, 3128, 3178, 3228, 3278, 3328, 3377, 3427, 3477, 3527, 3576, 3626, 3676, 3726, 3775, 3825, 3875, 3925]
    数据2 = [0, 1963, 2162, 2361, 2560, 2759, 2958, 3157, 3356, 3555, 3755, 3954, 4153, 4352, 4551, 4750, 4949, 5148, 5347, 5546, 5745, 5945, 6144, 6343, 6542, 6741, 6940, 7140, 7339, 7538, 
    7737, 7936, 8135, 8335, 8534, 8733, 8932, 9131, 9330, 9529, 9728, 9927, 10126, 10325, 10525, 10724, 10923, 11122, 11321, 11520, 11719, 11918, 12117, 12316, 12515, 12715, 12915, 13114, 13313, 13512, 13711, 13910, 14109, 14308, 14507, 14706, 14905, 15105, 15304, 15503, 15702]
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 重霄·枪炮师·男技能4(被动技能):
    名称 = '超动力补给包'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.01 * self.等级, 5)

class 重霄·枪炮师·男技能5(主动技能):
    名称 = '激光炮'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 42
    数据 = [0, 2218, 2444, 2668, 2894, 3119, 3344, 3569, 3795, 4019, 4245, 4469, 4695, 4920, 5145, 5370, 5595, 5820, 6045, 6270, 6495, 6721, 6945, 7171, 7395, 7621, 7846, 8071, 8296, 8521, 
    8746, 8972, 9196, 9422, 9647, 9872, 10097, 10322, 10547, 10773, 10997, 11223, 11447, 11673, 11898, 12123, 12348, 12573, 12798, 13024, 13248, 13474, 13699, 13924, 14149, 14374, 14599, 14825, 15049, 15275, 15499, 15725, 15950, 16175, 16400, 16625, 16850, 17075, 17300, 
    17525, 17751]
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.111

class 重霄·枪炮师·男技能6(被动技能):
    名称 = '蓄电激光炮'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['激光炮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.45 + 0.05 * self.等级, 5)

class 重霄·枪炮师·男技能7(主动技能):
    名称 = '聚焦喷火器'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 39
    数据 = [0, 224, 246, 269, 292, 315, 338, 361, 384, 406, 429, 452, 475, 497, 520, 543, 565, 588, 
    611, 634, 656, 679, 702, 725, 747, 770, 793, 815, 838, 861, 884, 906, 930, 953, 975, 998, 1021, 1044, 1066, 1089, 1112, 1135, 1157, 1180, 1203, 1225, 1248, 1271, 1294, 1316, 1339, 1362, 1385, 1407, 1430, 1453, 1475, 1498, 1522, 1545, 1567, 1590, 1613, 1635, 1658, 1681, 1704, 1726, 1749, 1772, 1795]
    攻击次数 = 29
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 重霄·枪炮师·男技能8(主动技能):
    名称 = 'FM31榴弹发射器'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 37
    数据 =[0, 1629, 1795, 1960, 2125, 2290, 2455, 2621, 2786, 2952, 3117, 3282, 3447, 3613, 3778, 3944, 4109, 4275, 4439, 4605, 4770, 4935, 5101, 5266, 5432, 5596, 5762, 5927, 6093, 6258, 
    6424, 6588, 6754, 6919, 7085, 7250, 7415, 7581, 7745, 7911, 8076, 8242, 8407, 8573, 8738, 8903, 9068, 9234, 9399, 9565, 9730, 9895, 10060, 10225, 10391, 10556, 10722, 10887, 11052, 11217, 11383, 11548, 11714, 11879, 12044, 12209, 12375, 12540, 12705, 12871, 13036] 
    攻击次数 = 4
    CD = 15.0
    TP成长 = 0.20
    TP上限 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.113

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.6 * 2
        elif x == 1:
            self.倍率 *= 0.64 * 2

class 重霄·枪炮师·男技能9(主动技能):
    名称 = 'FM92刺弹炮'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 37
    数据 = [0, 1679, 1850, 2020, 2190, 2361, 2531, 2702, 2872, 3043, 3213, 3384, 3554, 3724, 3895, 4065, 4235, 4405, 4576, 4746, 4917, 5087, 5257, 5428, 5598, 5769, 5939, 6110, 6280, 6450, 
    6621, 6791, 6962, 7132, 7303, 7473, 7644, 7814, 7984, 8155, 8325, 8495, 8665, 8836, 9006, 9177, 9347, 9517, 9688, 9858, 10029, 10199, 10370, 10540, 10710, 10881, 11051, 11222, 11392, 11563, 11733, 11904, 12074, 12244, 12415, 12585, 12755, 12925, 13096, 13266, 13437]
    攻击次数 = 5
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.069

class 重霄·枪炮师·男技能10(主动技能):
    名称 = '量子爆弹'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 34
    数据1 = [0, 1925, 2120, 2315, 2511, 2706, 2902, 3097, 3292, 3487, 3683, 3878, 4074, 4269, 4465, 4659, 4855, 5050, 5245, 5441, 5636, 5832, 6026, 6222, 6417, 6613, 6808, 7004, 7199, 7394, 
    7589, 7785, 7980, 8175, 8371, 8566, 8761, 8956, 9152, 9347, 9543, 9738, 9934, 10128, 10324, 10519, 10715, 10910, 11105, 11301, 11495, 11691, 11886, 12082, 12277, 12473, 12668, 12863, 13058, 13254, 13449, 13645, 13840, 14035, 14231, 14425, 14621, 14816, 15012, 15207, 
    15403]
    攻击次数1 = 1
    数据2 = [0, 6096, 6715, 7334, 7952, 8571, 9189, 9807, 10426, 11045, 11664, 12282, 12900, 13519, 14137, 14756, 15375, 15993, 16612, 17230, 17849, 18467, 19085, 19705, 20323, 20941, 21560, 22178, 22797, 23415, 24034, 24653, 25271, 25890, 26508, 27126, 27745, 28364, 28982, 29601, 30219, 30838, 31456, 32075, 32694, 33312, 33931, 34549, 35167, 35786, 36405, 37023, 37642, 38260, 38879, 39497, 40115, 40735, 41353, 41972, 42590, 43208, 43827, 44445, 45065, 
    45683, 46301, 46920, 47538, 48156, 48775]
    攻击次数2 = 1

    #感电
    数据3 =[0, 10, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 46, 47, 48, 49, 50, 51, 52, 53, 54, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    攻击次数3 = 1
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.154

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 *= 0.21 * 8 
            self.攻击次数3 *= 0.21
        elif x == 1:
            self.攻击次数1 = 0
            self.攻击次数2 *= 0.20 * 9 
            self.攻击次数3 *= 0.20

class 重霄·枪炮师·男技能11(主动技能):
    名称 = 'X1压缩量子炮'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 32
    数据 = [0, 17238, 18987, 20736, 22485, 24234, 25983, 27732, 29480, 31229, 32978, 34727, 36475, 38225, 39974, 41722, 43471, 45220, 46969, 48717, 50466, 52215, 53965, 55713, 57462, 59211, 60960, 62708, 64457, 66206, 67955, 69704, 71453, 73202, 74951, 76699, 78448, 80197, 81946, 83695, 85444, 87193, 88942, 90690, 92439, 94188, 95936, 97685, 99435, 101184, 102932, 
    104681, 106430, 108179, 109927, 111676, 113425, 115175, 116923, 118672, 120421, 122170, 123918, 125667, 127416, 129165, 130914, 132663, 134412, 136161, 137909]
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.15

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1984
        elif x == 1:
            self.倍率 *= 1.2768

class 重霄·枪炮师·男技能12(被动技能):
    名称 = '卫星定位'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

class 重霄·枪炮师·男技能13(主动技能):
    名称 = '卫星射线'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 3250, 4004, 4757, 5511, 6265, 7018, 7773, 8526, 9280, 10034, 10787, 11542, 12295, 13049, 13803, 14556, 15310, 16065, 16818, 17572, 18325, 19079, 19833, 20586, 21340, 22094, 22847, 23601, 24355, 25109, 25863, 26616, 27370, 28125, 28878, 29632, 30385, 31139, 31893, 32647, 33401, 34155, 34908, 35662, 36415, 37169, 37923, 38676, 39430, 40184, 40937, 41691, 42445, 43199, 43954, 44707, 45461, 46215, 46968, 47722, 48475, 49229, 49984, 50737, 51491, 52245, 52998, 53752, 54505, 55259]
    攻击次数1 = 1
    数据2 = [0, 1241, 1530, 1817, 2106, 2394, 2681, 2970, 3257, 3546, 3834, 4121, 4410, 4697, 4986, 5274, 5562, 5850, 6137, 6426, 6714, 7002, 7290, 7577, 7866, 8154, 8443, 8730, 9018, 9306, 
    9594, 9883, 10170, 10458, 10746, 11034, 11323, 11610, 11898, 12186, 12475, 12763, 13050, 
    13338, 13626, 13915, 14203, 14491, 14778, 15066, 15355, 15643, 15931, 16219, 16506, 16795, 17083, 17371, 17659, 17947, 18235, 18523, 18811, 19099, 19387, 19675, 19963, 20251, 20539, 20827, 21115]
    攻击次数2 = 8.4 / 0.2
    CD = 159.5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 * 1.1 * 1.059466669

class 重霄·枪炮师·男技能14(主动技能):
    名称 = '等离子放射器'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 24
    数据 = [0, 1263, 1391, 1519, 1647, 1775, 1904, 2032, 2160, 2288, 2416, 2545, 2673, 2800, 2928, 3056, 3185, 3313, 3441, 3569, 3697, 3825, 3954, 4082, 4210, 4338, 4466, 4595, 4723, 4851, 
    4979, 5107, 5235, 5364, 5492, 5620, 5748, 5876, 6005, 6132, 6260, 6388, 6516, 6645, 6773, 6901, 7029, 7157, 7285, 7414, 7542, 7670, 7798, 7926, 8055, 8183, 8311, 8439, 8567, 8695, 8824, 8952, 9080, 9208, 9335, 9464, 9592, 9720, 9848, 9976, 10105]
    攻击次数 = 12
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.112

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.16
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.25
            self.CD *= 0.88

class 重霄·枪炮师·男技能15(主动技能):
    名称 = 'FM92SW刺弹炮'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 19

    数据 = [0, 29776, 32788, 35804, 38832, 41852, 44880, 47892, 50920, 53936, 56964, 59980, 63004, 66020, 69040, 72068, 75084, 78108, 81124, 84152, 87168, 90192, 93208, 96240, 99256, 102272, 105296, 108312, 111340, 114356, 117384, 120396, 123428, 126444, 129472, 132488, 135500, 138528, 141544, 144572, 147588, 150616, 153632, 156660, 159676, 162704, 165716, 168732, 
    171760, 174776, 177804, 180820, 183848, 186864, 189892, 192904, 195932, 198948, 201964, 204992, 208008, 211036, 214052, 217080, 220096, 223120, 226136, 229164, 232180, 235200, 238224]
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率 * 1.073

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.305

class 重霄·枪炮师·男技能16(被动技能):
    名称 = '重火器改良'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

class 重霄·枪炮师·男技能17(主动技能):
    名称 = '地脉振荡器'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 17
    数据 = [0, 41977, 46241, 50499, 54758, 59017, 63274, 67533, 71792, 76057, 80308, 84573, 88831, 93084, 97353, 101611, 105863, 110128, 114382, 118643, 122907, 127162, 131419, 135683, 139936, 144199, 148460, 152717, 156982, 161233, 165500, 169758, 174016, 178274, 182531, 186790, 191054, 195312, 199572, 203823, 208090, 212352, 216604, 220870, 225121, 229380, 233643, 237902, 242160, 246424, 250677, 254936, 259199, 263459, 267716, 271974, 276233, 280492, 284755, 289014, 293266, 297532, 301789, 306047, 310312, 314565, 318829, 323089, 327346, 
    331611, 335868]
    CD = 40.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率 * 1.15

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3324

class 重霄·枪炮师·男技能18(主动技能):
    名称 = 'MSC7'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 14
    数据 = [0, 44280, 48772, 53264, 57757, 62250, 66741, 71234, 75726, 80219, 84711, 89203, 93695, 98187, 102679, 107172, 111664, 116156, 120650, 125141, 129633, 134126, 138618, 143111, 147603, 152094, 156587, 161079, 165571, 170064, 174556, 179049, 183541, 188033, 192525, 197018, 201510, 206002, 210494, 214986, 219479, 223971, 228463, 232956, 237449, 241940, 246433, 250925, 255416, 259910, 264402, 268894, 273386, 277878, 282370, 286863, 291355, 295849, 300340, 304832, 309325, 313816, 318309, 322802, 327294, 331785, 336278, 340770, 345261, 349755, 354248]
    CD = 45.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率 * 1.11

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3320

class 重霄·枪炮师·男技能19(主动技能):
    名称 = '毁灭射线'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据 = [0, 123558, 152210, 180872, 209524, 238165, 266826, 295478, 324130, 352782, 381433, 410095, 438736, 467388, 496050, 524691, 553353, 582005, 610656, 639308, 667959, 696621, 725263, 753915, 782576, 811227, 839879, 868531, 897183, 925834, 954485, 983137, 1011799, 1040441, 1069102, 1097754, 1126405, 1155057, 1183709, 1212370, 1241012, 1269664, 1298325, 1326977, 1355628, 1384280, 1412932, 1441584, 1470235, 1498886, 1527548, 1556190, 1584852, 1613503, 1642145, 1670806, 1699458, 1728120, 1756761, 1785413, 1814075, 1842726, 1871378, 1900029, 1928681, 1957333, 1985985, 2014636, 2043297, 2071939, 2100601]
    CD = 198.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率 * 1.113

class 重霄·枪炮师·男技能20(被动技能):
    名称 = '连锁卫星'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 重霄·枪炮师·男技能21(主动技能):
    名称 = 'MLDRS95发射器'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 7
    基础 = 86171.0
    成长 = 9730.0
    CD = 60.0

class 重霄·枪炮师·男技能22(主动技能):
    名称 = '裂核轨道炮'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 308971.0
    成长 = 93275.0
    CD = 319.0
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

重霄·枪炮师·男技能列表 = []
i = 0
while i >= 0:
    try:
        exec('重霄·枪炮师·男技能列表.append(重霄·枪炮师·男技能'+str(i)+'())')
        i += 1
    except:
        i = -1

重霄·枪炮师·男技能序号 = dict()
for i in range(len(重霄·枪炮师·男技能列表)):
    重霄·枪炮师·男技能序号[重霄·枪炮师·男技能列表[i].名称] = i

重霄·枪炮师·男一觉序号 = 0
重霄·枪炮师·男二觉序号 = 0
重霄·枪炮师·男三觉序号 = 0
for i in 重霄·枪炮师·男技能列表:
    if i.所在等级 == 50:
        重霄·枪炮师·男一觉序号 = 重霄·枪炮师·男技能序号[i.名称]
    if i.所在等级 == 85:
        重霄·枪炮师·男二觉序号 = 重霄·枪炮师·男技能序号[i.名称]
    if i.所在等级 == 100:
        重霄·枪炮师·男三觉序号 = 重霄·枪炮师·男技能序号[i.名称]

重霄·枪炮师·男护石选项 = ['无']
for i in 重霄·枪炮师·男技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        重霄·枪炮师·男护石选项.append(i.名称)

重霄·枪炮师·男符文选项 = ['无']
for i in 重霄·枪炮师·男技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        重霄·枪炮师·男符文选项.append(i.名称)

class 重霄·枪炮师·男角色属性(角色属性):

    实际名称 = '重霄·枪炮师·男'
    角色 = '神枪手(男)'
    职业 = '枪炮师'

    武器选项 = ['手炮']
    
    类型选择 = ['物理百分比']
    
    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.957
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(重霄·枪炮师·男技能列表)
        self.技能序号= deepcopy(重霄·枪炮师·男技能序号)

class 重霄·枪炮师·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 重霄·枪炮师·男角色属性()
        self.角色属性A = 重霄·枪炮师·男角色属性()
        self.角色属性B = 重霄·枪炮师·男角色属性()
        self.一觉序号 = 重霄·枪炮师·男一觉序号
        self.二觉序号 = 重霄·枪炮师·男二觉序号
        self.三觉序号 = 重霄·枪炮师·男三觉序号
        self.护石选项 = deepcopy(重霄·枪炮师·男护石选项)
        self.符文选项 = deepcopy(重霄·枪炮师·男符文选项)
