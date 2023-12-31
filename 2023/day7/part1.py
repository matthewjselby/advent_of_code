card_rankings = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

hand_rankings = {
    'five-of-a-kind': 7,
    'four-of-a-kind': 6,
    'full-house': 5,
    'three-of-a-kind': 4,
    'two-pair': 3,
    'one-pair': 2,
    'high-card': 1
}

def identify_hand(hand_info):
    card_counts = hand_info['map'].values()
    if 5 in card_counts:
        return 'five-of-a-kind'
    elif 4 in card_counts:
        return 'four-of-a-kind'
    elif 3 in card_counts and 2 in card_counts:
        return 'full-house'
    elif 3 in card_counts:
        return 'three-of-a-kind'
    elif 2 in card_counts and len(card_counts) == 3:
        return 'two-pair'
    elif 2 in card_counts:
        return 'one-pair'
    else:
        return 'high-card'

def compare_hands(hand_1_info, hand_2_info):
    """
    Returns True if hand 1 is ranked higher than hand 2, else returns False
    """
    hand_1_rank = hand_rankings[identify_hand(hand_1_info)]
    hand_2_rank = hand_rankings[identify_hand(hand_2_info)]
    if hand_1_rank > hand_2_rank:
        return True
    elif hand_1_rank < hand_2_rank:
        return False
    else:
        hand1 = hand_1_info['hand']
        hand2 = hand_2_info['hand']
        for card_idx in range(len(hand1)):
            if card_rankings[hand1[card_idx]] > card_rankings[hand2[card_idx]]:
                return True
            elif card_rankings[hand1[card_idx]] < card_rankings[hand2[card_idx]]:
                return False
        return False

with open('./input.txt') as data:
    lines = data.readlines()
    hands = []
    for line in lines:
        hand = line.split(' ')[0]
        bid = int(line.split(' ')[1].strip())
        hand_info = {'hand': hand, 'bid': bid}
        hand_map = {}
        for card in hand:
            if card not in hand_map:
                hand_map[card] = 1
            else:
                hand_map[card] += 1
        hand_info['map'] = hand_map
        if len(hands) == 0:
            hands.append(hand_info)
        else:
            hand_placed = False
            for hand_idx, hand in enumerate(hands):
                comparison = compare_hands(hand_info, hand)
                if compare_hands(hand_info, hand) == True:
                    hands.insert(hand_idx, hand_info)
                    hand_placed = True
                    break
            if not hand_placed:
                hands.append(hand_info)
    winnings = 0
    for hand_idx, hand in enumerate(hands):
        print(f'hand: {hand["hand"]}')
        winnings += hand['bid'] * (len(hands) - hand_idx)
    print(winnings)
    

