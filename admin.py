from django.contrib import admin

# Register your models here.
from .models import Affiliation, Battalion, CurrentUnit, Character, Gender, Movement, UnitClass, Weakness, Class_Weakness
admin.site.register(Affiliation)
admin.site.register(Battalion)
admin.site.register(Character)
admin.site.register(UnitClass)
admin.site.register(CurrentUnit)
admin.site.register(Weakness)
admin.site.register(Class_Weakness)
admin.site.register(Gender)
admin.site.register(Movement)