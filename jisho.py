import random

grade_1_k = ["one","two","three","four","five","six","seven","eight","nine","ten","one hundred","one thousand","ten thousand","top/above","bottom/below","left","right","inside","large","small","month/moon","day/sun","year","early","tree","woods","mountain","river","soil","sky","rice paddy","heaven/sky","life/bear/raw","flower","grass","insect","dog","person","name","female","male","child","eye","ear","mouth","hand","foot","see","sound","power","yen","evening","previous","air","enter","exit"]

genki_1 = {"um...":"ano","now":"ima","english language":"eego","yes (inf.)":"ee","student":"gakusee","high school":"kookoo","p.m.":"gogo","a.m.":"gozen","years old":"sai","Mr./Ms.":"san","o-clock":"ji","people group":"jin","major":"senkoo","teacher":"sensee","that's right":"soo desu","I see/Is that so?":"soo desu ka","college":"daigaku","telephone":"denwa","friend":"tomodachi","name":"namae","what":"nani","Japan":"nihon","_ year student":"nensee","yes (form.)":"hai","half":"han","number":"bangoo","international student":"ryuugakusee","I":"watashi","U.S.A":"amerika","Britain":"igirisu","Australia":"oosutoraria","Korea":"kankoku","Sweeden":"suweeden","China":"chuugoku","science":"kagaku","Asian studies":"ajia kenkyuu","economics":"keezai","international relations":"kokusaikankee","computer":"konpyuutaa","anthropology":"jinruigaku","politics":"seeji","business":"bijinesu","literature":"bungaku","history":"rekishi","job":"shigoto","doctor":"isha","office worker":"kaishain","high school student":"kookoosee","housewife":"shufu","grad student":"daigakuinsee","college student":"daigakusee","lawyer":"bengoshi","mother":"okaasan","father":"otoosan","older brother":"oniisan","older sister":"oneesan","younger brother":"otooto","younger sister":"imooto","good morning (inf.)":"ohayoo","good morning (form.)":"ohayoo gozaimasu","good afternoon":"konnichiwa","good evening":"konbanwa","goodbye (ritualistic)":"sayoonara","goodbye (inf.)":"jaa mata","goodbye (form.)":"shitsureeshimasu","good night":"oyasuminasai","thank you (inf.)":"arigatoo","thank you (form.)":"arigatoo gozaimasu","excuse me/I'm sorry":"sumimasen","no":"iie","i'll go and come back":"ittekimasu","please go and come back":"itterasshai","I'm home":"tadaima","welcome home":"okaerinasai","thank you for the meal (before eating)":"itadakimasu","thank you for the meal (after eating)":"gochisoosamadeshita","how do you do?":"hajimemashite","nice to meet you":"yoroshiku onegaishimasu"}

genki_2 = {"this one":"kore","that one":"sore","that one over there":"are","which one":"dore","this":"kono","that":"sono","that over there":"ano","which":"dono","here":"koko","there":"soko","over there":"asoko","where":"doko","who":"dare","delicious":"oishii","fish":"sakana","pork cutlet":"tonkatsu","meat":"niku","menu":"menyuu","vegetable":"yasai","pencil":"enpitsu","umbrella":"kasa","bag":"kaban","shoes":"kutsu","wallet":"saifu","jeans":"jiinzu","dictionary":"jisho","bicycle":"jitensha","newspaper":"shinbun","t shirt":"tiishatsu","watch/clock":"tokee","notebook":"nooto","pen":"pen","hat":"booshi","book":"hon","cafe":"kissaten","bank":"ginkoo","toilet":"toire","library":"toshokan","post office":"yuubinkyoku","usa":"amerika","britain":"igirisu","korea":"kankoku","china":"chuugoku","economics":"keezai","computer":"konpyuutaa","business":"bijinesu","history":"rekishi","mother":"okaasan","father":"otoosan","how much":"ikura","yen":"en","expensive":"takai","welcome to our store":"irasshaimase","please":"onegaishimasu","please give me":"kudasai","then":"jaa","here it is/please":"doozo","thank you":"doomo"}

genki_3 = {"music":"ongaku","movie":"eega","magazine":"zasshi","sports":"supootsu","date (romantic)":"deeto","tennis":"tenisu","TV":"terebi","ice cream":"aisukuriimu","breakfast":"asagohan","alcohol":"osake","green tea":"ocha","coffee":"koohii","dinner":"bangohan","hamburger":"hanbaagaa","lunch":"hirugohan","water":"mizu","home":"ie","school":"gakkoo","morning":"asa","tomorrow":"ashita","when":"itsu","today":"kyoo","at about":"goro","tonight":"konban","weekend":"shuumatsu","saturday":"doyoobi","sunday":"nichiyoobi","every day":"mainichi","every night":"maiban","to go":"iku","to return":"kaeru","to hear":"kiku","to drink":"nomu","to speak":"hanasu","to read":"yomu","to get up":"okiru","to eat":"taberu","to sleep":"neru","to see":"miru","to come":"kuru","to do":"suru","to study":"benkyoosuru","good":"ii","early":"hayai","not much":"amari","not at all":"zenzen","usually":"taitei","a little":"chotto","sometimes":"tokidoki","often/much":"yoku","that's right/let me see":"soo desu ne","but":"demo","how about":"doodesuka"}

genki_4 = {"spring":"horu","summer":"natsu","fall":"aki","winter":"fuyu","shopping":"kaimono","dog":"inu","souvenir":"omiyage","child":"kodomo","meal":"gohan","picture/photo":"shashin","desk":"tsukue","letter":"tegami","cat":"neko","person":"hito","temple":"otera","park":"kooen","bus stop":"basutei","hospital":"byooin","bookstore":"honya","town":"machi","yesterday":"kinoo","hours":"jikan","last week":"senshuu","when":"toki","monday":"getsuyoobi","tuesday":"kayoobi","wednesday":"suiyoobi","thursday":"mokuyoobi","friday":"kinyoobi","to meet":"au","to buy":"kau","to write":"kaku","to take":"toru","to wait":"matsu","alone":"hitoride","right":"migi","left":"hidari","front":"mae","back":"ushiro","inside":"naka","on":"ue","under":"shita","near/nearby":"chikaku","next":"tonari","between":"aida","part time job":"arubaito","class":"kurasu","you":"anata","chair":"isu","bread":"pan","e-mail":"meeru","supermarket":"suupaa","departement store":"depaato","hotel":"hoteru","restaurant":"resutoran","there is":"aru","to understand":"wakaru","a person is":"iru","about (interval of time)":"gurai","I'm sorry (inf.)":"gomennasai","so/therefore":"dakara","many/a lot":"takusan","together with a person":"to","why":"dooshite","and then":"soshite"}

genki_5 = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","surfing":"safin","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","test":"tesuto","weather":"tenki","drink":"nomimono","postcard":"hagaki","bus":"basu","airplane":"hikooki","room":"heya","I (used by men)":"boku","holiday":"yasumi","travel":"ryokoo","new":"atarashii","hot":"atsui","busy":"isogashii","large":"ooki","interesting/funny":"omoshiroi","good-looking":"kakkoii","frightening":"kowai","cold":"samui","fun":"tanoshii","small":"chiisai","boring":"tsumaranai","old (thing)":"furui","difficult":"muzukashi","easy (problem)/kind (person)":"yasashii","cheap":"yasui","disgusted with":"kiraina","clean/beautiful":"kireina","healthy/energetic":"genkina","quiet":"shizukana","fond of/to like":"sukina","to hate":"daikiraina","to love":"daisukina","lively":"nigiyakana","not busy":"himana","to swim":"oyogu","to ask":"kiku","to ride/board":"noru","to do/preform":"yaru","to go out":"dekakeru","together":"isshoni","extremeely":"sugoku","and then":"sorekara","it's okay":"daijoobu","very":"totemo","what kind of...":"donna","counter (flat objects)":"mai","to (a place)/till (a time)":"made"}

k1_genki = {"what":"nani","college/university":"daigaku"}

k2_genki = {"library":"toshokan","post office":"yuubinkyoku","bank":"ginkoo","who":"dare"}

k3_genki = {"movie":"eega","music":"ongaku","magazine":"zasshi","breakfast":"asagohan","alcohol":"osake","green tea":"ocha","dinner":"bangohan","lunch":"hirugohan","water":"mizu","home":"ie","school":"gakkoo","morning":"asa","tomorrow":"ashita","today":"kyoo","tonight":"konban","weekend":"shuumatsu","saturday":"doyoobi","sunday":"nichiyoobi","every day":"mainichi","every night":"maiban","to go":"iku","to return":"kaeru","to hear":"kiku","to drink":"nomu","to speak":"hanasu","to read":"yomu","to get up":"okiru","to eat":"taberu","to sleep":"neru","to see":"miru","to come":"kuru","to study":"benkyoosuru","early":"hayai","not at all":"zenzen","sometimes":"tokidoki"}

k4_genki = {"shopping":"kaimono","dog":"inu","souvenir":"omiyage","child":"kodomo","meal":"gohan","picture/photo":"shashin","desk":"tsukue","letter":"tegami","cat":"neko","person":"hito","temple":"otera","park":"kooen","bus stop":"basutei","hospital":"byooin","bookstore":"honya","town":"machi","yesterday":"kinoo","hours":"jikan","last week":"senshuu","when":"toki","monday":"getsuyoobi","tuesday":"kayoobi","wednesday":"suiyoobi","thursday":"mokuyoobi","friday":"kinyoobi","to meet":"au","to buy":"kau","to write":"kaku","to take":"toru","to wait":"matsu","alone":"hitoride","right":"migi","left":"hidari","front":"mae","back":"ushiro","inside":"naka","on":"ue","under":"shita","near/nearby":"chikaku","next":"tonari","between":"aida"}

k5_genki = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","weather":"tenki","drink":"nomimono","postcard":"hagaki","airplane":"hikooki","room":"heya","I (used by men)":"baku","holiday":"yasumi","travel":"ryokoo","new":"atarashii","hot":"atsui","busy":"isogashii","large":"ooki","interesting/funny":"omoshiroi","frightening":"kowai","cold":"samui","fun":"tanoshii","small":"chiisai","old (thing)":"furui","difficult":"muzukashi","cheap":"yasui","disgusted with":"kiraina","healthy/energetic":"genkina","quiet":"shizukana","fond of/to like":"sukina","to hate":"daikiraina","to love":"daisukina","not busy":"himana","to swim":"oyogu","to ask":"kiku","to ride/board":"noru","to go out":"dekakeru","together":"isshoni","it's okay":"daijoobu","counter (flat objects)":"mai"}

n5_jlpt = {"to meet":"au","blue":"ao","red":"aka","bright":"akaru","autumn":"aki","to open":"aku","to give":"ageru","morning":"asa","breakfast":"asagohan","day after tomorrow":"asatte","foot/leg":"ashi"}



learning = {"sea":"umi","postal stamp":"kitte","ticket":"kippu","homework":"shukudai","food":"tabemono","birthday":"tanjoobi","weather":"tenki","postcard":"hagaki","room":"heya","I (men)":"boku","holiday":"yasumi","travel":"ryokoo","new":"atarashii",}

combined_words = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5}
combined_kanji = grade_1_k

word_length = len(combined_words)
kanji_length = len(combined_kanji)
#genki_combined = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5}
#genki_combined = {**k3_genki}
#genki_combined = {**k4_genki, **k1_genki, **k2_genki}
#genki_combined = {**genki_1, **genki_2, **genki_3, **genki_4, **genki_5}
genki_combined = {**learning}
#genki_combined = {**genki_5}

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
