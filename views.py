from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse
from django.views import generic
from django.core import serializers
import json

# Create your views here.
from .models import Affiliation, Character, Movement, Battalion, UnitClass, CurrentUnit, Class_Weakness, Gender, Weakness
app_name = 'FE3HApp'

class IndexView(generic.TemplateView):
	template_name = app_name + '/index.html'


def characterlist(request):
	template_name = app_name + '/characterlist.html'
	character_list = Character.objects.order_by('id')
	gender = Gender.objects.order_by('id').values_list('gender', flat=True)[2:]
	affiliation_list = Affiliation.objects.order_by('id').values_list('affiliation', flat=True)[1:6]
	context = {
		'character_list': character_list,
		'gender': gender,
		'affiliation_list': affiliation_list,
	}
	return render(request, template_name, context)


def character(request, character_id):
	template_name = app_name + '/character.html'
	character = get_object_or_404(Character, pk=character_id)
	context = {
		'character': character, 
	}
	return render(request, template_name, context)


class MovementListView(generic.ListView):
	template_name = app_name + '/movementlist.html'
	context_object_name = 'movement_list'
	def get_queryset(self):
		return Movement.objects.order_by('id')

def movement(request, movement_id):
	return HttpResponse("You're looking at movement: %s" % movement_id)


class AffiliationListView(generic.ListView):
	template_name = app_name + '/affiliationlist.html'
	context_object_name = 'affiliation_list'
	def get_queryset(self):
		return Affiliation.objects.order_by('id')


def affiliation(request, affiliation_id):
	template_name = app_name + '/affiliation.html'
	affl_chara_list = Character.objects.filter(affiliation_id=affiliation_id)
	affl_btl_list = Battalion.objects.filter(affiliation_id=affiliation_id)

	context = {
		'affl_chara_list': affl_chara_list,
		'affl_btl_list': affl_btl_list,
	}
	return render(request, template_name, context)


def unitclasslist(request):
	template_name = app_name + '/unitclasslist.html'
	unitclass_list = UnitClass.objects.order_by('id')
	unitclass_weakness = Class_Weakness.objects.order_by('id')
	gender = Gender.objects.order_by('id')[2:]
	movement_list = Movement.objects.order_by('id')
	weakness_list = Weakness.objects.order_by('id')
	context = {
		'unitclass_list': unitclass_list,
		'unitclass_weakness': unitclass_weakness,
		'gender': gender,
		'movement_list': movement_list,
		'weakness_list': weakness_list,
	}
	return render(request, template_name, context)


def unitclass(request, unitclass_id):
	try:
		template_name = app_name + '/unitclass.html'
		unitclass = get_object_or_404(UnitClass, pk=unitclass_id)
		unitclass_weakness = Class_Weakness.objects.filter(class_id=unitclass_id)
		context = {
			'unitclass': unitclass,
			'unitclass_weakness': unitclass_weakness,
		}
	except Class_Weakness.DoesNotExist:
		context = {
			'unitclass': unitclass,
			'unitclass_weakness': None,
		}
	return render(request, template_name, context)


def battalionlist(request):
	template_name = app_name + '/battalionlist.html'
	battalion_list = Battalion.objects.order_by('id')
	affiliation_list = Affiliation.objects.exclude(affiliation="その他")[1:]
	context = {
		'battalion_list': battalion_list,
		'affiliation_list': affiliation_list,
	}
	return render(request, template_name, context)


def battalion(request, battalion_id):
	template_name = app_name + '/battalion.html'
	battalion = get_object_or_404(Battalion, pk=battalion_id)
	context = {
		'battalion': battalion,
	}
	return render(request, template_name, context)


def currentunitlist(request):
	try:
		template_name = app_name + '/currentunitlist.html'
		json_serializer = serializers.get_serializer("json")()
		character_list = json_serializer.serialize(Character.objects.all().order_by('id'), ensure_ascii=False)
		unitclass_list = json_serializer.serialize(UnitClass.objects.all().order_by('id'), ensure_ascii=False)
		unitclass_noblemale = UnitClass.objects.exclude(gender=4).exclude(name='平民').exclude(grade='特殊職').exclude(name='ロード')
		unitclass_noblefemale = UnitClass.objects.exclude(gender=3).exclude(name='平民').exclude(grade='特殊職').exclude(name='ロード')
		unitclass_commonmale = UnitClass.objects.exclude(gender=4).exclude(name='貴族').exclude(grade='特殊職').exclude(name='ロード')
		unitclass_commonfemale = UnitClass.objects.exclude(gender=3).exclude(name='貴族').exclude(grade='特殊職').exclude(name='ロード')

		unitclass_byleth = UnitClass.objects.exclude(name='貴族').exclude(name='ロード').exclude(name='踊り子').exclude(name='アーマーロード').exclude(name='カイゼリン').exclude(name='ハイロード').exclude(name='マスターロード').exclude(name='ドラゴンロード').exclude(name='バルバロッサ').exclude(name='死神騎士')
		unitclass_edelgard = UnitClass.objects.exclude(gender=3).exclude(name='平民').exclude(name='ニルヴァーナ').exclude(name='ハイロード').exclude(name='マスターロード').exclude(name='ドラゴンロード').exclude(name='バルバロッサ').exclude(name='死神騎士')
		unitclass_dimitri = UnitClass.objects.exclude(gender=4).exclude(name='平民').exclude(name='ニルヴァーナ').exclude(name='アーマーロード').exclude(name='カイゼリン').exclude(name='ドラゴンロード').exclude(name='バルバロッサ').exclude(name='死神騎士')
		unitclass_claude = UnitClass.objects.exclude(gender=4).exclude(name='平民').exclude(name='ニルヴァーナ').exclude(name='アーマーロード').exclude(name='カイゼリン').exclude(name='ハイロード').exclude(name='マスターロード').exclude(name='死神騎士')

		unitclass_grade_list = UnitClass.objects.distinct().values_list('grade', flat=True)

		currentunit_list = CurrentUnit.objects.order_by('id')
		message = ""
	except CurrentUnit.DoesNotExist:
		currentunit_list = None
	else:
		context = {
			'character_list': character_list,
			'currentunit_list': currentunit_list,
			'unitclass_list': unitclass_list,
			'unitclass_noblemale': unitclass_noblemale,
			'unitclass_noblefemale': unitclass_noblefemale,
			'unitclass_commonmale': unitclass_commonmale,
			'unitclass_commonfemale': unitclass_commonfemale,
			'unitclass_byleth': unitclass_byleth,
			'unitclass_edelgard': unitclass_edelgard,
			'unitclass_dimitri': unitclass_dimitri,
			'unitclass_claude': unitclass_claude,
			'unitclass_grade_list': unitclass_grade_list,
			'message': message,
		}
		return render(request, template_name, context)

def addchara(request):
	if request.method == 'POST':
		body = json.loads(request.body.decode('utf-8'))
		try:
			character_add = Character.objects.get(pk=body['character_id'])
			CurrentUnit.objects.create(character=character_add)
		except Character.DoesNotExist as e:
			print(str(e))
			return HttpResponse("Character does not exist")
		except ValueError as e:
			print(str(e))
			return HttpResponse("Character does not exist")
		except Exception as e:
			print(str(e))
			return HttpResponse("Character already exists")
		else:
			return HttpResponseRedirect(reverse('FE3HApp:currentunit_list'))

def removechara(request):
	if request.method == 'POST':
		body = json.loads(request.body.decode('utf-8'))
		try:
			chara = Character.objects.get(name=body['character'])
			character_remove = CurrentUnit.objects.get(character=chara)
			if character_remove:
				character_remove.delete()
		except Exception as e:
			print(str(e))
			return HttpResponse("Encountered problem")
		else:
			return HttpResponseRedirect(reverse('FE3HApp:currentunit_list'))

def updatechara(request):
	if request.method == 'POST':
		body = json.loads(request.body.decode('utf-8'))

		for unit in body:
			try:
				#print(unit['character'])
				chara = Character.objects.get(name=unit['character'])
				unit['character'] = chara.id
				if (unit['unit_class'] != None):
					cla = UnitClass.objects.get(name=unit['unit_class'])
					unit['unit_class'] = cla.id
				currUnit = CurrentUnit.objects.filter(character=chara).update(**unit)
				#for field in currUnit.get_fields():
					#if field.name != 'id':
						#print(currUnit[field.name])
			except Exception as e:
				print(str(e))
		# Return status code
		return HttpResponse(content=b'Test')

def getunusedchara(request):
	currentunits = CurrentUnit.objects.order_by('id')
	chara = Character.objects.order_by('id')
	for unit in currentunits:
		chara = chara.exclude(id=unit.character_id)

	json_serializer = serializers.get_serializer("json")()
	characters = json_serializer.serialize(chara, ensure_ascii=False)
	affiliation = json_serializer.serialize(Affiliation.objects.order_by('id'), ensure_ascii=False)
	context = {
		'characters': characters,
		'affiliation': affiliation,
	}
	data = json.dumps(context)
	return HttpResponse(data,
		headers={'Content-Type': 'application/json'},
		)

def getcharaunitclasslist(request):
	if request.method == 'POST':
		body = json.loads(request.body.decode('utf-8'))
		chara = body['character']
		unitclass_list = UnitClass.objects.order_by('id')
		try:
			match chara:
				case '主人公':
					unitclass_list = unitclass_list.exclude(name='貴族').exclude(name='ロード').exclude(name='踊り子').exclude(name='アーマーロード').exclude(name='カイゼリン').exclude(name='ハイロード').exclude(name='マスターロード').exclude(name='ドラゴンロード').exclude(name='バルバロッサ').exclude(name='死神騎士')
				case 'エーデルガルト':
					unitclass_list = unitclass_list.exclude(gender=3).exclude(name='平民').exclude(name='ニルヴァーナ').exclude(name='ハイロード').exclude(name='マスターロード').exclude(name='ドラゴンロード').exclude(name='バルバロッサ').exclude(name='死神騎士')
				case 'ディミトリ':
					unitclass_list = unitclass_list.exclude(gender=4).exclude(name='平民').exclude(name='ニルヴァーナ').exclude(name='アーマーロード').exclude(name='カイゼリン').exclude(name='ドラゴンロード').exclude(name='バルバロッサ').exclude(name='死神騎士')
				case 'クロード':
					unitclass_list = unitclass_list.exclude(gender=4).exclude(name='平民').exclude(name='ニルヴァーナ').exclude(name='アーマーロード').exclude(name='カイゼリン').exclude(name='ハイロード').exclude(name='マスターロード').exclude(name='死神騎士')
				case _:
					charaObj = Character.objects.get(name=chara)
					if charaObj.gender == '男':
						if charaObj.aristocrat:
							unitclass_list = unitclass_list.exclude(gender=4).exclude(name='平民').exclude(grade='特殊職').exclude(name='ロード')
						else:
							unitclass_list = unitclass_list.exclude(gender=4).exclude(name='貴族').exclude(grade='特殊職').exclude(name='ロード')
					else:
						if charaObj.aristocrat:
							unitclass_list = unitclass_list.exclude(gender=3).exclude(name='平民').exclude(grade='特殊職').exclude(name='ロード')
						else:
							unitclass_list = unitclass_list.exclude(gender=3).exclude(name='貴族').exclude(grade='特殊職').exclude(name='ロード')
		except Exception as e:
			print(str(e))
			return HttpResponse(content=b'character not found')
		else:
			json_serializer = serializers.get_serializer("json")()
			unitclass_json = json_serializer.serialize(unitclass_list, ensure_ascii=False)
			return HttpResponse(content=unitclass_json)

def getcharaclassgrowthrates(request):
	if request.method == 'POST':
		body = json.loads(request.body.decode('utf-8'))
		try:
			chara = Character.objects.filter(name=body['character'])
			unitclass = UnitClass.objects.filter(name=body['unit_class'])
		except Exception as e:
			return HttpResponse(content='ERROR')
		else: 
			json_serializer = serializers.get_serializer("json")()
			chara_json = json_serializer.serialize(chara, ensure_ascii=False)
			unitclass_json = json_serializer.serialize(unitclass, ensure_ascii=False)
			context = {
				'character': chara_json,
				'unitclass': unitclass_json,
			}
			data = json.dumps(context)
			return HttpResponse(data)
