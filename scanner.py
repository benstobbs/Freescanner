import urllib.request
import time
import os

def isint(n):
    try:
        int(n)
        return True
    except:
        return False

def pages(groupname):

    with urllib.request.urlopen("http://groups.freecycle.org/group/"+groupname+"/posts/all") as url:
        f = url.read()
    text = str(f)
    i = text.find("Showing 1 to 1")
    no = text[i+19:].split(' ', 1)[0]
    try:
        int(no)
        return int(no)
    except:
        return 0

def gengroups(s):
    groups = []
    i = 0
    ss= 'href="http://groups.freecycle.org/'

    while s.count(ss) > 0:
        n = s.find(ss)
        if s[n+34:].split('"', 1)[0] not in groups:
            groups.append(s[n+34:].split('"', 1)[0])
        s = s[n+34:]

    return groups

sgroups = """<section id="group_column_1"><p class="offscreen">Groups named from Barking &amp; Dagenham to Greenwich <a href="#group_column_2">skip to next block</a></p><ul><li><a href="http://groups.freecycle.org/BarkingandDagenham">Barking &amp; Dagenham</a></li><li><a href="http://groups.freecycle.org/BarnetUK">Barnet</a></li><li><a href="http://groups.freecycle.org/BexleyUK">Bexley</a></li><li><a href="http://groups.freecycle.org/BrentUK">Brent</a></li><li><a href="http://groups.freecycle.org/BromleyUK">Bromley</a></li><li><a href="http://groups.freecycle.org/HampsteadUK">Camden (Hampstead)</a></li><li><a href="http://groups.freecycle.org/KentishtownUK">Camden (Kentish Town)</a></li><li><a href="http://groups.freecycle.org/CamdenSouthUK">Camden South</a></li><li><a href="http://groups.freecycle.org/CityOfLondon">City of London</a></li><li><a href="http://groups.freecycle.org/CroydonUK">Croydon</a></li><li><a href="http://groups.freecycle.org/EalingUK">Ealing</a></li><li><a href="http://groups.freecycle.org/EnfieldUK">Enfield</a></li><li><a href="http://groups.freecycle.org/Feltham-Bedfont-HanworthUK">Feltham / Bedfont / Hanworth</a></li><li><a href="http://groups.freecycle.org/GreenwichUK">Greenwich</a></li></ul></section>

<section id="group_column_2"><p class="offscreen">Groups named from Hackney to Lambeth <a href="#group_column_3">skip to next block</a></p><ul><li><a href="http://groups.freecycle.org/HackneyUK">Hackney</a></li><li><a href="http://groups.freecycle.org/HammersmithandFulhamUK">Hammersmith &amp; Fulham</a></li><li><a href="http://groups.freecycle.org/HaringeyUK">Haringey</a></li><li><a href="http://groups.freecycle.org/HarrowUK">Harrow</a></li><li><a href="http://groups.freecycle.org/HaveringUK">Havering</a></li><li><a href="http://groups.freecycle.org/HillingdonUK">Hillingdon</a></li><li><a href="http://groups.freecycle.org/HounslowCentralNorthandEastUK">Hounslow - Central / North / East</a></li><li><a href="http://groups.freecycle.org/IslingtonEastUK">Islington East-Finsbury Park,Highbury,Newington Gr</a></li><li><a href="http://groups.freecycle.org/IslingtonNorthUK">Islington Nrth-Highgate,Archway,Tufnell Park etc.</a></li><li><a href="http://groups.freecycle.org/IslingtonSouthUK">Islington Sth-Clerkenwell-Essex Rd-Finsbury-Old St</a></li><li><a href="http://groups.freecycle.org/IslingtonWestUK">Islington West-Lower Holloway,Barnsbury,Kings X</a></li><li><a href="http://groups.freecycle.org/KensingtonandChelseaUK">Kensington and Chelsea</a></li><li><a href="http://groups.freecycle.org/KingstonUK">Kingston-upon-Thames</a></li><li><a href="http://groups.freecycle.org/LambethUK">Lambeth</a></li></ul></section>

<section id="group_column_3"><p class="offscreen">Groups named from Lewisham to Westminster <a href="#group_column_4">skip to next block</a></p><ul><li><a href="http://groups.freecycle.org/LewishamUK">Lewisham</a></li><li><a href="http://groups.freecycle.org/LibraryUK">LibraryUK</a></li><li><a href="http://groups.freecycle.org/MertonUK">Merton</a></li><li><a href="http://groups.freecycle.org/MuseumFreecycleUK">Museum Freecycle UK</a></li><li><a href="http://groups.freecycle.org/NewhamUK">Newham</a></li><li><a href="http://groups.freecycle.org/RedbridgeUK">Redbridge</a></li><li><a href="http://groups.freecycle.org/RichmondUponThamesUK">Richmond-upon-Thames</a></li><li><a href="http://groups.freecycle.org/SouthwarkUK">Southwark</a></li><li><a href="http://groups.freecycle.org/SuttonUK">Sutton</a></li><li><a href="http://groups.freecycle.org/TowerHamletsUK">Tower Hamlets</a></li><li><a href="http://groups.freecycle.org/WalthamForestUK">Waltham Forest</a></li><li><a href="http://groups.freecycle.org/WandsworthUK">Wandsworth</a></li><li><a href="http://groups.freecycle.org/WestminsterUK">Westminster</a></li></ul></section>

<section id="group_column_1"><p class="offscreen">Groups named from Alderney to Fareham <a href="#group_column_2">skip to next block</a></p><ul><li><a href="http://groups.freecycle.org/AlderneyUK">Alderney</a></li><li><a href="http://groups.freecycle.org/AndoverUK">Andover</a></li><li><a href="http://groups.freecycle.org/AscotUK">Ascot</a></li><li><a href="http://groups.freecycle.org/Ash-cum-RidleyUK">Ash-cum-Ridley</a></li><li><a href="http://groups.freecycle.org/AshfordUK">Ashford</a></li><li><a href="http://groups.freecycle.org/AylesburyUK">Aylesbury</a></li><li><a href="http://groups.freecycle.org/BanburyUK">Banbury</a></li><li><a href="http://groups.freecycle.org/BansteadUK">Banstead</a></li><li><a href="http://groups.freecycle.org/BasingstokeUK">Basingstoke</a></li><li><a href="http://groups.freecycle.org/BexhillUK">Bexhill</a></li><li><a href="http://groups.freecycle.org/BicesterUK">Bicester</a></li><li><a href="http://groups.freecycle.org/BognorRegisUK">Bognor Regis</a></li><li><a href="http://groups.freecycle.org/BordonAltonPetersfieldUK">Bordon, Alton &amp; Petersfield</a></li><li><a href="http://groups.freecycle.org/BracknellUK">Bracknell</a></li><li><a href="http://groups.freecycle.org/BrightonUK">Brighton</a></li><li><a href="http://groups.freecycle.org/BuckinghamUK">Buckingham</a></li><li><a href="http://groups.freecycle.org/BurgessHillUK">Burgess Hill</a></li><li><a href="http://groups.freecycle.org/BurwashUK">Burwash</a></li><li><a href="http://groups.freecycle.org/CanterburyUK">Canterbury</a></li><li><a href="http://groups.freecycle.org/caterhamUK">Caterham UK</a></li><li><a href="http://groups.freecycle.org/ChathamUK">Chatham</a></li><li><a href="http://groups.freecycle.org/CherwellValleyUK">Cherwell Valley</a></li><li><a href="http://groups.freecycle.org/ChichesterUK">Chichester</a></li><li><a href="http://groups.freecycle.org/ChilternUK">Chiltern District</a></li><li><a href="http://groups.freecycle.org/ChippingNortonUK">Chipping Norton</a></li><li><a href="http://groups.freecycle.org/CranbrookUK">Cranbrook</a></li><li><a href="http://groups.freecycle.org/CrawleyUK">Crawley</a></li><li><a href="http://groups.freecycle.org/CrowboroughUK">Crowborough</a></li><li><a href="http://groups.freecycle.org/DartfordUK">Dartford</a></li><li><a href="http://groups.freecycle.org/DorkingUK">Dorking UK</a></li><li><a href="http://groups.freecycle.org/DoverUK">Dover</a></li><li><a href="http://groups.freecycle.org/eastgrinstead">East Grinstead</a></li><li><a href="http://groups.freecycle.org/EastbourneUK">Eastbourne</a></li><li><a href="http://groups.freecycle.org/EastleighUK">Eastleigh</a></li><li><a href="http://groups.freecycle.org/ElmbridgeUK">Elmbridge</a></li><li><a href="http://groups.freecycle.org/Epsom">Epsom</a></li><li><a href="http://groups.freecycle.org/FarehamUK">Fareham</a></li></ul></section>

<section id="group_column_2"><p class="offscreen">Groups named from Farnborough &amp; Aldershot to Oxted <a href="#group_column_3">skip to next block</a></p><ul><li><a href="http://groups.freecycle.org/Farnborough_AldershotUK">Farnborough &amp; Aldershot</a></li><li><a href="http://groups.freecycle.org/Farnham">Farnham</a></li><li><a href="http://groups.freecycle.org/FavershamUK">Faversham</a></li><li><a href="http://groups.freecycle.org/FolkestoneUK">Folkestone</a></li><li><a href="http://groups.freecycle.org/GillinghamUK">Gillingham</a></li><li><a href="http://groups.freecycle.org/godalmingUK">Godalming UK</a></li><li><a href="http://groups.freecycle.org/GosportUK">Gosport</a></li><li><a href="http://groups.freecycle.org/GravesendUK">Gravesend</a></li><li><a href="http://groups.freecycle.org/GuernseyUK">Guernsey</a></li><li><a href="http://groups.freecycle.org/GuildfordUK">Guildford</a></li><li><a href="http://groups.freecycle.org/HastingsUK">Hastings</a></li><li><a href="http://groups.freecycle.org/HavantUK">Havant</a></li><li><a href="http://groups.freecycle.org/HaywardsHeathUK">Haywards Heath</a></li><li><a href="http://groups.freecycle.org/HenleyonThamesUK">Henley-on-Thames</a></li><li><a href="http://groups.freecycle.org/HighWycombeUK">High Wycombe</a></li><li><a href="http://groups.freecycle.org/HooPeninsulaUK">Hoo Peninsula</a></li><li><a href="http://groups.freecycle.org/HookHart">Hook Hart</a></li><li><a href="http://groups.freecycle.org/HorshamUK">Horsham</a></li><li><a href="http://groups.freecycle.org/HoveUK">Hove</a></li><li><a href="http://groups.freecycle.org/SheppeyUK">Isle of Sheppey</a></li><li><a href="http://groups.freecycle.org/IsleofWightUK">Isle of Wight</a></li><li><a href="http://groups.freecycle.org/JerseyUK">Jersey</a></li><li><a href="http://groups.freecycle.org/LancingUK">Lancing</a></li><li><a href="http://groups.freecycle.org/LeatherheadUK">Leatherhead</a></li><li><a href="http://groups.freecycle.org/LewesUK">Lewes District</a></li><li><a href="http://groups.freecycle.org/LittlehamptonUK">Littlehampton</a></li><li><a href="http://groups.freecycle.org/MaidstoneUK">Maidstone</a></li><li><a href="http://groups.freecycle.org/MarlowUK">Marlow</a></li><li><a href="http://groups.freecycle.org/MidhurstUK">Midhurst</a></li><li><a href="http://groups.freecycle.org/MiltonKeynesUK">Milton Keynes</a></li><li><a href="http://groups.freecycle.org/NewForestEastUK">New Forest East</a></li><li><a href="http://groups.freecycle.org/NewForestNorth">New Forest North</a></li><li><a href="http://groups.freecycle.org/NewForestWestUK">New Forest West</a></li><li><a href="http://groups.freecycle.org/NewburyUK">Newbury</a></li><li><a href="http://groups.freecycle.org/OlneyUK">Olney</a></li><li><a href="http://groups.freecycle.org/OxfordUK">Oxford</a></li><li><a href="http://groups.freecycle.org/OxtedUK">Oxted</a></li></ul></section>

<section id="group_column_3"><p class="offscreen">Groups named from Paddock Wood to Worthing <a href="#group_column_4">skip to next block</a></p><ul><li><a href="http://groups.freecycle.org/PaddockWood">Paddock Wood</a></li><li><a href="http://groups.freecycle.org/PortsladeUK">Portslade</a></li><li><a href="http://groups.freecycle.org/PortsmouthUK">Portsmouth</a></li><li><a href="http://groups.freecycle.org/ReadingUK">Reading UK</a></li><li><a href="http://groups.freecycle.org/ReigateUK">Reigate</a></li><li><a href="http://groups.freecycle.org/RomseyUK">Romsey</a></li><li><a href="http://groups.freecycle.org/RunnymedeUK">Runnymede</a></li><li><a href="http://groups.freecycle.org/Rye-EasternRother-UK">Rye &amp; Eastern Rother</a></li><li><a href="http://groups.freecycle.org/SevenoaksUK">Sevenoaks</a></li><li><a href="http://groups.freecycle.org/sittingbourne">Sittingbourne</a></li><li><a href="http://groups.freecycle.org/SloughUK">Slough</a></li><li><a href="http://groups.freecycle.org/SnodlandUK">Snodland</a></li><li><a href="http://groups.freecycle.org/SouthamptonUK">Southampton</a></li><li><a href="http://groups.freecycle.org/SpelthorneUK">Spelthorne</a></li><li><a href="http://groups.freecycle.org/Storrington">Storrington-Sullington</a></li><li><a href="http://groups.freecycle.org/StroodUK">Strood</a></li><li><a href="http://groups.freecycle.org/SurreyHeathUK">Surrey Heath</a></li><li><a href="http://groups.freecycle.org/Swanley">Swanley</a></li><li><a href="http://groups.freecycle.org/Tadley">Tadley</a></li><li><a href="http://groups.freecycle.org/ThanetUK">Thanet</a></li><li><a href="http://groups.freecycle.org/TonbridgeUK">Tonbridge</a></li><li><a href="http://groups.freecycle.org/TunbridgeWellsUK">Tunbridge Wells</a></li><li><a href="http://groups.freecycle.org/UckfieldUK">Uckfield</a></li><li><a href="http://groups.freecycle.org/ValeWhiteHorseUK">Vale of the White Horse</a></li><li><a href="http://groups.freecycle.org/WaldersladeUK">Walderslade</a></li><li><a href="http://groups.freecycle.org/WallingfordUK">Wallingford</a></li><li><a href="http://groups.freecycle.org/WestKingsdownUK">West Kingsdown</a></li><li><a href="http://groups.freecycle.org/WheatleyThameUK">Wheatley &amp; Thame</a></li><li><a href="http://groups.freecycle.org/Whitstable">Whitstable</a></li><li><a href="http://groups.freecycle.org/WinchesterUK">Winchester</a></li><li><a href="http://groups.freecycle.org/WindsorMaidenheadUK">Windsor &amp; Maidenhead</a></li><li><a href="http://groups.freecycle.org/WitneyUK">Witney</a></li><li><a href="http://groups.freecycle.org/WokingUK">Woking</a></li><li><a href="http://groups.freecycle.org/WokinghamUK">Wokingham</a></li><li><a href="http://groups.freecycle.org/WoodleyUK">Woodley - Earley</a></li><li><a href="http://groups.freecycle.org/WorthingUK">Worthing</a></li></ul></section>
"""

def getposts(group):

    ads = pages(group)
    nopage = int(ads/10)
    if ((ads/10)>(int(ads/10))):
        nopage += 1

    posts = []
    ss= 'https://groups.freecycle.org/group/'+group+'/posts/'

    for i in range(1, nopage+1):
        
        with urllib.request.urlopen(("https://groups.freecycle.org/group/"+group+"/posts/offer?page="+str(i)+"&resultsperpage=10&showall=off&include_offers=off&include_wanteds=off&include_receiveds=off&include_takens=off")) as url:
            f = url.read()
        page = str(f)
        while page.count(ss) > 0:
            n = page.find(ss)

            if isint(page[n+42+len(group)]):
                post = (page[n+42+len(group):].split("/", 1)[0])
                if isint(post):
                    if (page[n:].split("'", 1)[0]) not in posts:
                        posts.append((page[n:].split("'", 1)[0]))
            page = page[n+42+len(group):]
         
    return posts    


groups = gengroups(sgroups)

if not os.path.exists("/freescanner/data/"+time.strftime("%Y%m%d")):
    os.makedirs("/freescanner/data/"+time.strftime("%Y%m%d"))

for group in groups:
    print("["+str(groups.index(group)+1)+"/"+str(len(groups))+"] "+group)
    posts = getposts(group)
    with open("/freescanner/data/"+time.strftime("%Y%m%d")+"/"+group+".txt", "w") as myfile:
        for post in posts:
            myfile.write(post+"\n")
