map_layout = {
    # Existing stations 0-97 and 500-521 remain unchanged until connections are updated
    #########################
    ### TCL (Tung Chung Line)
    0: {"name": "香港", "line": "TCL", "connections": [25, 108], "x": 3516, "y": 3063, "type": "city", "assets": [
        {"name": "菲律賓購物中心", "price": 1000, "return_percentage": 50, "owner": None},
        {"name": "女傭購物天中心", "price": 1000, "return_percentage": 50, "owner": None},
        {"name": "甲級寫字樓", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "金融中心", "price": 2000, "return_percentage": 25, "owner": None},
        {"name": "交易廣場", "price": 2000, "return_percentage": 25, "owner": None},
        {"name": "IFFC商場", "price": 2500, "return_percentage": 40, "owner": None},
        {"name": "豪華酒店", "price": 3000, "return_percentage": 20, "owner": None}
    ]},
    500: {"name": "機會", "line": "TCL", "connections": [107, 109], "x": 2752, "y": 3063, "type": "event", "assets": []},
    1: {"name": "九龍", "line": "TCL", "connections": [2, 104, 106], "x": 2752, "y": 2350, "type": "city", "assets": [
        {"name": "溜冰場", "price": 1200, "return_percentage": 10, "owner": None},
        {"name": "元素商場", "price": 3000, "return_percentage": 5, "owner": None},

    ]},
    2: {"name": "奧運", "line": "TCL", "connections": [1, 3], "x": 2752, "y": 2099, "type": "city", "assets": [
        {"name": "運動場館", "price": 1000, "return_percentage": 2, "owner": None},
        {"name": "奧運商場", "price": 2000, "return_percentage": 10, "owner": None},
    ]},
    3: {"name": "南昌", "line": "TCL/TML", "connections": [501, 102, 101, 2], "x": 2752, "y": 1959, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 150, "return_percentage": 12, "owner": None},
        {"name": "屋村食肆", "price": 150, "return_percentage": 12, "owner": None},
    ]},
    501: {"name": "機會", "line": "TCL", "connections": [3, 102, 4, 5], "x": 2544, "y": 1959, "type": "event", "assets": []},
    4: {"name": "荔景", "line": "TCL/TSW", "connections": [501, 14, 15], "x": 2544, "y": 1430, "type": "city", "assets": [
        {"name": "乙級寫字樓", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
    ]},
    5: {"name": "青衣", "line": "TCL", "connections": [501, 502], "x": 2380, "y": 1959, "type": "city", "assets": [
        {"name": "青衣海洋商場", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "青衣商場", "price": 220, "return_percentage": 15, "owner": None}
    ]},
    502: {"name": "機會", "line": "TCL", "connections": [5, 6, 8], "x": 1940, "y": 1959, "type": "event", "assets": []},
    6: {"name": "愉景灣", "line": "TCL", "connections": [502, 7, 10], "x": 1940, "y": 2411, "type": "city", "assets": [
        {"name": "愉景灣渡假村", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "愉景灣渡假村", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "海景餐廳", "price": 380, "return_percentage": 5, "owner": None},
        {"name": "海景餐廳", "price": 380, "return_percentage": 5, "owner": None},
    ]},
    7: {"name": "東涌", "line": "TCL", "connections": [6], "x": 1940, "y": 2763, "type": "city", "assets": [
        {"name": "東涌Outlet商場", "price": 1000, "return_percentage": 20, "owner": None},
        {"name": "東涌名店Outlet商場", "price": 1600, "return_percentage": 30, "owner": None},
        {"name": "纜車站360", "price": 1500, "return_percentage": 15, "owner": None}
    ]},
    8: {"name": "機場", "line": "TCL", "connections": [502, 9], "x": 1522, "y": 1959, "type": "city", "assets": [
        {"name": "機場內餐廳", "price": 350, "return_percentage": 50, "owner": None},
        {"name": "機場外餐廳", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "機場酒店", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "機場酒店", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "機場酒店", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "機場酒店", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "機場酒店", "price": 1000, "return_percentage": 25, "owner": None}
    ]},
    9: {"name": "博覽館", "line": "TCL", "connections": [8], "x": 1122, "y": 1959, "type": "city", "assets": [
        {"name": "博覽館中心", "price": 1000, "return_percentage": 10, "owner": None},
        {"name": "特約展示店", "price": 400, "return_percentage": 1, "owner": None}
    ]},
    10: {"name": "迪士尼", "line": "TCL", "connections": [6], "x": 2134, "y": 2411, "type": "city", "assets": [
        {"name": "迪迪尼主題餐廳", "price": 800, "return_percentage": 25, "owner": None},
        {"name": "迪迪尼樂園酒店", "price": 1000, "return_percentage": 20, "owner": None},
        {"name": "迪迪尼樂園精品店", "price": 1000, "return_percentage": 20, "owner": None},
        {"name": "迪迪尼樂園精品店", "price": 1000, "return_percentage": 20, "owner": None},
        {"name": "迪迪尼樂園精品店", "price": 1000, "return_percentage": 20, "owner": None},
        {"name": "迪迪尼樂園", "price": 3000, "return_percentage": 2, "owner": None},
        
    ]},
    ### TSW (Tsuen Wan Line)
    11: {"name": "荃灣", "line": "TSW", "connections": [12], "x": 1368, "y": 1430, "type": "city", "assets": [
        {"name": "市集", "price": 100, "return_percentage": 50, "owner": None},
        {"name": "市集", "price": 100, "return_percentage": 50, "owner": None},
        {"name": "街頭小食店", "price": 100, "return_percentage": 50, "owner": None},
        {"name": "南風布廠", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "南風商場", "price": 1000, "return_percentage": 40, "owner": None},
        {"name": "購物商場", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "熊貓酒店", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "小甜甜廣場", "price": 2000, "return_percentage": 10, "owner": None},
    ]},
    12: {"name": "大窩口", "line": "TSW", "connections": [11, 13], "x": 1668, "y": 1430, "type": "city", "assets": [
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "工業大廈", "price": 700, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 700, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 700, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 700, "return_percentage": 3, "owner": None},
    ]},
    13: {"name": "葵興", "line": "TSW", "connections": [12, 14], "x": 1962, "y": 1430, "type": "city", "assets": [
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "工業大廈", "price": 700, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 700, "return_percentage": 3, "owner": None},
        {"name": "HIIT貨櫃碼頭", "price": 2000, "return_percentage": 5, "owner": None},
    ]},
    14: {"name": "葵芳", "line": "TSW", "connections": [13, 4], "x": 2244, "y": 1430, "type": "city", "assets": [
        {"name": "葵講商場", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "購物商場", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "購物商場", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "工業大廈", "price": 900, "return_percentage": 4, "owner": None},
        {"name": "工業大廈", "price": 900, "return_percentage": 4, "owner": None},
    ]},
    15: {"name": "美孚", "line": "TSW/TML", "connections": [4, 16, 515, 101], "x": 2752, "y": 1430, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 150, "return_percentage": 12, "owner": None},
        {"name": "屋村食肆", "price": 150, "return_percentage": 12, "owner": None},
        {"name": "荔園遊樂場", "price": 1000, "return_percentage": 30, "owner": None},

    ]},
    16: {"name": "荔枝角", "line": "TSW", "connections": [15, 100], "x": 3014, "y": 1430, "type": "city", "assets": [
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "工業大廈", "price": 900, "return_percentage": 4, "owner": None},
    ]},
    17: {"name": "長沙灣", "line": "TSW", "connections": [18, 100], "x": 3538, "y": 1430, "type": "city", "assets": [
        {"name": "文創空間", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "文創商場", "price": 900, "return_percentage": 25, "owner": None},
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "工業大廈", "price": 900, "return_percentage": 4, "owner": None},
    ]},
    18: {"name": "深水埗", "line": "TSW", "connections": [17, 503], "x": 3800, "y": 1430, "type": "city", "assets": [
        {"name": "夜市", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "玩具街", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "街頭小食店", "price": 100, "return_percentage": 300, "owner": None},
        {"name": "電子零件店", "price": 300, "return_percentage": 50, "owner": None},
        {"name": "電腦商場", "price": 1000, "return_percentage": 90, "owner": None},
        {"name": "電腦遊戲商場", "price": 1000, "return_percentage": 80, "owner": None},
        {"name": "購物商場", "price": 1000, "return_percentage": 10, "owner": None},
    ]},
    503: {"name": "機會", "line": "TSW", "connections": [18, 19], "x": 3800, "y": 1616, "type": "event", "assets": []},
    19: {"name": "太子", "line": "TSW/KTL", "connections": [503, 20, 504], "x": 3958, "y": 1616, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 100, "return_percentage": 200, "owner": None},
        {"name": "街頭小食店", "price": 100, "return_percentage": 200, "owner": None},
        {"name": "聯合商場", "price": 1000, "return_percentage": 10, "owner": None},
        {"name": "購物商場", "price": 1000, "return_percentage": 10, "owner": None},
        {"name": "女人街", "price": 800, "return_percentage": 250, "owner": None},
    ]},
    20: {"name": "旺角", "line": "TSW/KTL", "connections": [19, 21], "x": 3958, "y": 1854, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 100, "return_percentage": 300, "owner": None},
        {"name": "電腦商場", "price": 1000, "return_percentage": 50, "owner": None},
        {"name": "電腦遊戲商場", "price": 1000, "return_percentage": 150, "owner": None},
        {"name": "動漫精品商場", "price": 1000, "return_percentage": 100, "owner": None},
        {"name": "旺角服飾中心", "price": 1000, "return_percentage": 300, "owner": None},
        {"name": "女人街", "price": 800, "return_percentage": 300, "owner": None},
        {"name": "信和日本文化商場", "price": 1000, "return_percentage": 90, "owner": None},
    ]},
    21: {"name": "油麻地", "line": "TSW/KTL", "connections": [20, 22, 114], "x": 3958, "y": 2026, "type": "city", "assets": [
        {"name": "廟街夜市", "price": 250, "return_percentage": 50, "owner": None},
        {"name": "街頭小食店", "price": 100, "return_percentage": 150, "owner": None},
        {"name": "街頭小食店", "price": 100, "return_percentage": 150, "owner": None},
        {"name": "Boutique酒店", "price": 900, "return_percentage": 40, "owner": None},
        {"name": "酒店", "price": 1200, "return_percentage": 20, "owner": None},
    ]},
    510: {"name": "delete", "line": "delete", "connections": [], "x": 0, "y": 0, "type": "delete", "assets": []},
    22: {"name": "佐敦", "line": "TSW", "connections": [21, 23], "x": 3958, "y": 2314, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 200, "return_percentage": 50, "owner": None},
        {"name": "Boutique酒店", "price": 900, "return_percentage": 40, "owner": None},
        {"name": "Boutique酒店", "price": 900, "return_percentage": 40, "owner": None},
        {"name": "Boutique酒店", "price": 900, "return_percentage": 40, "owner": None},
        {"name": "酒店", "price": 1200, "return_percentage": 20, "owner": None},
    ]},
    23: {"name": "尖沙咀", "line": "TSW", "connections": [22, 505, 512, 68], "x": 3958, "y": 2601, "type": "city", "assets": [
        {"name": "Danki日式超市", "price": 900, "return_percentage": 80, "owner": None},
        {"name": "購物中心", "price": 1200, "return_percentage": 20, "owner": None},
        {"name": "Boutique酒店", "price": 1200, "return_percentage": 40, "owner": None},
        {"name": "海港觀景台", "price": 1400, "return_percentage": 20, "owner": None},
        {"name": "甲級寫字樓", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "高級酒店", "price": 2500, "return_percentage": 10, "owner": None},
        {"name": "Kate11商場", "price": 2600, "return_percentage": 5, "owner": None},
        {"name": "1/2島酒店", "price": 3000, "return_percentage": 30, "owner": None},
    ]},
    505: {"name": "機會", "line": "TSW", "connections": [23, 24, 82], "x": 3958, "y": 3068, "type": "event", "assets": []},
    24: {"name": "金鐘", "line": "TSW/ISL/ERL/SIL", "connections": [505, 124, 25, 30], "x": 3958, "y": 3304, "type": "city", "assets": [
        {"name": "購物中心", "price": 1200, "return_percentage": 20, "owner": None},
        {"name": "PP購物中心", "price": 1300, "return_percentage": 15, "owner": None},
        {"name": "甲級寫字樓", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "甲級寫字樓", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "商務中心", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "商務中心", "price": 1500, "return_percentage": 10, "owner": None},
    ]},
    25: {"name": "中環", "line": "TSW/ISL", "connections": [24, 0, 29], "x": 3516, "y": 3304, "type": "city", "assets": [
        {"name": "商務中心", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "商務中心", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "甲級寫字樓", "price": 1600, "return_percentage": 10, "owner": None},
        {"name": "甲級寫字樓", "price": 1600, "return_percentage": 10, "owner": None},
        {"name": "金融中心", "price": 1900, "return_percentage": 20, "owner": None},
        {"name": "金融中心", "price": 1900, "return_percentage": 20, "owner": None},
        {"name": "金融中心", "price": 1900, "return_percentage": 20, "owner": None},
    ]},
    ### ISL (Island Line)
    26: {"name": "堅尼地城", "line": "ISL", "connections": [27], "x": 1992, "y": 3304, "type": "city", "assets": [
        {"name": "小食店", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "文青咖啡店", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "文青咖啡店", "price": 100, "return_percentage": 100, "owner": None},
    ]},
    27: {"name": "港大", "line": "ISL", "connections": [26, 28], "x": 2360, "y": 3304, "type": "city", "assets": [
        {"name": "文青咖啡店", "price": 100, "return_percentage": 30, "owner": None},
    ]},
    28: {"name": "西營盤", "line": "ISL", "connections": [27, 29], "x": 2744, "y": 3304, "type": "city", "assets": [
        {"name": "小食店", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "文青咖啡店", "price": 100, "return_percentage": 30, "owner": None},
        {"name": "Awakening咖啡店", "price": 100, "return_percentage": 100, "owner": None}
    ]},
    29: {"name": "上環", "line": "ISL", "connections": [28, 25], "x": 3130, "y": 3304, "type": "city", "assets": [
        {"name": "小食店", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "食肆", "price": 200, "return_percentage": 25, "owner": None},
        {"name": "商務中心", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "商務中心", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "甲級寫字樓", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "乙級寫字樓", "price": 1200, "return_percentage": 10, "owner": None}
    ]},
    30: {"name": "灣仔", "line": "ISL", "connections": [24, 31], "x": 4376, "y": 3304, "type": "city", "assets": [
        {"name": "玩具街", "price": 100, "return_percentage": 80, "owner": None},
        {"name": "補習社", "price": 200, "return_percentage": 60, "owner": None},
        {"name": "食肆", "price": 200, "return_percentage": 25, "owner": None},
        {"name": "電腦商場", "price": 1000, "return_percentage": 30, "owner": None},
        {"name": "電腦遊戲商場", "price": 1000, "return_percentage": 30, "owner": None},
        {"name": "甲級寫字樓", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "乙級寫字樓", "price": 1200, "return_percentage": 10, "owner": None},
        {"name": "會展中心", "price": 2000, "return_percentage": 2, "owner": None}
    ]},
    31: {"name": "銅鑼灣", "line": "ISL", "connections": [30, 32], "x": 4712, "y": 3304, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 200, "return_percentage": 120, "owner": None},
        {"name": "豬王拉麵店", "price": 200, "return_percentage": 100, "owner": None},
        {"name": "食肆", "price": 200, "return_percentage": 25, "owner": None},
        {"name": "購物中心", "price": 1000, "return_percentage": 30, "owner": None},
        {"name": "時間廣場", "price": 1800, "return_percentage": 30, "owner": None},
        {"name": "日資商場", "price": 1900, "return_percentage": 30, "owner": None},
        {"name": "太丸百貨", "price": 2000, "return_percentage": 25, "owner": None},
        {"name": "SUGO", "price": 2300, "return_percentage": 35, "owner": None},
    ]},
    32: {"name": "天后", "line": "ISL", "connections": [31, 33], "x": 5036, "y": 3304, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "天后廟", "price": 250, "return_percentage": 45, "owner": None},
    ]},
    33: {"name": "炮台山", "line": "ISL", "connections": [32, 34], "x": 5416, "y": 3304, "type": "city", "assets": [
        {"name": "食肆", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "購物商場", "price": 1000, "return_percentage": 20, "owner": None}
    ]},
    34: {"name": "北角", "line": "ISL/TKO", "connections": [33, 35], "x": 5800, "y": 3304, "type": "city", "assets": [
        {"name": "雞蛋仔店", "price": 50, "return_percentage": 150, "owner": None},
        {"name": "街頭小食店", "price": 100, "return_percentage": 20, "owner": None},
    ]},
    35: {"name": "鰂魚涌", "line": "ISL/TKO", "connections": [34, 36, 506], "x": 6166, "y": 3304, "type": "city", "assets": [
        {"name": "購物廣場", "price": 1200, "return_percentage": 10, "owner": None},
        {"name": "商業中心", "price": 1500, "return_percentage": 20, "owner": None}
    ]},
    506: {"name": "機會", "line": "TCL", "connections": [35, 123, 507], "x": 6166, "y": 2959, "type": "event", "assets": []},
    507: {"name": "機會", "line": "TCL", "connections": [123, 506, 53], "x": 6166, "y": 2361, "type": "event", "assets": []},
    36: {"name": "太古", "line": "ISL", "connections": [35, 37], "x": 6556, "y": 3304, "type": "city", "assets": [
        {"name": "食肆", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "食肆", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "商業中心", "price": 1500, "return_percentage": 20, "owner": None},
        {"name": "太鼓城購物中心", "price": 2500, "return_percentage": 20, "owner": None},
    ]},
    37: {"name": "西灣河", "line": "ISL", "connections": [36, 508], "x": 6856, "y": 3304, "type": "city", "assets": [
        {"name": "藝術村", "price": 250, "return_percentage": 5, "owner": None},
        {"name": "創意商場", "price": 400, "return_percentage": 15, "owner": None}
    ]},
    508: {"name": "機會", "line": "TCL", "connections": [37, 38], "x": 6856, "y": 3440, "type": "event", "assets": []},
    38: {"name": "筲箕灣", "line": "ISL", "connections": [508, 509], "x": 7108, "y": 3440, "type": "city", "assets": [
        {"name": "海濱長廊", "price": 50, "return_percentage": 1, "owner": None},
    ]},
    509: {"name": "機會", "line": "TCL", "connections": [38, 39], "x": 7108, "y": 3632, "type": "event", "assets": []},
    39: {"name": "杏花邨", "line": "ISL", "connections": [509, 40], "x": 7232, "y": 3632, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 200, "return_percentage": 20, "owner": None},
        {"name": "街頭小食店", "price": 200, "return_percentage": 20, "owner": None}
    ]},
    40: {"name": "柴灣", "line": "ISL", "connections": [39], "x": 7232, "y": 3857, "type": "city", "assets": [
        {"name": "街頭小食店", "price": 200, "return_percentage": 100, "owner": None},
        {"name": "物流公司", "price": 500, "return_percentage": 25, "owner": None},
        {"name": "工業大廈", "price": 600, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 600, "return_percentage": 3, "owner": None},
    ]},
    ### KTL (Kwun Tong Line)
    41: {"name": "黃埔", "line": "KTL", "connections": [42], "x": 5496, "y": 2026, "type": "city", "assets": [
        {"name": "食肆", "price": 200, "return_percentage": 20, "owner": None},
        {"name": "食肆", "price": 200, "return_percentage": 20, "owner": None},
        {"name": "購物廣場", "price": 1200, "return_percentage": 20, "owner": None},
        {"name": "商業中心", "price": 1500, "return_percentage": 10, "owner": None},
        {"name": "黃埔購物天地", "price": 1800, "return_percentage": 15, "owner": None},
    ]},
    42: {"name": "何文田", "line": "KTL/TML", "connections": [41, 116, 522, 517], "x": 5012, "y": 2026, "type": "city", "assets": [
        {"name": "食肆", "price": 100, "return_percentage": 10, "owner": None},
    ]},
    504: {"name": "機會", "line": "KTL", "connections": [19, 43], "x": 4274, "y": 1616, "type": "event", "assets": []},
    43: {"name": "石硤尾", "line": "KTL", "connections": [504, 44], "x": 4274, "y": 1430, "type": "city", "assets": [
        {"name": "文創市集", "price": 250, "return_percentage": 40, "owner": None},
    ]},
    44: {"name": "九龍塘", "line": "KTL/ERL", "connections": [43, 45, 115, 519], "x": 4620, "y": 1430, "type": "city", "assets": [
        {"name": "懷舊小築", "price": 400, "return_percentage": 30, "owner": None},
        {"name": "幼稚園", "price": 600, "return_percentage": 100, "owner": None},
        {"name": "幼稚園", "price": 600, "return_percentage": 100, "owner": None},
        {"name": "有一城商場", "price": 2700, "return_percentage": 35, "owner": None},
    ]},
    45: {"name": "樂富", "line": "KTL", "connections": [44, 46], "x": 5026, "y": 1430, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 1200, "return_percentage": 25, "owner": None},
        {"name": "屋村商場", "price": 1200, "return_percentage": 30, "owner": None},
        {"name": "華人天主教墳場", "price": 1500, "return_percentage": 50, "owner": None},
    ]},
    46: {"name": "黃大仙", "line": "KTL", "connections": [45, 47], "x": 5340, "y": 1430, "type": "city", "assets": [
        {"name": "睇相鋪", "price": 50, "return_percentage": 300, "owner": None},
        {"name": "香燭店", "price": 100, "return_percentage": 80, "owner": None},
        {"name": "紙紮鋪", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "紙紮鋪", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "廟宇", "price": 600, "return_percentage": 70, "owner": None},
        {"name": "廟宇", "price": 600, "return_percentage": 70, "owner": None},
    ]},
    47: {"name": "鑽石山", "line": "KTL/TML", "connections": [46, 48, 518, 71], "x": 5672, "y": 1430, "type": "city", "assets": [
        {"name": "靜修中心", "price": 300, "return_percentage": 40, "owner": None},
        {"name": "好萊塢商場", "price": 1600, "return_percentage": 20, "owner": None},
    ]},
    48: {"name": "彩虹", "line": "KTL", "connections": [47, 49], "x": 6124, "y": 1430, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 1000, "return_percentage": 20, "owner": None},
        {"name": "屋村商場", "price": 1000, "return_percentage": 20, "owner": None},
    ]},
    49: {"name": "九龍灣", "line": "KTL", "connections": [48, 50], "x": 6568, "y": 1430, "type": "city", "assets": [
        {"name": "食肆", "price": 200, "return_percentage": 20, "owner": None},
        {"name": "購物廣場", "price": 1200, "return_percentage": 20, "owner": None},
        {"name": "SuperBigBox", "price": 1300, "return_percentage": 10, "owner": None},
        {"name": "演唱會場地", "price": 1400, "return_percentage": 5, "owner": None},
    ]},
    50: {"name": "牛頭角", "line": "KTL", "connections": [49, 51], "x": 6568, "y": 1652, "type": "city", "assets": [
        {"name": "Band房", "price": 100, "return_percentage": 40, "owner": None},
        {"name": "工業大廈", "price": 800, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 800, "return_percentage": 3, "owner": None},
        {"name": "工業大廈", "price": 800, "return_percentage": 3, "owner": None},
    ]},
    51: {"name": "觀塘", "line": "KTL", "connections": [50, 52], "x": 6568, "y": 1880, "type": "city", "assets": [
        {"name": "工業大廈", "price": 900, "return_percentage": 4, "owner": None},
        {"name": "工業大廈", "price": 900, "return_percentage": 4, "owner": None},
    ]},
    52: {"name": "藍田", "line": "KTL", "connections": [51, 53], "x": 6568, "y": 2153, "type": "city", "assets": [
        {"name": "屋村商場", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    53: {"name": "油塘", "line": "KTL/TKO", "connections": [52, 54, 507], "x": 6568, "y": 2361, "type": "city", "assets": [
        {"name": "屋村商場", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    54: {"name": "調景嶺", "line": "KTL/TKO", "connections": [53, 55], "x": 6883, "y": 2361, "type": "city", "assets": [
        {"name": "屋村商場", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    55: {"name": "將軍澳", "line": "TKO", "connections": [54, 56, 57], "x": 7198, "y": 2361, "type": "city", "assets": [
        {"name": "購物商場", "price": 900, "return_percentage": 20, "owner": None},
        {"name": "將軍O廣場", "price": 1000, "return_percentage": 30, "owner": None},
        {"name": "商業中心", "price": 1500, "return_percentage": 10, "owner": None},
    ]},
    56: {"name": "坑口", "line": "TKO", "connections": [55, 120], "x": 7198, "y": 2144, "type": "city", "assets": [
        {"name": "屋村商場", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    57: {"name": "康城", "line": "TKO", "connections": [55], "x": 7198, "y": 2468, "type": "city", "assets": [
        {"name": "購物商場", "price": 900, "return_percentage": 20, "owner": None},
    ]},
    58: {"name": "寶琳", "line": "TKO", "connections": [120], "x": 7198, "y": 1709, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    ### TML (Tuen Ma Line)
    59: {"name": "屯門", "line": "TML", "connections": [98], "x": 996, "y": 1203, "type": "city", "assets": [
        {"name": "短頸鹿模型店", "price": 250, "return_percentage": 100, "owner": None},
        {"name": "肥寶商場", "price": 400, "return_percentage": 50, "owner": None},
        {"name": "虹橋美食街", "price": 450, "return_percentage": 80, "owner": None},
        {"name": "商場", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "商場", "price": 1000, "return_percentage": 25, "owner": None},
        {"name": "U City", "price": 1500, "return_percentage": 35, "owner": None},
        {"name": "屯門市大形購物中心", "price": 2200, "return_percentage": 25, "owner": None},
        {"name": "廟宇", "price": 600, "return_percentage": 70, "owner": None},
    ]},
    60: {"name": "兆康", "line": "TML", "connections": [513, 98], "x": 996, "y": 772, "type": "city", "assets": [
        {"name": "富泰夜市", "price": 100, "return_percentage": 300, "owner": None},
        {"name": "傳統酒樓", "price": 400, "return_percentage": 15, "owner": None},
        {"name": "兆康商場", "price": 600, "return_percentage": 10, "owner": None},
    ]},
    513: {"name": "機會", "line": "TML", "connections": [60, 61], "x": 996, "y": 589, "type": "event", "assets": []},
    61: {"name": "天水圍", "line": "TML", "connections": [513, 514], "x": 1092, "y": 589, "type": "city", "assets": [
        {"name": "銀町商場", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "平價酒店", "price": 250, "return_percentage": 5, "owner": None},
        {"name": "濕地公園", "price": 250, "return_percentage": 10, "owner": None},
        {"name": "屋村商場", "price": 600, "return_percentage": 30, "owner": None},
        {"name": "屋村商場", "price": 600, "return_percentage": 30, "owner": None},
        {"name": "屋村商場", "price": 600, "return_percentage": 30, "owner": None}
    ]},
    514: {"name": "機會", "line": "TML", "connections": [61, 62], "x": 1304, "y": 589, "type": "event", "assets": []},
    62: {"name": "朗屏", "line": "TML", "connections": [514, 63], "x": 1304, "y": 745, "type": "city", "assets": [
        {"name": "屋村商場", "price": 600, "return_percentage": 30, "owner": None}
    ]},
    63: {"name": "元朗", "line": "TML", "connections": [62, 64], "x": 1304, "y": 901, "type": "city", "assets": [
        {"name": "街頭小食店.", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "街頭小食店.", "price": 100, "return_percentage": 100, "owner": None},
        {"name": "元朗食街.", "price": 250, "return_percentage": 120, "owner": None},
        {"name": "百色廣場.", "price": 1200, "return_percentage": 50, "owner": None},
        {"name": "大華華酒樓", "price": 1400, "return_percentage": 50, "owner": None},
        {"name": "YOLO商場", "price": 1900, "return_percentage": 25, "owner": None},
    ]},
    64: {"name": "錦上路", "line": "TML", "connections": [63, 65], "x": 1304, "y": 1057, "type": "city", "assets": [
        {"name": "市集", "price": 100, "return_percentage": 10, "owner": None},
    ]},
    65: {"name": "荃灣西", "line": "TML", "connections": [64, 99], "x": 1304, "y": 1212, "type": "city", "assets": [
        {"name": "有趣玩具店", "price": 200, "return_percentage": 100, "owner": None},
        {"name": "商場", "price": 400, "return_percentage": 25, "owner": None},
        {"name": "商場", "price": 400, "return_percentage": 25, "owner": None},
        {"name": "商場", "price": 400, "return_percentage": 25, "owner": None},
        {"name": "Danki日式超市", "price": 800, "return_percentage": 75, "owner": None},
        {"name": "百色廣場.", "price": 1550, "return_percentage": 50, "owner": None},
    ]},
    515: {"name": "機會", "line": "TML", "connections": [112, 15], "x": 2752, "y": 1212, "type": "event", "assets": []},
    511: {"name": "機會", "line": "TML", "connections": [103, 66], "x": 3828, "y": 1959, "type": "event", "assets": []},
    66: {"name": "柯士甸", "line": "TML", "connections": [511, 105, 512], "x": 3828, "y": 2350, "type": "city", "assets": [
        {"name": "文昌街食肆", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "文昌街食肆", "price": 100, "return_percentage": 20, "owner": None},
        {"name": "粵劇中心", "price": 1800, "return_percentage": 1, "owner": None},
    ]},
    512: {"name": "機會", "line": "TML", "connections": [66, 23], "x": 3828, "y": 2601, "type": "event", "assets": []},
    67: {"name": "delete", "line": "delete", "connections": [], "x": 0, "y": 0, "type": "delete", "assets": []},
    68: {"name": "紅磡", "line": "TML/ERL", "connections": [23, 516, 82, 83], "x": 4620, "y": 2601, "type": "city", "assets": [
        {"name": "成人進修大學", "price": 1400, "return_percentage": 80, "owner": None},
        {"name": "殯儀館", "price": 1500, "return_percentage": 200, "owner": None},
        {"name": "殯儀館", "price": 1500, "return_percentage": 200, "owner": None},
        {"name": "體育館", "price": 1900, "return_percentage": 25, "owner": None}
    ]},
    516: {"name": "機會", "line": "TML", "connections": [68, 116], "x": 5012, "y": 2601, "type": "event", "assets": []},
    517: {"name": "機會", "line": "TML", "connections": [42, 117], "x": 5012, "y": 1900, "type": "event", "assets": []},
    69: {"name": "土瓜灣", "line": "TML", "connections": [117, 70], "x": 5672, "y": 1900, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    70: {"name": "宋皇臺", "line": "TML", "connections": [69, 71], "x": 5672, "y": 1757, "type": "city", "assets": [
        {"name": "宋皇臺公園", "price": 100, "return_percentage": 1, "owner": None},
        {"name": "九龍城寨", "price": 10, "return_percentage": 100, "owner": None},
    ]},
    71: {"name": "啟德", "line": "TML", "connections": [70, 47], "x": 5672, "y": 1593, "type": "city", "assets": [
        {"name": "郵輪碼頭", "price": 2100, "return_percentage": -20, "owner": None},
    ]},
    518: {"name": "機會", "line": "TML", "connections": [47, 72], "x": 5672, "y": 1232, "type": "event", "assets": []},
    72: {"name": "顯徑", "line": "TML", "connections": [518, 118], "x": 5290, "y": 1232, "type": "city", "assets": [
        {"name": "購物中心", "price": 700, "return_percentage": 20, "owner": None},
    ]},
    519: {"name": "機會", "line": "TML", "connections": [118, 73, 44], "x": 4620, "y": 1232, "type": "event", "assets": []},

    73: {"name": "大圍", "line": "TML/ERL", "connections": [519, 121, 84], "x": 4620, "y": 1115, "type": "city", "assets": [
        {"name": "單車舖", "price": 250, "return_percentage": 10, "owner": None},
        {"name": "單車舖", "price": 250, "return_percentage": 10, "owner": None},
        {"name": "單車舖", "price": 250, "return_percentage": 10, "owner": None},
        {"name": "單車舖", "price": 250, "return_percentage": 10, "owner": None},
        {"name": "單車舖", "price": 250, "return_percentage": 10, "owner": None},
        {"name": "單車舖", "price": 250, "return_percentage": 10, "owner": None}
    ]},
    74: {"name": "車公廟", "line": "TML", "connections": [122, 75], "x": 5656, "y": 1115, "type": "city", "assets": [
        {"name": "睇相舖", "price": 50, "return_percentage": 300, "owner": None},
        {"name": "睇相舖", "price": 50, "return_percentage": 300, "owner": None},
        {"name": "香燭舖", "price": 250, "return_percentage": 100, "owner": None},
        {"name": "香燭舖", "price": 250, "return_percentage": 100, "owner": None},
        {"name": "紙紮鋪", "price": 250, "return_percentage": 100, "owner": None},
        {"name": "紙紮鋪", "price": 250, "return_percentage": 100, "owner": None},
        {"name": "廟宇", "price": 600, "return_percentage": 70, "owner": None},
    ]},
    75: {"name": "沙田圍", "line": "TML", "connections": [74, 76], "x": 5656, "y": 783, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    76: {"name": "第一城", "line": "TML", "connections": [75, 77], "x": 5656, "y": 589, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "購物中心", "price": 1100, "return_percentage": 20, "owner": None},
        {"name": "購物中心", "price": 1100, "return_percentage": 20, "owner": None},
    ]},
    77: {"name": "石門", "line": "TML", "connections": [76, 78], "x": 6011, "y": 589, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    78: {"name": "大水坑", "line": "TML", "connections": [77, 79], "x": 6366, "y": 589, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    79: {"name": "恆安", "line": "TML", "connections": [78, 80], "x": 6722, "y": 589, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    80: {"name": "馬鞍山", "line": "TML", "connections": [79, 81], "x": 7077, "y": 589, "type": "city", "assets": [
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
        {"name": "購物中心", "price": 1100, "return_percentage": 20, "owner": None},
        {"name": "購物中心", "price": 1100, "return_percentage": 20, "owner": None},
    ]},
    81: {"name": "烏溪沙", "line": "TML", "connections": [80], "x": 7432, "y": 589, "type": "city", "assets": [
        {"name": "度假中心", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "度假村", "price": 400, "return_percentage": 25, "owner": None}
    ]},
    ### ERL (East Rail Line)
    82: {"name": "會展", "line": "ERL", "connections": [505, 68], "x": 4620, "y": 3068, "type": "city", "assets": [
        {"name": "展覽中心", "price": 2500, "return_percentage": 5, "owner": None}
    ]},
    83: {"name": "旺角東", "line": "ERL", "connections": [68, 522], "x": 4620, "y": 2313, "type": "city", "assets": [
        {"name": "女人街", "price": 800, "return_percentage": 250, "owner": None},
        {"name": "購物商場", "price": 1900, "return_percentage": 10, "owner": None},

    ]},
    84: {"name": "沙田", "line": "ERL", "connections": [73, 85], "x": 4620, "y": 951, "type": "city", "assets": [
        {"name": "購物中心", "price": 1100, "return_percentage": 20, "owner": None},
        {"name": "購物中心", "price": 1100, "return_percentage": 20, "owner": None},
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    85: {"name": "火炭", "line": "ERL", "connections": [84, 86, 93], "x": 4620, "y": 783, "type": "city", "assets": [
        {"name": "冬菇亭", "price": 250, "return_percentage": 120, "owner": None},
        {"name": "屋村食肆", "price": 250, "return_percentage": 30, "owner": None},
    ]},
    86: {"name": "大學", "line": "ERL", "connections": [85, 87], "x": 4620, "y": 586, "type": "city", "assets": [
        {"name": "良知", "price": 100, "return_percentage": 300, "owner": None},
        {"name": "火魔法訓練場", "price": 100, "return_percentage": 300, "owner": None}
    ]},
    87: {"name": "大埔墟", "line": "ERL", "connections": [86, 88], "x": 4248, "y": 586, "type": "city", "assets": [
        {"name": "火車博物館", "price": 250, "return_percentage": 20, "owner": None},
        {"name": "屋村商場", "price": 400, "return_percentage": 10, "owner": None}
    ]},
    88: {"name": "太和", "line": "ERL", "connections": [87, 89], "x": 3875, "y": 586, "type": "city", "assets": [
        {"name": "屋村商場", "price": 400, "return_percentage": 10, "owner": None}
    ]},
    89: {"name": "粉嶺", "line": "ERL", "connections": [88, 90], "x": 3503, "y": 586, "type": "city", "assets": [
        {"name": "屋村商場", "price": 400, "return_percentage": 10, "owner": None}
    ]},
    90: {"name": "上水", "line": "ERL", "connections": [89, 119, 91], "x": 3130, "y": 586, "type": "city", "assets": [
        {"name": "藥房", "price": 200, "return_percentage": 50, "owner": None},
        {"name": "屋村商場", "price": 400, "return_percentage": 10, "owner": None},
        {"name": "商場", "price": 400, "return_percentage": 30, "owner": None}
    ]},
    91: {"name": "羅湖", "line": "ERL", "connections": [90], "x": 2876, "y": 586, "type": "city", "assets": [
        {"name": "藥房", "price": 200, "return_percentage": 50, "owner": None},
    ]},
    520: {"name": "機會", "line": "ERL", "connections": [119, 92], "x": 3130, "y": 986, "type": "event", "assets": []},
    92: {"name": "落馬洲", "line": "ERL", "connections": [520], "x": 2876, "y": 986, "type": "city", "assets": [
        {"name": "『購物中心』", "price": 300, "return_percentage": -50, "owner": None},
    ]},
    93: {"name": "馬場", "line": "ERL", "connections": [85], "x": 4920, "y": 783, "type": "city", "assets": [
        {"name": "馬場", "price": 2500, "return_percentage": 30, "owner": None},
    ]},
    ### SIL (South Island Line)
    94: {"name": "海洋公園", "line": "SIL", "connections": [124, 95], "x": 3958, "y": 3712, "type": "city", "assets": [
        {"name": "主題公園", "price": 2100, "return_percentage": 2, "owner": None},
        {"name": "酒店", "price": 1200, "return_percentage": 10, "owner": None}
    ]},
    95: {"name": "黃竹坑", "line": "SIL", "connections": [94, 113], "x": 3744, "y": 3712, "type": "city", "assets": [
        {"name": "製紙廠", "price": 500, "return_percentage": 3, "owner": None},
        {"name": "製磚廠", "price": 500, "return_percentage": 3, "owner": None},
        {"name": "食品廠", "price": 500, "return_percentage": 3, "owner": None},
        {"name": "禽畜訓練中心", "price": 500, "return_percentage": -10, "owner": None}
    ]},
    521: {"name": "機會", "line": "SIL", "connections": [113, 96], "x": 3094, "y": 3712, "type": "event", "assets": []},
    96: {"name": "利東", "line": "SIL", "connections": [521, 97], "x": 3094, "y": 3892, "type": "city", "assets": [
        {"name": "屋村商場", "price": 400, "return_percentage": 10, "owner": None},
    ]},
    97: {"name": "海怡半島", "line": "SIL", "connections": [96], "x": 2728, "y": 3892, "type": "city", "assets": [
        {"name": "『購物中心』", "price": 300, "return_percentage": 10, "owner": None},
    ]},
    ### New Question Stations (starting from 98)
    ### New Question Stations (starting from 98)
    # 1 between 屯門 (59) and 兆康 (60)
    98: {"name": "問號站1", "line": "TML", "connections": [59, 60], "x": 996, "y": 987, "type": "question", "assets": []},  # Midpoint: (996, (1203+772)/2 = 987)

    # 4 between 荃灣西 (65) and 機會 (515)
    # Distance: x=1304 to 2752 (1448 units), y=1212 (no change), split into 5 segments (289.6 each)
    99: {"name": "問號站2", "line": "TML", "connections": [65, 110], "x": 1593, "y": 1212, "type": "question", "assets": []},  # 1304 + 289.6
    110: {"name": "問號站3", "line": "TML", "connections": [99, 111], "x": 1883, "y": 1212, "type": "question", "assets": []},  # 1593 + 289.6
    111: {"name": "問號站4", "line": "TML", "connections": [110, 112], "x": 2172, "y": 1212, "type": "question", "assets": []},  # 1883 + 289.6
    112: {"name": "問號站5", "line": "TML", "connections": [111, 515], "x": 2462, "y": 1212, "type": "question", "assets": []},  # 2172 + 289.6

    # Even out 美孚 (15) to 深水埗 (18), 1 between 荔枝角 (16) and 長沙灣 (17)
    100: {"name": "問號站6", "line": "TSW", "connections": [16, 17], "x": 3276, "y": 1430, "type": "question", "assets": []},  # Adjusted: 3102 + 175 (midpoint shifted)

    # 1 between 美孚 (15) and 南昌 (3)
    101: {"name": "問號站7", "line": "TML", "connections": [15, 3], "x": 2752, "y": 1694, "type": "question", "assets": []},  # Midpoint: (2752, (1430+1959)/2 = 1694)

    # 2 between 南昌 (3) and 機會 (511)
    # Distance: (2752,1959) to (3828,1959) (1076 units), split into 3 segments (358.7 each)
    102: {"name": "問號站8", "line": "TCL", "connections": [3, 103], "x": 3110, "y": 1959, "type": "question", "assets": []},  # 2752 + 358
    103: {"name": "問號站9", "line": "TCL", "connections": [102, 511], "x": 3469, "y": 1959, "type": "question", "assets": []},  # 3110 + 359

    # 2 between 九龍 (1) and 柯士甸 (66)
    # Distance: (2752,2350) to (3828,2350) (1076 units), split into 3 (358.7 each)
    104: {"name": "問號站10", "line": "TML", "connections": [1, 105], "x": 3110, "y": 2350, "type": "question", "assets": []},  # 2752 + 358
    105: {"name": "問號站11", "line": "TML", "connections": [104, 66], "x": 3469, "y": 2350, "type": "question", "assets": []},  # 3110 + 359

    # 2 between 九龍 (1) and 西營盤 (28)
    # No direct connection exists, assume via a new path (e.g., south then east)
    # Path: (2752,2350) to (2744,3304) (y diff: 954, x diff: -8), split y into 3 (318 each)
    106: {"name": "問號站12", "line": "ISL", "connections": [1, 107], "x": 2752, "y": 2588, "type": "question", "assets": []},  # 2350 + 318
    107: {"name": "問號站13", "line": "ISL", "connections": [106, 500], "x": 2752, "y": 2826, "type": "question", "assets": []},  # 2668 + 318, slight x adjust

    # 2 between 香港 (0) and 機會 (500) to the west
    # Distance: (3516,3063) to (2752,3063) (764 units), split into 3 (254.7 each)
    108: {"name": "問號站14", "line": "TCL", "connections": [0, 109], "x": 3261, "y": 3063, "type": "question", "assets": []},  # 3516 - 255
    109: {"name": "問號站15", "line": "TCL", "connections": [108, 500], "x": 3006, "y": 3063, "type": "question", "assets": []},  # 3261 - 255
    
    # Crossing
    522: {"name": "機會", "line": "ERL", "connections": [114, 42, 115, 83], "x": 4620, "y": 2026, "type": "event", "assets": []},
    
# 20:19
    113: {"name": "問號站16", "line": "SIL", "connections": [95, 521], "x": 3419, "y": 3712, "type": "question", "assets": []},  # Midpoint: (3744+3094)/2 = 3419
    114: {"name": "問號站17", "line": "TSW", "connections": [21, 522], "x": 4289, "y": 2026, "type": "question", "assets": []},  # Midpoint: (3958+4620)/2 = 4289

    115: {"name": "問號站18", "line": "KTL", "connections": [44, 522], "x": 4620, "y": 1728, "type": "question", "assets": []},  # Midpoint: (1430+2026)/2 = 1728
    
    116: {"name": "問號站19", "line": "TML", "connections": [42, 516], "x": 5012, "y": 2313, "type": "question", "assets": []},  # Midpoint: (2026+2601)/2 = 2313
    
    117: {"name": "問號站20", "line": "TML", "connections": [517, 69], "x": 5342, "y": 1900, "type": "question", "assets": []},  # Midpoint: (5012+5672)/2 = 5342
    118: {"name": "問號站21", "line": "TML", "connections": [519, 72], "x": 4955, "y": 1232, "type": "question", "assets": []},  # Midpoint: (4620+5290)/2 = 4955
    119: {"name": "問號站22", "line": "ERL", "connections": [520, 90], "x": 3130, "y": 786, "type": "question", "assets": []},  # Midpoint: (986+586)/2 = 786
    120: {"name": "問號站23", "line": "TKO", "connections": [56, 58], "x": 7198, "y": 1926, "type": "question", "assets": []},  # Midpoint: (2050+1709)/2 = 1879
    121: {"name": "問號站24", "line": "TML", "connections": [73, 122], "x": 4965, "y": 1115, "type": "question", "assets": []},  # 4620 + 345
    122: {"name": "問號站25", "line": "TML", "connections": [121, 74], "x": 5310, "y": 1115, "type": "question", "assets": []},  # 4965 + 345
    123: {"name": "問號站26", "line": "TCL", "connections": [507, 506], "x": 6166, "y": 2660, "type": "question", "assets": []},  # 2361 + 299
    124: {"name": "問號站27", "line": "SIL", "connections": [24, 94], "x": 3958, "y": 3508, "type": "question", "assets": []},  # 3304 + 204
}