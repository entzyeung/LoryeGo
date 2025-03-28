# event.py

import random
from stations import map_layout  # Already present for map_layout

################ Note ################
# Adjusted Ranges
# Minor: $100–$200 (10%–20% of starting cash).
# Moderate: $300–$500 (30%–50%).
# Major: $600–$1000 (60%–100%).
# Extreme: $1000+ (rare, e.g., st009 capped at $1000).
######################################

################
### for all fly to destination function, need to register in random_event() in main.py. (Don't remove this nudge)
#    teleport_uids = ["fly_to_destination"]
#    if uid in ["free_business"]:
#    elif uid in ["lose_business"]:
#    elif uid in ["zilla"]

# Seasonal Events

seasonal_events = {
    "春季": [
        ("fly_to_destination", lambda p, dest=None: None, "alien_kidnap_animation",
        "嘩...!\n \n \n 嘩呀...!!\n \n \n 發生乜嘢事！吸住我左呀! \n \n 但好似去緊...\n終點喎! \n咁又唔拘啊！"), # register in random_event()
        ("sp00", lambda p, dest=None: setattr(p, "cash", p.cash + 500), "breaking_news_animation",
        "呵呵...!\n \n \n 呵呵呵...!!\n \n \n 點解突然多咗錢？\n \n \n 武漢肺炎過後，\n2023年旅遊業復甦，\n香港人氣急升，\n商店生意大旺，\n臨時多賺$500"),
        ("lundam", lambda p, dest=None: setattr(p, "cash", p.cash + 700), "lundam_animation",
        "嘩...!\n \n \n 嘩呀...!!\n \n \n 發生乜嘢事！\n80年代日本人愛遊港，\n連 金田一 同 Z-Lundom 都有去過香港！\n小店多賺$700"),

        ("sp40", lambda p, dest=None: setattr(p, "cash", p.cash - 150), "breaking_news_animation",
        "哎呀...\n \n \n 哎呀呀... \n 點解少咗錢嘅？\n \n \n 春雨連綿，導致漏水，\n60年代舊樓多問題，\n修一修蝕$150！"),
        ("zilla", lambda p, dest=None: setattr(p, "cash", p.cash - 600), "zilla_animation",
        "突發...!\n \n \n 突發呵...!!\n \n \n 有師奶侵襲市區！？\n \n \n 呀唔係,係突然有哥師奶侵襲市區，\n做成大量損毁，\n財物損失多達$600"),

        ],

    "夏季": [
        ("fly_to_destination", lambda p, dest=None: None, "alien_kidnap_animation",
        "嘩...!\n \n \n 嘩呀...!!\n \n \n 發生乜嘢事！吸住我左呀! \n \n 但好似去緊...\n終點喎! \n咁又唔拘啊！"), # register in random_event()

        ("rainstorm", lambda p, dest=None: setattr(p, "cash", p.cash - 400), "breaking_news_animation",
        "突發...!\n \n \n 突發呵...!!\n \n \n 暴雨成災，\n連續多日嘅雨水，\n導致大部份香港地區都成為澤國，\n社會損失嚴重，\n多達$400"),
        ("su00", lambda p, dest=None: setattr(p, "cash", p.cash + 300), "breaking_news_animation",
        "哎呀，\n \n \n 哎呀呀，\n \n \n 天氣太熱，個個都出來消費！\n收到臨時收入$300"),
        ("su03", lambda p, dest=None: setattr(p, "cash", p.cash + 400), "breaking_news_animation",
        "咦...？！\n \n \n 咁多遊客嘅！\n \n \n 因為夏天節日多，\n7.1維港煙花吸引人潮，\n賺大錢$400"),
        ("su40", lambda p, dest=None: setattr(p, "cash", p.cash - 300), "breaking_news_animation",
        "（哭）...\n \n \n 點解無晒錢的？？\n \n \n 2000年代網上騙案開始流行，\n損失$300！"),
        ("su41", lambda p, dest=None: setattr(p, "cash", p.cash - 300), "breaking_news_animation",
        "（哭）...\n \n \n 點解無晒錢的？？\n \n \n 暑假詐騙多，小心街頭假賣，\n損失$300！"),
        ("closer_to_destination", lambda p, dest=None: move_closer_to_destination(p), "breaking_news_animation", 
        "咦？快咗到達！新MTR線通車，\n2016年港鐵擴展，\n小朋友快到目的地啦！"),
        ("lose_business", lambda p, dest=None: lose_asset(p, map_layout), "breaking_news_animation",
        "哎呀？攤位被清！旺角小販多，\n70年代政府清場，失去一個資產！"),
        ("free_business", lambda p, dest=None: give_free_asset(p, map_layout), "breaking_news_animation",
        "呵呵呵...!\n \n \n 呵呵...!!\n \n \n 有免費屋？\n秋天政府推新計劃，\n2000年代填海地多，\n市民抽中免費資產！"),

        ],

    "秋季": [
        ("fly_to_destination", lambda p, dest=None: None, "alien_kidnap_animation",
        "嘩...!\n \n \n 嘩呀...!!\n \n \n 發生乜嘢事！吸住我左呀! \n \n 但好似去緊...\n終點喎! \n咁又唔拘啊！"), # register in random_event()
        ("free_business", lambda p, dest=None: give_free_asset(p, map_layout), "breaking_news_animation",
        "呵呵呵...!\n \n \n 呵呵...!!\n \n \n 有免費屋？\n秋天政府推新計劃，\n2000年代填海地多，\n市民抽中免費資產！"),
        ("au00", lambda p, dest=None: setattr(p, "cash", p.cash + 500), "breaking_news_animation",
        "哇！\n \n \n多咗錢！\n \n \n 秋季旅遊高峰，\n2003年後內地自由行暴增，\n商店生意火紅，\n賺$500！"),
        ("au40", lambda p, dest=None: setattr(p, "cash", p.cash - 200), "breaking_news_animation",
        "（哭）...\n \n \n 吓？\n \n \n 點解要罰？\n \n \n 秋風大，垃圾亂飛，\n60年代清潔問題多，\n罰款$200"),
        ("horse_racing", lambda p, dest=None: setattr(p, "cash", p.cash + 400), "horse_racing_animation",
        "咦突發...!\n \n \n 突發呵...!!\n \n \n 馬季開鑼，沙田馬場丁財兩旺，\n總投注額投注額創疫情後的新高, \n額外收入$400"),

        ("farther_from_destination", lambda p, dest=None: move_farther_from_destination(p), "breaking_news_animation",
        "2024年香港受到颱風桃芝吹襲，\n交通立立亂，離目的地更遠！"),
        
        ],

    "冬季": [
        ("fly_to_destination", lambda p, dest=None: None, "alien_kidnap_animation",
        "嘩...!\n \n \n 嘩呀...!!\n \n \n 發生乜嘢事！吸住我左呀! \n \n 但好似去緊...\n終點喎! \n咁又唔拘啊！"), # register in random_event()
        ("lose_business", lambda p, dest=None: lose_asset(p, map_layout), "snow_storm_animation",
        "落雪呀!\n \n \n 係落雪呀!\n \n \n 屋企被風雪吹爛！\n \n \n 香港自1967年至今有四次落雪的記錄，\n分別在歌連臣角和大帽山。\n你的舊樓因大雪積壓倒塌，\n失去一個資產！"),
        ("wi40", lambda p, dest=None: setattr(p, "cash", p.cash - 400), "breaking_news_animation",
        "吓...？\n \n \n 80年代中英談判，\n樓價曾大跌，\n人工追唔到，\n少左$400！"),
        ("tofu_building", lambda p, dest=None: setattr(p, "cash", p.cash - 600), "tofu_building_animation",
        "突發...!\n \n \n 突發呵...!!\n \n \n 又發現豆腐渣工程，\n清楚見到大廈搖搖欲墜，\n要即刻修理！\n少左$600！"),

        ("wi90", lambda p, dest=None: teleport_random(p), "breaking_news_animation",
        "...？點解變咗位？冬日迷霧多，突然傳送到新地點！"),
        ("blue_hut", lambda p, dest=None: setattr(p, "cash", p.cash + 600), "blue_hut_animation",
        "咦突發...!\n \n \n 突發呵...!!\n \n \n 藍屋餐廳再次神秘開幕！\n位於赤柱大街，建於1948年，\n曾經神秘失蹤，現在神秘開幕！\n曾名為鬼屋餐廳，\n適逢萬聖節，來臨打卡的人眾多，\n車水馬龍，\n帶來額外收入$600！"),
        ("wuhan_virus", lambda p, dest=None: setattr(p, "cash", p.cash - 777), "wuhan_virus_animation",
        "突發...!\n \n \n 突發呵...!!\n \n \n 有新病毒直接坐直通車落嚟！？\n \n \n 造成大量感染，\n社會損失嚴重，\n多達$777"),
 
        ]
}

# Station Events (50 Hong Kong-themed events)
station_events = [
    ("game_changing_02", lambda p, dest=None: setattr(p, "cash", p.cash + 1500), "",
     "新年好運！農曆新年紅包多，\n80年代經濟好，\n收到$1500利是！"),
    ("game_changing_03", lambda p, dest=None: setattr(p, "cash", p.cash + 1980), "",
     "哇！AI科技展好正！\n努力耕耘10年，\n2025年終於乘上AI熱，\n賺$2120！"),

    ("st400", lambda p, dest=None: setattr(p, "cash", p.cash - 300), "",
     "哇！十號風球來啦！\n1962年颱風溫黛襲港，\n商店關門，\n經濟損失$300，要小心風暴啊~"),
    ("st001", lambda p, dest=None: setattr(p, "cash", p.cash + 200), "",
     "咦？遊客好多！維港夜景出名，\n2000年代旅遊業旺，船票賣到斷貨，賺$200！"),
    ("st401", lambda p, dest=None: setattr(p, "cash", p.cash - 500), "",
     "吓？樓市跌咗！2008年金融海嘯，\n香港樓價急挫，投資失利，損失$500！"),
    ("st002", lambda p, dest=None: setattr(p, "cash", p.cash + 150), "",
     "點解多咗錢？點心節熱鬧，\n70年代飲食文化興盛，遊客愛食叉燒包，\n賺$150！"),
    ("st402", lambda p, dest=None: setattr(p, "cash", p.cash - 350), "",
     "吓？生意亂晒籠！\n2025年政府無能，\n旺角店舖關門，\n小商戶蝕$350，\n好無奈.....！"),
    ("st003", lambda p, dest=None: setattr(p, "cash", p.cash + 250), "",
     "哇！大嶼山人氣爆棚！\n2005年迪士尼開幕，\n遊客蜂擁而至，小店賺$250！"),
    ("st403", lambda p, dest=None: setattr(p, "cash", p.cash - 400), "",
     "租金貴咗！中環90年代地價狂升，\n店舖頂唔順高租，\n蝕$400！"),
    ("st004", lambda p, dest=None: setattr(p, "cash", p.cash + 180), "",
     "好嘢！\n贏咗比賽！端午龍舟賽熱鬧，\n80年代傳統復興，\n隊伍贏獎金$180！"),
    ("st404", lambda p, dest=None: setattr(p, "cash", p.cash - 200), "",
     "罰款！冬天霧霾嚴重，\n90年代內地工廠污染多，\n政府罰$200清空氣！"),
    ("closer_to_destination", lambda p, dest=None: move_closer_to_destination(p), "", 
     "咦？快咗到達！新MTR線通車，\n2016年港鐵擴展，\n小朋友快到目的地啦！"),
    ("st405", lambda p, dest=None: setattr(p, "cash", p.cash - 689), "",
     "股票跌咗！\n2003年SARS後股市亂，\n香港投資者驚慌，損失$689！"),
    ("st006", lambda p, dest=None: setattr(p, "cash", p.cash + 120), "",
     "哇！山頂人多！太平山纜車復古，\n90年代遊客愛影相，賣票賺$120！"),
    ("st406", lambda p, dest=None: setattr(p, "cash", p.cash - 350), "",
     "哎水浸！九龍暴雨頻繁，\n60年代排水差，\n店舖被淹蝕$350！"),
    ("st007", lambda p, dest=None: setattr(p, "cash", p.cash + 200), "",
     "燈籠好靚！中秋燈會熱鬧，\n80年代傳統復興，\n賣燈籠賺$200！"),
    ("st407", lambda p, dest=None: reduce_business_returns(p), "", 
     "工程延誤！港珠澳橋超支，\n2009年動工慢，\n生意少咗回報一年！"),
    ("st008", lambda p, dest=None: setattr(p, "cash", p.cash + 500), "",
     "哇！海濱熱賣！維港填海後，\n2000年代地產旺，\n賣樓賺大錢$500！"),
    ("st408", lambda p, dest=None: setattr(p, "cash", p.cash - 150), "",
     "的士罷工！\n2025年香港的士同業大會宣告生死存亡之戰，\n影響經濟，損失$150！"),

    ("st409", lambda p, dest=None: setattr(p, "cash", p.cash - 400), "",
     "皇后碼頭要被拆啦！\n皇后碼頭2007年於拆咗...！\n社會損失$400！"),
    ("st010", lambda p, dest=None: setattr(p, "cash", p.cash + 100), "",
     "哇！天星有錢賺！\n70年代維港熱鬧，\n渡輪遊客多，\n賣票收入$100！"),
    ("st410", lambda p, dest=None: setattr(p, "cash", p.cash - 200), "",
     "哎呀？避風塘壞咗！\n颱風季損壞多，修船貴，\n修理費$200！"),
    ("st011", lambda p, dest=None: setattr(p, "cash", p.cash + 250), "",
     "旺角好旺！街市人流多，\n賺$250！"),
    ("st411", lambda p, dest=None: setattr(p, "cash", p.cash - 300), "",
     "通脹好嚴重！\n2008年石油價格大起大落！\n油價上升，香港物價貴，\n生活費多$300！"),
    ("st012", lambda p, dest=None: setattr(p, "cash", p.cash + 180), "",
     "哇！煙花真靚！維港新年煙花，\n2000年代吸引遊客，\n賣紀念品賺$180！"),
    ("st412", lambda p, dest=None: setattr(p, "cash", p.cash - 150), "",
     "過橋費貴！2018年港珠澳橋通車，\n但收費高，車主蝕$150！"),
    ("st013", lambda p, dest=None: setattr(p, "cash", p.cash + 400), "",
     "新商場開張！太古廣場熱鬧，\n90年代消費旺，\n店舖賺$400！"),
    ("st413", lambda p, dest=None: setattr(p, "cash", p.cash - 100), "",
     "塞車好亂！九龍交通擠塞，\n70年代車多路窄，\n罰款$100！"),
    ("st014", lambda p, dest=None: setattr(p, "cash", p.cash + 220), "",
     "哇！文化節好玩！\n藝術展覽多人，\n2010年代文化熱，\n賣文青產品賺$220！"),
    ("st414", lambda p, dest=None: setattr(p, "cash", p.cash - 250), "",
     "哎呀...停電呀！冬天用電多，\n60年代電力不足，\n店舖蝕$250！"),
    ("st015", lambda p, dest=None: setattr(p, "cash", p.cash + 300), "",
     "海洋公園旺！2000年代擴建後，\n遊客愛玩機動遊戲，\n門票賺$300！"),
    ("st415", lambda p, dest=None: setattr(p, "cash", p.cash - 450), "",
     "樓市過熱，2010年代政府加稅，\n業主多交$450！"),
    ("st016", lambda p, dest=None: setattr(p, "cash", p.cash + 500), "",
     "哇！中秋賣月餅！80年代傳統熱，\n市民愛買香港華華月餅，\n又做月餅會，賺$500！"),
    ("st416", lambda p, dest=None: setattr(p, "cash", p.cash - 300), "",
     "哎呀？港口塞咗！貨輪延誤多，\n90年代貿易忙，\n罰款$300好頭痛！"),
    ("st017", lambda p, dest=None: setattr(p, "cash", p.cash + 350), "",
     "電影節好正！香港電影展，\n2000年代文化推廣，\n贊助賺$350！"),
    ("st417", lambda p, dest=None: setattr(p, "cash", p.cash - 400), "",
     "山泥傾瀉！暴雨頻繁，\n60年代舊區危險，\n修路蝕$400！"),
    ("st018", lambda p, dest=None: setattr(p, "cash", p.cash + 250), "",
     "太平山夜景靚，\n90年代遊客多，\n賣票賺$250！"),
    ("st418", lambda p, dest=None: setattr(p, "cash", p.cash - 200), "",
     "哎呀？交通罷工！\n市民步行上班，\n生意少$200！"),
    ("st019", lambda p, dest=None: setattr(p, "cash", p.cash + 300), "",
     "咦？Art Basel旺！\n藝術展多人，\n2010年代國際化，\n賣畫賺$300！"),
    ("st419", lambda p, dest=None: setattr(p, "cash", p.cash - 150), "",
     "吓？水荒罰款！夏天缺水，\n70年代水塘不足，\n罰$150要慳水！"),
    ("st020", lambda p, dest=None: setattr(p, "cash", p.cash + 180), "",
     "哇！夜市好熱鬧！旺角街頭旺，\n80年代小販多，\n賣小食賺$180！"),
    ("st420", lambda p, dest=None: setattr(p, "cash", p.cash - 500), "",
     "中環重建多，2000年代地價升，\n建築費蝕$500！"),
    ("st021", lambda p, dest=None: setattr(p, "cash", p.cash + 220), "",
     "包山節好玩！長洲搶包山，\n90年代傳統熱，賣票賺$220！"),
    ("st421", lambda p, dest=None: setattr(p, "cash", p.cash - 200), "",
     "飛機誤點！\n機場繁忙，航班亂，\n罰款$200好無奈！"),
    ("st022", lambda p, dest=None: setattr(p, "cash", p.cash + 400), "",
     "哇！新酒店開幕！銅鑼灣旺場，\n2000年代旅遊熱，投資賺$400！"),
    ("lose_business", lambda p, dest=None: lose_asset(p, map_layout), "",
     "哎呀？攤位被清！旺角小販多，\n70年代政府清場，失去一個資產！"),
    ("st423", lambda p, dest=None: setattr(p, "cash", p.cash - 150), "",
     "青馬橋貴！通車後收費高，\n90年代車主壓力，過橋蝕$150！"),
    ("st023", lambda p, dest=None: setattr(p, "cash", p.cash + 200), "",
     "咦？舞龍好精彩！\n新年表演多人睇，\n80年代傳統旺，\n賣票賺$200！"),
    ("farther_from_destination", lambda p, dest=None: move_farther_from_destination(p), "",
     "2024年香港受到颱風桃芝吹襲，\n交通立立亂，離目的地更遠！"),

    ("st425", lambda p, dest=None: setattr(p, "cash", p.cash - 100), "",
     "街食被禁！70年代政府清潔市容，\n小販生意少，蝕$100！"),
    ("st025", lambda p, dest=None: setattr(p, "cash", p.cash + 250), "",
     "海港遊好旺！維港船票熱賣，\n90年代旅遊熱，賺$250好開心！"),
]




## Event Functions
def give_free_asset(player, map_layout):
    space = map_layout[player.position]
    if space["type"] == "city":
        available = [a for a in space["assets"] if a["owner"] is None]
        if available:
            asset = random.choice(available)
            asset["owner"] = player.name
            player.assets.append(asset)
            return f"{player.name} 免費獲得咗 {asset['name']}！好彩到爆燈！"
        else:
            return f"{player.name} 想攞免費資產，但這裡空空如也！恭喜你，成為空手王！"
    return None  # If not a city, no message

def lose_asset(player, map_layout):
    if player.assets:
        asset = player.assets.pop(0)
        for space in map_layout.values():
            for a in space["assets"]:
                if a["name"] == asset["name"] and a.get("owner") == player.name:
                    a["owner"] = None
        return f"{player.name} 唔好彩失去咗 {asset['name']}！不如去飲杯茶, 食個包, \n定一定神？"
    else:
        return f"{player.name} 無資產可輸！恭喜你，輸到乾乾淨淨，真係人生贏家！"

def teleport_random(player):
    new_pos = random.choice(list(map_layout.keys()))
    player.position = new_pos
    player.x = map_layout[new_pos]["x"]
    player.y = map_layout[new_pos]["y"]
    print(f"{player.name} teleported to {map_layout[new_pos]['name']}!")

def move_closer_to_destination(player):
    def calculate_steps_to_goal(start_pos, dest_pos):
        if start_pos == dest_pos:
            return 0
        visited = set()
        queue = [(start_pos, 0)]
        visited.add(start_pos)
        while queue:
            current_pos, steps = queue.pop(0)
            for next_pos in map_layout[current_pos]["connections"]:
                if next_pos in visited:
                    continue
                if next_pos == dest_pos:
                    return steps + 1
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))
        return float('inf')

    destination = player.destination
    current_steps = calculate_steps_to_goal(player.position, destination)
    print(f"Current position: {map_layout[player.position]['name']}, Steps to {map_layout[destination]['name']}: {current_steps}")
    possible_destinations = map_layout[player.position]["connections"]
    print(f"Possible destinations: {[map_layout[d]['name'] for d in possible_destinations]}")
    min_steps = current_steps
    next_position = None
    old_position_name = map_layout[player.position]["name"]
    for dest in possible_destinations:
        steps = calculate_steps_to_goal(dest, destination)
        print(f"To {map_layout[dest]['name']}: {steps} steps")
        if steps < min_steps and steps != float('inf'):
            min_steps = steps
            next_position = dest
    if next_position:
        player.position = next_position
        player.x = map_layout[next_position]["x"]
        player.y = map_layout[next_position]["y"]
        print(f"{player.name} moved closer to destination from {old_position_name} to {map_layout[next_position]['name']}!")
    else:
        print(f"{player.name} couldn’t move closer to {map_layout[destination]['name']} from {old_position_name}!")

def move_farther_from_destination(player):
    def calculate_steps_to_goal(start_pos, dest_pos):
        if start_pos == dest_pos:
            return 0
        visited = set()
        queue = [(start_pos, 0)]
        visited.add(start_pos)
        while queue:
            current_pos, steps = queue.pop(0)
            for next_pos in map_layout[current_pos]["connections"]:
                if next_pos in visited:
                    continue
                if next_pos == dest_pos:
                    return steps + 1
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))
        return float('inf')

    destination = player.destination
    current_steps = calculate_steps_to_goal(player.position, destination)
    print(f"Current position: {map_layout[player.position]['name']}, Steps to {map_layout[destination]['name']}: {current_steps}")
    possible_destinations = map_layout[player.position]["connections"]
    print(f"Possible destinations: {[map_layout[d]['name'] for d in possible_destinations]}")
    max_steps = current_steps
    next_position = None
    for dest in possible_destinations:
        steps = calculate_steps_to_goal(dest, destination)
        print(f"To {map_layout[dest]['name']}: {steps} steps")
        if steps > max_steps and steps != float('inf'):
            max_steps = steps
            next_position = dest
    if next_position:
        old_position_name = map_layout[player.position]["name"]
        player.position = next_position
        player.x = map_layout[next_position]["x"]
        player.y = map_layout[next_position]["y"]
        print(f"{player.name} moved farther from destination from {old_position_name} to {map_layout[next_position]['name']}!")
    else:
        print(f"{player.name} couldn’t move farther from {map_layout[destination]['name']} from {map_layout[player.position]['name']} - no farther option available!")

def reduce_business_returns(player):
    if player.assets:
        for asset in player.assets:
            if "original_profit" not in asset:
                asset["original_profit"] = asset.get("profit", int(asset["price"] * asset["return_percentage"] / 100))
            profit = asset["original_profit"]
            asset["profit"] = int(profit * 0.5)
        print(f"{player.name}'s business returns reduced by 50% for this year!")