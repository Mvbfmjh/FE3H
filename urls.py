from django.urls import path

from . import views

app_name = 'FE3HApp'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('character/', views.characterlist, name='character_list'),
    #path('movement/', views.movementlist, name='movement_'),
    #path('affiliation/', views.affiliationlist, name='affiliation_list'),

    path('', views.IndexView.as_view(), name='index'),

    # Character-related pages
    path('character/', views.characterlist, name='character_list'),
    path('character/<int:character_id>/', views.character, name='character'),

    # Affiliation-related pages
    path('affiliation/', views.AffiliationListView.as_view(), name='affiliation_list'),
    path('affiliation/<int:affiliation_id>/', views.affiliation, name='affiliation'),

    # Movement-related pages
    path('movement/', views.MovementListView.as_view(), name='movement_list'),
    path('movement/<int:movement_id>/', views.movement, name='movement'),

    # UnitClass-related pages
    path('class/', views.unitclasslist, name='unitclass_list'),
    path('class/<int:unitclass_id>', views.unitclass, name='unitclass'),

    # Battalion-related pages
    path('battalion/', views.battalionlist, name='battalion_list'),
    path('battalion/<int:battalion_id>', views.battalion, name='battalion'),

    # Current-related pages
    path('currentunits/', views.currentunitlist, name='currentunit_list'),
    path('currentunits/add', views.addchara, name='currentunit_add'),
    path('currentunits/update', views.updatechara, name='currentunit_update'),
    path('currentunits/remove', views.removechara, name='currentunit_remove'),
    path('currentunits/getunused', views.getunusedchara, name='currentunit_getunused'),
    path('currentunits/getclasslist', views.getcharaunitclasslist, name='currentunit_classlist'),
    path('currentunits/getgrowthrates', views.getcharaclassgrowthrates, name='currentunit_growthrates'),
]