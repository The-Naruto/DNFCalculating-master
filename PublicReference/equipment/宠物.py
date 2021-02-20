##宠物属性部分

宠物列表 = [None] * 13

class 宠物12():
    名称 = '(21)至尊·火神的化身'
    def 城镇属性(self, 属性):
        属性.力量 += 160
        属性.智力 += 160
        属性.所有属性强化加成(25)
        属性.技能等级加成('所有',1,80,1)
        属性.加算冷却缩减 += 0.05
        属性.暴击伤害加成(0.20,辟邪玉加成 = 0)
        属性.百分比力智加成(0.12,辟邪玉加成 = 0)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +160<br>'
        temp += '智力 +160<br>'
        temp += '所有属性强化 +25<br>'
        temp += 'Lv1-80 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        temp += '暴击伤害 +20%<br>'
        temp += '百分比力智 +12%<br>'
        return temp

class 宠物11():
    名称 = '(21)普通·骑士/精灵使'
    def 城镇属性(self, 属性):
        属性.力量 += 150
        属性.智力 += 150
        属性.所有属性强化加成(25)
        属性.技能等级加成('所有',1,80,1)
        属性.加算冷却缩减 += 0.05
        属性.百分比三攻加成(0.12,辟邪玉加成 = 0)
        属性.附加伤害加成(0.10,辟邪玉加成 = 0)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +150<br>'
        temp += '智力 +150<br>'
        temp += '所有属性强化 +25<br>'
        temp += 'Lv1-80 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        temp += '百分比三攻 +12%<br>'
        temp += '附加伤害 +10%<br>'
        return temp

class 宠物10():
    名称 = '(20)至尊·暴风圣女'
    def 城镇属性(self, 属性):
        属性.力量 += 150
        属性.智力 += 150
        属性.所有属性强化加成(24)
        属性.附加伤害加成(0.15,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
        属性.最终伤害加成(0.05,辟邪玉加成 = 0)
        属性.百分比力智加成(0.12,辟邪玉加成 = 0)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +150<br>'
        temp += '智力 +150<br>'
        temp += '所有属性强化 +24<br>'
        temp += '附加伤害 +15%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        temp += '最终伤害 +5%<br>'
        temp += '百分比力智 +12%<br>'
        return temp

class 宠物9():
    名称 = '(19)至尊·神迹·莱恩'
    def 城镇属性(self, 属性):
        属性.力量 += 120
        属性.智力 += 120
        属性.所有属性强化加成(24)
        属性.附加伤害加成(0.15,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
        属性.最终伤害加成(0.05,辟邪玉加成 = 0)
        属性.百分比力智加成(0.08,辟邪玉加成 = 0)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +120<br>'
        temp += '智力 +120<br>'
        temp += '所有属性强化 +24<br>'
        temp += '附加伤害 +15%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        temp += '最终伤害 +5%<br>'
        temp += '百分比力智 +8%<br>'
        return temp

class 宠物8():
    名称 = '(20)普通·神官'
    def 城镇属性(self, 属性):
        属性.力量 += 140
        属性.智力 += 140
        属性.所有属性强化加成(24)
        属性.附加伤害加成(0.12,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
        属性.百分比力智加成(0.10,辟邪玉加成 = 0)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +140<br>'
        temp += '智力 +140<br>'
        temp += '所有属性强化 +24<br>'
        temp += '附加伤害 +12%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        temp += '百分比力智 +10%<br>'
        return temp

class 宠物7():
    名称 = '(19)至尊·莱恩'
    def 城镇属性(self, 属性):
        属性.力量 += 120
        属性.智力 += 120
        属性.所有属性强化加成(24)
        属性.附加伤害加成(0.15,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
        属性.最终伤害加成(0.05,辟邪玉加成 = 0)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +120<br>'
        temp += '智力 +120<br>'
        temp += '所有属性强化 +24<br>'
        temp += '附加伤害 +15%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        temp += '最终伤害 +5%<br>'
        return temp

class 宠物6():
    名称 = '(19)普通·莱恩'
    def 城镇属性(self, 属性):
        属性.力量 += 120
        属性.智力 += 120
        属性.所有属性强化加成(24)
        属性.附加伤害加成(0.12,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +120<br>'
        temp += '智力 +120<br>'
        temp += '所有属性强化 +24<br>'
        temp += '附加伤害 +12%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        return temp

class 宠物5():
    名称 = '(18)至尊·蒂娅'
    def 城镇属性(self, 属性):
        属性.力量 += 110
        属性.智力 += 110
        属性.所有属性强化加成(22)
        属性.附加伤害加成(0.12,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +110<br>'
        temp += '智力 +110<br>'
        temp += '所有属性强化 +22<br>'
        temp += '附加伤害 +12%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        return temp

class 宠物4():
    名称 = '(18)普通·蒂娅'
    def 城镇属性(self, 属性):
        属性.力量 += 100
        属性.智力 += 100
        属性.所有属性强化加成(20)
        属性.附加伤害加成(0.10,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +100<br>'
        temp += '智力 +100<br>'
        temp += '所有属性强化 +20<br>'
        temp += '附加伤害 +10%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        return temp

class 宠物3():
    名称 = '(17)克里斯'
    def 城镇属性(self, 属性):
        属性.物理攻击力 += 35
        属性.魔法攻击力 += 35
        属性.独立攻击力 += 55
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.08,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
    def 装备描述(self, 属性):
        temp = ''
        temp += '物理攻击力 +35<br>'
        temp += '魔法攻击力 +35<br>'
        temp += '独立攻击力 +55<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +8%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        return temp

class 宠物2():
    名称 = '(16)关羽'
    def 城镇属性(self, 属性):
        属性.力量 += 50
        属性.智力 += 50
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.05,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
        属性.加算冷却缩减 += 0.05
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +50<br>'
        temp += '智力 +50<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +5%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        temp += '技能冷却 -5%(加算)<br>'
        return temp

class 宠物1():
    名称 = '(15)墨仙雪莲'
    def 城镇属性(self, 属性):
        属性.力量 += 45
        属性.智力 += 45
        属性.物理攻击力 += 25
        属性.魔法攻击力 += 25
        属性.独立攻击力 += 45
        属性.附加伤害加成(0.08,辟邪玉加成 = 0)
        属性.技能等级加成('所有',1,50,1)
    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +45<br>'
        temp += '智力 +45<br>'
        temp += '物理攻击力 +25<br>'
        temp += '魔法攻击力 +25<br>'
        temp += '独立攻击力 +45<br>'
        temp += '附加伤害 +8%<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp

class 宠物0():
    名称 = '无'
    def 城镇属性(self, 属性):
        pass
    def 触发属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        return temp

for i in range(len(宠物列表)):
    exec('宠物列表[{}] = 宠物{}()'.format(len(宠物列表) - i - 1, i))

宠物序号 = dict()
for i in range(len(宠物列表)):
    宠物序号[宠物列表[i].名称] = i
