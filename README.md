# FE3H
Web application for Fire Emblem: Three Houses (日本語). Select and add units within your army and check: growth rates, stats, possible combinations of classes and skills, etc.\
ファイアーエムブレム：風花雪月向けのウェブアプリ\
ユニットを自軍へ追加し、ステータス・成長率・クラス・スキルを組み合わせてみよう！\

NOTE:\
This is a Django Application, and as far as I understand, requires a machine with Django installed to run it\
Start an application within Django and add the folders to it (... I guess? I haven't tested it yet.)

ANOTHER NOTE:\
Currently, I am working with <u>JP data</u>, so currently, the pages are *mainly* in Japanese (with some EN here and there).\
I may work on making multiple locales for the webapp. (Currently, this is just a possibility)

Build v0.1:
  - With the current build, it does not have the data stored within the database, nor does this build have the queries to insert it into the DB
    (I'll need to do something about that)
  - Pages for the following are made:
     - View playable character list
        - View character Limits and growth rates
     - View all classes
        - View class growth rates, weakness, etc.
     - View all Battalions available in the game
     - View Affiliations (in other words, the nations that characters reside under)
     - View for movement type (this was just to test out views may remove in future builds)
     - View for Current Units in your army
        - Add/remove units
        - Update their level, classes, stats
        - Also check a units growth rate depending on the character and selected class

Things to work on next:
  - Add skills data model
  - Skill list
     - Which characters are able to learn it
     - Requirements
  - Page to assign battalions to Current Units
  - Update Character page with possible classes and their growth rates - might help with deciding which class to change to
     - Along with the classes and growth rates, maybe also add the list of skills a character can learn -> clicking leads to a page showing requirements
  - Realized, I should also separate my scripts into other files

??Maybe I should add a reference page or something to dedicate where I got this info from??
