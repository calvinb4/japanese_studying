import random
import sys

len_args = len(sys.argv)

files_read = sys.argv[1:len_args+1]

keys = []
vals = []

for file in files_read:
    with open(file, 'r') as f:
        f = f.read()
        lines = f.splitlines()
        #keys = []
        #vals = []
        for line in lines:
            line = line.split(":")
            keys.append(line[0])
            vals.append(line[1])
        dictionary = dict(zip(keys, vals))

genki_combined = dict(zip(keys,vals))
        
# grade_1_k = ["one","two","three","four","five","six","seven","eight","nine","ten","one hundred","one thousand","ten thousand","top/above","bottom/below","left","right","inside","large","small","month/moon","day/sun","year","early","tree","woods","mountain","river","soil","sky","rice paddy","heaven/sky","life/bear/raw","flower","grass","insect","dog","person","name","female","male","child","eye","ear","mouth","hand","foot","see","sound","power","yen","evening","previous","air","enter","exit"]

# genki_1 = {"um...":"ano","now":"ima","english language":"eego","yes (inf.)":"ee","student":"gakusee","high school":"kookoo","p.m.":"gogo","a.m.":"gozen","years old":"sai","Mr./Ms.":"san","o-clock":"ji","people group":"jin","major":"senkoo","teacher":"sensee","that's right":"soo desu","I see/Is that so?":"soo desu ka","college":"daigaku","telephone":"denwa","friend":"tomodachi","name":"namae","what":"nani","Japan":"nihon","_ year student":"nensee","yes (form.)":"hai","half":"han","number":"bangoo","international student":"ryuugakusee","I":"watashi","usa":"amerika","britain":"igirisu","australia":"oosutoraria","korea":"kankoku","sweeden":"suweeden","china":"chuugoku","science":"kagaku","asian studies":"ajia kenkyuu","economics":"keezai","international relations":"kokusaikankee","computer":"konpyuutaa","anthropology":"jinruigaku","politics":"seeji","business":"bijinesu","literature":"bungaku","history":"rekishi","job":"shigoto","doctor":"isha","office worker":"kaishain","high school student":"kookoosee","housewife":"shufu","grad student":"daigakuinsee","college student":"daigakusee","lawyer":"bengoshi","mother":"okaasan","father":"otoosan","older brother":"oniisan","older sister":"oneesan","younger brother":"otooto","younger sister":"imooto","good morning (inf.)":"ohayoo","good morning (form.)":"ohayoo gozaimasu","good afternoon":"konnichiwa","good evening":"konbanwa","goodbye (ritualistic)":"sayoonara","goodbye (inf.)":"jaa mata","goodbye (form.)":"shitsureeshimasu","good night":"oyasuminasai","thank you (inf.)":"arigatoo","thank you (form.)":"arigatoo gozaimasu","excuse me/I'm sorry":"sumimasen","no":"iie","i'll go and come back":"ittekimasu","please go and come back":"itterasshai","I'm home":"tadaima","welcome home":"okaerinasai","thank you for the meal (before eating)":"itadakimasu","thank you for the meal (after eating)":"gochisoosamadeshita","how do you do?":"hajimemashite","nice to meet you":"yoroshiku onegaishimasu"}

# genki_2 = {"this one":"kore","that one":"sore","that one over there":"are","which one":"dore","this":"kono","that":"sono","that over there":"ano","which":"dono","here":"koko","there":"soko","over there":"asoko","where":"doko","who":"dare","delicious":"oishii","fish":"sakana","pork cutlet":"tonkatsu","meat":"niku","menu":"menyuu","vegetable":"yasai","pencil":"enpitsu","umbrella":"kasa","bag":"kaban","shoes":"kutsu","wallet":"saifu","jeans":"jiinzu","dictionary":"jisho","bicycle":"jitensha","newspaper":"shinbun","t shirt":"tiishatsu","watch/clock":"tokee","notebook":"nooto","pen":"pen","hat":"booshi","book":"hon","cafe":"kissaten","bank":"ginkoo","toilet":"toire","library":"toshokan","post office":"yuubinkyoku","usa":"amerika","britain":"igirisu","korea":"kankoku","china":"chuugoku","economics":"keezai","computer":"konpyuutaa","business":"bijinesu","history":"rekishi","mother":"okaasan","father":"otoosan","how much":"ikura","yen":"en","expensive":"takai","welcome to our store":"irasshaimase","please":"onegaishimasu","please give me":"kudasai","then":"jaa","here it is/please":"doozo","thank you":"doomo"}

# genki_3 = {"music":"ongaku","movie":"eega","magazine":"zasshi","sports":"supootsu","date (romantic)":"deeto","tennis":"tenisu","TV":"terebi","ice cream":"aisukuriimu","breakfast":"asagohan","alcohol":"osake","green tea":"ocha","coffee":"koohii","dinner":"bangohan","hamburger":"hanbaagaa","lunch":"hirugohan","water":"mizu","home":"ie","school":"gakkoo","morning":"asa","tomorrow":"ashita","when":"itsu","today":"kyoo","at about":"goro","tonight":"konban","weekend":"shuumatsu","saturday":"doyoobi","sunday":"nichiyoobi","every day":"mainichi","every night":"maiban","to go":"iku","to return":"kaeru","to hear":"kiku","to drink":"nomu","to speak":"hanasu","to read":"yomu","to get up":"okiru","to eat":"taberu","to sleep":"neru","to see":"miru","to come":"kuru","to do":"suru","to study":"benkyoosuru","good":"ii","early":"hayai","not much":"amari","not at all":"zenzen","usually":"taitei","a little":"chotto","sometimes":"tokidoki","often/much":"yoku","that's right/let me see":"soo desu ne","but":"demo","how about":"doodesuka"}

# genki_4 = {"spring":"horu","summer":"natsu","fall":"aki","winter":"fuyu","shopping":"kaimono","dog":"inu","souvenir":"omiyage","child":"kodomo","meal":"gohan","picture/photo":"shashin","desk":"tsukue","letter":"tegami","cat":"neko","person":"hito","temple":"otera","park":"kooen","bus stop":"basutei","hospital":"byooin","bookstore":"honya","town":"machi","yesterday":"kinoo","hours":"jikan","last week":"senshuu","when":"toki","monday":"getsuyoobi","tuesday":"kayoobi","wednesday":"suiyoobi","thursday":"mokuyoobi","friday":"kinyoobi","to meet":"au","to buy":"kau","to write":"kaku","to take":"toru","to wait":"matsu","alone":"hitoride","right":"migi","left":"hidari","front":"mae","back":"ushiro","inside":"naka","on":"ue","under":"shita","near/nearby":"chikaku","next":"tonari","between":"aida","part time job":"arubaito","class":"kurasu","you":"anata","chair":"isu","bread":"pan","e-mail":"meeru","supermarket":"suupaa","departement store":"depaato","hotel":"hoteru","restaurant":"resutoran","there is":"aru","to understand":"wakaru","a person is":"iru","about (interval of time)":"gurai","I'm sorry (inf.)":"gomennasai","so/therefore":"dakara","many/a lot":"takusan","together with a person":"to","why":"dooshite","and then":"soshite"}

# genki_5 = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","surfing":"safin","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","test":"tesuto","weather":"tenki","drink":"nomimono","postcard":"hagaki","bus":"basu","airplane":"hikooki","room":"heya","I (used by men)":"boku","holiday":"yasumi","travel":"ryokoo","new":"atarashii","hot":"atsui","busy":"isogashii","large":"ooki","interesting/funny":"omoshiroi","good-looking":"kakkoii","frightening":"kowai","cold":"samui","fun":"tanoshii","small":"chiisai","boring":"tsumaranai","old (thing)":"furui","difficult":"muzukashi","easy (problem)/kind (person)":"yasashii","cheap":"yasui","disgusted with":"kiraina","clean/beautiful":"kireina","healthy/energetic":"genkina","quiet":"shizukana","fond of/to like":"sukina","to hate":"daikiraina","to love":"daisukina","lively":"nigiyakana","not busy":"himana","to swim":"oyogu","to ask":"kiku","to ride/board":"noru","to do/preform":"yaru","to go out":"dekakeru","together":"isshoni","extremeely":"sugoku","and then":"sorekara","it's okay":"daijoobu","very":"totemo","what kind of...":"donna","counter (flat objects)":"mai","to (a place)/till (a time)":"made","mountain":"yama","river":"kawa","female":"onna","male":"otoko"}

# genki_6 = {"money":"okane","bath":"ofuro","kanji":"kanji","textbook":"kyookasho","this week":"konshuu","cd":"shiidii","municipal hospital":"shiminbyooin","shower":"shawaa","next":"tsugi","electricity":"denki","train":"densha","baggage":"nimotsu","personal computer":"pasokon","page":"peeji","window":"mado","night":"yoru","next week":"raishuu","next year":"rainen","tough situation":"taihenna","to play":"asobu","to hurry":"isogu","to take a bath":"ofuronihairu","to return (a thing)":"kaesu","to turn off/erase":"kesu","to die":"shinu","to sit down":"suwaru","to stand up":"tatsu","to smoke":"tabako o suu","to use":"tsukau","to help":"tetsudau","to enter":"hairu","to carry/hold":"motsu","to be absent; to rest":"yasumu","to open":"akeru","to teach":"oshieru","to get off":"oriru","to borrow":"kariru","to close":"shimeru","to take a shower":"shawaa o abiru","to turn on":"tsukeru","to make a phone call":"denwa o kakeru","to forget/leave behind":"wasureru","to bring a person":"tsuretekuru","to bring a thing":"mottekuru","later on":"atode","(do something) late":"osoku","that would be fine":"kekkoodesu","because":"kara","right away":"sugu","really?":"hontoodesuka","slowly/leisurely":"yukkuri","north":"kita","south":"minami","east":"higashi","west":"nishi","entrance":"kuchi","hometown":"shusshin","deru":"to exit","country":"kuni","foreign":"gaikoku"}

# genki_7 = {"older sister":"oneesan","apartment":"apaato","younger sister":"imooto","song":"uta","grandfather":"ojiisan","younger brother":"otooto","man":"otoko no hito","older brother":"oniisan","grandmother":"obaasan","woman":"onna no hito","company":"kaisha","family":"kazoku","hair":"kami","brothers and sisters":"kyoodai","mouth":"kuchi","country":"kuni","car":"kuruma","game":"geemu","conveinience store":"konbini","club activity":"saakuru","cafeteria/dining commons":"shokudoo","eye":"me","glasses":"megane","cute":"kawaii","tall (stature)":"takai","short (stature)":"hikui","long":"nagai","short (length)":"mijikai","fast":"hayai","kind":"shinsetsuna","convenient":"benrina","to sing":"utau","to put on a hat":"kaburu","to know":"shiru","to live":"sumu","to put on clothes (above waste)":"kiru","to put on clothes (below waste)":"haku","to gain weight":"futoru","to work for":"tsutomeru","to put on glasses":"kakeru","to lose weight":"yaseru","to get married":"kekkonsuru","not anything":"nanimo","one person":"hitori","two people":"futari","nothing in particular":"betsuni","hello (on phone)":"moshimoshi","of course":"mochiron","if you like":"yokattara"}

# genki_8 = {"it rains":"ame ga furu","to wash":"arau","to say":"iu","to need":"iru","to be late":"osokunaru","to think":"omoo","to cut":"kiru","to make":"tsukuru","to take (a thing)":"motteiku","to stare at":"jirojiromiru","to throw away":"suteru","to begin":"hajimeru","to drive":"untensuru","to do laundry":"sentakusuru","to clean":"soojisuru","to call":"denwasuru","to cook":"ryoorisuru","always":"itsumo","no":"uun","yes":"un","cheers!":"kanpai","that's too bad":"zannen","about/concerning":"nitsuite","not yet":"mada","all of the poeple together":"minnade","the day after tomorrow":"asatte","rain":"ame","office worker":"kaishain","camera":"kamera","karaoke":"karaoke","air":"kuuki","this morning":"kesa","blackboard":"kokuban","this month":"kongetsu","job/occupation":"shigoto","college student":"daigakusee","weather forecast":"tenkiyohoo","place":"tokoro","tomato":"tomato","summer":"natsu","something":"nanika","party":"paatii","barbecue":"baabekyuu","chopsticks":"hashi","winter":"fuyu","homestay":"hoomusutei","every week":"maishuu","next month":"raigetsu","skillful":"joozuna","clumsy/poor at":"hetana","famous":"yuumeina"}

# genki_9 = {"to dance":"odoru","something ends":"owaru","to be popular":"ninki ga aru","something begins":"hajimaru","to play a stringed instrument":"hiku","to get from somebody":"morau","to memorize":"oboeru","to appear/exit":"deru","to do physical exercise":"undoosuru","to take a walk":"sanposuru","from":"kara","by all means":"zehi","by the way":"tokorode","all":"minna","already":"moo","good child":"iiko","color":"iro","boxed lunch":"obentoo","japanese theatre art":"kabuki","guitar":"gitaa","last year":"kyonen","medicine":"kusuri","concert":"konsaato","near future":"kondo","essay/composition":"sakubun","exam":"shiken","ski":"sukii","last month":"sengetsu","word/vocabulary":"tango","piano":"piano","pizza":"piza","illness/sickness":"byooki","red":"akai","blue":"aoi","black":"kuroi","lonely":"sabishii","white":"shiroi","young":"wakai","mean-spirited":"ijiwaruna"}

# genki_10 = {"fall":"aki","doctor":"isha","station":"eki","rich person":"okanemochi","face":"kao","season":"kisetsu","milk":"gyuunyuu","cake":"keeki","this year":"kotoshi","soccer":"sakkaa","shirt":"shatsu","bullet train":"shinkansen","life/living":"seekatsu","world":"sekai","subway":"chikatetsu","gloves":"tebukuro","barber":"tokoya","spring":"haru","pants":"pantsu","beauty parlor":"biyooin","flight":"bin","ship/boat":"fune","baseball":"yakyuu","celebrity":"yuumeejin","reservation":"yoyaku","next semester":"raigakki","apple":"ringo","warm":"atatakai","slow/late":"osoi","cool (weather)":"suzushii","cold (things/people)":"tsumetai","sleepy":"nemui","easy/simple":"kantanna","to take":"kakaru","to stay (at a place (ni))":"tomaru","to become":"naru","to pay":"harau","to decide":"kimeru","to travel":"ryokoosuru","to practice":"renshuusuru","on foot":"aruite","best":"ichiban","or":"ka","for __ months":"kagetsu","after":"go","these days":"konogoro","for __ weeks":"shuukan","how":"dooyatte","how much/how long":"donogurai","early/quickly":"hayaku"}

# k1_genki = {"what":"nani","college/university":"daigaku"}

# k2_genki = {"library":"toshokan","post office":"yuubinkyoku","bank":"ginkoo","who":"dare"}

# k3_genki = {"movie":"eega","music":"ongaku","magazine":"zasshi","breakfast":"asagohan","alcohol":"osake","green tea":"ocha","dinner":"bangohan","lunch":"hirugohan","water":"mizu","home":"ie","school":"gakkoo","morning":"asa","tomorrow":"ashita","today":"kyoo","tonight":"konban","weekend":"shuumatsu","saturday":"doyoobi","sunday":"nichiyoobi","every day":"mainichi","every night":"maiban","to go":"iku","to return":"kaeru","to hear":"kiku","to drink":"nomu","to speak":"hanasu","to read":"yomu","to get up":"okiru","to eat":"taberu","to sleep":"neru","to see":"miru","to come":"kuru","to study":"benkyoosuru","early":"hayai","not at all":"zenzen","sometimes":"tokidoki"}

# k4_genki = {"shopping":"kaimono","dog":"inu","souvenir":"omiyage","child":"kodomo","meal":"gohan","picture/photo":"shashin","desk":"tsukue","letter":"tegami","cat":"neko","person":"hito","temple":"otera","park":"kooen","bus stop":"basutei","hospital":"byooin","bookstore":"honya","town":"machi","yesterday":"kinoo","hours":"jikan","last week":"senshuu","when":"toki","monday":"getsuyoobi","tuesday":"kayoobi","wednesday":"suiyoobi","thursday":"mokuyoobi","friday":"kinyoobi","to meet":"au","to buy":"kau","to write":"kaku","to take":"toru","to wait":"matsu","alone":"hitoride","right":"migi","left":"hidari","front":"mae","back":"ushiro","inside":"naka","on":"ue","under":"shita","near/nearby":"chikaku","next":"tonari","between":"aida"}

# k5_genki = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","weather":"tenki","drink":"nomimono","postcard":"hagaki","airplane":"hikooki","room":"heya","I (used by men)":"boku","holiday":"yasumi","travel":"ryokoo","new":"atarashii","hot":"atsui","busy":"isogashii","large":"ooki","interesting/funny":"omoshiroi","frightening":"kowai","cold":"samui","fun":"tanoshii","small":"chiisai","old (thing)":"furui","difficult":"muzukashii","cheap":"yasui","disgusted with":"kiraina","healthy/energetic":"genkina","quiet":"shizukana","fond of/to like":"sukina","to hate":"daikiraina","to love":"daisukina","not busy":"himana","to swim":"oyogu","to ask":"kiku","to ride/board":"noru","to go out":"dekakeru","together":"isshoni","it's okay":"daijoobu","counter (flat objects)":"mai"}

# k6_genki = {"money":"okane","bath":"ofuro","kanji":"kanji","textbook":"kyookasho","this week":"konshuu","municipal hospital":"shiminbyooin","next":"tsugi","electricity":"denki","train":"densha","baggage":"nimotsu","window":"mado","night":"yoru","next week":"raishuu","next year":"rainen","tough situation":"taihenna","to play":"asobu","to hurry":"isogu","to take a bath":"ofuronihairu","to return (a thing)":"kaesu","to turn off/erase":"kesu","to die":"shinu","to sit down":"suwaru","to stand up":"tatsu","to smoke":"tabako o suu","to use":"tsukau","to help":"tetsudau","to enter":"hairu","to carry/hold":"motsu","to be absent; to rest":"yasumu","to open":"akeru","to teach":"oshieru","to get off":"oriru","to borrow":"kariru","to close":"shimeru","to take a shower":"shawaa o abiru","to make a phone call":"denwa o kakeru","to forget/leave behind":"wasureru","to bring a person":"tsuretekuru","to bring a thing":"mottekuru","later on":"atode","(do something) late":"osoku","that would be fine":"kekkoodesu","really?":"hontoodesuka","north":"kita","south":"minami","east":"higashi","west":"nishi"}



# n5_jlpt_1 = {"to meet":"au","blue":"ao","red":"aka","bright":"akarui","autumn":"aki","to open":"akeru","to give":"ageru","morning":"asa","breakfast":"asagohan","day after tomorrow":"asatte","foot/leg":"ashi","tomorrow":"ashita","over there":"asoko","to play":"asobu","warm, mild":"atatakai","head":"atama","new":"atarashii","that side over there (form.)":"achira","hot/kind/warm":"atsui","that side over there (inf)":"acchi","afterwards":"ato","you":"anata","(hum) older brother":"ani","(hum) older sister":"ane","that over there":"ano","um...":"ano","apartment":"apaato","to bathe/shower":"abiru","dangerous":"abunai","generous, sweet":"amai","not very much":"amari","rain":"ame","candy":"ame","to wash":"arau","to be (object), to have":"aru","to walk":"aruku","that one over there":"are","good":"ii","no":"iie","to say":"iu","house":"ie","how (form)":"ikaga","to go":"iku","how many?/how old?":"ikutsu","how much?":"ikura","pond":"ike","doctor":"isha","chair":"isu","busy":"isogashii","painful":"itai","when":"itsu","together":"isshoni","always":"itsumo","dog":"inu","now":"ima","meaning":"imi","younger sister":"imooto","unpleasant":"iyana","entrance":"iriguchi","to be (person)":"iru","to put in":"ireru","color":"iro","various, all kinds of":"iroiro","on top of":"ue","behind":"ushiro","thin (object)":"usui","song":"uta","to sing":"utau","to be born":"umareru","sea":"umi","to sell":"uru","noisy, annoying":"urusai","jacket":"uwagi","picture, painting/drawing":"e","movie":"eega","cinema":"eegakan","english language":"eego","yes":"ee","station":"eki","elevator":"erebeetaa","pencil":"enpitsu","delicious":"oishii","many":"ooi","big":"ookii","a great number of people":"oozei","mother":"okaasan","sweets, candy":"okashi","money":"okane","to get up":"okiru","to put":"oku","wife":"okusan","alcohol":"osake","plate, dish":"osara","grandfather":"ojiisan","to teach":"oshieru","uncle":"ojisan","to push (like a button)":"osu","late/slow":"osoi","green tea":"ocha","bathroom":"otearai","father":"otoosan","younger brother":"otooto","man":"otoko","boy":"otoko no ko","day before yesterday":"ototoi","year before last":"ototoshi","adult":"otona","stomach":"onaka","same":"onaji","older brother":"oniisan","older sister":"oneesan","grandmother":"obaasan","aunt":"obasan","bath":"ofuro","boxed lunch":"obentoo","to remember":"oboeru","friendly term for policeman":"omawarisan","heavy":"omoi","interesting":"omoshiroi","to swim":"oyogu","to get off, descend":"oriru","to finish":"owaru","music":"ongaku","woman":"onna","girl":"onna no ko","foreign country":"gaikoku","foreigner":"gaikokujin","company":"kaisha","stairs":"kaidan","shopping":"kaimono","to buy":"kau","to return a thing":"kaesu","to go back":"kaeru","to take (time or money)":"kakaru","key":"kagi","to write":"kaku","student":"gakusee","to call by phone":"kakeru","umbrella":"kasa","to lend":"kasu","wind, a cold":"kaze","family":"kazoku","person (form.)":"kata","school":"gakkoo","cup":"kappu","household":"katei","a corner":"kado","bag, basket":"kaban","vase":"kabin","paper":"kami","camera":"kamera"}

# n5_jlpt_2 = {"tuesday":"kayoobi","spicy":"karai","body":"karada","to borrow":"kariru","light":"karui","curry":"karee","calendar":"karendaa","river":"kawa","cute":"kawaii","kanji":"kanji","tree":"ki","yellow":"kiiro","to disappear":"kieru","to hear, ask":"kiku","north":"kita","guitar":"gitaa","dirty":"kitanai","cafe":"kissaten","postal stamp":"kitte","ticket":"kippu","yesterday":"kinoo","nine":"kyuu","beef":"gyuuniku","milk":"gyuunyuu","today":"kyoo","classroom":"kyooshitsu","siblings (hum.)":"kyoodai","last year":"kyonen","to dislike":"kiraina","to cut, to wear from the shoulders down":"kiru","pretty, clean":"kireina","kilogram":"kiroguramu","kilometer":"kiromeetoru","bank":"ginkoo","friday":"kinyoobi","medicine":"kusuri","please":"kudasai","fruit":"kudamono","mouth, opening":"kuchi","shoes":"kutsu","socks":"kutsushita","country":"kuni","cloudy weather":"kumori","to become cloudy":"kumoru","gloomy":"kurai","class":"kurasu","gram":"guramu","car, vehicle":"kuruma","black":"kuro","policeman":"keekan","this morning":"kesa","to erase, turn off":"kesu","splendid, enough":"kekkoo","marriage":"kekkon","monday":"getsuyoobi","entry hall":"genkan","healthy":"genkina","park":"kooen","intersection":"koosaten","black tea":"koocha","police station":"kooban","voice":"koe","coat":"kooto","coffee":"koohii","here":"koko","p.m.":"gogo","a.m.":"gozen","to answer":"kotaeru","this side (form.)":"kochira","this side (inf.)":"kocchi","a glass":"koppu","this year":"kotoshi","word, language":"kotoba","child":"kodomo","this":"kono","meal, cooked rice":"gohan","to copy":"kopiisuru","to be worried":"komaru","this one":"kore","this month":"kongetsu","this week":"konshuu","such":"konna","this evening":"konban","well...":"saa","wallet":"saifu","fish":"sakana","the future, previous":"saki","to bloom":"saku","composition, writing":"sakubun","to stretch out hands, raise an umbrella":"sasu","magazine":"zasshi","sugar":"satoo","cold":"samui","year after next":"sarainen","to stroll":"sanposuru","salt":"shio","however":"shikashi","time":"jikan","job":"shigoto","dictionary":"jisho","quiet":"shizukana","below":"shita","question":"shitsumon","bicyle":"jitensha","automobile":"jidoosha","to die":"shinu","oneself":"jibun","to close, tie":"shimeru","lesson, class work":"jugyoo","skillful":"joozuna","strong/durable":"joobuna","soy souce":"shooyu","dining hall":"shokudoo","to know":"shiru","white":"shiro","skirt":"sukaato"}

# n5_jlpt_3 = {"a few (adj)":"sukunai","a few (n)":"sukoshi","refreshing":"suzushii","heater":"sutoobu","spoon":"supoon","pants":"zubon","to live":"sumu","slippers":"surippa","to sit":"suwaru","height/stature":"se","pupil":"seeto","sweater":"seetaa","soap":"sekken","business suit":"sebiro","narrow":"semai","washing/laundry":"sentaku","all":"zenbu","to clean/sweep":"soojisuru","outside":"soto","next to (any type)":"soba","sky":"sora","in that situation":"soredewa","embassy":"taishikan","important":"taisetsuna","kitchen":"daidokoro","taxi":"takushii","to put out":"dasu","length/height":"tate","building":"tatemono","to ask":"tanomu","probably":"tabun","egg":"tamago","somebody":"dareka","gradually":"dandan","birthday":"tanjoobi","near (adj.)":"chikai","near (adv.)":"chikaku","to differ":"chigau","underground train":"chikatetsu","map":"chizu","brown":"chairo","rice bowl":"chawan","exactly":"choodo","to get tired":"tsukareru","to use":"tsukau","next":"tsugi","to arrive at":"tsuku","to make":"tsukuru","powerful":"tsuyoi","to work for someone":"tsutomeru","cold to the touch":"tsumetai","table":"teeburu","to be able to":"dekiru","exit":"deguchi","with that...":"dewa","department store":"depaato","to leave/appear":"deru","door (japanese)":"to","door (western)":"doa","toilet":"toire","animal":"doobutsu","far":"tooi","place":"tokoro","year":"toshi","who":"donata","to fly/hop":"tobu","to come to a halt":"tomaru","bird":"tori","chicken meat":"toriniku","knife":"naifu","animal noise":"naku","to lose something":"nakusu","why":"naze","summer":"natsu","etc.":"nado","to learn":"narau","to line up":"narabu","to become":"naru","garden":"niwa","to take off clothes":"nugu","lukewarm":"nurui","notebook":"nooto","to climb":"noboru","tooth":"ha","party":"paatii","ashtray":"haizara","postcard":"hagaki","to enter":"hairu","to wear clothes below waste":"haku","box":"hako","bridge":"hashi","chopsticks":"hashi","to begin":"hajimeru","beginning":"hajime","for the first time":"hajimete","to run":"hashiru","to work":"hataraku","flower":"hana","nose":"hana","talk/story":"hanashi","to speak":"hanasu","early/fast":"hayai","spring":"haru","to stick":"haru","clear weather":"hare","to be sunny":"hareru","half":"han","evening":"ban","bread":"pan","handkerchief":"hankachi","number":"bangoo","east":"higashi","to pull":"hiku","to play a stringed instrument":"hiku","short (height)":"hikui","airplane":"hikooki","left":"hidari","person":"hito","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":""}

# learning = {}

# combined_words = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5, **genki_6}
# combined_kanji = grade_1_k
# more_kanji = {**k4_genki, **k5_genki, **k6_genki}

# word_length = len(combined_words)
# kanji_length = len(combined_kanji) + len(more_kanji)
# #genki_combined = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5}
# #genki_combined = {**k3_genki}
# #genki_combined = {**k4_genki, **k1_genki, **k2_genki, **k3_genki, **k5_genki, **k6_genki}
# #genki_combined = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5, **genki_6, **genki_7, **genki_8}
# #genki_combined = {**k5_genki}
# #genki_combined = {**genki_7}
# #genki_combined = {**n5_jlpt_1}
# #genki_combined = {**n5_jlpt_2}
# #genki_combined = {**n5_jlpt_3}
# #genki_combined = {**n5_jlpt_1, **n5_jlpt_2, **n5_jlpt_3}
# #genki_combined = {**genki_8}
# #genki_combined = {**genki_9}
# genki_combined = {**genki_10}

dict = True


keys = list(genki_combined.keys())

#list = grade_1_k # Keep this line below line above or there will be an error

random.shuffle(keys)


missed={}

print("Welcome to jisho.py! Keep studying hard! Stay focused! Remember the happy rock/seeds of happiness!")
#print("You have learned " + str(word_length) + " words. Great job!")
#print("You have learned " + str(kanji_length) + " kanji. Great job!")

#if (dict):
for key in keys:
    answer = input(str(key) + ": ")
    print(genki_combined[key])
    
    if (answer != genki_combined[key]):
        missed[key + "    " + genki_combined[key]] = answer

print("\nMissed words:")
print("English       Correct answer       Your answer\n")
for i in missed:
    print(i,"    ",missed[i])

# else:
#     for word in list:
#         answer = input(word+ ": ")
#         if (answer == "n"):
#             missed.append(word)

#     print("\nMissed words:\n")
#     for i in missed:
#         print(i)
