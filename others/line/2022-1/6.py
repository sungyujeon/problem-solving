def solution(req_id, req_info):
    answer = []

    # 판매할 골드의 양(sell_amount), 판매가격(sell_price)
    # 1. pending
    #    sell_price 이상인 구매 요청 찾기 else append pending
    #    가장 비싼, 가장 먼저
    # 2. 찾은 후
    #    구매골드양(buy_amount) ?>> min(buy_amount, sell_amount) * sell_price
    # 3. 거래 후
    #    최종골드양(amount) >> 판매자 계좌 -> 구매자 계좌(amount 이동)
    #                       구매자 계좌 -> 판매자 계좌(amount * sell_price 실버 이동)
    #                       구매요청 buy_amount -= min(buy_amoun, sell_amount)
    #                       if buy_amount == 0: 'done'
    # 4. if sell_amount > 1: pending으로 돌아감
    # pending 상태인 구/판매 있다면 등록하지 않음
    
    # init req_id
    req_id_dict = {}
    for id in req_id:
        req_id_dict[id] = [0, 0]  # gold, silver

    # req_info
    N = len(req_info)
    pending_buy = []
    pending_sell = []

    for i in range(N):  # i번째 등록 요청
        id = req_id[i]
        sType, amount, price = req_info[i]  # sType: 0(구매), 1(판매)
        print(id, sType, amount, price)

        if sType == 0:  # 구매
            if not pending_sell:  # 판매하는게 없으면
                pending_buy.append((id, sType, amount, price))
            else:  # 판매 있으면
                pending_buy.sort(key=lambda x: x[3])
                pid, psType, pamount, pprice = pending_buy.pop(0)
                rid = req_id_dict[pid]
                rid[0]

        else:           # 판매
            if not pending_buy:  # 구매 없으면
                pending_sell.append((id, sType, amount, price))
            else:  # 구매 있으면
                pass
        
    




    return answer  # string, 알파벳 사전순

req_id = ["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"]
req_info = [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]
print(solution(req_id, req_info))
print(["Andy +11 -240", "Louis 0 0", "Rohan -4 +100", "William -7 +140"])