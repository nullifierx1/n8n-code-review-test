"""Static hero catalogue and starter builds.

The item sets are short, role-oriented recommendations based on the public
pro-build catalogue at Dota2ProTracker. They are intentionally a static demo
snapshot, not a replacement for patch-specific in-game guides.
"""

BUILD_SOURCE = "https://dota2protracker.com/builds"


def build(hero, attribute, role, items):
    return {"hero": hero, "attribute": attribute, "role": role, "items": items}


BUILDS = {
    # Strength
    "axe": build("Axe", "strength", "Offlane", ["Phase Boots", "Blink Dagger", "Blade Mail", "Black King Bar"]),
    "bristleback": build("Bristleback", "strength", "Offlane", ["Power Treads", "Eternal Shroud", "Aghanim's Scepter", "Bloodstone"]),
    "centaur-warrunner": build("Centaur Warrunner", "strength", "Offlane", ["Phase Boots", "Blink Dagger", "Pipe of Insight", "Heart of Tarrasque"]),
    "chaos-knight": build("Chaos Knight", "strength", "Carry", ["Power Treads", "Armlet of Mordiggian", "Echo Sabre", "Black King Bar"]),
    "dragon-knight": build("Dragon Knight", "strength", "Mid", ["Power Treads", "Blink Dagger", "Black King Bar", "Assault Cuirass"]),
    "earthshaker": build("Earthshaker", "strength", "Support", ["Arcane Boots", "Blink Dagger", "Aghanim's Scepter", "Black King Bar"]),
    "huskar": build("Huskar", "strength", "Mid", ["Power Treads", "Armlet of Mordiggian", "Heaven's Halberd", "Black King Bar"]),
    "kunkka": build("Kunkka", "strength", "Mid", ["Phase Boots", "Mage Slayer", "Aghanim's Scepter", "Black King Bar"]),
    "legion-commander": build("Legion Commander", "strength", "Offlane", ["Phase Boots", "Blink Dagger", "Blade Mail", "Black King Bar"]),
    "mars": build("Mars", "strength", "Offlane", ["Phase Boots", "Blink Dagger", "Pipe of Insight", "Refresher Orb"]),
    # Agility
    "anti-mage": build("Anti-Mage", "agility", "Carry", ["Power Treads", "Battle Fury", "Manta Style", "Butterfly"]),
    "drow-ranger": build("Drow Ranger", "agility", "Carry", ["Power Treads", "Dragon Lance", "Hurricane Pike", "Black King Bar"]),
    "juggernaut": build("Juggernaut", "agility", "Carry", ["Phase Boots", "Maelstrom", "Manta Style", "Butterfly"]),
    "luna": build("Luna", "agility", "Carry", ["Power Treads", "Mask of Madness", "Manta Style", "Black King Bar"]),
    "monkey-king": build("Monkey King", "agility", "Carry", ["Power Treads", "Maelstrom", "Black King Bar", "Butterfly"]),
    "phantom-assassin": build("Phantom Assassin", "agility", "Carry", ["Power Treads", "Battle Fury", "Black King Bar", "Satanic"]),
    "slark": build("Slark", "agility", "Carry", ["Power Treads", "Diffusal Blade", "Aghanim's Scepter", "Black King Bar"]),
    "sniper": build("Sniper", "agility", "Mid", ["Power Treads", "Dragon Lance", "Hurricane Pike", "Black King Bar"]),
    "spectre": build("Spectre", "agility", "Carry", ["Power Treads", "Radiance", "Manta Style", "Heart of Tarrasque"]),
    "ursa": build("Ursa", "agility", "Carry", ["Phase Boots", "Battle Fury", "Blink Dagger", "Black King Bar"]),
    # Intelligence
    "crystal-maiden": build("Crystal Maiden", "intelligence", "Support", ["Arcane Boots", "Glimmer Cape", "Force Staff", "Black King Bar"]),
    "death-prophet": build("Death Prophet", "intelligence", "Mid", ["Power Treads", "Kaya and Sange", "Black King Bar", "Shiva's Guard"]),
    "invoker": build("Invoker", "intelligence", "Mid", ["Boots of Travel", "Hand of Midas", "Aghanim's Scepter", "Black King Bar"]),
    "leshrac": build("Leshrac", "intelligence", "Mid", ["Arcane Boots", "Kaya and Sange", "Black King Bar", "Bloodstone"]),
    "lion": build("Lion", "intelligence", "Support", ["Arcane Boots", "Blink Dagger", "Force Staff", "Aghanim's Scepter"]),
    "lina": build("Lina", "intelligence", "Mid", ["Power Treads", "Gleipnir", "Black King Bar", "Daedalus"]),
    "pugna": build("Pugna", "intelligence", "Support", ["Arcane Boots", "Aether Lens", "Glimmer Cape", "Aghanim's Scepter"]),
    "queen-of-pain": build("Queen of Pain", "intelligence", "Mid", ["Power Treads", "Orchid Malevolence", "Black King Bar", "Shiva's Guard"]),
    "skywrath-mage": build("Skywrath Mage", "intelligence", "Support", ["Arcane Boots", "Rod of Atos", "Glimmer Cape", "Aghanim's Scepter"]),
    "witch-doctor": build("Witch Doctor", "intelligence", "Support", ["Arcane Boots", "Glimmer Cape", "Force Staff", "Aghanim's Scepter"]),
    # Universal
    "abaddon": build("Abaddon", "universal", "Support", ["Arcane Boots", "Holy Locket", "Solar Crest", "Aghanim's Scepter"]),
    "arc-warden": build("Arc Warden", "universal", "Carry", ["Hand of Midas", "Gleipnir", "Hurricane Pike", "Black King Bar"]),
    "bane": build("Bane", "universal", "Support", ["Arcane Boots", "Aether Lens", "Glimmer Cape", "Blink Dagger"]),
    "brewmaster": build("Brewmaster", "universal", "Offlane", ["Phase Boots", "Radiance", "Blink Dagger", "Black King Bar"]),
    "dark-seer": build("Dark Seer", "universal", "Offlane", ["Arcane Boots", "Pipe of Insight", "Blink Dagger", "Aghanim's Scepter"]),
    "dark-willow": build("Dark Willow", "universal", "Support", ["Arcane Boots", "Glimmer Cape", "Force Staff", "Aghanim's Scepter"]),
    "enigma": build("Enigma", "universal", "Offlane", ["Arcane Boots", "Blink Dagger", "Black King Bar", "Refresher Orb"]),
    "magnus": build("Magnus", "universal", "Offlane", ["Power Treads", "Blink Dagger", "Harpoon", "Black King Bar"]),
    "marci": build("Marci", "universal", "Support", ["Phase Boots", "Solar Crest", "Black King Bar", "Basher"]),
    "void-spirit": build("Void Spirit", "universal", "Mid", ["Power Treads", "Mage Slayer", "Aghanim's Scepter", "Black King Bar"]),
}

HEROES_BY_ATTRIBUTE = {
    attribute: sorted(key for key, hero in BUILDS.items() if hero["attribute"] == attribute)
    for attribute in ("strength", "agility", "intelligence", "universal")
}
