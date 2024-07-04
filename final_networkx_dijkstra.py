import networkx as nx
import matplotlib.pyplot as plt
import math

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

people = []#存所有角色的名字
inn_all = []#存每筆輸入
peonum = 0#存角色總數
f_start = 0
f_end = 0

def show_graph(N):
    # 印出
    edge_la = nx.get_edge_attributes(N, 'name')
    colors = nx.get_edge_attributes(N, 'color').values()
    pos = nx.spring_layout(N, iterations=20)

    nx.draw(N, pos, with_labels = True, font_color="whitesmoke", \
            node_color='black', node_size=600, \
            edge_color=colors, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edge_labels(N, pos, edge_labels=edge_la, font_size=10)
    plt.show()


def dijkstra(inn_map, inn_if_rel, dis, peonum, fs):
    visited = [0 for _ in range(peonum)]#存取是否找過節點

    dis[fs] = 0
    pre[fs] = fs
    pas = 0

    for pas in range(peonum):
        min_d = peonum+10
        min_j = 0

        for j in range(peonum):
            if (not(visited[j]) and dis[j]<min_d):
                min_d = dis[j]
                min_j = j

        visited[min_j] = 1

        for v in range(peonum):
            if(not(visited[v]) and inn_if_rel[min_j][v]):
                if(dis[min_j]+1 < dis[v]):
                    dis[v] = dis[min_j]+1
                    pre[v] = min_j


def findPath(inn_map, peonum, people, fs, d, New):
    if(d != fs):
        if(inn_map[pre[d]][d][0]=='@'):
            return G
            
        New.add_edge(people[pre[d]], people[d], \
                     name=inn_map[pre[d]][d][0], color='y')
        findPath(inn_map, peonum, people, fs, pre[d], New)
    return New
    
        

# 建立圖片
G = nx.DiGraph()
print("這是一個幫你理清人物關係的程式！\n\
輸入個角色名字與角色間的關係，我就會幫你生成簡易的人物關係圖。\n\
\n\
----------輸入說明----------\n\
輸入：小明 小芳 戀人 red\n\
表示：小明為小芳的戀人，他們兩個之間的連線顯示為紅色\n\
\n\
另外，你輸入的所有關係皆為單向，若要雙向關係，要反過來輸入一遍，但關係名稱需一致！\n\
以前面的情境來說，你需要輸入「小明 小芳 戀人 red」、「小芳 小明 戀人 red」，\n\
如此才能表示小明為小芳的戀人、小芳為小明的戀人。\n\
\n\
顏色有這些選擇：red、blue、black、gray、green、orange、purple、pink、brown、violet\n\
\n\
當人物關係都輸入好之後，輸入0 0 0 0我就會幫你生成關係圖啦！\n\
\n\
----------輸入開始----------\n\
請輸入：A角色 B角色 A角色是B角色的誰 A與B之間箭頭的顏色\n\
（角色名、關係名、顏色名皆不可包含空格喔）")


#讀取輸入
while(True):
    start, end, relate, color = [x for x in input().split()]
    if (start=='0' and end=='0' and relate=='0' and color=='0'):
        break

    G.add_edge(start, end, name=relate, color=color)# for networkx
    
    if(not(start in people)):
        people.append(start)
        peonum += 1
    if(not(end in people)):
        people.append(end)
        peonum += 1
    inn_all.append([start, end, relate, color])



inn_map = [['@' for _ in range(peonum)]for _ in range(peonum)]#存角色間關係
inn_if_rel = [[0 for _ in range(peonum)] for _ in range(peonum)]#存角色是否有關係


#開始存取
for i in inn_all:
    a = people.index(i[0])
    b = people.index(i[1])
    c = i[2]
    d = i[3]
    inn_map[a][b] = [c, d]
    inn_if_rel[a][b] = 1

print("恭喜你，系統已經在生成關係圖啦~\n\
稍等一會兒就能看到了！\n\
這個程式不僅能為你生成人物關係圖，還能幫你找到兩個角色之間最近的關係噢！\n\
在體驗這個功能前，記得將系統所顯示出的所有人物關係圖按右上角的叉叉關掉\n\
不然系統無法正常顯示新的關係圖噢！\n\
想體驗這個功能的話請照以下格式輸入~\n\
\n\
----------輸入說明----------\n\
輸入：小明 小芳\n\
表示：查詢小明和小芳間最近的關係\n\
\n\
----------輸入開始----------\n\
請輸入：A角色 B角色\n\
（角色名不可包含空格喔）")
show_graph(G)

#讀使用者想查詢哪兩人的關係    
while(True):
    dis = [(peonum+10) for _ in range(peonum)]#每次找關係都要更新的距離
    pre = [-1 for _ in range(peonum)]#存取此點的距離來自哪裡
    
    f_start_name, f_end_name = [x for x in input().split()]
    
    f_start = people.index(f_start_name)
    f_end = people.index(f_end_name)
    
    dijkstra(inn_map, inn_if_rel, dis, peonum, f_start)
    New = nx.DiGraph()
    for i in inn_all:
        New.add_edge(i[0], i[1], name=i[2], color=i[3])
    show_graph(findPath(inn_map, peonum, people, f_start, f_end, New))


        
    
