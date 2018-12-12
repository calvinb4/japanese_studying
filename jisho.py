import random

grade_1_k = ["one","two","three","four","five","six","seven","eight","nine","ten","one hundred","one thousand","ten thousand","top/above","bottom/below","left","right","inside","large","small","month/moon","day/sun","year","early","tree","woods","mountain","river","soil","sky","rice paddy","heaven/sky","life/bear/raw","flower","grass","insect","dog","person","name","female","male","child","eye","ear","mouth","hand","foot","see","sound","power","yen","evening","previous","air","enter","exit"]

genki_1 = {"um...":"ano","now":"ima","english language":"eego","yes (inf.)":"ee","student":"gakusee","high school":"kookoo","p.m.":"gogo","a.m.":"gozen","years old":"sai","Mr./Ms.":"san","o-clock":"ji","people group":"jin","major":"senkoo","teacher":"sensee","that's right":"soo desu","I see/Is that so?":"soo desu ka","college":"daigaku","telephone":"denwa","friend":"tomodachi","name":"namae","what":"nani","Japan":"nihon","_ year student":"nensee","yes (form.)":"hai","half":"han","number":"bangoo","international student":"ryuugakusee","I":"watashi","usa":"amerika","britain":"igirisu","australia":"oosutoraria","korea":"kankoku","sweeden":"suweeden","china":"chuugoku","science":"kagaku","asian studies":"ajia kenkyuu","economics":"keezai","international relations":"kokusaikankee","computer":"konpyuutaa","anthropology":"jinruigaku","politics":"seeji","business":"bijinesu","literature":"bungaku","history":"rekishi","job":"shigoto","doctor":"isha","office worker":"kaishain","high school student":"kookoosee","housewife":"shufu","grad student":"daigakuinsee","college student":"daigakusee","lawyer":"bengoshi","mother":"okaasan","father":"otoosan","older brother":"oniisan","older sister":"oneesan","younger brother":"otooto","younger sister":"imooto","good morning (inf.)":"ohayoo","good morning (form.)":"ohayoo gozaimasu","good afternoon":"konnichiwa","good evening":"konbanwa","goodbye (ritualistic)":"sayoonara","goodbye (inf.)":"jaa mata","goodbye (form.)":"shitsureeshimasu","good night":"oyasuminasai","thank you (inf.)":"arigatoo","thank you (form.)":"arigatoo gozaimasu","excuse me/I'm sorry":"sumimasen","no":"iie","i'll go and come back":"ittekimasu","please go and come back":"itterasshai","I'm home":"tadaima","welcome home":"okaerinasai","thank you for the meal (before eating)":"itadakimasu","thank you for the meal (after eating)":"gochisoosamadeshita","how do you do?":"hajimemashite","nice to meet you":"yoroshiku onegaishimasu"}

genki_2 = {"this one":"kore","that one":"sore","that one over there":"are","which one":"dore","this":"kono","that":"sono","that over there":"ano","which":"dono","here":"koko","there":"soko","over there":"asoko","where":"doko","who":"dare","delicious":"oishii","fish":"sakana","pork cutlet":"tonkatsu","meat":"niku","menu":"menyuu","vegetable":"yasai","pencil":"enpitsu","umbrella":"kasa","bag":"kaban","shoes":"kutsu","wallet":"saifu","jeans":"jiinzu","dictionary":"jisho","bicycle":"jitensha","newspaper":"shinbun","t shirt":"tiishatsu","watch/clock":"tokee","notebook":"nooto","pen":"pen","hat":"booshi","book":"hon","cafe":"kissaten","bank":"ginkoo","toilet":"toire","library":"toshokan","post office":"yuubinkyoku","usa":"amerika","britain":"igirisu","korea":"kankoku","china":"chuugoku","economics":"keezai","computer":"konpyuutaa","business":"bijinesu","history":"rekishi","mother":"okaasan","father":"otoosan","how much":"ikura","yen":"en","expensive":"takai","welcome to our store":"irasshaimase","please":"onegaishimasu","please give me":"kudasai","then":"jaa","here it is/please":"doozo","thank you":"doomo"}

genki_3 = {"music":"ongaku","movie":"eega","magazine":"zasshi","sports":"supootsu","date (romantic)":"deeto","tennis":"tenisu","TV":"terebi","ice cream":"aisukuriimu","breakfast":"asagohan","alcohol":"osake","green tea":"ocha","coffee":"koohii","dinner":"bangohan","hamburger":"hanbaagaa","lunch":"hirugohan","water":"mizu","home":"ie","school":"gakkoo","morning":"asa","tomorrow":"ashita","when":"itsu","today":"kyoo","at about":"goro","tonight":"konban","weekend":"shuumatsu","saturday":"doyoobi","sunday":"nichiyoobi","every day":"mainichi","every night":"maiban","to go":"iku","to return":"kaeru","to hear":"kiku","to drink":"nomu","to speak":"hanasu","to read":"yomu","to get up":"okiru","to eat":"taberu","to sleep":"neru","to see":"miru","to come":"kuru","to do":"suru","to study":"benkyoosuru","good":"ii","early":"hayai","not much":"amari","not at all":"zenzen","usually":"taitei","a little":"chotto","sometimes":"tokidoki","often/much":"yoku","that's right/let me see":"soo desu ne","but":"demo","how about":"doodesuka"}

genki_4 = {"spring":"horu","summer":"natsu","fall":"aki","winter":"fuyu","shopping":"kaimono","dog":"inu","souvenir":"omiyage","child":"kodomo","meal":"gohan","picture/photo":"shashin","desk":"tsukue","letter":"tegami","cat":"neko","person":"hito","temple":"otera","park":"kooen","bus stop":"basutei","hospital":"byooin","bookstore":"honya","town":"machi","yesterday":"kinoo","hours":"jikan","last week":"senshuu","when":"toki","monday":"getsuyoobi","tuesday":"kayoobi","wednesday":"suiyoobi","thursday":"mokuyoobi","friday":"kinyoobi","to meet":"au","to buy":"kau","to write":"kaku","to take":"toru","to wait":"matsu","alone":"hitoride","right":"migi","left":"hidari","front":"mae","back":"ushiro","inside":"naka","on":"ue","under":"shita","near/nearby":"chikaku","next":"tonari","between":"aida","part time job":"arubaito","class":"kurasu","you":"anata","chair":"isu","bread":"pan","e-mail":"meeru","supermarket":"suupaa","departement store":"depaato","hotel":"hoteru","restaurant":"resutoran","there is":"aru","to understand":"wakaru","a person is":"iru","about (interval of time)":"gurai","I'm sorry (inf.)":"gomennasai","so/therefore":"dakara","many/a lot":"takusan","together with a person":"to","why":"dooshite","and then":"soshite"}

genki_5 = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","surfing":"safin","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","test":"tesuto","weather":"tenki","drink":"nomimono","postcard":"hagaki","bus":"basu","airplane":"hikooki","room":"heya","I (used by men)":"boku","holiday":"yasumi","travel":"ryokoo","new":"atarashii","hot":"atsui","busy":"isogashii","large":"ooki","interesting/funny":"omoshiroi","good-looking":"kakkoii","frightening":"kowai","cold":"samui","fun":"tanoshii","small":"chiisai","boring":"tsumaranai","old (thing)":"furui","difficult":"muzukashi","easy (problem)/kind (person)":"yasashii","cheap":"yasui","disgusted with":"kiraina","clean/beautiful":"kireina","healthy/energetic":"genkina","quiet":"shizukana","fond of/to like":"sukina","to hate":"daikiraina","to love":"daisukina","lively":"nigiyakana","not busy":"himana","to swim":"oyogu","to ask":"kiku","to ride/board":"noru","to do/preform":"yaru","to go out":"dekakeru","together":"isshoni","extremeely":"sugoku","and then":"sorekara","it's okay":"daijoobu","very":"totemo","what kind of...":"donna","counter (flat objects)":"mai","to (a place)/till (a time)":"made","mountain":"yama","river":"kawa","female":"onna","male":"otoko"}

genki_6 = {"money":"okane","bath":"ofuro","kanji":"kanji","textbook":"kyookasho","this week":"konshuu","cd":"shiidii","municipal hospital":"shiminbyooin","shower":"shawaa","next":"tsugi","electricity":"denki","train":"densha","baggage":"nimotsu","personal computer":"pasokon","page":"peeji","window":"mado","night":"yoru","next week":"raishuu","next year":"rainen","tough situation":"taihenna","to play":"asobu","to hurry":"isogu","to take a bath":"ofuronihairu","to return (a thing)":"kaesu","to turn off/erase":"kesu","to die":"shinu","to sit down":"suwaru","to stand up":"tatsu","to smoke":"tabako o suu","to use":"tsukau","to help":"tetsudau","to enter":"hairu","to carry/hold":"motsu","to be absent; to rest":"yasumu","to open":"akeru","to teach":"oshieru","to get off":"oriru","to borrow":"kariru","to close":"shimeru","to take a shower":"shawaa o abiru","to turn on":"tsukeru","to make a phone call":"denwa o kakeru","to forget/leave behind":"wasureru","to bring a person":"tsuretekuru","to bring a thing":"mottekuru","later on":"atode","(do something) late":"osoku","that would be fine":"kekkoodesu","because":"kara","right away":"sugu","really?":"hontoodesuka","slowly/leisurely":"yukkuri","north":"kita","south":"minami","east":"higashi","west":"nishi","entrance":"kuchi","hometown":"shusshin","deru":"to exit","country":"kuni","foreign":"gaikoku"}

k1_genki = {"what":"nani","college/university":"daigaku"}

k2_genki = {"library":"toshokan","post office":"yuubinkyoku","bank":"ginkoo","who":"dare"}

k3_genki = {"movie":"eega","music":"ongaku","magazine":"zasshi","breakfast":"asagohan","alcohol":"osake","green tea":"ocha","dinner":"bangohan","lunch":"hirugohan","water":"mizu","home":"ie","school":"gakkoo","morning":"asa","tomorrow":"ashita","today":"kyoo","tonight":"konban","weekend":"shuumatsu","saturday":"doyoobi","sunday":"nichiyoobi","every day":"mainichi","every night":"maiban","to go":"iku","to return":"kaeru","to hear":"kiku","to drink":"nomu","to speak":"hanasu","to read":"yomu","to get up":"okiru","to eat":"taberu","to sleep":"neru","to see":"miru","to come":"kuru","to study":"benkyoosuru","early":"hayai","not at all":"zenzen","sometimes":"tokidoki"}

k4_genki = {"shopping":"kaimono","dog":"inu","souvenir":"omiyage","child":"kodomo","meal":"gohan","picture/photo":"shashin","desk":"tsukue","letter":"tegami","cat":"neko","person":"hito","temple":"otera","park":"kooen","bus stop":"basutei","hospital":"byooin","bookstore":"honya","town":"machi","yesterday":"kinoo","hours":"jikan","last week":"senshuu","when":"toki","monday":"getsuyoobi","tuesday":"kayoobi","wednesday":"suiyoobi","thursday":"mokuyoobi","friday":"kinyoobi","to meet":"au","to buy":"kau","to write":"kaku","to take":"toru","to wait":"matsu","alone":"hitoride","right":"migi","left":"hidari","front":"mae","back":"ushiro","inside":"naka","on":"ue","under":"shita","near/nearby":"chikaku","next":"tonari","between":"aida"}

k5_genki = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","weather":"tenki","drink":"nomimono","postcard":"hagaki","airplane":"hikooki","room":"heya","I (used by men)":"boku","holiday":"yasumi","travel":"ryokoo","new":"atarashii","hot":"atsui","busy":"isogashii","large":"ooki","interesting/funny":"omoshiroi","frightening":"kowai","cold":"samui","fun":"tanoshii","small":"chiisai","old (thing)":"furui","difficult":"muzukashii","cheap":"yasui","disgusted with":"kiraina","healthy/energetic":"genkina","quiet":"shizukana","fond of/to like":"sukina","to hate":"daikiraina","to love":"daisukina","not busy":"himana","to swim":"oyogu","to ask":"kiku","to ride/board":"noru","to go out":"dekakeru","together":"isshoni","it's okay":"daijoobu","counter (flat objects)":"mai"}

k6_genki = {"money":"okane","bath":"ofuro","kanji":"kanji","textbook":"kyookasho","this week":"konshuu","municipal hospital":"shiminbyooin","next":"tsugi","electricity":"denki","train":"densha","baggage":"nimotsu","window":"mado","night":"yoru","next week":"raishuu","next year":"rainen","tough situation":"taihenna","to play":"asobu","to hurry":"isogu","to take a bath":"ofuronihairu","to return (a thing)":"kaesu","to turn off/erase":"kesu","to die":"shinu","to sit down":"suwaru","to stand up":"tatsu","to smoke":"tabako o suu","to use":"tsukau","to help":"tetsudau","to enter":"hairu","to carry/hold":"motsu","to be absent; to rest":"yasumu","to open":"akeru","to teach":"oshieru","to get off":"oriru","to borrow":"kariru","to close":"shimeru","to take a shower":"shawaa o abiru","to make a phone call":"denwa o kakeru","to forget/leave behind":"wasureru","to bring a person":"tsuretekuru","to bring a thing":"mottekuru","later on":"atode","(do something) late":"osoku","that would be fine":"kekkoodesu","really?":"hontoodesuka","north":"kita","south":"minami","east":"higashi","west":"nishi"}



n5_jlpt_1 = {"to meet":"au","blue":"ao","red":"aka","bright":"akarui","autumn":"aki","to open":"akeru","to give":"ageru","morning":"asa","breakfast":"asagohan","day after tomorrow":"asatte","foot/leg":"ashi","tomorrow":"ashita","over there":"asoko","to play":"asobu","warm, mild":"atatakai","head":"atama","new":"atarashii","that side over there (form.)":"achira","hot/kind/warm":"atsui","that side over there (inf)":"acchi","afterwards":"ato","you":"anata","(hum) older brother":"ani","(hum) older sister":"ane","that over there":"ano","um...":"ano","apartment":"apaato","to bathe/shower":"abiru","dangerous":"abunai","generous, sweet":"amai","not very much":"amari","rain":"ame","candy":"ame","to wash":"arau","to be (object), to have":"aru","to walk":"aruku","that one over there":"are","good":"ii","no":"iie","to say":"iu","house":"ie","how (form)":"ikaga","to go":"iku","how many?/how old?":"ikutsu","how much?":"ikura","pond":"ike","doctor":"isha","chair":"isu","busy":"isogashii","painful":"itai","when":"itsu","together":"isshoni","always":"itsumo","dog":"inu","now":"ima","meaning":"imi","younger sister":"imooto","unpleasant":"iyana","entrance":"iriguchi","to be (person)":"iru","to put in":"ireru","color":"iro","various, all kinds of":"iroiro","on top of":"ue","behind":"ushiro","thin (object)":"usui","song":"uta","to sing":"utau","to be born":"umareru","sea":"umi","to sell":"uru","noisy, annoying":"urusai","jacket":"uwagi","picture, painting/drawing":"e","movie":"eega","cinema":"eegakan","english language":"eego","yes":"ee","station":"eki","elevator":"erebeetaa","pencil":"enpitsu","delicious":"oishii","many":"ooi","big":"ookii","a great number of people":"oozei","mother":"okaasan","sweets, candy":"okashi","money":"okane","to get up":"okiru","to put":"oku","wife":"okusan","alcohol":"osake","plate, dish":"osara","grandfather":"ojiisan","to teach":"oshieru","uncle":"ojisan","to push (like a button)":"osu","late/slow":"osoi","green tea":"ocha","bathroom":"otearai","father":"otoosan","younger brother":"otooto","man":"otoko","boy":"otoko no ko","day before yesterday":"ototoi","year before last":"ototoshi","adult":"otona","stomach":"onaka","same":"onaji","older brother":"oniisan","older sister":"oneesan","grandmother":"obaasan","aunt":"obasan","bath":"ofuro","boxed lunch":"obentoo","to remember":"oboeru","friendly term for policeman":"omawarisan","heavy":"omoi","interesting":"omoshiroi","to swim":"oyogu","to get off, descend":"oriru","to finish":"owaru","music":"ongaku","woman":"onna","girl":"onna no ko","foreign country":"gaikoku","foreigner":"gaikokujin","company":"kaisha","stairs":"kaidan","shopping":"kaimono","to buy":"kau","to return a thing":"kaesu","to go back":"kaeru","to take (time or money)":"kakaru","key":"kagi","to write":"kaku","student":"gakusee","to call by phone":"kakeru","umbrella":"kasa","to lend":"kasu","wind, a cold":"kaze","family":"kazoku","person (form.)":"kata","school":"gakkoo","cup":"kappu","household":"katei","a corner":"kado","bag, basket":"kaban","vase":"kabin","paper":"kami","camera":"kamera"}

n5_jlpt_2 = {"tuesday":"kayoobi","spicy":"karai","body":"karada","to borrow":"kariru","light":"karui","curry":"karee","calendar":"karendaa","river":"kawa","cute":"kawaii","kanji":"kanji","tree":"ki","yellow":"kiiro","to disappear":"kieru","to hear, ask":"kiku","north":"kita","guitar":"gitaa","dirty":"kitanai","cafe":"kissaten","postal stamp":"kitte","ticket":"kippu","yesterday":"kinoo","nine":"kyuu","beef":"gyuuniku","milk":"gyuunyuu","today":"kyoo","classroom":"kyooshitsu","siblings (hum.)":"kyoodai","last year":"kyonen","to dislike":"kiraina","to cut, to wear from the shoulders down":"kiru","pretty, clean":"kireina","kilogram":"kiroguramu","kilometer":"kiromeetoru","bank":"ginkoo","friday":"kinyoobi","medicine":"kusuri","please":"kudasai","fruit":"kudamono","mouth, opening":"kuchi","shoes":"kutsu","socks":"kutsushita","country":"kuni","cloudy weather":"kumori","to become cloudy":"kumoru","gloomy":"kurai","class":"kurasu","gram":"guramu","car, vehicle":"kuruma","black":"kuro","policeman":"keekan","this morning":"kesa","to erase, turn off":"kesu","splendid, enough":"kekkoo","marriage":"kekkon","monday":"getsuyoobi","entry hall":"genkan","healthy":"genkina","park":"kooen","intersection":"koosaten","black tea":"koocha","police station":"kooban","voice":"koe","coat":"kooto","coffee":"koohii","here":"koko","p.m.":"gogo","a.m.":"gozen","to answer":"kotaeru","this side (form.)":"kochira","this side (inf.)":"kocchi","a glass":"koppu","this year":"kotoshi","word, language":"kotoba","child":"kodomo","this":"kono","meal, cooked rice":"gohan","":"","":"","":"","":"","":"","":"","":"","":"","":"",}

learning = {}

combined_words = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5, **genki_6}
combined_kanji = grade_1_k
more_kanji = {**k4_genki, **k5_genki, **k6_genki}

word_length = len(combined_words)
kanji_length = len(combined_kanji) + len(more_kanji)
#genki_combined = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5}
#genki_combined = {**k3_genki}
#genki_combined = {**k4_genki, **k1_genki, **k2_genki, **k3_genki, **k5_genki, **k6_genki}
#genki_combined = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5, **genki_6}
#genki_combined = {**k5_genki}
#genki_combined = {**genki_6}
#genki_combined = {**n5_jlpt_1}
genki_combined = {**n5_jlpt_2}

dict = True


keys = list(genki_combined.keys())

list = grade_1_k # Keep this line below line above or there will be an error

random.shuffle(keys)


missed=[]

print("Welcome to jisho.py! Keep studying hard! Stay focused! Remember the happy rock/seeds of happiness!")
print("You have learned " + str(word_length) + " words. Great job!")
print("You have learned " + str(kanji_length) + " kanji. Great job!")

if (dict):
    for key in keys:
        answer = input(str(key) + ": ")
        print(genki_combined[key])
    
        if (answer != genki_combined[key]):
            missed.append(key)

    print("\nMissed words:\n")
    for i in missed:
        print(i,genki_combined[i])

else:
    for word in list:
        answer = input(word+ ": ")
        if (answer == "n"):
            missed.append(word)

    print("\nMissed words:\n")
    for i in missed:
        print(i)
