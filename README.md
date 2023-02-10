# FE3H
Web application for Fire Emblem: Three Houses (日本語). Select and add units within your army and check: growth rates, stats, possible combinations of classes and skills, etc.
ファイアーエムブレム：風花雪月向けのウェブアプリ
ユニットを自軍へ追加し、ステータス・成長率・クラス・スキルを組み合わせてみよう！

NOTE: This is a Django Application, and as far as I understand, requires a machine with Django installed to run it
Start an application within Django and add the folders to it (... I guess? I haven't tested it yet.)


Build v0.1:
  - With the current build, it does not have the data stored within the database, nor does this build have the queries to insert it into the DB
    (I'll need to do something about that)
  - Pages for the following are made:
     -- View playable character list
        - View character Limits and growth rates
     -- View all classes
        - View class growth rates, weakness, etc.
     -- View all Battalions available in the game
     -- View Affiliations (in other words, the nations that characters reside under)
     -- View for movement type (this was just to test out views may remove in future builds)
     -- View for Current Units in your army
        - Add/remove units
        - Update their level, classes, stats
        - Also check a units growth rate depending on the character and selected class
