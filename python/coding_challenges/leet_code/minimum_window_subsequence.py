"""
REVISIT: The implementation works, but is timing out due to not checking the order
    when inserting the item into the is valid frequency check.
Question: https://leetcode.com/problems/minimum-window-subsequence/
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.


Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""
from collections import defaultdict


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        return self.first_implementation(S, T)

    def first_implementation(self, inp: str, seeking: str) -> str:
        """
        Using the frequency calculation to determine if a set of letters
        are within the wanted window.
        The window would start at the first instance of finding any of the
        characters in the seeking string.
        Question: Would there be a possibility of repetition in T, or would the characters be unique.
        If the characters are unique then a set would be used else we'd use a dict.
        For this instance there are multiple instances of the same char possible. The dict works for
        both cases the set/dict combo may be a bit faster though.
        This works albeit slowly, would need to optimize the code to ensure the segments are in order as well.
        """

        # initialize the frequency dictionaries. And the needed pointers in the window.
        frequency = defaultdict(int)
        s_freq = defaultdict(int)
        for x in seeking:
            s_freq[x] += 1
        freq_keys = s_freq.items()
        min_word = ""
        left = 0
        right = 0

        def handle_freq(char, op=1):
            if char in s_freq:
                frequency[char] += op

        def is_valid():
            # ensure that the values being sought exist at the minimum frequency needed for the current window.
            for key, value in freq_keys:
                if key not in frequency or frequency[key] < value:
                    return False
            cur_window = inp[left:right]
            idx = 0
            for char in cur_window:
                if char == seeking[idx]:
                    idx += 1
            if idx == len(seeking) and (not min_word or len(cur_window) < len(min_word)):
                return True

            return False

        while left < len(inp):
            # check if the window contains the right set of letters
            # ensuring that the minimum occurrence of each key is in the sought frequency range.

            if right >= len(inp) or (min_word and right - left >= len(min_word)):
                # can't search right anymore, start trimming the window from the left.
                # If the size of the window is greater than the size of the smallest match then shrink it.
                handle_freq(inp[left], -1)
                left += 1
            else:
                # Keep trying to ingest from the right hand side until we've exhausted this pointer
                # then we'll play catchup from the left hand pointer validating as needed.
                handle_freq(inp[right], 1)
                right += 1

            if is_valid():
                min_word = inp[left:right]
            # print(left, right, min_word)

            if len(min_word) == len(seeking):
                # early break case as the len of the word being sought cannot be smaller than this.
                return min_word
        return min_word


"""
Test Cases:

"abcdebdde"
"bde"
"jbsgekcxgwzachbcahyrdvycugbfnlvhbmdploguqigvlmjkznliugdqmtiqurlguofvgntaazeoamgqjikhwiuuvdosqkxmxpbuticodcxybweydapqikefbcqdlkiuebdfxckojqzcjsytceouwtkzjyjqwwfvroqnnaqetrpjjfqpssjnkmuxuhxchjrpzlnfnyfbepdjzpyphzjdovoyynsjrovtqvpzkgsytgzlgkrctgrfarehhhmyowcccoonhouavksclacghhhwwpcikqqbzflscsyypyzzzndfmxuajwrokdbcjddudwxzqtqvomtpejewfkjnujabojkeblgxjkpjcoabgkyigqewlvgsdmqtgylmknojaajkupndjgypgowdkhyptezzrgcscaydwqyvjzhozoqmkhhxvgfhwxzvrhwlpadejyjfssfagfnbgwztmgglcwpkovssutzozkfxfxgeyqdgechviomqiygccxfydywpjxzskrrmyrdxxtthsirsdoxzbcwferhhuszgrzfoqiatlnzkahhnqdghmnatmiuhthmfwzaalpfnntyuqgflkhlqxuhnazekmdysmttomrofuczrqtrmnlvvsjhrxczslnbjjeycctluxewbldtyeddfutapqcvivmocskjzhaqsvodrnehxlnzqdjrflaphxgeffldghutmxdesrrjfjvuixjjylzmtowipyaoqylbmnqzsxhjhtpmmrommmfqzbfrdrzidjacvupujpkzblnleggmkhhjgfhonyyuvbfyhhyqafogbvgulvfphmedaroesvjwfofstjfnomihiqmfrwycwybwwwoozcwbdyyfbufnzvscuvvonxlezxktunteuzbrukpyjfzljlwrbaqocpwkukgynizjrtvqigpfbrihfvygtotcuhnpwubznvzjxheiwwbmnoivokxvfbzjvjzqzsaxgfreyrfbsqtfwtjzyfurtvhmnqaeurfwvzbpxhbzxzyjojwxqbsrsvultfnyspgjmtvprkdfajgcnsrnfiygzqzrospzpocrrlfvquowbosdufcznhqjntczesgsugmcjshevfbrghkgqpfkwkrkohwxeqluigswkgzokvmmovxwiitjntdtpkzvwztajtaiuommghpvrxoetqthaikjqviqxajbgnhqvswcyadbxbdpvmhyiibxeotjtbsycsuiutxoyixkbbyxcqvpxwujfzvclbpnibukzkylgudtumekozxvsytlvpyvsbjzuyrkdypzallwiiavatvzdeulnaegtviknuqjnsqfczfwtxaojnxgpjtucefkvfzzouxvrchtlxxcxkfkfqjqnrmenpizdjiqxenjomycnrpikwmmwvoboctukncxaxolngzlyjmojppgbsplqnmzhwbjmuiculgsxreauxungfuafpqyefymmotzhwlhqmgzbvxgrrxkfndycmzdjdknzrduoiqavgemfvmvpkpxhbzdskljxemmlykckkncuymrubbikkwkzmwzzmkoegrzdiluwwdlywkxuulsjxboiuzutzfgdkauvfsafspcxvhholecbxglqvmefaujtyxgoajfcblwoxdugjuguzideviaduoxmyevjqfsxhaombkimmfhvhlfxygmnbkuvttjyuecqkmiptiokrscnysvhsypkoamertftkfzcludcchxdqaaxlmjnpyuwcolpjcizassuzmptagxwzqgvbhytfxwgkcrsvpdcmugyntuuwotuevkydawypsqboyoquhgaqtzotedvasxjnhhmrerwcbktaczoavtdlcoctxpgeijaromhfxhgwegumgpnyohxubutftutfltxglpnvpredranlbfnwigpxauiqfbmwnytqodbujplmxfmntncmkmupycjvfrvcuncovjpcferdpbeerdvnhxlvttaowotckwzlglbltlxdyhdsjceyeuxmpubnfyaskjupcwrqqusjaqmkfhlwyesonsiwskofwzdjldxmpjocxmsknswomqrdoaaqyszdwmgolaawckvdbjjfiledjkgvwanapwwppivdwhhuzcdegbhdpumuhzkazzrixzjddwmlvgogswalqecdaostjctvmacmzclrtoadqzdidcqadpevgpcjljsmwnlqbwvmsqwzkjvkbucqfayaijgelrbsemjettxucnlgmwpwdxgcjiduwsborrvzlxqayvnttwuwzekvmxnnznhdqwleawdogllababjckbruztqkvrbxrmlflezehxuezodvqzsimmhcndvedbkiesnezphgjyrufwmfsjslhoguhjgfvdnxanxrunyvvqzeihadqwgqyaajwidxfigkubjuhzjyvgvupfpylfhieralqjnwbcqdsthmyhuxjgqpniahwezavdolvosblmevbvtlijlaykvtiafpvssklmuolnnrrogsptefcgalmcpmubcqjkgkbfoxhchqkqmeahqpaepbbpnpyvzsmyygpaxljsguwiuaiwsscsefbvsvynzkeztlcgncskshqebnwccmxhmotrfttipvxzgnyzamrtjejmluqhuawtcchaumaxqoadttzwtutyyozkpvkrlusdeiioyivdkvbrfypdpuwqnwuaedcnegparkmenoqrevosnwmktcssvkrzkiulvagaqxkcuusohgwcbqmybjwufgghuostgronsrnuhdxlfctrqnpcgnmswjmfkbwtcefdcmdjfaarawupgjduectaefpicuxhfvutohxlahyxfohgfrwxeafzjisueltaywroyvndswlqdoomyhkiymxodkkkisbeuhxmusytytbliwvigmcapqrwxubiogvfthbapljhjhhgthiluetsmdcykgtfbqkgfetfggntxrttnedyptjlyrtehncwjndeluucnvhfshupyyonhetbfslblynsetlwhgdycxzfoczxubkzbfouocvnlmzbbtpjkkxzewicpqojiyafcctbtgzbptpnlpmluwhzvonpeozlakomkxizxpaygrrlwmmcqjlsxswpzqagrolsraalsgwfwqbssmcmokspjdylrsewllxskkajauxmozhsbuoyihynrvkkwnawkgeclcdzplxmqalzvvzjymvglkdpxaftpgkhvthsnmrmzwidiwrnohwekmomisokbmtqyfgvdvikdxavqrhxwaukoaufpyjkrqgdmgdbhaqwdakykzwqenenzglnrndihvauqzqgxkzaqcldlwhsexuczhwmswrgabwcmqbhkbzchfghvlpmfhxatunbneaxabgvlbzghqfiivyzzydbppjhtykjovgacgtooskatdzofozdwfrvvzwnwxxrnlxhctmjjynmlfdqdpdaskzkypndamthectfmiajvolpgimsnjqqxjuveadoagrqaujqxbhbhkxkbeilhphlvqucnqqnkfhjchjewwgoxuxziluupktzdberdhfzhzunotnxounrwcwgiotiknscejhmsqfazhmoiajgbhpdlpcvqnrmpjshtmamlpezyxouzfheonuiwfjytjpkukjwtbivnicimhykhvvgjuxmocjdqrhtsumwtwpdxtwczpozyzaspdtzgaphxokvbipzjwyxlxkgrzcgykiklvlvhxaccqkjitjoboiihucvqjjbubkeenaoorrcscciyndajtwugvktifzjprtajtogetrnxvqzelutigumcxmiubkyejprwmywalzyvifbgekxdmbjzohjttkcgpgogreypnrsmzdkoaaelqoycfkagcsqrbfbayegzwqqicrdhraktneyjqqqgdikyfrzdicwoiqwlbfgleqawcnfgbgbzkwsjvtgvwyqmngivjsfafwztwdgyydsbnzozhusgexpxnhxnocciyjznsuzgujebwfibviztcxvkwzaxlukvhoiobeobpixywkzgccjxorzjrrelblxudlnmffmhcljjfpcyehhzjltlozifcpyerovgaxhtzadrndchxlaowtntjvxmxgxkfwwylnjtbispqottrhflgezdesfsascmkpnubzgpvwytecuymjzkhftjsschaseosuttthnbqtjvewrumxlsqphdzekpsjkwsctwenuwlbvttlyjcckqibaefylnqmxjxcumswmgxgpxpvsmvlpbkphsalvhucfwuwgfvnvypqdztusportfhbjxmgohizsmtwpvtnkdjmjvifdehqnbnjwkcuvgmetlzonumnhudkndltvglpetcqkhuxxpfiywdndqdwebryopuwyuskwqccvhergzbpxfosmpldfvtgzbqvyfaixvkmitfiieqvmstxrvsnawmreworucntyhpnclopxzhvrwxqamgfqekwphdmqzmrgpuzcpxrqzlvssqtpokxflhgbgyyvrnqxgyyxnaxonaxuqkdzrykngpwcrhyeaimmjosfdpbjxclvofbieagpbkivosijbfshkjwlfbxqrkrxbtiisjumjyrgygrwovgqmjnswzydenofzuhhwszdajeiquosdualsttmvulgxkxjwhiqyiycslgubaijdymllperwgezqrdwfddwpjnanatlrzazmxhzdujqzupbefavuienylsxlzxhsyfzjuizzhbrwrubxlsptuuvcdpsyvrcyjomqsahyjnqilzbfjiuxbfywkwcrqegqcbquusmnmqgpdlopdwzrvwgphaldawxmtvqfmuopmduxbhlhsxcwvcyonpnfvgtixvgpibwgvomylownrpugzmdrofaoqurwrabmjswfhvwgacuqplelpmaympfjtdldtpkyoakaeuufnpniwjwcjmaalfgbaqrqkdnzbmneuutknsfgboicpjitbpbcvkrtohpficdedkegsfsmsjtoivfeyejrhkwkqarhbdmpbdudeuevaqjiifrqoctbslveczgmeejxoylxuvgikrqapztshjyebzjaijbglbbkemsenlefsqoywlcnrtcemhfnuqxsntbvsprbsgffagetnyiwucxfycoxatektpwmluygpkkokemdlohnfhajxvctrpinjuwcyaeqbkblrqqbflaiqhegxyhggfjxrljizawtyervvwhhejzyqnbcfmywvmrwlvqofggbuwrnwcaijriosdalflllazcfwplqksefwmukpgsfdnfzkanzqshdoxgnagrelwnhhooywxhrmvwrpxjfyygndwzfcjipmfyotwoftibgmcajfifpkqtyjsofmrdkorqsheqadydumootmuookxokypvebipuvldjzglbripnsflcpidcztwahhorsnwbsznojufukkjpxwzuvyyxcxlibcxjdwxbieupjonckbabireuieenqkaqbipefvayktnesafirjwfdizytqxrvxlfnfngdcasymyteamhqpukerpgxrikxjajwnluyzwdzhxciyaqgcxlodjulnwzsnlwyygmcvjlptqxswtezmxwssasjksgtifuvwsjsgvkbmkjqybbmqmnbtowtopobimaqqlcyqgvvidzzsegoituxznknjmkcmyqnmpjuhhjptvzvvkrvcxgmkkiearftyehscvlqvgzvhazymoihoykefsxpfbdfdaijeixulztrhfcfcnvbrxjbcqesfbmjhwekvfbdzkmllhaqbriipaqrflircskwbzideewmudctatullbjayrifdivustyczkqmxrorvhstciclscukvfyvoqularvfbyfvgzzvwhskvsbstsezfcfvbozmrirefnckgpllfynkukywieqpkhmdkczhkzsuenkedxempawuldsvovarkgvbwjyynyohswbkelnwvzxszqfgyofqemvfmurfumtgqcumegndsrmycthtjkjouwvgbxiobwpfippmvszxdxwctdwoghpmksnmwrfhzafowyhcfqkagabhkpiskvesibfagguuublwbdamxznvkcmduqafesgxblevdtcdpooijjcmylseqtsaksnfwjvyqwmxriinbinndzzbnvihdvofeaadwvhcqtkwnlzhdjkpqbixpbnqhtfdngtazwnxuhfeesafphvzlyqdhpcvswokftxxwysbroanqgpkztmjmgsidjkxswxrdgjypwycsutygdpyyurwsullyfmcmerlolrjgnphfoizossvuxoiensfickdtynkdhrwpkuepifxslthbpqjeejoilrtlzcqedzngnjebvnjdmncxadysrhmjtnngcirmoqzjhubfstuogccrrefoyihyguznhmpbyjjabonxbolijzzahsjcxvvrmygbuykfotaztbnuvpzcmfgwvdqigeqekiixomchndcbegcvvgtzhfodwddnelfmhqaqjkdidemcnlzxwkbsajtisgayfnnckxojexrljpebaffyfdqekkbkdqcxamhiukbjsykphkwjxkbqdsxkkskqqojglqlxyrfhxozumwzplexuzrptxcuvrxmofspejtcsojgsupnofovrwrbxgjzfkxtshggqiwribzssvbciytaneomptohytmjzffvcfgidhvbgyokmoediwajzoamxjkgbpointuxyrrrkybgzvgaqbvnpcauwfwayrzvheiggyklzinhwbksdvgvpwnhskngzzaavwudwtnslpztrjcyvcaetixwxgowgrayijcyzafgrlpxphcuscxevahiiwbcbbpljaevtvaaeqqxdohqxjczjosgeeplgiwnjtpjnuuetvurwfyygrvuybnjrhsgvzwxmulwyheibxwgrzpmnwdohxfwgrehkozvovurlkmxedfzhrplabtgeojykjesuujxbzbefezlzjkguncqybcefmmuqmiqznbbojmehvelqqoofkirmagmsrxyqaxbeeqgghsaslfqpwmtrqcmgsygcqxcfrcuusxuqogvraxyxlkukkqezhzsxwnkfnycpmqumftpvtpheiwiuskxynkyrxfawayvuqrkecjoiyuerkxbjivrkkqeokjfsftnckqernpegjsifpbkqlwfhpztthovhyxkpfhbmydesmnnyxxikpwtxthpsmoefyjonnjhojirxtrjnaoobtomzxzujcwrykrpzgdslrxbauluzcbbbmtmhkspmuehdnhdeptiwwtypquiznozhtnglbyrbbelzbvihkpumcryzmrbjagsntozlombiahvdgtmehffomccrevlvqulivxaoqdacjpvwodmnuopfeldscrzoxpgmwodzfonfpujmoubqfvvljyufgtfjufezzlaeofpxudynxprbtkyhdncizgnkrdtbhlgzvikqmqmodroaubmkihyehmfcbnadnxkgnbtfkgzkgciveyhdvhplxoluumkrfirszbfhnpectropyzpmwexgfaouokkvffpaxhqfhvkzdedknqrnstfihdptmacugdraiqjqctqybkbtaaktdsapbcgpoaladreeoyulbxlheybmsbtcxqwpqrdbuiqiutcyhkvuhpumadiylegrkzyqzvpqbxinfeafvzvahxbqgtyiqfbebpjifdqyxcifzhpqlobtjiwexhquexhdimqdusglxgifyjwwkmuddoecwmbgpwgdnijegynifwekzrtpqvfoejerpwchbjtjpcgtokyhoyssdunywshbxywwjizqklbfsiytdsvptymtnqopbprlmgiveimfeadujtprvwatjkskghhhtkebphdauycurfvtwulmuouwkcglimgiwyrxswnwobedlfstkxadpwmjdvfreyybgpbbpgzgjblfanaybzngckipkrzqhajprpyqxrqqrcbtnlyjtopjvpqpmeckvnbexulatotvpzyvfzqbcbzzfynduurgaczkjwacnkavmitsqzjjkgrscmeucqfioykuqpuucpgpqhhibhsquzufwmgadyyzalakuykrwyhmfwxumzgalhlwadrgrynxyiwblhlugqodtokrwsulgohqdhstxyajcvxvngvtluxyakiujttaobucrncloyuskqlxflyxkivcyygozccucweswxyippobtabcqpylkvwmuowhajznlautebntpidzkymupzrdmujhxwdszbpuiprekyasthdfoigkpbbiwzjobmwccqfcdotiqvsjftfomyewwzuahsiuuiccgwlhzbbcexwtgiyvrvlxaxoigeahepsrsfflxwmyzufozitlbarvsjdyatpkcuvgkwggkgkuvcpagndyqzxlvuztligtfniemgknrfmqzhjillmdrfemgmekwpuxtguegzqkaqqariehhjkinigwsmfetygapoudshepaekswcwafvymqngborlfzcihmdkiduqqfxsheuzfteifrtqjcqiwcsbietldjwfkdtmujosihsgqeppmeumextxtpbtiiyivmhurejfeioosourgswejlowwtfpackctcgiqyjtyjhbnawbyvedjzvesrbgktqnwmudinidgtbobquisdooeiwtlacehfspisrntmsfkerdnpwkxnaemvpcykpjclqystkdtguemlgpfmqaooqoivsdvzeeafxtwfxktlbdlmtyvcihvogtcqulirnvwwgwxrjfjlqtmocngtvorkfcsfxwvgzzfumlwqnuskxfacbnetpxncawxhjrfxbdxjnkuxesmqjowawzjoujlmdfaokhlaysayyerylxyytoltyuzorrplljkzmowsgnrnbmbkwcapbilnqqopameaynnqnvmylgxozotigudxkuedsekhjwbauwrkutctnwdmtyuxenvbsvrmaxlamrtpyotxycmnizxhugicywvaqpoxyigrvczdkbncbaplbzyxwhiymjgeryyrxgrauyqsexoeilyoyvhtmylwpmzbfnukaalxpeakwiooniwzfaspzlaftokualigdeykznqyzyyopfxxwlhqayeououwzraidlzeichnacxsnyguuuvrtbzujosjetkaxuvwliagkznfjufcmycpkdfwezgbkfjscjttxeuvgvxwcwrmpbkagwajcsumdyvjfvqbennkkqqmjntuvldbqergiohsbyrxpyhopxvnrtcuushpiybajdujozclcivukqllnpsicxntxetiwpxamcmpxxzfhealjaiptyrmivqqcbnbqfkfbzmsosvyrkhntbjgramvxjsjbhrkbylohpyhwuipserbgdtdypatmjdablxblzrmbeypjwoggguywhbzaputvqblduvdowjrwwlfbnkbnizwfnlihpvmnvgsuuinytcnoqitlnmfawrkflgadjldxdbofgbmindetjbhvtipwbxoxtbxikmelsfjhcugsjlfnknsmvbkajloiadbjblccsvibkersuhvoxyxaguartaicuejgthxvdkwqyzwvzbjpohswinowrzrtomjvbflqbzjqojjxmaguayzlumapruurivupsijxwqlaffwyahufoayxwactvtxwznxotnalpgfinypxayqdzczcvqeuodcvsfgjmdlffjnkzdoqsjbwepsvvjtxqlxdfghuuqlrdddvvldgojkxrdysowifiaufllqwcpfufybaxisffyqcsmqkgpeueknuexcdgbijcldkzluherxvcpeiurjlpgknylkkxfewnkfbdscvytxqdeclpqtdqtwglhaulpiqhfzymvayfdysbfwgpsh"
"jlwowjmfgptfxqjhwqwgoxpzqeedvhdszyhgmukgiinhkehzxyhtegbsnvibpobqrvuguxzpnjukvomtivipiawficslplawxdfl"
"""
