from random import choice
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
            if isinstance(name_or_power, str):
                name = name_or_power
                cost = FantasyCardFactory.get_random('cost')
            else:
                name = FantasyCardFactory.get_random('creature', 'name')
                cost = name_or_power
            return CreatureCard(
                name,
                cost,
                FantasyCardFactory.get_random('rarity'),
                FantasyCardFactory.get_random('attack'),
                FantasyCardFactory.get_random('health'),
                FantasyCardFactory.get_random('creature', 'effect'))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = FantasyCardFactory.get_random('cost')
        else:
            name = FantasyCardFactory.get_random('spell', 'name')
            cost = name_or_power
        return SpellCard(
            name,
            cost,
            FantasyCardFactory.get_random('rarity'),
            FantasyCardFactory.get_random('spell', 'effect_type')
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = FantasyCardFactory.get_random('cost')
        else:
            name = FantasyCardFactory.get_random('artifact', 'name')
            cost = name_or_power
        return ArtifactCard(
            name,
            cost,
            FantasyCardFactory.get_random('rarity'),
            FantasyCardFactory.get_random('durability'),
            FantasyCardFactory.get_random('artifact', 'effect')
        )

    def create_themed_deck(self, size: int) -> dict:

        deck = Deck()
        creatures = []
        spells = []
        artifacts = []
        while len(deck.cards) < size:
            if len(deck.cards) < size / 3:
                card_type = 'creature'
            elif len(deck.cards) < (2 * size) / 3:
                card_type = 'spell'
            else:
                card_type = 'artifact'
            
            if card_type == 'creature':
                random_creature = FantasyCardFactory.get_random('creature', 'name')
                creature = self.create_creature(random_creature)
                deck.add_card(creature)
                creatures.append(creature.name)
            elif card_type == 'spell':
                random_spell = FantasyCardFactory.get_random('spell', 'name')
                spell = self.create_spell(random_spell)
                deck.add_card(spell)
                spells.append(spell.name)
            elif card_type == 'artifact':
                random_artifact = FantasyCardFactory.get_random('artifact', 'name')
                artifact = self.create_artifact(random_artifact)
                deck.add_card(artifact)
                artifacts.append(artifact.name)

        return ({
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts
        })

    def get_supported_types(self) -> dict:
        pass

    @staticmethod
    def get_random(card_type: str, attribute: str=None) -> str | int:
        pools = {
            'creature': {
                'name': [
                    'Fire Dragon', 'Goblin Warrior', 'Ice Wizard', 'Lightning Elemental',
                    'Stone Golem', 'Shadow Assassin', 'Healing Angel', 'Forest Sprite'
                ],
                'effect': ['damage', 'heal', 'buff', 'debuff']
            },
            'spell': {
                'name': [
                    'Lightning Bolt', 'Healing Potion', 'Fireball', 'Shield Spell',
                    'Meteor', 'Ice Shard', 'Divine Light', 'Magic Missile'
                ],
                'effect_type': ['damage', 'heal', 'buff']
            },
            'artifact': {
                'name': [
                    'Mana Crystal', 'Sword of Power', 'Ring of Wisdom', 'Shield of Defense',
                    'Crown of Kings', 'Boots of Speed', 'Cloak of Shadows', 'Staff of Elements'
                ],
                'effect': [
                    'Permanent: +1 mana per turn',
                    'Permanent: +2 attack to equipped creature',
                    'Permanent: Draw an extra card each turn',
                    'Permanent: +3 health to all friendly creatures',
                    'Permanent: +1 cost reduction to all cards',
                    'Permanent: Cards cost 1 less mana',
                    'Permanent: Creatures have stealth',
                    'Permanent: +1 spell damage'
                ]
            },
            'rarity': ['Legendary', 'Common', 'Rare', 'Uncommon'],
            'number': list(range(1, 10)),
        }
        card_type = card_type.lower()
        if attribute:
            attr = attribute.lower()

        if card_type == 'card_type':
            return choice(pools['card_type'])
        elif card_type in ['cost', 'durability', 'attack', 'health', 'number']:
            return choice(pools['number'])
        elif card_type == 'rarity':
            return choice(pools['rarity'])
        elif card_type == 'creature':
            if attr == 'name':
                return choice(pools['creature']['name'])
            elif attr == 'effect':
                return choice(pools['creature']['effect'])
        elif card_type == 'spell':
            if attr == 'name':
                return choice(pools['spell']['name'])
            elif attr == 'effect_type':
                return choice(pools['spell']['effect_type'])
        elif card_type == 'artifact':
            if attr == 'name':
                return choice(pools['artifact']['name'])
            elif attr == 'effect':
                return choice(pools['artifact']['effect'])
        return ""
