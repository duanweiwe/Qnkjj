from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models
import datetime
import os
from p2 import settings


class Person(models.Model):
    SEX_CHOICE = (
        ('1', '男'),
        ('2', '女'),
    )

    RACE_CHOICE = (
        ('1', '汉族'),
        ('2', '蒙古族'),
        ('3', '回族'),
        ('4', '藏族'),
        ('5', '维吾尔族'),
        ('6', '苗族'),
        ('7', '彝族'),
        ('8', '壮族'),
        ('9', '布依族'),
        ('10', '朝鲜族'),
        ('11', '满族'),
        ('12', '侗族'),
        ('13', '瑶族'),
        ('14', '白族'),
        ('15', '土家族'),
        ('16', '哈尼族'),
        ('17', '哈萨克族'),
        ('18', '傣族'),
        ('19', '黎族'),
        ('20', '傈僳族'),
        ('21', '佤族'),
        ('22', '佤族'),
        ('23', '高山族'),
        ('24', '拉祜族'),
        ('25', '水族'),
        ('26', '东乡族'),
        ('27', '纳西族'),
        ('28', '景颇族'),
        ('29', '柯尔克孜族'),
        ('30', '土族'),
        ('31', '达斡尔族'),
        ('32', '仫佬族'),
        ('33', '羌族'),
        ('34', '布朗族'),
        ('35', '撒拉族'),
        ('36', '毛难族'),
        ('37', '仡佬族'),
        ('38', '锡伯族'),
        ('39', '阿昌族'),
        ('40', '普米族'),
        ('41', '塔吉克族'),
        ('42', '怒族'),
        ('43', '乌孜别克族'),
        ('44', '俄罗斯族'),
        ('45', '鄂温克族'),
        ('46', '崩龙族'),
        ('47', '保安族'),
        ('48', '裕固族'),
        ('49', '京族'),
        ('50', '塔塔尔族'),
        ('51', '独龙族'),
        ('52', '鄂伦春族'),
        ('53', '赫哲族'),
        ('54', '门巴族'),
        ('55', '珞巴族'),
        ('56', '基诺族'),
        ('57', '其他'),
        ('58', '外国血统'),
    )

    NATION_CHOICE = (
        ('1', '中国'),
        ('2', '美国'),
        ('3', '加拿大'),
        ('4', '墨西哥'),
        ('5', '巴西'),
        ('6', '古巴'),
        ('7', '阿根廷'),
        ('8', '智利'),
        ('9', '印度'),
        ('10', '日本'),
        ('11', '越南'),
        ('12', '泰国'),
        ('13', '柬埔寨'),
        ('14', '印度尼西亚'),
        ('15', '澳大利亚'),
        ('16', '老挝'),
        ('16', '菲律宾'),
        ('17', '新加坡'),
        ('18', '新西兰'),
        ('19', '俄罗斯'),
        ('20', '巴基萨塔'),
        ('21', '法国'),
        ('22', '英国'),
        ('23', '德国'),
        ('24', '西班牙'),
        ('25', '挪威'),
        ('26', '瑞士'),
        ('27', '瑞典'),
        ('28', '希腊'),
        ('29', '埃及'),
        ('30', '以色列'),
        ('31', '比利时'),
        ('32', '罗马尼亚'),
        ('33', '丹麦'),
        ('34', '波兰'),
        ('35', '荷兰'),
        ('36', '南非'),
        ('37', '朝鲜'),
        ('38', '韩国'),
        ('40', '土耳其'),
        ('41', '其他'),
    )

    POLITICAL_CHOICE = (
        ('1', '中共党员'),
        ('2', '中共预备党员'),
        ('3', '共青团员'),
        ('4', '民革党员'),
        ('5', '民盟党员'),
        ('6', '民建党员'),
        ('7', '民进党员'),
        ('8', '农工党党员'),
        ('9', '致公党党员'),
        ('10', '九三学社社员'),
        ('11', '台盟盟员'),
        ('12', '无党派人士'),
        ('13', '群众'),
    )
    DEGREE_CHOICE = (
        ('1', '研究生'),
        ('2', '本科'),
        ('3', '专科'),
        ('4', '中专'),
        ('5', '技工'),
        ('6', '其他'),
    )
    TITLE_CHOICE = (
        ('1', '高级'),
        ('2', '副高级'),
        ('3', '中级'),
        ('4', '初级'),
    )
    HIGHEST_DEGREE_CHOICE = (
        ('1', '博士'),
        ('2', '硕士'),
        ('3', '学士'),
        ('4', '其他'),
    )



    person_name = models.CharField(max_length=100, verbose_name='姓名', help_text='姓名')
    person_sex = models.CharField(max_length=2, choices=SEX_CHOICE, verbose_name='性别', help_text='性别')
    person_birthday = models.DateField(verbose_name='出生日期', help_text='出生日期')
    person_race = models.CharField(max_length=20, verbose_name='民族', help_text='民族', choices=RACE_CHOICE)
    person_degree = models.CharField(max_length=2, verbose_name='学历', help_text='学历', choices=DEGREE_CHOICE)
    person_highest_degree = models.CharField(max_length=2, verbose_name='学位', help_text='学位',
                                             choices=HIGHEST_DEGREE_CHOICE)
    person_major = models.CharField(max_length=30, verbose_name='专业技术职务', help_text='现所从事的研究领域或专业')
    person_position = models.CharField(max_length=20, verbose_name='行政职务', help_text='行政职务')
    person_excel = models.CharField(max_length=100, verbose_name='专业专长', help_text='专业专长')
    person_second_major = models.CharField(max_length=20, verbose_name='所属二级学科', help_text='所属二级学科')
    person_nation = models.CharField(max_length=20, verbose_name='国籍', help_text='国籍', choices=NATION_CHOICE)
    person_id_no = models.CharField(max_length=30, verbose_name='身份证号', help_text='身份证号')
    person_political_status = models.CharField(max_length=30, verbose_name='政治面貌', help_text='政治面貌',
                                               choices=POLITICAL_CHOICE)
    person_province = models.CharField(max_length=20, verbose_name='所在地-省', help_text='所在地-省')
    person_city = models.CharField(max_length=20, verbose_name='所在地-市', help_text='所在地-市')
    person_mobile = models.CharField(max_length=20, verbose_name='手机', help_text='手机')
    person_email = models.EmailField(verbose_name='电子信箱', help_text='电子信箱')
    person_org_position = models.TextField(verbose_name='在国内外团体的任职情况', help_text='在国内外团体的任职情况')
    person_social_position = models.TextField(verbose_name='社会职务', help_text='担任省级以上人大代表、政协委员、党代会代表及以上职 务')

    def __unicode__(self):
        return self.person_name


class Study(models.Model):
    study_begin = models.DateField(verbose_name='起始年月', help_text='起始年月')
    study_end = models.DateField(verbose_name='结束年月', help_text='结束年月')
    study_place = models.CharField(max_length=50, verbose_name='校及院系名称', help_text='校及院系名称')
    study_major = models.CharField(max_length=30, verbose_name='专业', help_text='专业')
    study_degree = models.CharField(max_length=20, verbose_name='学位', help_text='学位')
    person = models.ForeignKey(Person, related_name='study')

    def __unicode__(self):
        return self.study_major


class Experience(models.Model):
    exp_begin = models.DateField(verbose_name='起始年月', help_text='从大专或大学开始')
    exp_end = models.DateField(verbose_name='结束年月', help_text='结束年月')
    exp_place = models.CharField(max_length=120, verbose_name='工作单位', help_text='工作单位')
    occupation = models.CharField(max_length=50, verbose_name='职务/职称', help_text='职务/职称')
    person = models.ForeignKey(Person, related_name='experiences')

    def __unicode__(self):
        return self.occupation


class Fund(models.Model):
    fund_year =models.IntegerField(verbose_name='年度',help_text='年度')
    fund_type=models.CharField(max_length=10,verbose_name='基金种类',help_text='基金种类')
    fund_name=models.CharField(max_length=25,verbose_name='基金项目名称',help_text='基金项目名称')
    fund_money=models.IntegerField(verbose_name='金额',help_text='金额')
    fund_order=models.IntegerField(verbose_name='排名',help_text='排名')
    person=models.ForeignKey(Person, related_name='funds')

    def __unicode__(self):
        return self.fund_name


class Project(models.Model):
    STATUS_CHOICE = (
        ('0', '申报填写'),
        ('1', '学会初审'),
        ('2', '申请撤回'),
        ('3', '专家审核'),
        ('4', '审核结束'),
    )
    LEVEL_CHOICE = (
        ('0', '未获奖'),
        ('1', '一等奖'),
        ('2', '二等奖'),
        ('3', '三等奖'),
    )
    TYPE_CHOICE = (
        (0, '学术研究'),
        (1, '技术实践'),
        (2, '推广普及'),
    )

    project_status = models.CharField(max_length=2, verbose_name='申报状态', choices=STATUS_CHOICE, default='0')
    project_level = models.CharField(max_length=2, verbose_name='评奖等级', choices=LEVEL_CHOICE, default='0')
    project_type = models.CharField(max_length=2, verbose_name='项目类型', choices=TYPE_CHOICE, default='0')
    project_pdf = models.FileField(upload_to='pdf/' + str(datetime.datetime.now().year), verbose_name='报告地址', null=True,
                                   blank=True)
    person=models.ForeignKey(Person,related_name='projects')


class Unit(models.Model):
    UNIT_CHOICE = (
        ('1', '高等院校'),
        ('2', '科研院所'),
        ('3', '国有企业'),
        ('4', '民营企业'),
        ('5', '外资企业'),
        ('6', '事业单位'),
        ('7', '政府机关'),
        ('8', '自由职业者'),
        ('9', '其他'),
    )
    person_unit = models.CharField(max_length=100, verbose_name='工作单位', help_text='工作单位')
    person_unit_type = models.CharField(max_length=100, verbose_name='单位性质', help_text='单位性质', choices=UNIT_CHOICE)
    person_unit_position = models.CharField(max_length=100, verbose_name='单位地址', help_text='单位地址')
    unit_zipcode = models.CharField(max_length=10, verbose_name='邮政编码', help_text='邮政编码')
    unit_contact_phone = models.CharField(max_length=100, verbose_name='单位电话', help_text='单位电话')
    unit_fax = models.CharField(max_length=50, verbose_name='传真号码', help_text='传真号码')
    person=models.OneToOneField(Person,related_name='unit')

    def __unicode__(self):
        return self.person_unit

    def merged_status(self):
        merged_status = '0'
        if os.path.exists(os.path.join(settings.BASE_DIR, 'app3', 'templates', 'temp', str(self.id)+'_1.pdf')):
            merged_status = '1'
        if os.path.exists(os.path.join(settings.BASE_DIR, 'media', 'merged', str(self.id)+'_merged.pdf')):
            merged_status = '2'
        return merged_status

    def __unicode__(self):
        return self.project_status


class App3User(models.Model):
    user = models.OneToOneField(User, related_name='app3_user')  #save unauth
    setup_date = models.DateField(auto_now_add=datetime.datetime.now(), verbose_name="创建时间")
    user_unit = models.ForeignKey(Unit, related_name='users', null=True)


class Reward(models.Model):
    LEVEL_CHOICE = (
        ('0', '特等奖'),
        ('1', '一等奖'),
        ('2', '二等奖'),
        ('3', '三等奖'),
        ('4', '其他等级'),

    )
    reward_type = models.CharField(max_length=100, verbose_name='奖项类型', help_text='奖项类型')
    reward_name = models.CharField(max_length=200, verbose_name='奖项名称', help_text='奖项名称')
    reward_level = models.CharField(max_length=2, verbose_name='奖项等级', help_text='奖项等级', choices=LEVEL_CHOICE)
    reward_year = models.CharField(max_length=10, verbose_name='奖项年度', help_text='奖项年度')
    reward_order = models.IntegerField(verbose_name='奖项排名', help_text='奖项排名')
    reward_work = models.TextField(verbose_name='工作概述', help_text='工作概述')
    person = models.ForeignKey(Person, related_name='rewards')

    def __unicode__(self):
        return self.reward_name

    class Meta:
        ordering = ('reward_order',)


class ProjectAppendix(models.Model):
    project_appendix = models.FileField(upload_to='appendix', verbose_name='附件目录', help_text='附件目录')
    project = models.OneToOneField(Project, related_name='appendixes')


class Apply(models.Model):
    apply_content=models.TextField(verbose_name='科技成果应用情况或技术推广情况', help_text='技术实践类、普及推广类填写，请附有关证明材料')
    person = models.ForeignKey(Person, related_name='applies', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.apply_content


class Property(models.Model):
    property_content = models.TextField(verbose_name='发表论文、专著的情况',help_text='发表论文、专著的情况')
    person = models.OneToOneField(Person, related_name='property')


class Innovation(models.Model):
    innovation = models.TextField(verbose_name='主要科学发现、技术创新或技术推广要点', help_text='主要科学发现、技术创新或技术推广要点', null=True)
    person = models.OneToOneField(Person, related_name='innovation')


class Achievements(models.Model):
    achievements=models.TextField(verbose_name='主要科学技术成就和贡献',help_text='应以国内取得的成果为主，并均应为主要完成人或主要贡献者')
    person = models.OneToOneField(Person, related_name='achievements')


class ProjectRecommendOpinion(models.Model):
    project_recommend_opinion = models.TextField(verbose_name='推荐单位意见', help_text='推荐单位意见')
    project = models.OneToOneField(Project, related_name='project_recommend_opinion')


class WorkUnitRecommendOpinion(models.Model):
    recommend_opinion = models.TextField(verbose_name='工作单位意见', help_text='工作单位意见')
    person = models.OneToOneField(Project, related_name='workUnit_recommend_opinion')



