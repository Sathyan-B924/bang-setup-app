import random
import streamlit as st


# Character lists (display names)
character_pools = {
    "Base Game": [
        "Suzy Lafayette", "Paul Regret", "Pedro Ramirez", "Calamity Janet",
        "El Gringo", "Jourdonnais", "Lucky Duke", "Slab the Killer",
        "Willy the Kid", "Jesse Jones", "Bart Cassidy", "Black Jack",
        "Kit Carlson", "Rose Doolan", "Sid Ketchum", "Vulture Sam"
    ],
    "Dodge City": [
        "Doc Holyday", "Tequila Joe", "Belle Star", "Greg Digger",
        "Apache Kid", "Chuck Wengam", "Bill Noface", "Elena Fuente",
        "Herb Hunter", "Jose Delgado", "Molly Stark", "Sean Mallory",
        "Pat Brennan", "Pixie Pete", "Vera Custer"
    ],
    "Wild West": [
        "Big Spencer", "Flint Westwood", "Youl Grinner", "Gary Looter",
        "Teren Kill", "Greygory Deck", "John Pain", "Lee Van Kliff"
    ],
    "Valley of Shadows": [
        "Black Flower", "Colorado Bill", "Der Spot-Burst Ringer",
        "Evelyn Shebang", "Henry Block", "Mick Defender",
        "Tuco Franziskaner", "Lemonade Jim"
    ]
}

# Abilities dict with normalized keys
bang_characters = {

# Base characters
    "suzylafayette": "As soon as she has no cards in her hand, she draws a card from the draw pile",
    "paulregret": "He is considered to have a Mustang in play at all times; all other players must add 1 to the distance to him. If he has another real Mustang in play, he can count both of them, increasing all distances to him by a total of 2",
    "pedroramirez": "During phase 1 of his turn, he may choose to draw the first card from the top of the discard pile or from the deck. Then, he draws the second card from the deck",
    "calamityjanet": "She can use BANG! cards as Missed! cards and vice versa. If she plays a Missed! as a BANG!, she cannot play another BANG! card that turn (unless she has a Volcanic in play)",
    "elgringo": "Each time he loses a life point due to a card played by another player, he draws a random card from the hands of that player (one card for each life point). If that player has no more cards, too bad!, he does not draw. Note that Dynamite damages are not caused by any player",
    "jourdonnais": "He is considered to have a Barrel in play at all times; he can 'draw!' when he is the target of a BANG!, and on a Heart he is missed. If he has another real Barrel card in play, he can count both of them, giving him two chances to cancel the BANG! before playing a Missed!",
    "luckyduke": "Each time he is required to 'draw!', he flips the top two cards from the deck, and chooses the result he prefers. Discard both cards afterwards",
    "slabthekiller": "Players trying to cancel his BANG! cards need to play 2 Missed!. The Barrel effect, if successfully used, only counts as one Missed!",
    "willythekid": "He can play any number of BANG! cards during his turn",
    "jessejones": "During phase 1 of his turn, he may choose to draw the first card from the deck, or randomly from the hand of any other player. Then he draws the second card from the deck",
    "bartcassidy": "Each time he loses a life point, he immediately draws a card from the deck",
    "blackjack": "During phase 1 of his turn, he must show the second card he draws: if it's Heart or Diamonds, he draws one additional card (without revealing it)",
    "kitcarlson": "During phase 1 of his turn, he looks at the top three cards of the deck: he chooses 2 to draw, and puts the other one back on the top of the deck, face down",
    "rosedoolan": "She is considered to have a Scope in play at all times; she sees the other players at a distance decreased by 1. If she has another real Scope in play, she can count both of them, reducing her distance to all other players by a total of 2",
    "sidketchum": "At any time, he may discard 2 cards from his hand to regain one life point. If he is willing and able, he can use this ability more than once at a time. But remember: you cannot have more life points than your starting amount!",
    "vulturesam": "Whenever a character is eliminated from the game, Sam takes all the cards that player had in his hand and in play, and adds them to his hand",

# Dodge city characters
    "docholyday": "Once during his turn, he can discard any two cards from his hand for the effect of a BANG! against a player within range of his weapon. This ability does not count towards his limit of one BANG! card per turn. To hit Apache Kid in this way, at least one of the two discarded cards must not be a Diamond",
    "tequilajoe": "Each time he plays a Beer, he regains 2 life points instead of 1. He only regains 1 life point from similar cards like Saloon, Tequila, or Canteen",
    "bellestar": "During her turn, no card in front of any other player has any effect. This applies both to the blue- as well as to the green-bordered cards",
    "gregdigger": "Each time another character is eliminated, he regains 2 life points. As usual, he cannot exceed his initial number of life points in this way",
    "apachekid": "He is unaffected by cards from the suit of Diamonds played by the other players. During a Duel, his ability does not work",
    "chuckwengam": "During his turn, he can choose to lose 1 life point to draw 2 cards from the deck. He may also use this ability more than once in the same turn; however, he cannot choose to lose his last life point this way",
    "billnoface": "During phase 1 of his turn, he draws 1 card, plus 1 card for each injury (lost life point) he currently suffers. So, if he is at full life, he draws 1 card; with one life point less, he draws 2 cards; with two life points less, he draws 3 cards, and so forth",
    "elenafuente": "She can use any card in her hand as a Missed!",
    "herbhunter": "Each time another character is eliminated, he draws 2 extra cards from the deck. So, if he kills an Outlaw himself, he draws 5 cards",
    "josedelgado": "During his turn he can discard a blue-bordered card from his hand to draw 2 cards from the deck. He may use this ability twice per turn",
    "mollystark": "Each time she plays or voluntarily discards a Missed!, Beer, or BANG! card when it is not her turn, she draws one card from the deck. If she discards a BANG! during a Duel, she does not draw her replacement cards until the end of the Duel, when she would draw one card for each BANG! she used during the Duel. Cards that she is forced to discard due to cards like Cat Balou, Brawl, or Can-Can are not considered voluntarily discarded!",
    "seanmallory": "In phase 3 of his turn, he can hold up to 10 cards in his hand. He does not have to discard any cards if he has more cards than the number of life points he has left, but less than 11",
    "patbrennan": "During phase 1 of his turn, he may choose to draw the usual two cards from the deck, or, instead draw one card (and this one card only) from in play and add it to his hand. The card can be in front of any player, and can be either a blue-bordered card or a green-bordered card",
    "pixiepete": "During phase 1 of his turn, he draws 3 cards instead of 2",
    "veracuster": "At the beginning of her turn, before drawing any cards (in phase 1), she chooses any other character still in play. Until her next turn, she has the same ability as that character",


# Wild west characters
    "bigspencer": "He starts with 5 cards. He can't play Missed!",
    "flintwestwood": "During his turn, he may trade one card from hand with 2 cards at random from the hand of another player. CLARIFICATION: The card from your hand is of your choice, not at random. If the target player has only one card, you get only one card",
    "youlgrinner": "Before drawing, players with more hand cards than him must give him one card of their choice",
    "garylooter": "He draws all excess cards discarded by other players at the end of their turn",
    "terenkill": "Each time he would be eliminated, 'draw!': if it is not Spades, Teren stays at 1 life point, and draws 1 card. CLARIFICATION: If the 'draw!' is unsuccessful, you can't play a Beer to save you",
    "greygorydeck": "At the start of his turn, he may draw 2 characters at random. He has all the abilities of the drawn characters. CLARIFICATION: The only valid characters are those from the basic game. At the beginning of your next turn, you decide whether to keep the characters or to change them. If you choose to change them, you must change both of them. This ability also applies at the beginning of the game",
    "johnpain": "If he has less than 6 cards in hand, each time any player 'draws!', John adds the card just drawn to his hand. CLARIFICATION: The card drawn this way may not be used immediately; you must wait until the previous effect ends. For example, if it's a Beer and you lose at the same time your last life point, you may not use it",
    "leevankliff": "During his turn, he may discard a BANG! to repeat the effect of a brown-bordered card he just played. CLARIFICATION: The brown-bordered card may be also another BANG! You may repeat each effect one time only. If you repeat the effect of a Stagecoach or Wells Fargo, the WWS card only changes the first time. Repeating the effect counts as one card played, if Miss Susanna is in play",

# Valley of shadows characters
    "blackflower": "Once during your turn, you may use any Clubs card as an extra BANG!. CLARIFICATION: You can use a Clubs card as a BANG! in addition to your normal one BANG! per turn.",
    "coloradobill": "Each time you play a BANG! card, 'draw!': on Spades, this shot cannot be avoided. CLARIFICATION: Cards like Missed! or Barrel or Jourdonnais' ability cannot be used.",
    "derspotburstringer": "Once during your turn, you may use a BANG! card as a Gatling. CLARIFICATION: This BANG! card is not counted against the limit of one BANG! card per turn.",
    "evelynshebang": "You may refuse to draw cards in your draw phase. For each card skipped, shoot a BANG! at a different target in reachable distance. CLARIFICATION: You must choose to draw 0, 1, or 2 cards before drawing (you cannot draw one card, look at it and then choose to 'shoot' the next).",
    "henryblock": "Any player drawing or discarding one of your cards (in hand or in play) is the target of a BANG!. CLARIFICATION: The card is drawn (or discarded) only after the automatic BANG! is resolved. This ability works against Jesse Jones' or Pat Brennan's, but not against automatic abilities like El Gringo's.",
    "lemonadejim": "Each time another player plays a Beer card, you may discard any card from hand to also regain 1 life point.",
    "mickdefender": "If you are the target of a brown card other than BANG!, you may use a Missed! card to avoid that card. CLARIFICATION: This ability also works against cards that affect multiple players (Gatling, Indians, etc.). The Missed! card only prevents the card effects on you, not on the others.",
    "tucofranziskaner": "During your draw phase, if you have no blue cards in play, draw 2 extra cards.",
}


# Normalize name for lookup
def normalize(name: str) -> str:
    return "".join(ch.lower() for ch in name if ch.isalnum())

# Assign characters
def assign_characters(player_list, selected_pools):
    available = []
    for pool, include in selected_pools.items():
        if include:
            available.extend(character_pools[pool])
    if len(available) < len(player_list) * 2:
        st.error("Not enough characters selected.")
        return {}
    random.shuffle(player_list)
    assignments = {}
    for p in player_list:
        picks = random.sample(available, 2)
        assignments[p] = picks
        for c in picks:
            available.remove(c)
    return assignments

# App title
st.title("Bang! Game Setup Helper")

with st.form("bang_setup"):
    # Player names input
    names_input = st.text_input("Enter player names (comma-separated, 4–8 players)")
    players = [n.strip().capitalize() for n in names_input.split(",") if n.strip()]
    
    # Expansion checkboxes with tooltips
    st.subheader("Select Expansions")
    selected_pools = {
        pool: st.checkbox(pool, value=True, help=f"Include characters from {pool} expansion")
        for pool in character_pools
    }

    submitted = st.form_submit_button("Generate Setup")

if submitted:
    if not (4 <= len(players) <= 8):
        st.error("Requires 4–8 players.")
    elif len(players) != len(set(players)):
        st.error("Duplicate names detected. Please enter unique player names.")
    else:
        sheriff = random.choice(players)
        seating = random.sample(players, len(players))
        st.markdown(f"**Sheriff:** {sheriff}")
        st.markdown(f"**Seating order:** {' → '.join(seating)}")

        # Assign characters
        char_map = assign_characters(players, selected_pools)
        if char_map:
            st.subheader("Character Options (choose one)")
            for player, options in char_map.items():
                st.markdown(f"**{player}:**")
                for opt in options:
                    key = normalize(opt)
                    ability = bang_characters.get(key, "Ability not found.")
                    st.markdown(f"<details><summary>{opt}</summary>{ability}</details>", unsafe_allow_html=True)