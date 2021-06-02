def bellman_ford(graph, source):
    d = {}
    pre = {}

    max = 99999
    for v in graph:
        d[v] = max  #赋值为无穷完成初始化
        pre[v] = None#赋值前驱节点为空 
     
    d[source] = 0
 
    for i in range(len( graph ) - 1):    #如果不存在负权环,则在nodenum-1次循环后最短路必求出来
        for u in graph:                  #松弛每条边
            for v in graph[u]:
                if d[v] > graph[u][v] + d[u]:
                    d[v] = graph[u][v] + d[u]
                    pre[v] = u    #完成松弛操作，p为前驱节点
    return d, pre                
def mistake(graph,d):                    #判断是否存在负权环路
    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                return -1
 

def Route_print(pre,graph,a,d):
    def print_again(k,begin):
        if pre[k]==None:
            return
        if pre[k]==begin:
           # print("->{}".format(k),end="")
            return
        print_again(pre[k],begin)
    #    print(k,pre[k])
        print_again(k,pre[k])
    for i in graph:
        if i==a:
            print('')
            #print("\n点{}是起点".format(a))  
    for i in graph:
        if pre[i]==None:
            continue
     #   print("\n最短路径：{}".format(a), end="")
        print_again(i, a)
      #  print("。最短距离:{}".format(d[i]))
    print('')
    
def single_get_path(pre,end,a):
    path = []
    node = end
    if pre[end] == None:
        return []
    while(node != a):
        path.append(int(node))
        node = pre[node]
    path.append(int(a))
    path.reverse()
    return path
if __name__=='__main__':    
    graph={
           '0':{'1':1255.7,'14':1080.9},
            '1':{'0':1255.7,'2':828.8,'18':132.9},
            '2':{'1':828.8,'3':416.6,'19':118.9},
            '3':{'2':416.6,'4':562.2,'20':111.5},
            '4':{'3':562.2,'5':991.7},
            '5':{'4':991.7,'6':138,'17':1519.4,'236':189},
            '6':{'40':532.8,'5':138,'235':153.1,'236':189,'247':79.8,'248':123.3,'249':271,'7':594.1,'251':340,'22':378.2},
            '7':{'8':107.2,'246':75.7,'251':254.3,'6':594.1},
            
            
            '8':{'7':161,'9':250.3,'24':114,'166':135.1,'235':538},
            '9':{'8':232.3,'10':206.7},
            '10':{'9':206.7,'11':672,'19':501.1,'143':77.5,'240':296.5},
            '11':{'10':672,'12':581.5,'43':125,'117':128.4,'11':195.2},
            '12':{'11':581.5,'13':223.7,'44':254.2,'257':106,'258':126.1,'262':389.9},
            '13':{'12':223.7,'14':331.2,'42':476.7,'37':366,'268':170.8},
            '14':{'13':331.2,'15':1247.3,'0':1080.9},
            '15':{'14':1247.3,'16':1194},
            '16':{'15':1194,'17':1522.6,'36':214},
            '17':{'16':1522.6,'5':1519.4},
            '18':{'254':352.6,'1':132.9,'19':812.4,'43':349.6},
            '19':{'2':132.9,'18':812.4,'10':501.1,'20':390.3,'254':459.8,'240':205.2},
            '20':{'3':111.5,'21':476,'19':390.3,'242':267.2,'239':215.8},
            '21':{'20':476,'22':533,'253':56.1,'245':265.2},
            '22':{'6':378.2,'21':533,'245':268.1,'247':298.7},
            '23':{'27':314,'24':1166,'44':152.3,'186':126.3,'134':23.1},
            '24':{'8':114,'25':221.4,'166':21.8,'200':551},
            '25':{'26':166.4,'24':221.4,'167':92,'231':89.1},
            '26':{'25':166.4,'28':1113,'30':290,'31':533.2,'174':163.4,'224':218,'229':221},
            '27':{'28':76.9,'23':314,'44':162.2},
            '28':{'27':76.9,'26':1113,'29':308.1,'197':65.1,'213':64},
            '29':{'28':308.1,'30':892,'33':143.6,'205':185,'208':99.5,'217':166.1,'199':787},
            '30':{'26':290,'32':615,'35':194.2,'29':892,'215':134.1,'223':132.1,'225':301},
            #截止
            '31':{'32':269,'26':533.2,'40':359,'224':315,'233':192},
            '32':{'31':269,'39':413.1,'30':615},
            '33':{'29':143.6,'34':169},
            '34':{'33':169,'38':281.6,'36':819.4,'217':146.1,'219':293.2,'285':84.1},
            '35':{'30':194.2,'36':181},
            '36':{'16':214,'34':819.4,'35':181,'39':662.7,'222':178,'223':246},
            '37':{'38':674.6,'13':366,'277':229.1,'280':543.8},
            '38':{'34':281.6,'37':674.6,'280':130.7,'283':65.3},
            '39':{'32':413.1,'36':662.7,'41':623.8,'227':322},
            '40':{'6':532.8,'31':359,'41':776.9,'233':167,'238':216.6},
            '41':{'39':623.8,'40':776.9},
            '42':{'13':476.7,'43':600.4,'267':183},
            '43':{'11':125,'18':349.6,'42':600.5},
            '44':{'12':254.2,'27':162.2,'23':152.3},
            '45':{},
            '46':{},
            '47':{},
            '48':{},
            '49':{},
            '50':{},
            '51':{},
            '52':{},
            '53':{},
            '54':{},
            '55':{},
            '56':{},
            '57':{},
            '58':{},
            '59':{},
            '60':{},
            '61':{},
            '62':{},
            '63':{},
            '64':{},
            '65':{},
            '66':{},
            '67':{},
            '68':{},
            '69':{},
            '70':{},
            '71':{},
            '72':{},
            '73':{},
            '74':{},
            '75':{},
            '76':{},
            '77':{},
            '78':{},
            '79':{},
            '80':{},
            '81':{},
            '82':{},
            '83':{},
            '84':{},
            '85':{},
            '86':{},
            '87':{},
            '88':{},
            '89':{},
            '90':{},
            '91':{},
            '92':{},
            '93':{},
            '94':{},
            '95':{},
            '96':{},
            '97':{},
            '98':{},
            '99':{},
            '100':{},
            '101':{'102':23.3},
            '102':{'101':23.3,'103':53.3,'112':53.3,'110':133.9},
            '103':{'102':53.3,'104':51,'108':18},
            '104':{'103':51,'105':74},
            '105':{'104':74,'106':38.1},
            '106':{'105':38.1},
            '107':{},
            '108':{'103':18,'109':132},
            '109':{'108':132,'122':20.1,'110':40},
            '110':{'109':40,'111':110,'102':133.9},
            '111':{'110':110,'114':32,'115':40},
            '112':{'102':53.3,'113':41.2},
            '113':{'112':41.2,'114':45.9},
            '114':{'111':32,'113':45.9},
            '115':{'111':40,'116':82,'131':239},
            '116':{'115':82,'117':74,'118':146.5},
            '117':{'116':74,'119':156,'11':128.4},
            '118':{'116':146.5,'119':50.9},
            '119':{'117':156,'118':50.9,'132':86},
            '120':{'122':48,'121':56.1,'135':35.5},
            '121':{'120':56.1,'124':76.1,'134':259,'135':52.1,'182':134.2,'24':884},
            '122':{'109':20.1,'120':48,'123':72.1},
            '123':{'122':72.1,'125':106,'124':96},
            '124':{'121':76.1,'123':96,'125':143.8,'180':141.4,'181':143.3,'200':257.1},
            '125':{'123':106,'124':143.8,'126':34},
            '126':{'125':34,'127':86},
            '127':{'126':86,'128':66.1},
            '128':{'127':66.1,'129':60},
            '129':{'131':27.2,'128':60},
            '130':{'131':32.4,'132':125,'136':77.2},
            '131':{'115':239,'129':27.2,'130':32.4},
            '132':{'119':86,'130':125,'10':302.1,'136':48},
            '133':{'105':32,'134':118},
            '134':{'133':118,'121':259,'23':23.1},
            '135':{'120':35.5,'121':52.1},
            '136':{'130':77.2,'137':28,'132':48},
            '137':{'136':28,'138':19},
            '138':{'137':19,'139':54},
            '139':{'138':54,'140':43.3},
            '140':{'141':43.9,'139':43.3},
            '141':{'140':43.9,'142':61.7},
            '142':{'141':61.7,'153':99.1},
            '144':{'153':22.2,'145':68.4,'152':31.1},
            '143':{'10':77.5},
            '145':{'144':68.4,'152':87.1,'154':34,'146':69},
            '146':{'147':60,'145':69,'161':40},
            '147':{'148':28,'150':17,'146':60},
            '148':{'147':28,'160':109.2,'149':30},
            '149':{'148':30,'151':46.1},
            '150':{'147':17,'151':27},
            '151':{'150':27,'152':55,'149':46.1},
            '152':{'151':55,'153':24,'145':87.1,'144':31.1},
            '153':{'152':24,'144':22.2,'142':99.1},
            '154':{'145':34,'155':18.4,'162':108},
            '155':{'154':18.4,'156':102},
            '156':{'155':102,'157':170,'163':124.3},
            '157':{'156':170,'163':46.7},
            '158':{},
            '159':{'128':44,'161':51,'160':49.6},
            '160':{'159':49.6,'129':121,'148':109.2},
            '161':{'159':51,'146':40,'162':35.1},
            '162':{'161':35.1,'154':108},
            '163':{'157':46.7,'164':65,'156':124.3},
            '164':{'163':65,'165':155,'176':142.1},
            '165':{'164':155,'166':96,'168':103},
            '166':{'165':96,'167':110,'8':150.1,'24':21.8},
            '167':{'166':110,'168':99.2,'25':92,'232':42.2},
            '168':{'167':99.2,'169':194,'165':103},
            '169':{'168':194,'171':88.1},
            '170':{'171':64.3,'172':62.4},
            '171':{'170':64.3,'169':88.1,'174':77.1},
            '172':{'170':62.4,'175':81.1,'173':66},
            '173':{'172':66,'174':121,'178':156.1,'214':63.4},
            '174':{'173':121,'171':77.1,'26':163.4,'214':58.1},
            '175':{'176':292,'172':81.1},
            '176':{'177':75,'175':292,'164':142.1},
            '177':{'178':357},
            '178':{'177':357,'173':156.1},
            '179':{},
            '180':{'181':37.6,'124':141.4},
            '181':{'180':37.6,'124':143.3,'182':139},
            '182':{'181':139,'121':134.2,'189':28.2},
            '183':{'184':56.6,'187':36.8},
            '184':{'183':56.6,'185':20.5},
            '185':{'184':20.5,'186':65},
            '186':{'185':65,'23':126.3,'28':263.3,'275':105},
            '187':{'183':36.8,'188':42.4,'192':74.8,'191':111.8},
            '188':{'187':42.4,'189':77},
            '189':{'188':77,'182':28.2,'190':78.2},
            '190':{'189':78.2,'191':43.2,'196':186.2},
            '191':{'190':43.2,'192':93},
            '192':{'191':93,'187':74.8},
            '193':{'196':33,'194':42.1,'199':68.3,'201':107.8},
            '194':{'193':42.1,'195':64.4,'199':110,'210':145},
            '195':{'194':64.4,'196':110.9,'198':144.1},
            '196':{'195':110.9,'190':186.2,'193':33},
            '197':{'198':55,'28':65.1,'210':14.9},
            '198':{'197':55,'195':144.1},
            '199':{'193':68.3,'201':102.4,'194':110,'202':160.7,'26':787},
            '200':{'124':257.1,'24':551},
            '201':{'199':102.4,'193':107.8,'209':68,'202':74.2,'193':107.8},
            '202':{'209':32.1,'193':62.8,'201':74.2,'199':106.7},
            '203':{},
            '204':{'205':64},
            '205':{'204':64,'29':185},
            '206':{'207':61.1},
            '207':{'206':61.1,'208':62.8},
            '208':{'207':62.8,'213':142.7,'29':99.5},
            '209':{},
            '210':{'211':58.5,'28':71,'194':145},
            '211':{'210':58.5,'212':31.4,'213':34.2},
            '212':{'211':31.4},
            '213':{'28':67.4,'211':34.2,'208':142.7},
            '214':{'173':63.4,'174':58.1,'215':265},
            '215':{'214':165,'30':134.1,'220':110},
            '216':{'178':276.1,'218':212,'220':104},
            '217':{'29':166.1,'34':146.1},
            '218':{'205':147,'216':212,'219':334},
            '219':{'218':334,'34':293.2,'222':348.1},
            '220':{'216':104,'221':128.5,'215':110},
            '221':{'220':128.5,'223':174,'222':235},
            '222':{'221':235,'219':348.1,'36':178},
            '223':{'221':174,'30':132.1,'36':246},
            '224':{'26':218,'31':315,'228':147.1},
            '225':{'228':118,'227':407,'30':301},#少点
            '226':{},
            '227':{'225':407,'39':322},
            '228':{'224':147.1,'225':118},
            '229':{'30':112,'26':221},
            '230':{},#少点
            '231':{'25':89.1},
            '232':{'167':42.2,'166':68.2,'234':612},
            '233':{'31':192,'40':167},
            '234':{'237':105.9,'236':149.2,'235':204.8,'232':612},
            '235':{'6':153.1,'234':204.8,'8':548.4,'236':280.8},
            '236':{'235':280.8,'6':189,'234':149.2,'5':189,'238':127.8},
            '237':{'234':105.9,'238':159},
            '238':{'237':159,'40':216.6,'236':127.8},
            '239':{'20':215.8,'243':227,'253':260,'241':287},
            '240':{'19':205.2,'243':153.1,'10':296.5},
            '241':{'245':271,'244':116,'242':226,'239':287},
            '242':{'20':267.2,'241':226},
            '243':{'240':153.1,'239':227},
            '244':{},
            '245':{'241':271,'21':265.2,'22':268.1},
            '246':{'7':75.7},
            '247':{'248':70.3,'6':79.8,'22':298.7},
            '248':{'247':70.3,'6':123.2},
            '249':{'6':271,'251':69.1},
            '250':{},
            '251':{'249':69.1,'252':91,'7':254.3,'6':340},
            '252':{'252':91},
            '253':{'21':56.1},
            '254':{'256':44.2,'19':489.8,'18':352.6},
            '255':{'256':124.1,'240':449.1},
            '256':{'255':124.1,'254':44.2},
            '257':{'258':70.5,'12':106},
            '258':{'257':70.5,'12':126.1,'259':107},
            '259':{'258':107,'260':71,'265':101.1,'273':140.9},
            '260':{'259':71,'261':72},
            '261':{'260':72,'274':67,'262':176},
            '262':{'11':195.2,'12':389.8},
            '263':{'264':155},
            '264':{'263':155,'11':110.3},
            '265':{'259':101.1,'266':72},
            '266':{'265':72,'267':61.4},
            '267':{'266':61.4,'42':183,'268':79.6},
            '268':{'267':79.6,'13':170.8,'269':120},
            '269':{'268':120,'270':163.1},
            '270':{'269':163.1,'271':62.2},
            '271':{'270':62.2,'272':83.5},
            '272':{'271':83.5},
            '273':{'259':140.9,'274':86},
            '274':{'273':86,'261':67},
            '275':{'276':44,'186':105,'28':158.7},
            '276':{'275':44},
            '277':{'278':53.5,'275':417.7,'37':229.1},
            '278':{'277':53.5},
            '279':{'208':50},
            '280':{'37':543.8,'281':28.1,'38':130.7},
            '281':{'280':28.1},
            '282':{},
            '283':{'284':28,'38':65.3,'285':132.2},
            '284':{'283':28},
            '285':{'283':132.2,'34':84.1,'286':45},
            '286':{'285':45}
            }

    a=input("请输入起点：")
    end=input('请输入终点：')
    d,pre = bellman_ford(graph,a)
    if mistake(graph,d)==-1:
        print("图中存在负权环")
    else:
        Route_print(pre,graph,a,d)
        path = single_get_path(pre,end,a)
    print(path)

