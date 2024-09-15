punctuation = ["!", "?", "…", ",", "."]  # @是SP停顿
punctuation.append("-")
pu_symbols = punctuation + ["SP", "SP2", "SP3", "UNK"]
pad = "_"

c = [
    "AA",
    "EE",
    "OO",
    "b",
    "c",
    "ch",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "sh",
    "t",
    "w",
    "x",
    "y",
    "z",
    "zh",
]
v = [
    "E1",
    "En1",
    "a1",
    "ai1",
    "an1",
    "ang1",
    "ao1",
    "e1",
    "ei1",
    "en1",
    "eng1",
    "er1",
    "i1",
    "i01",
    "ia1",
    "ian1",
    "iang1",
    "iao1",
    "ie1",
    "in1",
    "ing1",
    "iong1",
    "ir1",
    "iu1",
    "o1",
    "ong1",
    "ou1",
    "u1",
    "ua1",
    "uai1",
    "uan1",
    "uang1",
    "ui1",
    "un1",
    "uo1",
    "v1",
    "van1",
    "ve1",
    "vn1",
    "E2",
    "En2",
    "a2",
    "ai2",
    "an2",
    "ang2",
    "ao2",
    "e2",
    "ei2",
    "en2",
    "eng2",
    "er2",
    "i2",
    "i02",
    "ia2",
    "ian2",
    "iang2",
    "iao2",
    "ie2",
    "in2",
    "ing2",
    "iong2",
    "ir2",
    "iu2",
    "o2",
    "ong2",
    "ou2",
    "u2",
    "ua2",
    "uai2",
    "uan2",
    "uang2",
    "ui2",
    "un2",
    "uo2",
    "v2",
    "van2",
    "ve2",
    "vn2",
    "E3",
    "En3",
    "a3",
    "ai3",
    "an3",
    "ang3",
    "ao3",
    "e3",
    "ei3",
    "en3",
    "eng3",
    "er3",
    "i3",
    "i03",
    "ia3",
    "ian3",
    "iang3",
    "iao3",
    "ie3",
    "in3",
    "ing3",
    "iong3",
    "ir3",
    "iu3",
    "o3",
    "ong3",
    "ou3",
    "u3",
    "ua3",
    "uai3",
    "uan3",
    "uang3",
    "ui3",
    "un3",
    "uo3",
    "v3",
    "van3",
    "ve3",
    "vn3",
    "E4",
    "En4",
    "a4",
    "ai4",
    "an4",
    "ang4",
    "ao4",
    "e4",
    "ei4",
    "en4",
    "eng4",
    "er4",
    "i4",
    "i04",
    "ia4",
    "ian4",
    "iang4",
    "iao4",
    "ie4",
    "in4",
    "ing4",
    "iong4",
    "ir4",
    "iu4",
    "o4",
    "ong4",
    "ou4",
    "u4",
    "ua4",
    "uai4",
    "uan4",
    "uang4",
    "ui4",
    "un4",
    "uo4",
    "v4",
    "van4",
    "ve4",
    "vn4",
    "E5",
    "En5",
    "a5",
    "ai5",
    "an5",
    "ang5",
    "ao5",
    "e5",
    "ei5",
    "en5",
    "eng5",
    "er5",
    "i5",
    "i05",
    "ia5",
    "ian5",
    "iang5",
    "iao5",
    "ie5",
    "in5",
    "ing5",
    "iong5",
    "ir5",
    "iu5",
    "o5",
    "ong5",
    "ou5",
    "u5",
    "ua5",
    "uai5",
    "uan5",
    "uang5",
    "ui5",
    "un5",
    "uo5",
    "v5",
    "van5",
    "ve5",
    "vn5",
]

v_without_tone = [
    "E",
    "En",
    "a",
    "ai",
    "an",
    "ang",
    "ao",
    "e",
    "ei",
    "en",
    "eng",
    "er",
    "i",
    "i0",
    "ia",
    "ian",
    "iang",
    "iao",
    "ie",
    "in",
    "ing",
    "iong",
    "ir",
    "iu",
    "o",
    "ong",
    "ou",
    "u",
    "ua",
    "uai",
    "uan",
    "uang",
    "ui",
    "un",
    "uo",
    "v",
    "van",
    "ve",
    "vn",
]

# japanese
ja_symbols = [
    "I",
    "N",
    "U",
    "a",
    "b",
    "by",
    "ch",
    "cl",
    "d",
    "dy",
    "e",
    "f",
    "g",
    "gy",
    "h",
    "hy",
    "i",
    "j",
    "k",
    "ky",
    "m",
    "my",
    "n",
    "ny",
    "o",
    "p",
    "py",
    "r",
    "ry",
    "s",
    "sh",
    "t",
    "ts",
    "u",
    "v",
    "w",
    "y",
    "z",
    ###楼下2个留到后面加
    # "[", #上升调型
    # "]", #下降调型
    # "$", #结束符
    # "^", #开始符
]

arpa = {
    "AH0",
    "S",
    "AH1",
    "EY2",
    "AE2",
    "EH0",
    "OW2",
    "UH0",
    "NG",
    "B",
    "G",
    "AY0",
    "M",
    "AA0",
    "F",
    "AO0",
    "ER2",
    "UH1",
    "IY1",
    "AH2",
    "DH",
    "IY0",
    "EY1",
    "IH0",
    "K",
    "N",
    "W",
    "IY2",
    "T",
    "AA1",
    "ER1",
    "EH2",
    "OY0",
    "UH2",
    "UW1",
    "Z",
    "AW2",
    "AW1",
    "V",
    "UW2",
    "AA2",
    "ER",
    "AW0",
    "UW0",
    "R",
    "OW1",
    "EH1",
    "ZH",
    "AE0",
    "IH2",
    "IH",
    "Y",
    "JH",
    "P",
    "AY1",
    "EY0",
    "OY2",
    "TH",
    "HH",
    "D",
    "ER0",
    "CH",
    "AO1",
    "AE1",
    "AO2",
    "OY1",
    "AY2",
    "IH1",
    "OW0",
    "L",
    "SH",
}

ko_symbols = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅓㅗㅜㅡㅣㅐㅔ空停"

yue_symbols = {
    "Yeot3",
    "Yip1",
    "Yyu3",
    "Yeng4",
    "Yut5",
    "Yaan5",
    "Ym5",
    "Yaan6",
    "Yang1",
    "Yun4",
    "Yon2",
    "Yui5",
    "Yun2",
    "Yat3",
    "Ye",
    "Yeot1",
    "Yoeng5",
    "Yoek2",
    "Yam2",
    "Yeon6",
    "Yu6",
    "Yiu3",
    "Yaang6",
    "Yp5",
    "Yai4",
    "Yoek4",
    "Yit6",
    "Yam5",
    "Yoeng6",
    "Yg1",
    "Yk3",
    "Yoe4",
    "Yam3",
    "Yc",
    "Yyu4",
    "Yyut1",
    "Yiu4",
    "Ying3",
    "Yip3",
    "Yaap3",
    "Yau3",
    "Yan4",
    "Yau1",
    "Yap4",
    "Yk6",
    "Yok3",
    "Yai1",
    "Yeot6",
    "Yan2",
    "Yoek6",
    "Yt1",
    "Yoi1",
    "Yit5",
    "Yn4",
    "Yaau3",
    "Yau4",
    "Yuk6",
    "Ys",
    "Yuk",
    "Yin6",
    "Yung6",
    "Ya",
    "You",
    "Yaai5",
    "Yau5",
    "Yoi3",
    "Yaak3",
    "Yaat3",
    "Ying2",
    "Yok5",
    "Yeng2",
    "Yyut3",
    "Yam1",
    "Yip5",
    "You1",
    "Yam6",
    "Yaa5",
    "Yi6",
    "Yek4",
    "Yyu2",
    "Yuk5",
    "Yaam1",
    "Yang2",
    "Yai",
    "Yiu6",
    "Yin4",
    "Yok4",
    "Yot3",
    "Yui2",
    "Yeoi5",
    "Yyun6",
    "Yyu5",
    "Yoi5",
    "Yeot2",
    "Yim4",
    "Yeoi2",
    "Yaan1",
    "Yang6",
    "Yong1",
    "Yaang4",
    "Yung5",
    "Yeon1",
    "Yin2",
    "Ya3",
    "Yaang3",
    "Yg",
    "Yk2",
    "Yaau5",
    "Yut1",
    "Yt5",
    "Yip4",
    "Yung4",
    "Yj",
    "Yong3",
    "Ya1",
    "Yg6",
    "Yaau6",
    "Yit3",
    "Yun3",
    "Ying1",
    "Yn2",
    "Yg4",
    "Yl",
    "Yp3",
    "Yn3",
    "Yak1",
    "Yang5",
    "Yoe6",
    "You2",
    "Yap2",
    "Yak2",
    "Yt3",
    "Yot5",
    "Yim2",
    "Yi1",
    "Yn6",
    "Yaat5",
    "Yaam3",
    "Yoek5",
    "Ye3",
    "Yeon4",
    "Yaa2",
    "Yu3",
    "Yim6",
    "Ym",
    "Yoe3",
    "Yaai2",
    "Ym2",
    "Ya6",
    "Yeng6",
    "Yik4",
    "Yot4",
    "Yaai4",
    "Yyun3",
    "Yu1",
    "Yoeng1",
    "Yaap2",
    "Yuk3",
    "Yoek3",
    "Yeng5",
    "Yeoi1",
    "Yiu2",
    "Yok1",
    "Yo1",
    "Yoek1",
    "Yoeng2",
    "Yeon5",
    "Yiu1",
    "Yoeng4",
    "Yuk2",
    "Yat4",
    "Yg5",
    "Yut4",
    "Yan6",
    "Yin3",
    "Yaa6",
    "Yap1",
    "Yg2",
    "Yoe5",
    "Yt4",
    "Ya5",
    "Yo4",
    "Yyu1",
    "Yak3",
    "Yeon2",
    "Yong4",
    "Ym1",
    "Ye2",
    "Yaang5",
    "Yoi2",
    "Yeng3",
    "Yn",
    "Yyut4",
    "Yau",
    "Yaak2",
    "Yaan4",
    "Yek2",
    "Yin1",
    "Yi5",
    "Yoe2",
    "Yei5",
    "Yaat6",
    "Yak5",
    "Yp6",
    "Yok6",
    "Yei2",
    "Yaap1",
    "Yyut5",
    "Yi4",
    "Yim1",
    "Yk5",
    "Ye4",
    "Yok2",
    "Yaam6",
    "Yat2",
    "Yon6",
    "Yei3",
    "Yyu6",
    "Yeot5",
    "Yk4",
    "Yai6",
    "Yd",
    "Yg3",
    "Yei6",
    "Yau2",
    "Yok",
    "Yau6",
    "Yung3",
    "Yim5",
    "Yut6",
    "Yit1",
    "Yon3",
    "Yat1",
    "Yaam2",
    "Yyut2",
    "Yui6",
    "Yt2",
    "Yek6",
    "Yt",
    "Ye6",
    "Yang3",
    "Ying6",
    "Yaau1",
    "Yeon3",
    "Yng",
    "Yh",
    "Yang4",
    "Ying5",
    "Yaap6",
    "Yoeng3",
    "Yyun4",
    "You3",
    "Yan5",
    "Yat5",
    "Yot1",
    "Yun1",
    "Yi3",
    "Yaa1",
    "Yaap4",
    "You6",
    "Yaang2",
    "Yaap5",
    "Yaa3",
    "Yaak6",
    "Yeng1",
    "Yaak1",
    "Yo5",
    "Yoi4",
    "Yam4",
    "Yik1",
    "Ye1",
    "Yai5",
    "Yung1",
    "Yp2",
    "Yui4",
    "Yaak4",
    "Yung2",
    "Yak4",
    "Yaat4",
    "Yeoi4",
    "Yut2",
    "Yin5",
    "Yaau4",
    "Yap6",
    "Yb",
    "Yaam4",
    "Yw",
    "Yut3",
    "Yong2",
    "Yt6",
    "Yaai6",
    "Yap5",
    "Yik5",
    "Yun6",
    "Yaam5",
    "Yun5",
    "Yik3",
    "Ya2",
    "Yyut6",
    "Yon4",
    "Yk1",
    "Yit4",
    "Yak6",
    "Yaan2",
    "Yuk1",
    "Yai2",
    "Yik2",
    "Yaat2",
    "Yo3",
    "Ykw",
    "Yn5",
    "Yaa",
    "Ye5",
    "Yu4",
    "Yei1",
    "Yai3",
    "Yyun5",
    "Yip2",
    "Yaau2",
    "Yiu5",
    "Ym4",
    "Yeoi6",
    "Yk",
    "Ym6",
    "Yoe1",
    "Yeoi3",
    "Yon",
    "Yuk4",
    "Yaai3",
    "Yaa4",
    "Yot6",
    "Yaang1",
    "Yei4",
    "Yek1",
    "Yo",
    "Yp",
    "Yo6",
    "Yp4",
    "Yan3",
    "Yoi",
    "Yap3",
    "Yek3",
    "Yim3",
    "Yz",
    "Yot2",
    "Yoi6",
    "Yit2",
    "Yu5",
    "Yaan3",
    "Yan1",
    "Yon5",
    "Yp1",
    "Yong5",
    "Ygw",
    "Yak",
    "Yat6",
    "Ying4",
    "Yu2",
    "Yf",
    "Ya4",
    "Yon1",
    "You4",
    "Yik6",
    "Yui1",
    "Yaat1",
    "Yeot4",
    "Yi2",
    "Yaai1",
    "Yek5",
    "Ym3",
    "Yong6",
    "You5",
    "Yyun1",
    "Yn1",
    "Yo2",
    "Yip6",
    "Yui3",
    "Yaak5",
    "Yyun2",
}

symbols = [pad] + c + v + ja_symbols + pu_symbols + list(arpa)
symbols = sorted(set(symbols))
symbols += ["[", "]"]  ##日文新增上升下降调型
symbols += sorted(list(ko_symbols))
symbols += sorted(
    list(yue_symbols)
)  ##新加的yue统一摆在后头#已查过开头加Y后没有重复，韩文显然不会重复
