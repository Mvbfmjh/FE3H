from django.db import models

# Create your models here.
SUBJECT_LEVEL = (
	('E', 'E'),
	('E+', 'E+'),
	('D', 'D'),
	('D+', 'D+'),
	('C', 'C'),
	('C+', 'C+'),
	('B', 'B'),
	('B+', 'B+'),
	('A', 'A'),
	('A+', 'A+'),
	('S', 'S'),
	('S+', 'S+'),
)

class Gender(models.Model):
	gender = models.CharField(max_length=6)

	def __str__(self):
		return self.gender

class Movement(models.Model):
	movement_type = models.CharField(max_length=20)
	is_flying = models.BooleanField()

	def __str__(self):
		if self.is_flying:
			return self.movement_type + " flying"
		return self.movement_type + " grounded"

class Weakness(models.Model):
	weakness = models.CharField(max_length=20)
	def __str__(self):
		return self.weakness

class Affiliation(models.Model):
	affiliation = models.CharField(max_length=50)
	def __str__(self):
		return self.affiliation

class Character(models.Model):
	name = models.CharField(max_length=50)
	gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
	affiliation = models.ForeignKey(Affiliation, on_delete=models.SET_NULL, null=True)
	aristocrat = models.BooleanField()

	hp_growth = models.PositiveSmallIntegerField()
	str_growth = models.PositiveSmallIntegerField()
	mag_growth = models.PositiveSmallIntegerField()
	dex_growth = models.PositiveSmallIntegerField()
	spd_growth = models.PositiveSmallIntegerField()
	lck_growth = models.PositiveSmallIntegerField()
	def_growth = models.PositiveSmallIntegerField()
	res_growth = models.PositiveSmallIntegerField()
	cha_growth = models.PositiveSmallIntegerField()

	hp_limit = models.PositiveSmallIntegerField()
	str_limit = models.PositiveSmallIntegerField()
	mag_limit = models.PositiveSmallIntegerField()
	dex_limit = models.PositiveSmallIntegerField()
	spd_limit = models.PositiveSmallIntegerField()
	lck_limit = models.PositiveSmallIntegerField()
	def_limit = models.PositiveSmallIntegerField()
	res_limit = models.PositiveSmallIntegerField()
	cha_limit = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name + " (" + self.gender.gender + ") Affl: " + self.affiliation.affiliation

	def get_growth_rates(self):
		return [self.hp_growth, self.str_growth, self.mag_growth, self.dex_growth, self.spd_growth, self.lck_growth, self.def_growth, self.res_growth, self.cha_growth]

class Battalion(models.Model):
	name = models.CharField(max_length=50)
	affiliation = models.ForeignKey(Affiliation, on_delete=models.SET_NULL, null=True)
	#Need to think of movement relationships again
	movement = models.ForeignKey(Movement, on_delete=models.SET_NULL, null=True)
	auth_requirement = models.CharField(max_length=2, choices=SUBJECT_LEVEL)

	endurance = models.PositiveSmallIntegerField(default=0)
	physical = models.SmallIntegerField(default=0)
	magical = models.SmallIntegerField(default=0)
	hit_rate = models.SmallIntegerField(default=0)
	critical = models.SmallIntegerField(default=0)
	avoidance = models.SmallIntegerField(default=0)
	protection = models.SmallIntegerField(default=0)
	resistance = models.SmallIntegerField(default=0)
	charm = models.SmallIntegerField(default=0)

	gambit = models.CharField(max_length=50, default='')

class UnitClass(models.Model):
	name = models.CharField(max_length=50, default='')
	grade = models.CharField(max_length=10, default='')
	level_requirement = models.PositiveSmallIntegerField(default=0)
	gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
	movement = models.ForeignKey(Movement, on_delete=models.SET_NULL, null=True)
	weakness = models.ManyToManyField(
		Weakness,
		through='Class_Weakness',
		through_fields=('class_id','weakness_id'),
		)

	hp_growth = models.SmallIntegerField(default=0)
	str_growth = models.SmallIntegerField(default=0)
	mag_growth = models.SmallIntegerField(default=0)
	dex_growth = models.SmallIntegerField(default=0)
	spd_growth = models.SmallIntegerField(default=0)
	lck_growth = models.SmallIntegerField(default=0)
	def_growth = models.SmallIntegerField(default=0)
	res_growth = models.SmallIntegerField(default=0)
	cha_growth = models.SmallIntegerField(default=0)

	hp_base = models.PositiveSmallIntegerField(null=True, default=0)
	str_base = models.PositiveSmallIntegerField(null=True, default=0)
	mag_base = models.PositiveSmallIntegerField(null=True, default=0)
	dex_base = models.PositiveSmallIntegerField(null=True, default=0)
	spd_base = models.PositiveSmallIntegerField(null=True, default=0)
	lck_base = models.PositiveSmallIntegerField(null=True, default=0)
	def_base = models.PositiveSmallIntegerField(null=True, default=0)
	res_base = models.PositiveSmallIntegerField(null=True, default=0)
	cha_base = models.PositiveSmallIntegerField(null=True, default=0)

	prof_sword = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_lance = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_axe = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_bow = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_brawl = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_reason = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_faith = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_authority = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_armor = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_riding = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	prof_flying = models.CharField(max_length=2, null=True, default='', choices=SUBJECT_LEVEL)
	
	def get_growth_rates(self):
		return [self.hp_growth, self.str_growth, self.mag_growth, self.dex_growth, self.spd_growth, self.lck_growth, self.def_growth, self.res_growth, self.cha_growth]

	def get_base_stats(self):
		return [self.hp_base, self.str_base, self.mag_base, self.dex_base, self.spd_base, self.lck_base, self.def_base, self.res_base, self.cha_base]

	def __str__(self):
		return self.name + ' (' + self.grade + ')'


class Class_Weakness(models.Model):
	class_id  = models.ForeignKey(UnitClass, on_delete=models.CASCADE)
	weakness_id = models.ForeignKey(Weakness, on_delete=models.CASCADE)

class CurrentUnit(models.Model):
	character = models.OneToOneField(Character, on_delete=models.CASCADE)
	unit_class = models.ForeignKey(UnitClass, null=True, default=None, on_delete=models.SET_NULL)
	battalion = models.ForeignKey(Battalion, null=True, default=None, on_delete=models.SET_NULL)
	level = models.PositiveSmallIntegerField(default=0)

	unit_hp = models.PositiveSmallIntegerField(default=0)
	unit_str = models.PositiveSmallIntegerField(default=0)
	unit_mag = models.PositiveSmallIntegerField(default=0)
	unit_dex = models.PositiveSmallIntegerField(default=0)
	unit_spd = models.PositiveSmallIntegerField(default=0)
	unit_lck = models.PositiveSmallIntegerField(default=0)
	unit_def = models.PositiveSmallIntegerField(default=0)
	unit_res = models.PositiveSmallIntegerField(default=0)
	unit_cha = models.PositiveSmallIntegerField(default=0)

	prof_sword = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_lance = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_axe = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_bow = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_brawl = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_reason = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_faith = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_authority = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_armor = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_riding = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)
	prof_flying = models.CharField(max_length=2, default='E', choices=SUBJECT_LEVEL)

	def check_if_under_limit(self):
		hp_check = unit_hp < character.hp_limit
		str_check = unit_str < character.str_limit
		mag_check = unit_mag < character.mag_limit
		dex_check = unit_dex < character.dex_limit
		spd_check = unit_spd < character.spd_limit
		lck_check = unit_lck < character.lck_limit
		def_check = unit_def < character.def_limit
		res_check = unit_res < character.res_limit
		cha_check = unit_cha < character.cha_limit
		return [hp_check, str_check, mag_check, dex_check, spd_check, lck_check, def_check, res_check, cha_check]
